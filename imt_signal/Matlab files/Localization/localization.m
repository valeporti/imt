clear all; clc; close all;

load('signaux_localisation.mat')

figure
plot(signal_BS1)
figure
plot(signal_BS2)
figure
plot(signal_BS3)
[r, lags] = xcorr(signal_ref, signal_BS1);

figure
plot(lags, r)
[~,I] = max(abs(r));
lagDiff = lags(I)