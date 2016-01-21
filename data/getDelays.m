%%
fs = 100e6/128;   % Sample rate
freq = 10000;   % Frequency of sinusoid

samplesPerPeriod = fs/freq;

x=read_complex_binary('channel0_complex_1_6_2015.bin');
y=read_complex_binary('channel1_complex_1_6_2015.bin');
z=read_complex_binary('channel2_complex_1_6_2015.bin');

x = real(x);y = real(y);z = real(z);

[~,pksX] = findpeaks(x,'MinPeakDistance',samplesPerPeriod/2);
[~,pksY] = findpeaks(y,'MinPeakDistance',samplesPerPeriod/2);
[~,pksZ] = findpeaks(z,'MinPeakDistance',samplesPerPeriod/2);

X = pksX(1);Y = pksY(1);Z = pksZ(1);

plot(x(X:end));
hold on;plot(y(Y:end),'r');hold off;
hold on;plot(z(Z:end),'k');hold off;
axis([0 1000 1.5*min(x) 1.5*max(x)])