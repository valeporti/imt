clear
clc
close all

A =[4 3 ; 3 4]
eig(A)
[P,D]=eig(A)
A*P
P*D

