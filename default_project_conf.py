# -*- coding: utf-8 -*-
"""
Default control parameters for siman

"""
from __future__ import division, unicode_literals, absolute_import 


"""Cluster constants"""
CLUSTERS = {}
DEFAULT_CLUSTER = 'cee'
PATH2PROJECT = '' # path to project on cluster relative to home folder


CLUSTERS['cee'] = {'address':'aksenov@10.30.16.62',
'homepath':'/home/aksenov/',
'schedule':'SLURM',
'corenum':16,
'pythonpath':'/usr/lib64/python2.7/site-packages/numpy',
'vasp_com':'prun /opt/vasp/bin/vasp5.4.1MPI',
}

CLUSTERS['skol'] = {'address':'Dmitry.Aksenov@10.30.17.10',
'homepath':'/home/Dmitry.Aksenov/',
'schedule':'PBS',
'corenum':16,
'pythonpath':'/usr/lib64/python2.7/site-packages/numpy'

}



"""Local constants"""
path_to_potentials = '/home/aksenov/scientific_projects/PAW_PBE_VASP'
pmgkey = "AWqKPyV8EmTRlf1t"

path_to_paper        = '/home/aksenov/Research/CEStorage/aksenov_report/'
PATH2DATABASE        = '/home/aksenov/Data/CEStorage/_aksenov'


geo_folder           = './'
path_to_images       = path_to_paper+'/fig/'
path_to_wrapper      = '/home/aksenov/Simulation_wrapper/'



"""List of constants determined during installation"""
CIF2CELL = True 






"""List of manually added calculations:"""
MANUALLY_ADDED = [# calc name, calc folder, calc des  
    ( 'Li111'        ,"Li",        "2 Li"                                  ),
    ]




















"""
Naming conventions:

endings:
'_ml' - was used to show that this calculation uses manual equilibrium lattice determination and 
contains several versions of identical structures with different
lattice constants. Now not in use, because I always use this method. Usually 16 versions for hcp;

'_r' - calculation with structure constructed for fitted lattice constants; 
Now was replaced with '.f'; Usually one version.
'.ur' - unrelaxed
.r - relaxed atomic positions
.o - optimised cell and volume and atomic positions automatically
'.f'  - fitted
'.fr' - means that current calculation based on the structure for which lattice constants were fitted and
positions of atoms were relaxed. However see description to know for wich set they were fitted and relaxed.
Calculations with '.f' and '.fr' can have different versions which are correspondig to different sets.

.m - only matrix, all impurities were removed and matrix was freezed


letters in name, wich are usually between didgits and element's names:
b - stands for bulk, which denote ideal cells without boundaries.
g - cells with grain boundary;
v - means that impurity is in the volume of grain; far away from boundaries;
i - means that impurity is close to interface plane (grain boundary)

Versions:
20 - usually means that lattice constatns was used from other calculation and this is very good assumtion.


"""


