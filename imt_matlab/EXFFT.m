clear all
close all

time = [0 : 0.0001 : 0.1023];
signal = 2 * cos(2 * pi * 50 * time);
N = length(signal); % Number of points
spectre=abs(fft(signal, N)); % FFT signal
Fs = 1 / 0.0001; % sampling frequency
freq = (0 : N/2 - 1) * Fs/N; % frequency vector
plot(freq, 2 * spectre(1:N/2))