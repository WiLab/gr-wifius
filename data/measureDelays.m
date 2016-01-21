%%
fs = 100e6/128;   % Sample rate
freq = 10000;   % Frequency of sinusoid

samplesPerPeriod = fs/freq;
samplesPerRadian = 2*pi/samplesPerPeriod;
samplesPerDegree = 360/samplesPerPeriod;

x=read_complex_binary('channel0_complex_1_6_2015.bin');
y=read_complex_binary('channel1_complex_1_6_2015.bin');
z=read_complex_binary('channel2_complex_1_6_2015.bin');

f = 1e3;g = 100;
x = real(x(1:f));y = real(y(1:f));z = real(z(1:f));

[~,pksX] = findpeaks(x(1:g),'MinPeakDistance',samplesPerPeriod/2);
[~,pksY] = findpeaks(y(1:g),'MinPeakDistance',samplesPerPeriod/2);
[~,pksZ] = findpeaks(z(1:g),'MinPeakDistance',samplesPerPeriod/2);

m = min([length(pksX),length(pksY),length(pksZ)]);

pksX = pksX(1:m);pksY = pksY(1:m);pksZ = pksZ(1:m);

d = mode(pksX-pksY);
e = mode(pksX-pksZ);

X = pksX(1);
Y = pksY(1);
Z = pksZ(1);

%x = [zeros(e,1);x];
%y = [zeros(e,1);y];
%z = [zeros(10,1);z];
%x = x(samplesPerPeriod-e:end);
%y = y(samplesPerPeriod-e:end);

        plot(x(X:end));
hold on;plot(y(Y:end),'r');hold off;
hold on;plot(z(Z:end),'k');hold off;
axis([0 1000 1.5*min(x) 1.5*max(x)])

figure(2);
%plot(x(e:end));
plot(x(1:end));
hold on;plot(z(1:end),'k');hold off;
axis([0 1000 1.5*min(x) 1.5*max(x)])


%%
scale = max(real(x));

all = [x,y,z];

plot(real(all(1:1e3,:)));

maxPeriods = 30;
n = (samplesPerPeriod)*maxPeriods; % Samples to view

%% Phase Estimate 2

maxPeriods = maxPeriods/2;
twoPeriods = samplesPerPeriod*2;

t2= 0:1/fs:(n-1)/fs;
t = t2(1:twoPeriods);
theta_est = zeros(maxPeriods,1);

for g=1:maxPeriods
    
    s1_p = x( (g-1)*twoPeriods + 1: g*twoPeriods );
    s2_p = y( (g-1)*twoPeriods + 1: g*twoPeriods );
    
    % Measure Peak distances
    [~,ind_1] = max(s1_p(1:samplesPerPeriod));
    [~,ind_2] = max(s2_p(ind_1+1:ind_1+samplesPerPeriod-1));
    %[~,ind_2] = max(s2_p(1:samplesPerPeriod));
    ind_2 = ind_2 + ind_1;

    if (ind_2 > samplesPerPeriod/2)
        ind_2 = ind_2 - samplesPerPeriod;
    end

    difference = ind_1 - ind_2;
    
    differenceInRadians = (difference*samplesPerRadian);
    differenceInDegrees = (difference*samplesPerRadian)*180/pi;
    % Unwrap
    if difference < 0
        differenceInRadians = differenceInRadians+2*pi;
        differenceInDegrees = differenceInDegrees+360;
    end
    
    disp(differenceInRadians);
    theta_est(g) = mod(differenceInRadians,2*pi);
       
    % %% Plot
    if true
%         subplot(2,1,1);
        plot(t.*fs,s1_p,'b',t.*fs,s2_p,'r',...
            ind_1.*ones(size(t)), scale.*linspace(-1,1,length(t)),'b',...
            ind_2.*ones(size(t)), scale.*linspace(-1,1,length(t)),'r');
%         subplot(2,1,2);
%         plot((1:length(sg1))./fs,sg1,'g',...
%              (1:length(sg2))./fs,sg2,'k');
            
        pause(2);
    end
    
    
    
end
