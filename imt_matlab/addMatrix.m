function M = addMatrix(A, B)

 if size(A) ~= size(B)
    M = A + B;
 else 
    error('dimension error');
 end
             