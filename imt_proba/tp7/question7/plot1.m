
errorsume=zeros(100,1);
for i=1:100
    errorsume(i,1)=errorsum2(i*10000,2);
end
figure(5)
plot(errorsume)

