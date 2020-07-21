"""
    import some functions/modules for running notebooks
    examine the working envirorment 
"""

import sys, glob, os, io, logging, socket, warnings, time

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

from ism3d.uvhelper.imager import invert
from ism3d.uvhelper.ms import rmColumns
from ism3d.uvhelper.ms import rmPointing
from ism3d.uvhelper.ms import read_ms, write_ms
from ism3d.uvhelper import invert_ft,make_psf
from ism3d.uvhelper.ft import advise_header
from ism3d.xyhelper.cube import hextract

from ism3d.utils.io import to_hdf5
from ism3d.utils.io import from_hdf5
from ism3d.visualize.nb import make_gif, show_gif
from ism3d.utils.misc import check_config

from ism3d.visualize.plts import im_grid
from ism3d.visualize.plts import plt_rcProf

from ism3d.interface import read_inp, write_inp, inp_to_mod
from ism3d.utils.meta import create_header

from ism3d.arts.sparse import clouds_from_disk3d,clouds_morph,clouds_discretize_2d
from ism3d.arts.apmodel2d import eval_apmodel2d
from ism3d.arts.sparse import clouds_from_obj
from ism3d.maths.geometry import points_in_triangle


from ism3d.arts.lens import sie_rt
from ism3d.utils.misc import prepdir
from ism3d.arts.apmodel2d import eval_apmodel2d

from ism3d.simxy.render import xy_render
from ism3d.simuv.render import uv_render
from ism3d.modeling.model import model_realize
from ism3d.simxy.render import render_apmodel2d as xy_render_apmodel2d
from ism3d.simxy.render import render_spmodel3d as xy_render_spmodel3d
from ism3d.simxy.render import render_spmodel3d_xyz as xy_render_spmodel3d_xyz
from ism3d.simxy.render import render_lens as xy_render_lens

ism3d.logger_config(logfile='ism3d.log',loglevel='INFO',logfilelevel='INFO')
# ism3d.logger_config(logfile='ism3d.log',loglevel='DEBUG',logfilelevel='DEBUG')

# from ism3d.model import makepb
# from ism3d.vis_utils import gpredict_ms
# from ism3d.vis_utils import cpredict_ms
# from ism3d.utils import hextract
# from ism3d.utils import pprint
# from ism3d.tests.plt_compare import comp_dirtymap,comp_specs

# casa6

from casatasks import mstransform, tclean, listobs
from casatasks import tclean

# check-up


from ism3d.xyhelper.sky import linear_offset_coords
from IPython.display import display, clear_output
import ipyvolume as ipv


ism3d.check_config()
ism3d.logger_status()


"""
if  'hypersion' or 'mini' in socket.gethostname() :
    os.chdir(ism3d.__demo__+'/../ism3d/tests/results/test_discretize')
"""









