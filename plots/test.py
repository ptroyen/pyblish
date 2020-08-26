# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------
## Set Defaults For Plotting Here
plt.style.use('default')

# Figure Size Definition
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size

## Fonts Details and Typesetting
plt.rcParams["font.family"] = "Arial" ## "Arial"
## plt.rc('font', family='serif', serif='Times')

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#-----------------------------------------------------------------------------

## --------------------------------------------------------------------------
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)


halfwide = 3.5
wide = 7.0

halfheight = halfwide/1.618
height = wide/1.618

fig, ax = plt.subplots(figsize = (6,4)) 

ax.plot(t, s,label='this is a label')
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')

# ax.set_xlim(0, 3*np.pi)
fig.set_size_inches(wide,height)
ax.grid()
ax.legend(loc=1)
fig.tight_layout()
fig.savefig("testw.png")
# plt.savefig('example.pgf')
plt.show()
