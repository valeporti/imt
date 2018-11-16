clear; clc; close all;

% proposed values
s = 1;
alpha = 1;

n = 10000;
U = rand(n, 1);

lambda = (s * sqrt(s * s + 4) / 2);


X = s - log(U)/lambda;
figure(1);
plot(X);

M2 = (alpha / lambda) * exp((lambda * lambda/2) - lambda * s);
figure(2);
plot(M2);
