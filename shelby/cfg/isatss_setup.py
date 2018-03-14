# isatss configuration
import os

# This file goes in ISatSS/host directory

# path to instance of isatss_support directory.  If not using isatss_support, set to None
#conda_home     = '/raftr/asatss/isatss_support'
conda_home     = None
# path to installed anaconda install.  If not using a local anaconda install, set to None
#conda_path     = '/raftr/anaconda2'
conda_path     = '/usr/local/isatss/anaconda'
# path to the python binary to be used by ISatSS
python         = conda_path+'/bin/python'
# path to site customization area
home = os.path.expanduser('~')
isatss_home    = home+'/git/ISatSS'
#sitemods       = '/raftr/asatss/ISatSS_NCEP/NAPO'
sitemods       = '/home/brapp/git/ISatSS_NCEP/shelby'
