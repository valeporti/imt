function xf = myDFT(x, N)

% Inputs
% x: signal in time domain
% N: Number of samples in frequency domain

% Outputs
% xf: signal in frequency domain

K = length(x);
xf = zeros(1, N);

for n = 0: N-1
    for k = 0: K-1
        xf(n + 1) = xf(n + 1) + x(k + 1) * exp(-1i * 2 * k * pi * n / N);
    end
end