"""
    import some functions/modules for running notebooks
    examine the working envirorment 
"""

import sys, glob, os, io, logging, socket, warnings

import numpy as np

from pprint import pprint
from copy import deepcopy

# astropy / astropy-afflicite

from astropy.io import fits
from astropy.io import ascii
from astropy.wcs import WCS
from astropy.cosmology import Planck13
from astropy.coordinates import SkyCoord
import astropy.units as u
import regions

from spectral_cube import SpectralCube
from spectral_cube.utils import SpectralCubeWarning
warnings.filterwarnings(action='ignore', category=SpectralCubeWarning,append=True)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore")

# matplotlib

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.ticker as plticker
mpl.use("Agg")
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams.update({'font.size': 12})
mpl.rcParams["font.family"] = "serif"
mpl.rcParams["image.origin"]="lower"
mpl.rcParams['agg.path.chunksize'] = 10000
mpl.rc('text', usetex=True)

# ism3d

import ism3d
from ism3d.uvhelper.proc import setLogfile
from ism3d.uvhelper.imager import invert
from ism3d.uvhelper.proc import rmColumns
from ism3d.uvhelper.proc import rmPointing
from ism3d.uvhelper.ms import read_ms
from ism3d.uvhelper import invert_ft,make_psf
from ism3d.uvhelper.ft import advise_header

from ism3d.utils.io import to_hdf5
from ism3d.utils.io import from_hdf5

from ism3d.utils.misc import check_config
# from ism3d.model import makepb
# from ism3d.vis_utils import gpredict_ms
# from ism3d.vis_utils import cpredict_ms
# from ism3d.utils import hextract
# from ism3d.utils import pprint
# from ism3d.tests.plt_compare import comp_dirtymap,comp_specs

# casa6

from casatasks import mstransform, tclean
from casatasks import tclean

# check-up

print('\n'+ism3d.__version__)
print(ism3d.__email__)
print('\nworking dir: {}\n'.format(os.getcwd()))

ism3d.logger_status(root=False)
ism3d.check_config()

"""
if  'hypersion' or 'mini' in socket.gethostname() :
    os.chdir(ism3d.__demo__+'/../ism3d/tests/results/test_discretize')
ism3d.logger_config(logfile='ism3d.log',loglevel='DEBUG',logfilelevel='DEBUG')
"""









