# isatss configuration

devtop  = '/home/brapp/git'
devdata = '/home/brapp'
devfs   = '/home'

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
# The mysite and mysitevals configuration parameters allow an install to mimic a deployed site.
#     sitemod - name of site in ISatSS_NCEP
#     hid     - host id to run all jobs as
#     inst    - instance value to use in interpreting isatss_config.py
#
mysite = 'NHC1'
mysitevals = {}
mysitevals['AWC']     = {'sitemod':'AWC7',  'hid':1,'inst':'AWC7'}
mysitevals['AWCDev1'] = {'sitemod':'AWCDev','hid':1,'inst':'AWCDEV7'}
mysitevals['OPG']     = {'sitemod':'OPG',   'hid':1,'inst':'OPG'}
mysitevals['SPC1']    = {'sitemod':'SPC',   'hid':1,'inst':'S1'}
mysitevals['NHC1']    = {'sitemod':'NHC',   'hid':1,'inst':'NHC1'}
mysitevals['NHC2']    = {'sitemod':'NHC',   'hid':1,'inst':'NHC2'}
mysitevals['NHCDev1'] = {'sitemod':'NHCDev','hid':1,'inst':'NHCDEV1'}
mysitevals['NHCDev2'] = {'sitemod':'NHCDev','hid':1,'inst':'NHCDEV2'}
mysitevals['IDPDev1'] = {'sitemod':'IDPDev','hid':1,'inst':'CPDEV'}
mysitevals['NAPO2']   = {'sitemod':'NAPO2', 'hid':1,'inst':'N1'}
mysitevals['NAPO']    = {'sitemod':'NAPO',  'hid':1,'inst':'N1'}
mysitevals['STAR']    = {'sitemod':'STAR',  'hid':1,'inst':'STAR'}

#
# The mymods variable points to a personal directory for configuration, data, library, documentation, and applications.
# If they exist, subdirectories cfg, lib, apps , agents, and data are placed in the python sys.path in front of the corresponding
# sitemods and baseline counterparts.
#

ipacks = []
ipacks.append({'path':devtop+'/Developer','name':'Developer'})

# sitemods defines the path to the mimic'ed configuration area
sitemods       = devtop+'/ISatSS-config/'+mysitevals[mysite]['sitemod']

# add_ons provides configuration information for software that augments what is provided by nwspy
# The authid value corresponds to an authentication entry made using the "isatss creds add" command
# 'packages' entries are populated using the addons command
# 'binaries' are manually placed'
# TODO: update this and make it clearer and document it

add_ons = {'top':'','packages':{},'binaries':{},'javascript':{},'authid':0,'protocol':'ssh'}
add_ons['top']                        = devtop+'/add_ons'
add_ons['packages']['glmtools']       = {'branch':'p37_n117_v4.2'} 
add_ons['packages']['lmatools']       = {'branch':'p37_n117_v4.2'}
add_ons['packages']['stormdrain']     = {'branch':'p37_n116_v3'}
add_ons['packages']['pyclipper']      = {'branch':'p37_n116_v3'}
add_ons['javascript']['ckeditor']     = 'ckeditor'
#add_ons['javascript']['d3']           = 'd3'      
#add_ons['binaries']['xRITDecompress'] = 'xRITDecompress/2.06/xRITDecompress/xRITDecompress'

# Flag to indicate if Tracebacks are to be displayed on failed imports
import_tracebacks = True

# Flag to indicate handling of failed import
quit_on_failed_import = False

# python run time warnings
pythonWarnings = 'disabled'

# local fstypes for development - comment out completely if not used
# these fstypes override the entries in the isatss_config.py configuration file for the mimic'ed site
localfstypes = {}
localfstypes['fastest']   = {'root':'/dev/shm/isatss_data',           'filesystem':'/dev/shm', 'stype':'attached','cutoff':100e6}
localfstypes['grb']       = {'root':'/dev/shm/isatss_data',           'filesystem':'/dev/shm', 'stype':'attached','cutoff':100e6}
localfstypes['local']     = {'root':devdata+'/isatss_data',           'filesystem':devfs,      'stype':'attached','cutoff':100e6}
localfstypes['backup']    = {'root':devdata+'/isatss_data/backup',    'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage']   = {'root':devdata+'/isatss_data/storage',   'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage1']  = {'root':devdata+'/isatss_data/storage1',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage2']  = {'root':devdata+'/isatss_data/storage2',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage3']  = {'root':devdata+'/isatss_data/storage3',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage4']  = {'root':devdata+'/isatss_data/storage4',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage5']  = {'root':devdata+'/isatss_data/storage5',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage6']  = {'root':devdata+'/isatss_data/storage6',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage7']  = {'root':devdata+'/isatss_data/storage7',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage8']  = {'root':devdata+'/isatss_data/storage8',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage9']  = {'root':devdata+'/isatss_data/storage9',  'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage10'] = {'root':devdata+'/isatss_data/storage10', 'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage11'] = {'root':devdata+'/isatss_data/storage11', 'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage12'] = {'root':devdata+'/isatss_data/storage12', 'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage13'] = {'root':devdata+'/isatss_data/storage13', 'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage14'] = {'root':devdata+'/isatss_data/storage14', 'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['storage15'] = {'root':devdata+'/isatss_data/storage15', 'filesystem':devfs,      'stype':'network', 'cutoff':100e6}
localfstypes['pdainput']  = {'root':devdata+'/isatss_data/pdainput',  'filesystem':devfs,      'stype':'attached','cutoff':100e6}
localfstypes['pdainput2'] = {'root':devdata+'/isatss_data/pdainput2', 'filesystem':devfs,      'stype':'attached','cutoff':100e6}
localfstypes['pdainput3'] = {'root':devdata+'/isatss_data/pdainput3', 'filesystem':devfs,      'stype':'attached','cutoff':100e6}

# default host and instance - comment out completely if not used
# These entries override default entries in the isatss_config.py configuration file for the mimic'ed site
defaultlocalhostid   = mysitevals[mysite]['hid']
defaultlocalpidpath  = devdata+'/isatss_data/pid'
defaultlocalinstance = mysitevals[mysite]['inst']

# vugraf variables
#vugraf_d3         = '/home/jzajic/isatss/ISatSS/admin/d3.js'
#vugraf_ckeditor   = '/home/jzajic/isatss/ISatSS/admin/ckeditor'
#vugraf_draftcount = 15
#vugraf_thingdb_config = 'spbot'

