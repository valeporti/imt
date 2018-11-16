function N = factorielle(n)

N = 1;

if n > 0
    for i = 1:n
       N = N * i; 
    end
end

