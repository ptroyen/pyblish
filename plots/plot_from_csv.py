
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import pandas as pd

fname1 = "def_end_pulse.csv"
fname2 = "no_def_end_pulse.csv"
read1 = pd.read_csv(fname1)
read2 = pd.read_csv(fname2)


arc_length = (read1['arc_length']) * 1000 # now in mm
def_T = read1['T']
no_def_T = read2['T']
def_Te  = read1['Te']
no_def_Te  = read2['Te']
def_Tv  = read1['Tv']
no_def_Tv = read2['Tv']

# Plots
import publish

fig, ax1 = plt.subplots(1,1)
# # ax2 = ax1.twinx()

# print(np.shape(arc_length))

# print(arc_length)

# arc_length = arc_length*1000

# print(arc_length)
ax1.plot(arc_length,def_T,'-',color='black',label='T - D')
ax1.plot(arc_length,no_def_T,'-.',color='black',label='T - ND')


ax1.plot(arc_length,def_Te,'-',color='red',label='Te - D')
ax1.plot(arc_length,no_def_Te,'-.',color='red',label='Te - ND')

ax1.plot(arc_length,def_Tv,'-',color='blue',label='Tv - D')
ax1.plot(arc_length,no_def_Tv,'-.',color='blue',label='Tv - ND')

# ax1.plot(X_d1,OH_d1,'-',color='blue',label='OH - I')
# ax1.plot(X_d2,OH_d2,'-.',color='blue',label='OH - II')
# ax1.plot(X_d3,OH_d3,':',color='blue',label='OH - III')

# ax1.plot(X_d1,O_d1,'-',color='black',label='O - I')
# ax1.plot(X_d2,O_d2,'-.',color='black',label='O - II')
# ax1.plot(X_d3,O_d3,':',color='black',label='O - III')


# for same y in temper as well

# ax2.plot(X_d1,T_d1,'-',color='red',label='T - I')
# ax2.plot(X_d2,T_d2,'-.',color='red',label='T - II')
# ax2.plot(X_d3,T_d3,'-',color='red',label='T - D')

# ax2.plot(X_nd3,T_nd3,'-.',color='r',label='T - ND')

# ax1.plot(X,H_nd,color='black',label='non defocused, y=0')

# ax1.plot(X2,H_d2,'-.',color='blue',label='defocused, y=0.0107')
# ax1.plot(X2,H_nd2,color='blue',label='non defocused, y=0.0107')


# ax1.plot(T_hill,K_hill,'o',color='black',label='Hill & Peterson')
# ax1.grid()
# Change major ticks to show every 20.
# ax1.xaxis.set_major_locator(MultipleLocator(20))
# ax1.yaxis.set_major_locator(MultipleLocator(20))

# # Change minor ticks to show every 5. (20/4 = 5)
ax1.xaxis.set_minor_locator(AutoMinorLocator(4))
ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
# ax1.xaxis.set_minor_locator(AutoMinorLocator())

ax1.grid(':')
ax1.grid(which='minor',linestyle=':')
ax1.grid(which='major',linestyle=':')
ax1.legend(loc=5)
# ax2.legends(loc=2)
ax1.set_ylabel("Temperature [K] ")
ax1.set_xlabel("X [mm]")

plt.xlim([0002.5,0017.25])

# ax1.limitx
# ax2.set_ylabel("Temperature [K]" , color = 'r')
# plt.title("$K_p$")
plt.tight_layout()
plt.yscale('log')
# fig.savefig("Kp_plot.png")
plt.show()


