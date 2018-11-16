function FFT = fastFourierTransform(A, n)

t = [0 : 3];
figure(1)
plot(t, A)

%Fourier transform
Sub_S = [];
for (k = 0: 3)
    if (k == 0 || k == 1)
        sk = 1;
    else 
        sk = 0;
    end 
    value = sk * exp (-1i * pi * (n / N)
    Sub_S = [Sub_S,  
end

%search S
S = [];
for (index = 0:n)
    value = 1 + exp(-1i * pi * index / 2);
    S = [S, value];
end

figure (2)
plot(t, S)

FFT = S;