clear all; clc; close all;

C = [[1 -1 5]
    [0 1 -2]
    [1 3 -3]];
I = eye(3);
S = I;

S = I + C * S;