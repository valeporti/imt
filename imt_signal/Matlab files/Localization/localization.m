clear all; clc; close all;

load('signaux_localisation.mat')

[r, lags] = xcorr(signal_ref, signal_BS1);
figure
plot(lags, r);
[~,I] = max(abs(r));
lagDiff_SigBS1 = abs(lags(I)); % in micro seconds
[r, lags] = xcorr(signal_ref, signal_BS2);
figure
plot(lags, r);
[~,I] = max(abs(r));
lagDiff_SigBS2 = abs(lags(I)); % in micro seconds
[r, lags] = xcorr(signal_ref, signal_BS3);
figure
plot(lags, r);
[~,I] = max(abs(r));
lagDiff_SigBS3 = abs(lags(I)); % in micro seconds

speed_of_light = physconst('LightSpeed'); % m/s
distance_BS1 = ((lagDiff_SigBS1 / 1000000) * speed_of_light) / 1000 % in km 
distance_BS2 = ((lagDiff_SigBS2 / 1000000) * speed_of_light) / 1000 % in km
distance_BS3 = ((lagDiff_SigBS3 / 1000000) * speed_of_light) / 1000 % in km