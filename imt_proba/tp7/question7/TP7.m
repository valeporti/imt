clear all
close all
clc
f=@(x)exp(-2*x)

%7.1.3
T = 10000;
lambda = 2;

U = rand(T, 1); % generation of uniform R.V.}
Y = ( - 1 / lambda) * log(1 - U);

mean(Y)
var(Y)

plot(Y)

%7.1.4
figure(1)
z = histogram(Y,'Normalization','probability')
ccdf=zeros(length(z.Values), 1);
error=zeros(length(z.Values),1);

xaxis=zeros(length(z.Values),1);
for i=1:length(z.Values)
    xaxis(i,1)=(z.BinEdges(i)+z.BinEdges(i+1))/2
end
for i=1:length(z.Values)
    ccdf(i, 1) = sum(z.Values(i:end));
end
figure(2)
plot(xaxis,ccdf)

    
    
for i=1:length(z.Values)
    error(i,1) = ccdf(i,1)-f((z.BinEdges(i)+z.BinEdges(i+1))/2)
    
end
figure(3)
plot(xaxis,error)
errorsum=0;
for i=1:length(error)

    errorsum=errorsum+error(i)*(z.BinEdges(i+1)-z.BinEdges(i));
end
display(errorsum)








