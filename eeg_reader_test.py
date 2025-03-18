import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

fn = 'D:/Biological Python Data/AA001_clean_eeg.mat'
data = sio.loadmat(fn)
eeg = np.array(data['eeg'])
c1 = eeg[:, 0]
c2 = eeg[:, 1]  
c3 = eeg[:, 2]
c4 = eeg[:, 3]
c5 = eeg[:, 4]
c6 = eeg[:, 5]
c7 = eeg[:, 6]
c8 = eeg[:, 7]
c9 = eeg[:, 8]
c10 = eeg[:, 9]
c11 = eeg[:, 10]
c12 = eeg[:, 11]
c13 = eeg[:, 12]
c14 = eeg[:, 13]
c15 = eeg[:, 14]
c16 = eeg[:, 15]
c17 = eeg[:, 16]
c18 = eeg[:, 17]
c19 = eeg[:, 18]
c20 = eeg[:, 19]
c21 = eeg[:, 20]
c22 = eeg[:, 21]
c23 = eeg[:, 22]
c24 = eeg[:, 23]
c25 = eeg[:, 24]
c26 = eeg[:, 25]
c27 = eeg[:, 26]
c28 = eeg[:, 27]
c29 = eeg[:, 28]
c30 = eeg[:, 29]
c31 = eeg[:, 30]
c32 = eeg[:, 31]
c33 = eeg[:, 32]
c34 = eeg[:, 33]
c35 = eeg[:, 34]
c36 = eeg[:, 35]
c37 = eeg[:, 36]
c38 = eeg[:, 37]
c39 = eeg[:, 38]
c40 = eeg[:, 39]
c41 = eeg[:, 40]
c42 = eeg[:, 41]
c43 = eeg[:, 42]
c44 = eeg[:, 43]
c45 = eeg[:, 44]
c46 = eeg[:, 45]
c47 = eeg[:, 46]
c48 = eeg[:, 47]
c49 = eeg[:, 48]
c50 = eeg[:, 49]
c51 = eeg[:, 50]
c52 = eeg[:, 51]
c53 = eeg[:, 52]
c54 = eeg[:, 53]
c55 = eeg[:, 54]
c56 = eeg[:, 55]
c57 = eeg[:, 56]
c58 = eeg[:, 57]
c59 = eeg[:, 58]
c60 = eeg[:, 59]
c61 = eeg[:, 60]
c62 = eeg[:, 61]
fn = 'D:/Biological Python Data/AA001_clean_events.mat'
ev = sio.loadmat(fn)
events = np.array(ev['rawEvents'])
plt.plot(c1)
plt.ylabel('EEG Signal')
plt.xlabel('Time')
plt.grid(True)
plt.show()



 



