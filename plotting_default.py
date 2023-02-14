import matplotlib as mpl
import matplotlib.pyplot as plt
from utils_colors import colorblind_list
import cmcrameri.cm as cmc
from cycler import cycler

##########
# FONTS: #
##########

'''
# Default fonts - only used if usetex = False. The fontsize remains important though.
mpl.rc('font',**{'family':'sans-serif', 'serif':['Computer Modern Serif'], 
             'sans-serif':['Helvetica'], 'size':16, 
             'weight':500, 'variant':'normal'}) 

# The default matplotlib LaTeX - only matters if usetex=False.
mpl.rc('mathtext',**{'default':'regular','fontset':'cm', 
                 'bf':'monospace:bold'})
mpl.rc('text', **{'usetex':False}) 
'''


mpl.rc('font', **{'family': 'sans-serif','sans-serif':'DejaVu Sans'})
mpl.rc('mathtext',**{'fontset':'dejavusans'})
mpl.rc('text',**{'usetex':False})

###########
# COLORS: #
########### 

mpl.rc('axes',**{'prop_cycle':cycler('color',colorblind_list)})

mpl.rc('image', cmap=cmc.batlowW)


###########
# SIZE  : #
########### 

mpl.rc('figure',**{'figsize':(3.5,2.5)})

fsize = 15
tsize = 18
tdir = 'in'
major_size = 4.0
minor_size = 2.0
major_w = 1
minor_w = 1
lwidth = 1
lhandle = 2.0


plt.style.use('default')
plt.rcParams['text.usetex'] = False

plt.rc('font', family='serif')


plt.rcParams['legend.handlelength'] = lhandle

mpl.rc('xtick',**{'direction':'in',
                  'labelsize':fsize,
                  'major.size':major_size,
                  'major.width':major_w,
                  'minor.size':minor_size,
                  'minor.width':minor_w,
                  'minor.visible':True,
                  'top':True
                  })

mpl.rc('ytick',**{'direction':'in',
                  'labelsize':fsize,
                  'major.size':major_size,
                  'major.width':major_w,
                  'minor.size':minor_size,
                  'minor.width':minor_w,
                  'minor.visible':True,
                  'right':True
                  })

mpl.rc('axes',**{'linewidth':lwidth,
                 'labelsize':fsize,
                 })
mpl.rc('grid',**{'linewidth':lwidth})
mpl.rc('lines',**{'linewidth':lwidth,
                  'markersize':6})

mpl.rc('legend',**{'frameon':False,
                   'fontsize':fsize,
                   'title_fontsize':fsize})

