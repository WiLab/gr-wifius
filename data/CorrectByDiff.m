function [offset, delay,fullSig] = CorrectByDiff(signals,period,delay,fullSig)

maxShift = floor(period/2);

ref = signals(:,1);
chan2 = signals(:,2);

diff = zeros(maxShift+1,1);
diff2 = zeros(maxShift+1,1);

for i=0:maxShift
    % Shift signal forward
   diff(i+1) = sum( abs( ref(i+1:end) - chan2(1:end-i) ) ); 
    % Shift backwark
   diff2(i+1) = sum( abs( ref(1:end-i) - chan2(i+1:end) ) ); 
end

if min(diff)<min(diff2)
   [~,offset] = min(diff);
   offset = -offset;
else
   [~,offset] = min(diff2);
end

delay = delay + 0.01*offset;
disp(delay);

plot([ref,chan2]);


end



function sig = DelaySig(sig,gap)

sig = [sig(gap:end); zeros(gap-1,1)];

end

function sig = SkipSig(sig,gap)

sig = [zeros(gap-1,1); sig(1:end-gap)];

end

