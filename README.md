# Scientific_Figure_Matplotlib

This is a simple Python library for producing publication quality scientific figure.

## Installation

Install the colormap cmcrameri from https://pypi.org/project/cmcrameri/ as well as matplotlib
Just copy plotting_default.py and utils_colors.py

```python
import plotting_default
from utils_colors import colorblind_list,lighten_color
```

## Usage

```python
plt.figure(figsize=(15,15))
# Now, create the gridspec structure, as required
gs = gridspec.GridSpec(2,3, height_ratios=[1,0.05], width_ratios=[0.2,1,0.2])

ax0 = plt.subplot(gs[0,:]) # place it where it should be.

plt0 = ax0.imshow(np.exp(np.random.randn(10,10)),cmap=cmc.batlowW,vmin=0,vmax=5)
ax0.set_xticks(np.arange(10))
ax0.set_xticklabels([f'column {i}' for i in range(10)],rotation=45,ha='left')
ax0.xaxis.set_label_position('top') 
ax0.xaxis.tick_top()

ax0.set_yticks(np.arange(10))
ax0.set_yticklabels([f'row {i}' for i in range(10)])
ax0.minorticks_off()

ax1 = plt.subplot(gs[1,1]) # place it where it should be.


# colorbar
cb = plt.colorbar(plt0, cax=ax1, orientation = 'horizontal',fraction=0.046, pad=0.04, ticklocation = 'bottom')
cb.set_label(r'Colorbar !', labelpad=10)
plt.show()
```

