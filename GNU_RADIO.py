# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 22:35:10 2025

@author: grans
"""
import numpy as np
import matplotlib.pyplot as plt
import os
datafile = "C:/Users/grans/Documents/Baloon/signal_Tot2.txt"
df = np.fromfile(open(datafile), dtype = np.float32)
plt.plot(df)
#conver power to dbm
dbm = np.zeros(len(df))
if df != 0:
    dbm = 10*np.log10(df) + 30
else:
    dbm = 30
#Start Time = 17:54:03, End Time = 20:25:49
T_trans = 2*60*60 + 31*60 +46 # seconds

Time = np.arange(0,T_trans, T_trans/len(df))

plt.figure(figsize= (6,6))
plt.plot(Time, df)
plt.title("Received Power Over time of the Transmission",fontsize=20)
plt.ylabel("Received Power in Watts", fontsize = 15)
plt.xlabel("Time since transmission Start in Seconds", fontsize = 15)

plt.figure(figsize = (6,6))
plt.plot(Time, dbm)
plt.title('Received Power (dBm) over time of the Transmission',fontsize=20)
plt.ylabel("Received Power (dBm)",fontsize=15)
plt.xlabel("Time since Transmission Start in Seconds", fontsize=15)
dout = (Time,df,dbm)

doutfile = "C:/Users/grans/Documents/Baloon/Scaled.csv"
np.savetxt(datafile, dout, delimiter = ",")
