fs = 100e6/256;   % Sample rate
freq = 10000;   % Frequency of sinusoid

samplesPerPeriod = floor(fs/freq);

x=read_complex_binary('channel0_complex_1_6_2015.bin');
y=read_complex_binary('channel1_complex_1_6_2015.bin');
z=read_complex_binary('channel2_complex_1_6_2015.bin');

x = real(x);y = real(y);

% Add some significant delay
%y = [zeros(10,1);y(1:end-10)];
y = [y(11:end);zeros(10,1)];

twoPeriods = 4*samplesPerPeriod;
p = floor(length(x)/twoPeriods);

% Starting delay 
lastDelay = 0;

yorg = y;

for u = 1:p
   
    indexs = ((u-1)*twoPeriods+1):u*twoPeriods;
    x1 = x(indexs);
    % Use last delays
    y1 = y(floor(lastDelay)+indexs);    
    sig = [x1,y1];
    [offset,lastDelay] = CorrectByDiff(sig,samplesPerPeriod/2,lastDelay,y);
    pause(0.1);
    
end