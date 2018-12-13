clear all; clc; close all;

load('signaux_localisation.mat')

[r, lags] = xcorr(signal_ref, signal_BS1);
figure
plot(lags, r);
[~,I] = max(abs(r));
lagDiff_SigBS1 = abs(lags(I)); % in 10-7 seconds
[r, lags] = xcorr(signal_ref, signal_BS2);
figure
plot(lags, r);
[~,I] = max(abs(r));
lagDiff_SigBS2 = abs(lags(I)); % in 10-7 seconds
[r, lags] = xcorr(signal_ref, signal_BS3);
figure
plot(lags, r);
[~,I] = max(abs(r));
lagDiff_SigBS3 = abs(lags(I)); % in 10-7 seconds

speed_of_light = physconst('LightSpeed'); % m/s
distance_BS1 = ((lagDiff_SigBS1 / 10000000) * speed_of_light) / 1000; % in km 
distance_BS2 = ((lagDiff_SigBS2 / 10000000) * speed_of_light) / 1000; % in km
distance_BS3 = ((lagDiff_SigBS3 / 10000000) * speed_of_light) / 1000; % in km

[x_out_12, y_out_12] = circcirc(0, 0, distance_BS1, 4, 2, distance_BS2)
[x_out_13, y_out_13] = circcirc(0, 0, distance_BS1, 1, 4, distance_BS3)
[x_out_23, y_out_23] = circcirc(4, 2, distance_BS2, 1, 4, distance_BS3)

figure
circle(0, 0, distance_BS1)
hold on
circle(4, 2, distance_BS2)
circle(1, 4, distance_BS3)
hold off

function circle(x,y,r)
%x and y are the coordinates of the center of the circle
%r is the radius of the circle
%0.01 is the angle step, bigger values will draw the circle faster but
%you might notice imperfections (not very smooth)
ang=0:0.001:2*pi; 
xp=r*cos(ang);
yp=r*sin(ang);
plot(x+xp,y+yp);
end
