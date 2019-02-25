clear
clc
close all

A =[25 0 20;0 1 0;20 0 41]
eig(A)
[P,D]=eig(A)
A*P
P*D
