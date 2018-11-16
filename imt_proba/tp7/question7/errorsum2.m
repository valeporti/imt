function errorsum1 = errorsum2(T,lambda)

f=@(x)exp(-lambda*x);

%7.1.3


U = rand(T, 1); % generation of uniform R.V.}
Y = ( - 1 / lambda) * log(1 - U);

z = histogram(Y,'Normalization','probability');
ccdf=zeros(length(z.Values), 1);
error=zeros(length(z.Values),1);

xaxis=zeros(length(z.Values),1);
for i=1:length(z.Values)
    xaxis(i,1)=(z.BinEdges(i)+z.BinEdges(i+1))/2;
end
for i=1:length(z.Values)
    ccdf(i, 1) = sum(z.Values(i:end));
end
%plot(xaxis,ccdf);
for i=1:length(z.Values)
    error(i,1) = ccdf(i,1)-f((z.BinEdges(i)+z.BinEdges(i+1))/2);
    
end
%plot(xaxis,error)
errorsum1=0;
for i=1:length(z.Values)

    errorsum1=errorsum1+error(i,1)*(z.BinEdges(i+1)-z.BinEdges(i));
end
