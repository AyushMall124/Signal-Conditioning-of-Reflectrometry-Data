function []=GoodMethod()
%Read Data -> HighPass Filter -> BandPass Filter -> Homomorphic method

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% INITIALISATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Load data
filename = 'linF-250us-5MSps-108p5cm01.asc';
I_data = load(filename);
filename = 'linF-250us-5MSps-108p5cm02.asc';
Q_data = load(filename);
%Snip data
%t = I_data(5200:15200,1);
%I = I_data(5200:15200,2);
%Q = Q_data(5200:15200,2);
t = I_data(2700:5200,1);
I = I_data(2700:5200,2);
Q = Q_data(2700:5200,2);
signal = I+1j*Q;

%Sampling frequency
%fs = 10e6;
fs = 1/(t(2)-t(1))
len = length(t)

%Time Plot data
%{
figure
subplot(2,1,1)
plot(t,I)
grid
subplot(2,1,2)
plot(t,Q)
grid
%}
%FFT Plot data
%{
figure
fftI = fft(signal);
Ilen = length(fftI);
Iz = fftshift(fftI);
fI = ((-0.5*Ilen+0.5):(0.5*Ilen-0.5))*(fs/Ilen);
plot(fI,abs(Iz));
grid
xlim([0,5e6]);
ylim([0,100])
%}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% BASELINE WANDERING REMOVAL
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%HighPass filter
orderh = 2;
highcut = 1e5;
fc = highcut;
[B,A] = butter(orderh,2*fc/fs,'high'); 
filt_signal = filtfilt(B,A,signal);

%Time plot
%{
figure
subplot(2,1,1)
plot(t,real(filt_signal));
grid
subplot(2,1,2)
plot(t,imag(filt_signal));
grid
%}
%FFT plot
%{
figure
fftI = fft(filt_signal);
Ilen = length(fftI);
Iz = fftshift(fftI);
fI = ((-0.5*Ilen+0.5):(0.5*Ilen-0.5))*(fs/Ilen);
plot(fI,abs(Iz));
grid
xlim([0,5e6]);
ylim([0,100]);
%}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SIGNAL CONDITIONING
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%BandPass Filter
orderb = 1;
fc1 = 1e5;
fc2 = 1.6e6;
[B,A] = butter(orderb,[2*fc1,2*fc2]/fs,'bandpass'); 
cond_signal = filtfilt(B,A,filt_signal);

%Time plot
%{
figure
subplot(2,1,1)
plot(t,real(cond_signal));
grid
subplot(2,1,2)
plot(t,imag(cond_signal));
grid
%}
%FFT plot
%{
figure
fftI = fft(cond_signal);
Ilen = length(fftI);
Iz = fftshift(fftI);
fI = ((-0.5*Ilen+0.5):(0.5*Ilen-0.5))*(fs/Ilen);
plot(fI,abs(Iz));
grid
xlim([0,5e6]);
ylim([0,100]);
%}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SIGNAL NORMALISATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Homomorphic method 
inst_phase = unwrap(angle(cond_signal));
%norm_signal = cos(inst_phase);
norm_signal = cos(inst_phase) + 1j*sin(inst_phase);

%Time plot
%{
figure
subplot(2,1,1)
plot(t,real(norm_signal));
grid
subplot(2,1,2)
plot(t,imag(norm_signal));
grid
%}
%FFT plot
%{
figure
fftI = fft(norm_signal);
Ilen = length(fftI);
Iz = fftshift(fftI);
fI = ((-0.5*Ilen+0.5):(0.5*Ilen-0.5))*(fs/Ilen);
plot(fI,abs(Iz));
grid
xlim([0,5e6]);
%ylim([0,100]);
%}


%Spectrogram
%
nfft = 256;
nov = 64;
figure
spectrogram(signal,hamming(nfft),nov,nfft,fs,'centered','yaxis');
figure
spectrogram(filt_signal,hamming(nfft),nov,nfft,fs,'centered','yaxis');
figure
spectrogram(cond_signal,hamming(nfft),nov,nfft,fs,'centered','yaxis');
figure
spectrogram(norm_signal,hamming(nfft),nov,nfft,fs,'centered','yaxis');
%}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% STORING RESULTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Write data into file
%{
A = [t'; (imag(norm_signal))'; (real(norm_signal))'];

filename = fopen('GoodM_mat.txt','wt');
for i = 1:size(A,1)
    fprintf(filename,'%e ',A(i,:));
    fprintf(filename,'\n');
end
fclose(filename);
%}

end
