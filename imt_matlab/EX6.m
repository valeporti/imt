clear all
clc

N = 10;
tic;
factorial(N);
toc

tic;
factorielle(N);
toc

tic;
prod([1:N]);
toc

fprintf("--- fibonacci ---")
tic;
fibo(5)
toc