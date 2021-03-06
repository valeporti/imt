clear all
close all
clc

samples = 10000;
points_in_graph = 50;
sigma_2 = 0.5;
U = normrnd(0, sqrt(sigma_2), [samples, 1]);
V = normrnd(0, sqrt(sigma_2), [samples, 1]);
X = sqrt(U.^2 + V.^2);
r=@(x) (x/(sigma_2))*exp(-(x^2/(2*(sigma_2)))); 


% PDF
pdf_range = linspace(0,3,points_in_graph+1);
delta = pdf_range(2);
pdf = histcounts(X, pdf_range)/samples;

% Function
pdf_range = (pdf_range(1:end-1) + pdf_range(2:end))/2;
r = (pdf_range/sigma_2).*exp(-pdf_range.^2/(2*sigma_2));

% Plot both
figure
hold on
plot(pdf_range,pdf,'-x'); % Plot distribution
plot(pdf_range, r*delta); title('pdf'); grid on;

% Plot CDF of X = sqrt(..)
cdf = cumsum(pdf);
figure
plot(cdf)

%show values
mean_calculated = sqrt(sigma_2) * sqrt(pi / 2)
mean_X = mean(X)
variance_calculated = ((4-pi)/2) * sigma_2
variance_X = var(X)

% 7.
samples = 10000;
points_in_graph = 50;
sigma_2 = 0.5;
Y = exprnd((1/(2*sigma_2)), [samples, 1]);
X = sqrt(Y);

% PDF
pdf_range = linspace(0,3,points_in_graph+1);
delta = pdf_range(2);
pdf = histcounts(X, pdf_range)/samples;

% Function
pdf_range = (pdf_range(1:end-1) + pdf_range(2:end))/2;
r = (pdf_range/sigma_2).*exp(-pdf_range.^2/(2*sigma_2));

% Plot both
figure
hold on
plot(pdf_range,pdf,'-x'); % Plot distribution
plot(pdf_range, r*delta); title('pdf'); grid on;

% Plot CDF of X = sqrt(..)
cdf = cumsum(pdf);
figure
plot(cdf)

%figure(1)
%plot(X)
%figure(2)
%histogram(X, points_in_graph)
%figure(3)
%histogram(X, 'Normalization','probability')

%X_histo = histogram(X, points_in_graph)
%X_histo_norma = histogram(X, points_in_graph, 'Normalization','probability')
%bin_min = X_histo_norma.BinLimits(1,1);
%bin_max = X_histo_norma.BinLimits(1,2);
%step = X_histo_norma.BinWidth;

%X_histo_val = X_histo.Values ./ samples
%plot(X_histo_val)

%figure
%histogram(X, 'Normalization','probability')
%X_range = [0,5]
%X_range = fplot(r, X_histo.BinLimits)
%fplot(r, X_range)

%r(pdf_range)
%transpose(pdf_range)
%r_points = r(transpose(pdf_range))