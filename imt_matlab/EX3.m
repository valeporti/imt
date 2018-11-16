function [] = EX3()

    clear all
    close all

    % Time specifications:
    Fs = 1000;                   % samples per second
    dt = 1/Fs;                   % seconds per sample
    StopTime = 5;             % seconds
    %t = (0:dt:StopTime-dt)';     % seconds
    %t = (0: 0.5: 2000);
    t = linspace(0, 9 * 10^-4, 10000);
    
    % Sinwave 
    amplitude = 0.3; %V
    phase = 30; %°
    phaseRad = phase * pi / 180;
    freq = 100 * 1000;                     % hertz
    
    s= amplitude * sin(phaseRad + 2 * pi * freq * t);
    
    subplot(2,2,1);
    plot (t, s) 
    title('Sinwave signal');
    xlabel('time (s)');
    ylabel('magnitude (V)');
    
    %t1 = 5 * (10^-4) * (0:2000)/2000;
    %y = amplitude * sin(2*pi*freq*t1 + phaseRad);
    %figure
    %plot(t1,y,'r') % red color
    
    %Amplitude modulated signal
    amplitude = 1; %V
    fc = 10^5; % hertz
    fm = 5 * 10^3;
    mu = 0.5;
    
    y = amplitude * (1 + mu * cos (2 * pi * fm * t)) .* sin(2 * pi * fc * t);
    
    subplot(2,2,2);
    plot(t, y, 'r');
    
    % generation signal aleatoire gaussien
    z = 0.1 * randn(1, length(t));
    
    subplot(2,2,3);
    plot(t, z, 'g');
    
    
    % generation phase modulated signal
    x = sin(2 * pi * fc * t + z + phaseRad);
    subplot(2,2,4);
    plot(t, x, 'm')
    
    
    figure(2)
    subplot(2,1,1)
    plot(t,z)
    
    subplot(2,1,2)
    hist(z,100)
    
    
    % Exercise about fourrier
    
    time = [0 : 0.0001 : 0.0103];
    N = length(s);
    spectre_s = abs(fft(s, N));
    Fs = 1 / 0.0001;
    freq = (0 : N/2 - 1) * Fs / N;
    
    
    figure(3)
    subplot(2,2,1);
    plot(freq, 2 * spectre_s(1:N/2));
    subplot(2,2,2);
    plot(abs(fft(y)), 'r');
    subplot(2,2,3);
    plot(abs(fft(x)), 'g');
    subplot(2,2,4);
    plot(abs(fft(z)), 'm');
    
    N = 512;
    Nfft = 1024;
    Tmax = 5 * 10^0.4;
    t = linspace(0, Tmax, N);
    
    Ts
    
    
   