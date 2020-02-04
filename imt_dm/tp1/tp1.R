# https://towardsdatascience.com/association-rules-2-aa9a77241654
# https://towardsdatascience.com/association-rule-mining-be4122fc1793
# https://towardsdatascience.com/association-rule-mining-in-r-ddf2d044ae50

library("arules")
# library("arulesViz")

# Get the groceries data
data("Groceries")

# Transform it into a classs
class(Groceries)

# index | labels | level1 | level2
Groceries@itemInfo

# A way of aplying a function to several items, instead of using a loop, we use apply
apply(Groceries@data[,1:10],2, function (r) paste(Groceries@itemInfo[r,"labels"],collapse=","))

Groceries@itemInfo[13,"labels"]

summary(Groceries)
help("apply")


# minlen is the minimum number of items required in the rule
# maxlen is the maximum number of items that can be present in the rule
# support is an indication of how frequently the itemset appears in the dataset
help("apriori")
itemsets <- apriori(Groceries,parameter=list(minlen=1,maxlen=1,support=0.02,target="frequent itemsets"))

summary(itemsets)

inspect(head(sort(itemsets,by="support"),10))
length(itemsets) 

itemsets <- apriori(Groceries,parameter=list(minlen=2,maxlen=2,support=0.02,target="frequent itemsets"))
summary(itemsets)
inspect(head(sort(itemsets,by="support"),10))

itemsets <- apriori(Groceries,parameter=list(minlen=3,maxlen=3,support=0.02,target="frequent itemsets"))
inspect(sort(itemsets,by="support"))

itemsets <- apriori(Groceries,parameter=list(minlen=4,maxlen=4,support=0.0001,target="frequent itemsets"))
inspect(head(sort(itemsets,by="support"),10))

# run the algorithm without specifying the maxlen parameter
itemsets<- apriori(Groceries,parameter=list(minlen=1,support=0.02,target="frequent itemsets"))
inspect(head(sort(itemsets,by="support"),10))
# herewe obtain the ones with min len = 1 plus the others
length(itemsets) 

# We can also obtain de rules
rules <- apriori(Groceries,parameter=list(support=0.001,confidence=0.6,target="rules"))
# here we obtain
# set of 2918 rules
# 
# rule length distribution (lhs + rhs):sizes
# 2    3    4    5    6 
# 3  490 1765  626   34 
summary(rules)
length(rules) 

# Access to the quality of the rules (with @) to display alsoa scatterplot matrix 
# that will compare the support, confidence and lift of the 2918 rules
plot(rules)
plot(rules@quality)


inspect(head(sort(rules,by="lift"),10))
confidentRules<-rules[quality(rules)$confidence>0.9]
confidentRules

plot(confidentRules,method="matrix",measure=c("lift","confidence"),control=list(reorder=TRUE))

highliftRules <- head(sort(rules,by="lift"),5)
plot(highliftRules,method="graph",control=list(type="items"))
