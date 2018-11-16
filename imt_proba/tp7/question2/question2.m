% NORMAL SAMPLES USING BOX-MUELLER METHOD
% DRAW SAMPLES FROM PROPOSAL DISTRIBUTION
u = rand(2, 10000);
r = sqrt(-2*log(u(1,:)));
theta = 2*pi*u(2,:);
x = r.*cos(theta);
y = r.*sin(theta);
z1=2*x+5;
z2=2*y+5;

 
% DISPLAY BOX-MULLER SAMPLES
figure(1)
% X SAMPLES
hist(x,100)
colormap hot;axis square
title(sprintf('Box-Muller Samples X\n Mean = %1.2f\n Variance = %1.2f',mean(x),var(x)))

 
% Y SAMPLES
figure(2)
hist(y,100)
colormap hot;axis square
title(sprintf('Box-Muller Samples Y\n Mean = %1.2f\n Variance = %1.2f\n',mean(y),var(y)))

figure(3)
[ftshist,binpos] = hist(z1,100);
h_z1 = hist(z1,100);
plot(h_z1, 'r');
colormap hot;axis square
title(sprintf('Box-Muller Samples Z1\n Mean = %1.2f\n Variance = %1.2f\n',mean(z1),var(z1)))
h_z1_normalised= zeros(length(h_z1));
a=sum(h_z1)*(binpos(2)-binpos(1));
for i = 1:length(h_z1)
    h_z1_normalised(i)=h_z1(i)/a;
end
figure(4)
plot(h_z1_normalised, 'b');
colormap hot;axis square
title(sprintf('Box-Muller Samples Z1 normalised histogram\n Mean = %1.2f\n Variance = %1.2f\n',mean(z1),var(z1)))
    

