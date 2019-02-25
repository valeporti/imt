clear
clc
close all

A =[1 1 ; 1 1]
eig(A)
[P,D]=eig(A)
A*P
P*D
