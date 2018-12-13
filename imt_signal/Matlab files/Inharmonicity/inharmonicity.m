clear all; clc; close all; 

[x,Fs]=audioread('piano1.wav');
%1
figure
plot(x)
%2
X_fft = fft(x);
step = length(X_fft);
line_vector = linspace(-Fs/2, Fs/2, step);
X_ffts = fftshift(abs(X_fft));
X_ffts_log = 20*log10(X_ffts);
figure
plot(line_vector, X_ffts_log)

%Q.2.1
freq_on_graph = [220.5 442.1 663.3 885.6 1108 1332 1556];
n = length(freq_on_graph);
E_n = zeros(n);
for i=1:n
    E_n(i) = 1200 * (log2(freq_on_graph(i)) - log2(i * freq_on_graph(1)));
end
f_1 = freq_on_graph(1)
E_n

[x,Fs]=audioread('piano2.wav');
%1
figure
plot(x)
%2
X_fft = fft(x);
step = length(X_fft);
line_vector = linspace(-Fs/2, Fs/2, step);
X_ffts = fftshift(abs(X_fft));
X_ffts_log = 20*log10(X_ffts);
figure
plot(line_vector, X_ffts_log)

%Q.2.3
freq_on_graph = [217.9 443 668.1 892.7 1118 1347 1572];
n = length(freq_on_graph);
E_n = zeros(n);
for i=1:n
    E_n(i) = 1200 * (log2(freq_on_graph(i)) - log2(i * freq_on_graph(1)));
end
f_1 = freq_on_graph(1)
E_n



