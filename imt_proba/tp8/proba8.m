clear; clc; close all;

s = 1;

n = 10000; % Samples
x = randn(n,1); % N[0,1]
y = x>s; % Condition
P_r = sum(~y)/n; % P["rejection"]
y = x.*y; % Y distribution

nd = 50; % Number of bars in the graph
p = linspace(-5,5,nd+1); % Auxiliar points to plot
pdf = histcounts(y,p)/n; % Get histogram
pdf(nd/2+1) = pdf(nd/2+1)-P_r; % Take out the unnecesary counts in 0
p = (p(1:end-1) + p(2:end))/2; % Get central points
bar(p,pdf); title("pdf"); grid on;

z = (1/sqrt(2*pi))*exp(-((p).^2/(2)))*(p(2)-p(1));
hold on; plot(p,z,'r'); legend("Y/M","Ideal Normal distribution")

cdf = cumsum(pdf);
alpha = 1/cdf(end); % Catch value of M
cdf = cdf*alpha;  % CDF of the final distribution
figure; plot(p,cdf); title("cdf"); grid on;
%%

clear; clc; close all;

n = 10000;

lambda = 1/2; % s = -3/2
s = -2;

x = s-log(rand(n,1))/lambda;
u = rand(n,1);
y = zeros(n,1);
c = (lambda*sqrt(2*pi)); 
P_r = 0;

for i=1:n
    if (u(i)<=(exp(-x(i)^2/2)/(c*exp(-lambda*x(i)))))
        y(i) = x(i);
    else
        P_r = P_r+1;
    end
end
P_r = P_r/n;

nd = 50; % Number of bars in the graph
p = linspace(-5,5,nd+1); % Auxiliar points to plot
pdf = histcounts(y,p)/n; % Get histogram
pdf(nd/2+1) = pdf(nd/2+1)-P_r; % Take out the unnecesary counts in 0

cdf = cumsum(pdf);
alpha = 1/cdf(end); % Catch value of M
pdf = pdf*alpha;
cdf = cdf*alpha;  % CDF of the final distribution

p = (p(1:end-1) + p(2:end))/2; % Get central points
bar(p,pdf); title("pdf"); grid on;
z = (1/sqrt(2*pi))*exp(-((p).^2/(2)))*(p(2)-p(1));
hold on; plot(p,z,'r'); legend("Y/M","Ideal Normal distribution")
figure; plot(p,cdf); title("cdf"); grid on;