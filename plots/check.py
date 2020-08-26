# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------
## Set Defaults For Plotting Here
plt.style.use('default')

# Figure Size Definition
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 6.5/2
fig_size[1] = fig_size[0] / 1.68
plt.rcParams["figure.figsize"] = fig_size

## Fonts Details and Typesetting
plt.rcParams["font.family"] = "serif" ## "Arial"
## plt.rc('font', family='serif', serif='Times')

SMALL_SIZE = 10
MEDIUM_SIZE = 12
BIGGER_SIZE = 14

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#-----------------------------------------------------------------------------


# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)


halfwide = 3.487
wide = 2*halfwide

halfheight = halfwide/1.618
fullheight = wide/1.618

fig, ax = plt.subplots(figsize = (6,4)) 

ax.plot(t, s,label='this is a label')
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')

# ax.set_xlim(0, 3*np.pi)
fig.set_size_inches(halfwide,halfheight)
ax.grid()
ax.legend(loc=1)
fig.tight_layout()
fig.savefig("test.png")
# plt.savefig('example.pgf')
plt.show()

