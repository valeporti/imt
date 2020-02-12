#library("arules", lib.loc="/Library/Frameworks/R.framework/Versions/3.2/Resources/library")
#library("arulesViz", lib.loc="/Library/Frameworks/R.framework/Versions/3.2/Resources/library")

library("arules")
library("arulesViz")        
        
data("Groceries")

class(Groceries)

### On affiche les noms des produits et leurs catégories.
Groceries@itemInfo

### On affiche proprement les 10 premières transactions du jeu de données
apply(Groceries@data[,1:10],2, function (r) paste(Groceries@itemInfo[r,"labels"],collapse=", "))

### On génère des items fréquents à l'aide d'un algorithme a priori

itemsets <- apriori(Groceries,parameter=list(minlen=1,maxlen=1,support=0.02,target="frequent itemsets"))
summary(itemsets)

### on utilise la fonction inspect() pour afficher le top ten des items fréquents triés en 
## en fonction de leur support.
inspect(head(sort(itemsets,by="support"),10))

### On va maintenant regarder les candidats de cardinal 2 en changeant les paramètres 
## de l'algorithme
itemsets <- apriori(Groceries,parameter=list(minlen=2,maxlen=2,support=0.02,target="frequent itemsets"))
summary(itemsets)
inspect(head(sort(itemsets,by="support"),10))

### On va relancer les mêmes instructions, pas à pas, pour les cardinaux 3 et 4, et observer à la main
itemsets <- apriori(Groceries,parameter=list(minlen=3,maxlen=3,support=0.02,target="frequent itemsets"))
summary(itemsets)
inspect(head(sort(itemsets,by="support"),10))
itemsets <- apriori(Groceries,parameter=list(minlen=4,maxlen=4,support=0.02,target="frequent itemsets"))
summary(itemsets)


# Il n'y a pas d'item fréquents de cardinal 4 trouvés, l'algorithme converge. Nous avons
# lancé l'algorithme à la main et on converge donc pour k=4. Il y a 59 items fréquents de
# cardinal 1, 61 de cardinal 2 et 2 de cardinal 3. 

### Sans spécifier le paramètre maxlen, l'algorithme va continuer son exploration jusqu'à convergence
# pour k=4
itemsets<- apriori(Groceries,parameter=list(minlen=1,support=0.02,target="frequent itemsets"))


### Génération de règles. Ce coup-ci, on va générer des règles au lieu de générer des
### items fréquents. On fournit un support minimum et un niveau de confiance.

rules <- apriori(Groceries,parameter=list(support=0.001,confidence=0.6,target="rules"))
summary(rules)
plot(rules)
plot(rules@quality)
#### on calcule 1/support(Y)
slope <- sort(round(rules@quality$lift/rules@quality$confidence,2))
### et on va afficher le nombre de fois que chaque slope apparait dans le jeu de données
unlist(lapply(split(slope,f=slope),length))

### On affiche à présent le contenu des règles générées précédemment
inspect(head(sort(rules,by="lift"),10))

### On peut augmenter les exigences avec un niveau de confiance de 0.9
confidentRules<-rules[quality(rules)$confidence>0.9]
confidentRules

### On affiche avec le "lift" et la "confidence". 
plot(confidentRules,method="matrix",measure=c("lift","confidence"),control=list(reorder=TRUE))
plot(confidentRules,method="matrix",measure=c("lift","confidence"))#,control=list(reorder=TRUE))


### On va regarder les règles les plus pertinentes
highliftRules <- head(sort(rules,by="lift"),5)
plot(highliftRules,method="graph",control=list(type="items"))
