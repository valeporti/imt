clear; clc; close all;

N = 1000; % Samples
n = 50; % Points in the graph
sigma = 0.5;

% Generation of the distribution
X = randn(N,1)*sigma;
Y = randn(N,1)*sigma;
R = sqrt(X.^2+Y.^2);

% PDF
x = linspace(0,5,n+1);
delta = x(2); pdf = histcounts(R,x)/N;
x = (x(1:end-1) + x(2:end))/2;
plot(x,pdf,'-x'); hold on; % Plot distribution
x = linspace(0,5,10*n);
r = (x/sigma^2).*exp(-x.^2/(2*sigma^2));
plot(x,r*delta); title("pdf"); grid on; 

cdf = cumsum(pdf);

mean_calculated = sigma*sqrt(pi/2)
mean_obtained = mean(R)
variance_calculated = sigma^2*(4-pi)/2
variance_obtained = var(R)
clear; clc; close all;

N = 1000; % Samples
n = 50; % Points in the graph
sigma = sqrt(0.5);

% Generation of the distribution
X = randn(N,1)*sigma;
Y = randn(N,1)*sigma;
R = sqrt(X.^2+Y.^2);

% PDF
x = linspace(0,5,n+1);
delta = x(2); pdf = histcounts(R,x)/N;
x = (x(1:end-1) + x(2:end))/2;
plot(x,pdf,'-x'); hold on; % Plot distribution
xn = linspace(0,5,10*n);
r = (xn/sigma^2).*exp(-xn.^2/(2*sigma^2));
plot(xn,r*delta); title("pdf"); grid on;

mean_calculated = sigma*sqrt(pi/2)
mean_obtained = mean(R)
variance_calculated = sigma^2*(4-pi)/2
variance_obtained = var(R)

cdf = cumsum(pdf);
figure; plot(x,cdf); grid on;