clear all
clc

q_samples = 2000;
mean_v=zeros(q_samples);
variance_v=zeros(q_samples);

for T =1:q_samples
    u = rand(2, T);
    r = sqrt(-2*log(u(1,:)));
    theta = 2*pi*u(2,:);
    x = r.*cos(theta);
    y = r.*sin(theta);
    z1=2*x+5;
    z2=2*y+5;
    mean_v(T)=mean(z1);
    variance_v(T)=var(z2);
end
figure(1)
plot(mean_v)
figure(2)
plot(variance_v)
mean_v=mean_v-5;
variance_v=variance_v-4;
figure(3)
plot(mean_v)
figure(4)
plot(variance_v)

    
    
