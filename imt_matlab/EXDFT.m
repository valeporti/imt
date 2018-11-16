clear all
close all

N = 10;
s = [1 1 0 0];

sf = myDFT(s, N);

plot(abs(s))

figure

plot(sf)

sfft = fft(abs(s), N);

figure 
plot(sfft)