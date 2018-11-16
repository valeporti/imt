clear all
close all


N = 512;        % nombre d'echantillons temporels
Nfft = 2048;    % nombre de points frequentiels
Tmax = 5*10^-4; % duree max du signal en secondes

t = linspace(0,Tmax,N); % generation du vecteur temps

Ts = Tmax/N;            % Periode d'echantillonage
Fs = 1/Ts;              % frequence d'echantillonage
f = linspace(0,Fs/2,Nfft/2); % generation du vecteur de frequence

% generation de sinus
A = 0.3;
p = 30*pi/180;
fc = 10^5;

s = A*sin(2*pi*fc*t+p);     % signal sinus
subplot(2,2,1)
plot(t,s)
title('sinewave signal')

sf = fft(s,Nfft);           % Transformee de Fourier 

% generation du signal AM
A = 0.1;
fc = 10^5;
fm = 5*10^3;
mu = 1;

y = A*(1+mu*cos(2*pi*fm*t)).*sin(2*pi*fc*t); % signal AM

subplot(2,2,2)
plot(t,y,'r')
title('AM modulated signal')

yf = fft(y,Nfft);           % Transformee de Fourier

% generation signal aleatoire gaussien
z = 0.1*randn(1,length(t));


subplot(2,2,3)
plot(t,z,'k')
title('white noise signal')

zf = fft(z,Nfft);
% generation phase modulated signal

x = sin(2*pi*fc*t + z + p);
subplot(2,2,4)
plot(t,x,'g')
title('phase modulated signal')

xf = fft(x,Nfft);

%======== Representation histogramme signal aleatoire ==
figure(2)
subplot(2,1,1)
plot(t,z);

subplot(2,1,2)
hist(z,50)
%======== Representation frequentielle des signaux ======
figure(3)
subplot(2,2,1)
plot(f,abs(sf(1:Nfft/2))/sqrt(Nfft))
title('sinewave signal')

subplot(2,2,2)
plot(f,abs(yf(1:Nfft/2))/sqrt(Nfft),'r')
title('AM modulated signal')

subplot(2,2,3)
plot(f,abs(zf(1:Nfft/2))/sqrt(Nfft),'k')
title('white noise signal')

subplot(2,2,4)
plot(f,abs(xf(1:Nfft/2))/sqrt(Nfft),'g')
title('phase modulated signal')