import ugradio
import numpy as np
import matplotlib.pyplot as plt

sampleRates = float(3.2e6)
LO = 1419.906e6 #40 MHz for example. Keep in mind the LO must be great or equal to 25 MHz, and less that 1750 MHz  (Try at 1419.906 as well)

sdr = ugradio.sdr.SDR(direct=False, center_freq = LO, sample_rate=sampleRates, fir_coeffs = None, gain = 'auto')

nsamples = int(2048) #(4096)
nblocks = int(1024) #about 100k data points
data_3D = sdr.capture_data(nsamples=nsamples, nblocks = nblocks)

#Now decompress your data to a 2D array only saving the real components of the IQ:
data_2D = data_3D[:,:,0]

#power spectrum where power = voltage^2
power = np.mean(np.fft.fftshift(np.abs(np.fft.fft(data_2D)))**2, axis = 0)
#frequency
freqs = np.fft.fftshift(np.fft.fftfreq(nsamples, 1/sampleRates))
# plot to check that you are recieving the expected observed frequency from function generator
plt.semilogy(freqs, power)
#plt.ylim(0,10e3) # This line kinda works with semilogy


plt.grid(True)
plt.show() 

#save your data in .gz format - you will have to unzip this file to analyze
np.savetxt("nodb906_p_no.gz",data_2D) #you will likely get errors saving a 3D array this way - for the purpose of this lab, you do not need to save the full 3D array