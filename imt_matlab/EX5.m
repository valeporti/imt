clear all
close all
clc

m = 1000;
n = 1000;

A = randn(n, m); % random 1000 x 1000 matrix
b = rand(m, 1); % random vector 1000 x 1

% Calculate time to find inverse matrix of A and performing the operation x
% = A-1 * b
tic; 
x = inv(A) * b;
toc

% Calculate the time of solving hte linear system Ax = b with mldivide
tic;
x = mldivide(A, b);
toc

% Calculate the time of solving the linear system Ax = b with an iterative
% method of your choice
tic;
x = cgs(A, b);
A_cgs_time = toc

m = 100;
B = randn(n, m);
c = randn(m, 1);


tic;
x = mldivide(B, b);
toc
