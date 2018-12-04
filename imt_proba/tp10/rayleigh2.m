clear; clc; close all;

N = 1000; % Samples
n = 50; % Points in the graph
beta = 1.4;
eta = 76;

U = rand(N,1);
X = eta*(-log(U)).^(1/beta);

% PDF
x = linspace(0,500,n+1);
pdf = histcounts(X,x)/N;
x = (x(1:end-1) + x(2:end))/2;
plot(x,pdf,'-x'); hold on; % Plot distribution
xn = linspace(0,500,10*n);
Y = beta/eta*(xn/eta).^(beta-1).*exp(-(xn/eta).^beta);
plot(xn,Y*(x(2)-x(1))); title("pdf"); grid on;