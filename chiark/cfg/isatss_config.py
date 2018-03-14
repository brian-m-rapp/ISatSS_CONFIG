# isatss main configuration file
"""
    IDP Satellite Support Subsystem
    Copyright (C) 2016 Joseph K. Zajic (joe.zajic@noaa.gov), Brian M. Rapp (brian.rapp@noaa.gov)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Defaults for hosts: 'user': 'isatss', 'ext': 1337, 'cmd': 2, 'resp': 3
hosts = {}
hosts[0] = {'host':'chiark.dilireum.org'}
hosts[1] = {'host':'masaq.dilireum.org'}

# processing nodes
nodes = {}
nodes[0]  = {'path':'/scratch/isatss_data/info/default_info',		 'ctype':'info','stype':'attached'}
nodes[1]  = {'path':'/scratch/isatss_data/log',						 'ctype':'log', 'stype':'attached'}
nodes[2]  = {'path':'/scratch/isatss_data/info/agent86_commands_out','ctype':'cmd', 'stype':'attached'}
nodes[3]  = {'path':'/scratch/isatss_data/info/agent86_response',    'ctype':'resp','stype':'attached'}
nodes[4]  = {'path':'/scratch/isatss_data/incoming/grb_lhcp',        'ctype':'data','stype':'attached'}
nodes[5]  = {'path':'/scratch/isatss_data/incoming/grb_rhcp',        'ctype':'data','stype':'attached'}
nodes[6]  = {'path':'/scratch/isatss_data/info/g2j11_input',         'ctype':'info','stype':'attached'}	#goes-16 ldmer
nodes[7]  = {'path':'/scratch/isatss_data/info/g2j11_cntl',          'ctype':'cntl','stype':'attached'}
nodes[8]  = {'path':'/scratch/isatss_data/info/g2j9_input',          'ctype':'info','stype':'attached'}	#goes-16 ncm
nodes[9]  = {'path':'/scratch/isatss_data/info/g2j9_cntl',           'ctype':'cntl','stype':'attached'}
nodes[10] = {'path':'/scratch/isatss_data/info/g2j8_input',          'ctype':'info','stype':'attached'}	#goes-16 george meso
nodes[11] = {'path':'/scratch/isatss_data/info/g2j8_cntl',           'ctype':'cntl','stype':'attached'}
nodes[12] = {'path':'/scratch/isatss_data/info/g2j7_input',          'ctype':'info','stype':'attached'}	#goes-16 george fd/co
nodes[13] = {'path':'/scratch/isatss_data/info/g2j7_cntl',           'ctype':'cntl','stype':'attached'}
nodes[14] = {'path':'/data/isatss_data/products',		             'ctype':'data','stype':'network','incinerator':{'gid':2,'jid':2}}
nodes[15] = {'path':'/scratch/isatss_data/intermediate',             'ctype':'data','stype':'attached'}
nodes[16] = {'path':'/scratch/isatss_data/info/g2j10_input',         'ctype':'info','stype':'attached','nodata':True}	#goes-16 notifier
nodes[17] = {'path':'/scratch/isatss_data/info/g2j10_cntl',          'ctype':'cntl','stype':'attached'}


# system defaults
workarea    = '/data/isatss_work'            # default temporary file work area
fault_cache = '/data/isatss_data/fault_cache'
#TODO: the definitions are buried in the ISatSSLog class
loglevel = 4                                        # V_INFO logging level

#defaults
defaults = {}
defaults['log']           = 'isatss_log'				# default log file name
defaults['logpath']       = '/scratch/isatss_data/log'	# path to storage area for log files
defaults['loopsleep']     = 0							# im_daemon loop delay
defaults['pidpath']       = '/scratch/isatss_data/pid'	# path to storage area for pid files
defaults['node']          = 0							# default station to write and read info messages
defaults['command_node']  = 2							# default station to write command messages	(hosts[i]['cmd']
defaults['response_node'] = 3							# default station to read command responses (hosts[i]['resp']
defaults['user']          = 'brapp'
defaults['traceprint']    = False						# default exception printing to include traceback or not
defaults['cap_alert']     = 75							# Send alert if filesystem utilization is more than this percentage

#groups
groups = {}

groups[0] = {}
groups[0]['name']     = 'default'
groups[0]['jobs']     = {}
groups[0]['jobs'][0]  = 'default'

groups[1] = {}
groups[1]['name']     = 'agent86ers'
groups[1]['jobs']     = {}
groups[1]['jobs'][1]  = {'host':0,'cfg':'agent86_config'}
groups[1]['jobs'][2]  = {'host':1,'cfg':'agent86_config'}
groups[1]['jobs'][3]  = {'host':0,'cfg':'mi6_config'}
groups[1]['jobs'][4]  = {'host':1,'cfg':'mi6_config'}

groups[2] = {}
groups[2]['name']     = 'goes-16_grb'
groups[2]['jobs']     = {}
groups[2]['jobs'][1]  = {'host':0,'cfg':'grb_incinerator_config'}
groups[2]['jobs'][2]  = {'host':1,'cfg':'grb_incinerator_config'}
groups[2]['jobs'][3]  = {'host':2,'cfg':'grb_incinerator_config'}
groups[2]['jobs'][4]  = {'host':3,'cfg':'grb_incinerator_config'}
groups[2]['jobs'][5]  = {'host':0,'cfg':'gpacket_config'}
groups[2]['jobs'][6]  = {'host':0,'cfg':'grb_abi_lhcp_processor'}
groups[2]['jobs'][7]  = {'host':0,'cfg':'grb_abi_rhcp_processor'}
groups[2]['jobs'][8]  = {'host':0,'cfg':'grb_abi_band2_processor'}
groups[2]['jobs'][9]  = {'host':1,'cfg':'george_goesr_test_tiles_scmirecttiles'} #1
groups[2]['jobs'][10] = {'host':2,'cfg':'george_goesr_test_meso_tiles_scmirecttiles'} #2
groups[2]['jobs'][11] = {'host':3,'cfg':'ncm_goesr_scmirecttiles_area'} #3
groups[2]['jobs'][12] = {'host':0,'cfg':'grb_notifier_config'}
groups[2]['jobs'][13] = {'host':0,'cfg':'grb_ldm_manager'} #4
groups[2]['jobs'][14] = {'host':4,'cfg':'grb_incinerator_config'} 
