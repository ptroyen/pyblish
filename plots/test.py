import numpy as np
import matplotlib.pyplot as plt
## Edit "publish.py" to change default parameters
import publish

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

## To import data from ".txt" file
# fname = 'name.txt'
# read = np.loadtxt(fname)
# column_1 = read[:,0]
# column_2 = read[:,1]


# For resizing-figures
wide = 7.0
height = wide/1.618
halfwide = wide/2
halfheight = height/2


fig, ax = plt.subplots(figsize = (6,4)) 

ax.plot(t,s,'.-',label='this is a label')
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='A Simple Plot')

# ax.set_xlim(0, 3*np.pi)
fig.set_size_inches(wide,height)
# ax.grid()
ax.legend(loc=1)
fig.tight_layout()
fig.savefig("testw.png")
plt.show()
