function fullSig = AdjustSignals(pks, samplesPerPeriod,fullSig)

others = size(pks,1);
ref = pks(1); % Signal 1 is the reference

for i=2:others
    
    %diff = ceil(mod(pks(i)-ref,samplesPerPeriod/2));
    diff = pks(i)-ref;
    
    if (diff)>samplesPerPeriod/4 % Over 180 off
       fullSig = SkipSig(fullSig,diff);
%       fullSig = DelaySig(fullSig,diff);
    else
       fullSig = DelaySig(fullSig,diff);
%       fullSig = SkipSig(fullSig,diff);
    end
end

end

function sig = DelaySig(sig,gap)

sig = [sig(gap:end); zeros(gap-1,1)];

end

function sig = SkipSig(sig,gap)

sig = [zeros(gap-1,1); sig(1:end-gap)];

end