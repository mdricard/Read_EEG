import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

fn = 'C:/Data/AA001_clean_eeg.mat'
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

def get_channel_max(c1):
    """
    This function gets the max of an eec channel
    :param c1: input eeg channel
    :return: max
    """
    c1_max = c1[0]
    for i in range(1, len(c1)):
        if c1[i] > c1_max:
            c1_max = c1[i]
            max_pt = i
    return c1_max, max_pt

def plot_eeg(c1_mean, c1_max, max_pt):
    plt.plot(c1)
    plt.hlines(c1_mean, 0, len(c1), colors='k', linestyles='solid')
    #plt.scatter(max_pt, c1_mean, size=3, color='r')
    plt.scatter(max_pt, c1_max, s=10, color='r')
    plt.ylabel('EEG Signal')
    plt.xlabel('Time')
    plt.grid(True)
    plt.show()

def get_channel_mean(channel):
    sum = 0.0
    cntr = 0
    for i in range(len(channel)):
        sum += channel[i]
        cntr += 1
    mean_eeg = sum / cntr
    return mean_eeg

fn = 'C:/Data/AA001_clean_events.mat'
ev = sio.loadmat(fn)
events = np.array(ev['rawEvents'])

c1_mean = get_channel_mean(c1)
print('Channel 1 mean: ', c1_mean)
print(ev)
c1_correct = c1 - c1_mean
c1_max, max_pt = get_channel_max(c1)
plot_eeg(c1_mean, c1_max, max_pt)



 



