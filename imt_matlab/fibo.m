function n = fibo(k)

f = [0 1];

if k == 0
    n = f(1);
elseif k == 1
    n = f(2);
else
    flag = 1;
    n = 1;
    for i = 2 : k
        n = f(1) + f(2);
        f(1) = f(2);
        f(2) = n;
    end
end



    