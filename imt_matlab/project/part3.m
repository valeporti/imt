clear all; clc; close all;

A = [[0 0 1.5 4.2 3.8 2.5 1.5 0 0 0]
    [0.65 0 0 0 0 0 0 0 0 0]
    [0 0.68 0 0 0 0 0 0 0 0]
    [0 0 0.75 0 0 0 0 0 0 0]
    [0 0 0 0.7 0 0 0 0 0 0]
    [0 0 0 0 0.6 0 0 0 0 0]
    [0 0 0 0 0 0.55 0 0 0 0]
    [0 0 0 0 0 0 0.4 0 0 0]
    [0 0 0 0 0 0 0 0.35 0 0]
    [0 0 0 0 0 0 0 0 0.2 0]];
x1 = transpose([100 0 0 0 0 0 0 0 0 0]);

%  -- 1
%If the haddock population in 1900 is x(1) = [100; 0; 0; 0; 0; 0; 0; 0; 0; 0]T (units are
%millions of pounds), what will the population be like in 1910? 1920? 1930? 1950?
%1990? 2000? Based upon what you have seen, do you believe the population to be
%stable or unstable?

haddock1910 = population_haddock_in_time(x1, A, 1910 - 1900) ;
haddock1920 = population_haddock_in_time(x1, A, 1920 - 1900) ;
haddock1930 = population_haddock_in_time(x1, A, 1930 - 1900) ;
haddock1950 = population_haddock_in_time(x1, A, 1950 - 1900) ;
haddock1990 = population_haddock_in_time(x1, A, 1990 - 1900) ;
haddock2000 = population_haddock_in_time(x1, A, 2000 - 1900) ; 

% I think the population will be stable since it's consistently growing and
% so, just consuming part of the fish would let it to reproduce and grow and to be
% used as food

% -- 2
%Suppose pollution has the efect of lowering each birth rate by 10% of the value
%given above and each survival coecient by 15% beginning in 1950. What efect
%does this have on the population in 1990 as compared to having no pollution efects?

A1 = A;
A1(1,:) = A1(1,:) * 0.85; % first line is the birth rate info
with_pollution_haddock_pop_1990 = population_affectation_in_time_survival(x1, A, 1990 - 1900, 1900, 1950, 0.9);
sum(with_pollution_haddock_pop_1990)
sum(haddock1990)

% The population without pollution is 20 times bigger than the one with pollution

% -- 3
%Beginning in 1925, assume that fsh 3 years old and older are caught at a rate such
%that each year, 25% of those groups are taken. Fish under 3 years old may not be
%taken (the distinction is based upon size).

%(a)What is the matrix form of the model now? ( modification of equation (1),
%above). Did you assume the fish were harvested before or after the annual birth
%process occured? Please generalize to show a model reecting any harvesting rate which 
%you may denote by h. Thus above, h = 0:20.

A2 = A;
A2(4:end,:) = A(4:end,:) * 0.75;
x2 = transpose([0 0 0 0.75 0.75 0.75 0.75 0.75 0.75 0.75]);
% took into account that they are harvested after the annual birth
harvest_haddock1930 = population_haddock_in_time(x1, A2, 1930 - 1900) 
haddock1930
harvest_haddock1950 = population_haddock_in_time(x1, A2, 1950 - 1900) 
haddock1950
harvest_haddock1990 = population_haddock_in_time(x1, A2, 1990 - 1900) 
haddock1990
harvest_haddock2000 = population_haddock_in_time(x1, A2, 2000 - 1900) 
haddock2000

%(b) What does the population now look like for 1930, 1950, 1995, 2000? Is this a
%good strategy?

function [R] = population_haddock_in_time(x1, A, k)
    R = mpower(A, k) * x1;
end

function [R] = population_affectation_in_time_survival(x1, A, k, start_date, from_date_survival, affectation_survival)
    
    diff_from_start = from_date_survival - start_date;
    A1 = mpower(A, diff_from_start);
    A2 = A;
    A2(2:end,:) = A(2:end,:) * affectation_survival;
    diff_from_k = k - (from_date_survival - start_date);
    A2 = mpower(A2, diff_from_k);
    
    R = (A2 * A1) * x1;
end

