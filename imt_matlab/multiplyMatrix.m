function M = multiplyMatrix (A, B)

% verify compatibility
[na, ma] = size(A);
[nb, mb] = size(B);

if ma == nb
   M = A * B; 
else
   error ('dimension error');
end