import ugradio
import numpy as np
import matplotlib.pyplot as plt

sampleRates = float(3.2e6)
sdr = ugradio.sdr.SDR(direct=True, sample_rate=sampleRates, fir_coeffs = None, gain = 'auto')

nsamples = int(2048) #(4096)
nblocks = int(1024) #about 100k data points
data = sdr.capture_data(nsamples=nsamples, nblocks = nblocks)

#power spectrum where power = voltage^2
power = np.mean(np.fft.fftshift(np.abs(np.fft.fft(data)))**2, axis = 0)
#frequency
freqs = np.fft.fftshift(np.fft.fftfreq(nsamples, 1/sampleRates))
# plot to check that you are recieving the expected observed frequency from function generator
plt.semilogy(freqs, power)
plt.show() 

#save your data in .gz format - you will have to unzip this file to analyze
np.savetxt("dataName.gz",data)