function M = createCelsiusFar(increment, de, a )

M = [];
for ii = de : increment : a
    value = 5 / 9 * ii - 32;
    M = [M ; [ii value]];
end


