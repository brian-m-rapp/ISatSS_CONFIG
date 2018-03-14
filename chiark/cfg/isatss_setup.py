# isatss configuration
import os

# path to instance of isatss_support directory.  If not using isatss_support, set to None
conda_home     = None
# path to installed anaconda install.  If not using a local anaconda install, set to None
conda_path     = '/home/brapp/raftr/asatss/isatss_p36/anaconda'
# path to the python binary to be used by ISatSS
python		   = conda_path+'/bin/python'

home = os.path.expanduser('~')
isatss_home    = home+'/git/ISatSS'
# path to site customization area
sitemods       = '/home/brapp/git/ISatSS_NCEP/chiark'
