function [pkIndx,otherPeaks] = FixDelays(sig,samplesPerPeriod)

others = size(sig,2);

% Assume that channel 0 is reference

% Get first peak of channel 0
ref = sig(:,1);
[~,pkIndx] = max(ref(1:samplesPerPeriod));

% Get peaks after reference first peak
otherPeaks = zeros(others-1,1);
for x=2:others
    y = sig(:,x);
    %[~,otherPeaks(x-1)] = max(y(1+pkIndx:samplesPerPeriod+pkIndx));
    [~,otherPeaks(x-1)] = max(y(1:samplesPerPeriod));
    % unbias
    %otherPeaks(x-1) = otherPeaks(x-1) + pkIndx;
end
end



