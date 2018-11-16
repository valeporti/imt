clear; clc; close all;

T = 10000; % samples

s = -1:0.05:1 %proposed values of S

U = rand(T,1);

alpha = sqrt(2/pi) * (1 ./ (erfc(s./sqrt(2))));

M1 = 2./erfc (s / sqrt(2));

lambda = (s + sqrt(s .* s + 4)) / 2;
M2 = (alpha ./ lambda) .* exp((lambda .* lambda/2) - lambda .* s);

hold on
figure(1)
plot(s, M1);
plot(s, M2);
hold off
