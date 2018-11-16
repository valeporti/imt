lambda=2;
meani=zeros(5000);
variancei=zeros(5000);
errormeani=zeros(5000);
errorvariancei=zeros(5000);
for i=1:5000
    
    U = rand(i, 1); % generation of uniform R.V.}
    Y = ( - 1 / lambda) * log(1 - U);

    meani(i)=mean(Y);
    variancei(i)=var(Y);
end
for i=1:5000
    
    

    errormeani(i)=meani(i)-0.5;
    errorvariancei(i)=variancei(i)-0.25;
end

figure(1)
plot(meani)
figure(2)
plot(variancei)
figure(3)
plot(errormeani)
figure(4)
plot(errorvariancei)
