clear; clc; close all;

N = [2 5 10 100 1000 10000]';
sigma = sqrt(0.5);
estimator = zeros(length(N),1);

for i=1:length(N)
    X = randn(N(i),1)*sigma;
    Y = randn(N(i),1)*sigma;
    R = sqrt(X.^2+Y.^2);
    estimator(i) = sum(R)/N(i)*sqrt(2/pi);
end

sqrt(0.5)
N,estimator