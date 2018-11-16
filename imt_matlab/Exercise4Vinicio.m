function  Exercise4Vinicio()
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

hold on

%Plotting sine signal
f=100000;
N=1000;
p=pi/6;
t=linspace(0,5*10^-4,N);
y=0.3*sin(2*pi*f*t+p);


%Computing FFT and myDFT

N=1000;
sf=myDFT(y,N);  %Faire la transformation
figure(2)   %plot
subplot(2,2,1)
plot(y,'k');
title('s(t) time domain signal')
subplot(2,2,2)
plot(abs(sf),'r-*')
title('S(F) frequency domain signal')
sfft=fft(y,N);
subplot(2,2,3)
plot(y,'k');
title('s(t) time domain signal')
subplot(2,2,4)
plot(abs(sfft),'r-*')
title('S(F) frequency domain signal')

%Plotting AM signal

A=1;
fc=10^5;
fm=5*10^3;
mu=0.1;
AM=A*(1+mu*cos(2*pi*fm*t).*sin(2*pi*fc*t));

%Computing FFT and myDFT

sf=myDFT(AM,N);
figure(3)
subplot(2,2,1)
plot(AM,'k');
title('s(t) time domain signal')
subplot(2,2,2)
plot(abs(sf),'r-*')
title('S(F) frequency domain signal')
sfft=fft(AM,N);
subplot(2,2,3)
plot(AM,'k');
title('s(t) time domain signal')
subplot(2,2,4)
plot(abs(sfft),'-*')
title('S(F) frequency domain signal')


%Plotting random signal
r= 0.1*randn(1,length(t));

%Computing FFT and myDFT

sf=myDFT(r,N);
figure(4)
subplot(2,2,1)
plot(r,'k');
title('s(t) time domain signal')
subplot(2,2,2)
plot(abs(sf),'r-*')
title('S(F) frequency domain signal')
sfft=fft(r,N);
subplot(2,2,3)
plot(r,'k');
title('s(t) time domain signal')
subplot(2,2,4)
plot(abs(sfft),'-*')
title('S(F) frequency domain signal')

%Plotting Phase Modulation signal
PhM=sin(2*pi*fc*t+r+p);

%Computing FFT and myDFT

sf=myDFT(PhM,N);
figure(5)
subplot(2,2,1)
plot(PhM,'k');
title('s(t) time domain signal')
subplot(2,2,2)
plot(abs(sf),'r-*')
title('S(F) frequency domain signal')
sfft=fft(PhM,N);
subplot(2,2,3)
plot(PhM,'k');
title('s(t) time domain signal')
subplot(2,2,4)
plot(abs(sfft),'-*')
title('S(F) frequency domain signal')