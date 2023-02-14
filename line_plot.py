import numpy as np

# Plotting
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
from matplotlib.ticker import MultipleLocator


import plotting_default
from utils_colors import colorblind_list,lighten_color


x = np.linspace(0,10,1000)

fig,ax = plt.subplots(figsize=(8,5))
for i in range(3):
    plt.plot(x,np.sin(x)+0.1*i,label='blue',lw=2,color=colorblind_list[0])
plt.plot(x,np.cos(x),color=colorblind_list[1],label='orange',lw=2)

# Avoid Repeatition in legend
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(),bbox_to_anchor=(1,1))

plt.xlabel('Time')
plt.ylabel('Amplitude')



fig,ax = plt.subplots(figsize=(8,5))
x = np.linspace(0,10,1000)
for i in range(10):
    plt.plot(x,np.sin(x+i*0.1),label=i,lw=1.5)
    
ax.legend(title='Order',bbox_to_anchor=(1,1))


ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(.5))

ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(.1))


plt.xlabel(r'Current ($\mu$A)')
plt.ylabel('Voltage (mV)')


fig,ax = plt.subplots(figsize=(8,5))
x = np.linspace(0,10,1000)
plt.plot(x,np.sin(x),label='Curve',lw=1.5)
    
ax.fill_between(x, np.sin(x)+0.3, np.sin(x)-0.3, color=colorblind_list[0], alpha=0.4)

ax.legend(title='Order',bbox_to_anchor=(1,1))

ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(.5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(.1))

plt.xlabel(r'Current ($\mu$A)')
plt.ylabel('Voltage (mV)')


fig,ax = plt.subplots(figsize=(8,5))
x = np.linspace(0,10,1000)

for i in range(0,10):
    plt.plot(x,np.sin(x)+0.1*i,lw=1.5,color = lighten_color(colorblind_list[0],min(1,0.1+0.05*i)))
    

ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(.5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(.1))

plt.xlabel(r'Current ($\mu$A)')
plt.ylabel('Voltage (mV)')
plt.savefig('test.svg')
plt.show()