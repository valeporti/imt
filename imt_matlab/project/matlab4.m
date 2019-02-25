clear
clc
close all

A =[0 1 ; 1 0]
eig(A)
[P,D]=eig(A)
A*P
P*D
