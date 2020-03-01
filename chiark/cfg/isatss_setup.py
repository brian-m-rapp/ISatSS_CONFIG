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
sitemods       = '/home/brapp/git/ISatSS_CONFIG/chiark'

#add on packages
add_ons = {'top':'','packages':{},'authid':0,'protocol':'ssh'}
add_ons['top'] = '/home/brapp/nwspy/add_ons'
add_ons['packages']['elasticsearch'] = {'stype':'conda', 'channel':'conda-forge'}
add_ons['packages']['glmtools']      = {'branch':'p37_n117_v4.1'}
add_ons['packages']['lmatools']      = {'branch':'p37_n116_v3'}
add_ons['packages']['stormdrain']    = {'branch':'p37_n116_v3'}
add_ons['packages']['pyclipper']     = {'branch':'p37_n116_v3'}

# Flag to indicate if Tracebacks are to be displayed on failed imports
import_tracebacks = True

# Flag to indicate handling of failed import
quit_on_failed_import = True

# python run time warnings
pythonWarnings = 'disabled'
