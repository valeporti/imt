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

r=@(x) (x/(sigma^2))*exp(-(x^2/(2*(sigma^2)))); 

sigma_values = [];
for i=1:length(N)
    % for each value of N, run Monte Carlo test of 1000 trials
    %U = randn(1000,1)*sigma;
    %V = randn(1000,1)*sigma;
    %X = sqrt(X.^2+Y.^2);
    R = zeros(1000, 1);
    for j=1:1000
        value = randn * 5
        R(j, 1) = r(value);
    end
    sum_x = sum(R);
    m_chapeau = (1/N(i)) * sum_x;
    sigma_chapeau = m_chapeau * (sqrt(2) / sqrt(pi));
    sigma_values = [sigma_values, sigma_chapeau]
    %mean_estimator 
    for i=1:1000
        
                
    end
end