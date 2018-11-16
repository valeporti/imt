function [] = LPF(fc)

%f = [1:10:10^3];

f=logspace(0,6,200);
H=1./(1+i*f/fc); % uso . para decirle a la funcioón que debe ser multiplicada por todos los alores del vector f
G=20*log10(abs(H));
P=angle(H)*180/pi;
subplot (2,1,1)
semilogx(f,G)
grid on
subplot (2,1,2)
semilogx(f,P)
grid on