
# path to installed anaconda install.  If not using a local anaconda install, set to None
conda_path     = '/home/brapp/nwspy/anaconda'

# path to optional site customization area.  If not used, the sitemods variable can be set to None, or simply removed.
# a customization area contains up to three directories:
#   cfg     site specific configuration files
#   lib     site specific libraries
#   host    site specific applications
#
# During the boostrapping that occurs in host/isatss_init.py, the sitemods directories are added to sys.path directly
# in front of their baseline counterparts so that a sitemods version of a file is imported prior to the baseline version.
# All of the isatss paths are appended to the sys.path after the baseline python areas, and the order of isatss paths is:
#
#   site     cfg
#   baseline cfg
#   site     lib
#   baseline lib
#   site     host
#   baseline host
#
# Additionally, isatss_init.py looks in the sitemods cfg directory for the file 'im_site_commands.py'.  If present, the
# command definitions in that file are added to the isatss commands defined in the baseline cfg/im_commands.py file.
#
add_ons = {'packages':{}, 'authid':0, 'protocol':'ssh', 'javascript':{}}
add_ons['top']                       = '/home/brapp/nwspy/add_ons'
add_ons['packages']['elasticsearch'] = {'stype':'conda', 'channel':'conda-forge'}
add_ons['packages']['glmtools']      = {'branch':'p37_n116_v3'} 
add_ons['packages']['lmatools']      = {'branch':'p37_n116_v3'}
add_ons['packages']['stormdrain']    = {'branch':'p37_n116_v3'}
add_ons['packages']['pyclipper']     = {'branch':'p37_n116_v3'}
add_ons['packages']['svn']           = {'stype':'pypi', 'src':'https://files.pythonhosted.org/packages/a1/e7/79a64af11e5d2a1e0996e1e2ce781e297ce711d9835fbe37b43dd6134343/svn-0.3.46.tar.gz'}
add_ons['javascript']['ckeditor']    = 'ckeditor'
add_ons['javascript']['d3']          = 'd3'

sitemods       = '/home/brapp/git/ISatSS_CONFIG/cobra'

#ipacks = []
#ipacks.append({'path':'/home/brapp/git/ISatSS_CONFIG/cobra/cfg','name':'brapp'})

# local fstypes for development - if present, the localfstypes dictionary will override the fstypes dictionary
# in the isatss_config.py file, allowing for convenient local development without change to the nodes dictionary.
'''
localfstypes = {}
localfstypes['fastest']  = {'root':'/dev/shm/isatss_data',     'filesystem':'/dev/shm', 'stype':'attached'}
localfstypes['grb']      = {'root':'/data/isatss_data',        'filesystem':'/data',    'stype':'attached'}
localfstypes['local']    = {'root':'/scratch/isatss_data',     'filesystem':'/scratch', 'stype':'attached'}
localfstypes['backup']   = {'root':'/data/isatss_data/nfsbak', 'filesystem':'/data',    'stype':'attached'}
localfstypes['storage']  = {'root':'/data/isatss_data/nfsops', 'filesystem':'/data',    'stype':'attached'}
localfstypes['storage1'] = {'root':'/data/isatss_data',        'filesystem':'/data',    'stype':'attached'}
localfstypes['storage2'] = {'root':'/data/isatss_data',        'filesystem':'/data',    'stype':'attached'}
localfstypes['pdainput'] = {'root':'/data/isatss_backup',      'filesystem':'/data',    'stype':'attached'}

defaultlocalhostid   = 1
defaultlocalinstance = 'NAPO'
defaultlocaluser     = 'brapp'
defaultlocalpidpath  = '/scratch/isatss_data/pid'
'''
vugraf_draftcount = 15

# Flag to indicate if Tracebacks are to be displayed on failed imports
import_tracebacks = True
