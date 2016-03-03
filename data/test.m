%% EE779 Computing Assignment 3 (Q1a) ($$\theta = 15\,^{\circ}$)
% Ashwin Kachhara, 10d070048
%%
% Specifying data required: Covariance matrix P and the value of theta.
P = eye(1);
theta = 15;
%%
% Preparing the empty arrays 
y = zeros(4, 100, 50);
phi1 = zeros(50, 128);
phi2 = zeros(50, 128);
theta1 = zeros(50, 1);
theta2 = zeros(50, 1);
%% Data, Processing
% Because of the noise component in generation of the ULA data, we will
% take fifty iterations of ULA data generation and average the final
% results.
%%
% In each iteration, we calculate a new ULA data set, the corresponding
% spectra via Beamforming, Capon's method. Also, we calculate the Direction
% of arrival estimates using the Root Music method as well as ESPRIT
% method.
for i=1:50,
    y(:,:,i) = uladata(theta ,P,100,1,4,0.5);
    
    %phi1(i,:) = beamform(y(:,:,i), 128, 0.5);
    %phi2(i,:) = capon_sp(y(:,:,i), 128, 0.5);
    theta1(i,:) = root_music_doa(y(:,:,i), 1, 0.5);
    theta2(i,:) = reallocation(4,1,y(:,:,i), 100, 2);
end
%%
% % Beamforming: We calculate the average spectrum corresponding to each set
% % of ULA data and plot it. 
% phi1avg(1:128) = mean(phi1(:,1:128));
% figure(1)
% plot(20*log10(phi1avg))
% ylabel('dB')
% title('Averaged Spatial Spectrum: Beamforming method');
% xlabel('n')
% 
% %%
% % Capon's method: We calculate the average spectrum corresponding to each set
% % of ULA data and plot it. 
% phi2avg(1:128) = mean(phi2(:,1:128));
% figure(2)
% plot(20*log10(phi2avg))
% ylabel('dB')
% title('Averaged Spatial Spectrum: Capon''s method');
xlabel('n')

%%
% For Root-Music, we get estimated direction of arrival. We will attempt to
% see the spread of estimates by plotting the estimates from each data set
% with the same height
figure(3)
stem(theta1(:), ones(50,1));
title('Root-Music method')
xlabel('Angle')
axis([0 180 0 20]);

% %%
% % For ESPRIT, we get estimated direction of arrival. We will attempt to
% % see the spread of estimates by plotting the estimates from each data set
% % with the same height
% figure(4)
% stem(theta2(:), ones(100,1));
% title('ESPRIT method')
% xlabel('Angle')

%% Conclusions



