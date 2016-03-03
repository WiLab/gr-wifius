function doa = root_music_doa(Y,n,d)
%
% The MUSIC method for direction of arrival estimation
%
% call doa=root_music_doa(Y,n,d)
%
%      Y    <- received data where columns are from each antenna 
%      n    <- the number of transmitted signals
%      d    <- sensor spacing in wavelengths
%      doa  -> the vector of DOA estimates

% Based on the script by R. Moses (1996,2005)

% Good References:
% http://www.iaeng.org/publication/IMECS2008/IMECS2008_pp1507-1510.pdf
%
%

% The root-MUSIC method is based on the eigenvectors of the
% sensor array correlation matrix R. It obtains the signal estimation
% by examining the roots of the spectrum polynomial. The peaks
% in the spectrum space correspond to the roots of the polynomial
% lying close to the unit circle. 

% Get system dimensions
[elements,samples] = size(Y);

% compute the sample covariance matrix
R = Y*Y'/samples;

% do the eigendecomposition; use svd because it sorts eigenvalues
[U,~,~] = svd(R);

% Pickout eigenvectors that span signal+noise subspace
G = U(:,n+1:elements);
C = G*G';   % mxm

% find the coefficients of the polynomial in (4.5.16)
a = zeros(2*elements-1,1);
for kk = 1:2*elements-1,
    a(kk,1) = sum(diag(C,kk-elements));
end

% Get roots of spectrum polynomial
ra = roots(a);

% find the n roots of the a polynomial that are nearest and inside the unit circle,
[~,ind] = sort(abs(ra));
rb = ra(ind(1:elements-1));

% pick the n roots that are closest to the unit circle
[~,I] = sort(abs(abs(rb)-1));
w = angle(rb(I(1:n)));


% compute the doas
doa = asin(w/d/pi/2)*180/pi;


return
