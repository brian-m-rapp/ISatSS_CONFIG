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

"""
Name of the ISatSS Processing facility - MI6 includes this in telemetry, notifications, and alerts

For Redhat and Centos, the default 'sudo -Su' works.
For openSUSE, use 'sudo -iu'.
"""
sudocmd = 'sudo -iu'	# defaults to 'sudo -Su'

"""
The sites list allows multiple ISatSS installations to be defined within a site.  This could apply
if a site has separate 'dev', 'qa', and 'ops' installations covered by a single configuration tree,
or if sub-sites are defined within a single configuration tree (see SPC).  It can also be used to
allows the same configuration tree to be used across multiple physical locations.

The 'sites' construct is a list of dictionaries, with each dictionary defining a 'site', and the
method to be used to determine a match.  Note that the same site can be listed more than once with
multiple means of performing a match specified.  The first matching record is the winner.
Dictionary fields:
	site     (required)	Site specifier string.  This will be defined as 'isc.site' after processing by isatss_init.py
	var      (optional) Dictionary of variables to be defined in isc.
	method   (required)	Method for performing a match.  Values can be 'by_ip' or 'by_name'.  For 'by_ip', the IP address
	                    of the interface specified by the 'intf' key is matched.  For 'by_name', the hose name of the
	                    current machine is matched.
	intf     (optional) Defines the interface that will contain the matching IP address.  Only used for 'by_ip' method.
	operator (required) Defines how to compare the value returned by the method with the 'value' key.  Possible values
	                    are 'start_with', 'ends_with', 'contains', and 'is'.
	value    (required) Defines the value that will determine a match
	replace  (optional) Dictionary defining token replacements for hosts names.  A token string appearing in the host
	                    hostname will be replaced with the isc variable content.  For instance 'replace':{'%tier%':'tier'}
	                    will replace the token '%tier%' with the value of isc.tier.
"""

"""
The instance_attrs dictionary allows arbitrary variables to be defined based on an 'instance'
key.  This can be useful for defining multiple isatss instances within a given 'site'; if you
have a laptop with different environments on different networks; or if you want to use the same
configuration set at different locations (which is the case here).  The instance applied is
determined by resolving the host name at runtime and matching it against the hosts defined in
the 'hosts' dictionary.  This in turn determines the instance_id to be applied to define the
hosts, groups, jobs, site ID, and tier in the current instance.
"""
instance_attrs = {}
instance_attrs['NAPO'] = {'site':'NAPO', 'tier':'dev', 'instance_keys':['NAPO']}
instance_attrs['ROCK'] = {'site':'ROCK', 'tier':'dev', 'instance_keys':['ROCK']}

"""
The host dictionary identifies all of the members of an ISatSS cluster, and defines the ports and nodes used by the agent86 control and communications app.
Host IDs are referenced in the isatss_config.groups dictionary to identify on what machine and by which account an application is to be run.
A host is defined by a fully qualified domain name and a valid user on that system.
Dictionary fields:
    host    (required)  fully qualified domain name of the host, must be the same as that returned by socket.getfqdn() on the host.
    user    (optional)  valid user listed in the /etc/passwd file on the host.  Defaults to isatss_config.defaults['user']
    ext     (optional)  "extension" for the im_shoephone library that agent86 on this server will listen on.  This is a tcp port that is open for communication on
                        the network that connects all of the hosts in the cluster.  Defaults to the value of the global variable lib/im_shoephone.DefaultPort
    cmd     (optional)  id of node in isatss_config.nodes that agent86 is going to watch for remote command execution request infomsgs.
                        Defaults to isatss_config.defaults['command_node']
    resp    (optional)  id of the node to which agent86 is going to write command response infomsgs.  Defaults to isatss_config.defaults['response_node']

If no entries are provided, ISatSS assumes it is running on a non-clustered system.

Example entry:
hosts[2] = {'host':['grb01.nhc.noaa.gov'],'user':'ldm', 'ext':1336,'cmd':4,'resp':5}
"""

hosts = {}
hosts['NAPO'] = {}
hosts['NAPO'][1] = {'host':['cobra.napo.nws.noaa.gov'], 'shortname':'cobra', 'sudocmd':'sudo -iu'}
hosts['NAPO'][2] = {'host':['cobra.napo.nws.noaa.gov'], 'shortname':'ldm',   'sudocmd':'sudo -iu', 'user':'ldm', 'ext':1338, 'cmd':72, 'resp':73, 'shell':'bash'}
hosts['ROCK'] = {}
hosts['ROCK'][1] = {'host':['chiark.dilireum.org'], 'shortname':'chiark'}
hosts['ROCK'][2] = {'host':['masaq.dilireum.org'],  'shortname':'masaq'}

hattr = {}
hattr[1] = {'nics': [('netname', 'eth0')],   'filesystems': []}
hattr[2] = {'nics': [('netname', 'eth0')],   'filesystems': []}

"""
The nodes dictionary defines all filesystem locations that are accessed (read, write, delete) by ISatSS applications.  For clustered configurations, it is assumed
that all hosts are configured with identical local file systems, and the same access to shared filesystems.  isatss_config.nodes is used in conjunction with the
data dictionary defined in an application configuration file to fully define the path where files are stored, and the retention policy to be implemented by the
host/incinerator application.
Dictionary fields:
    path        (required)  full filesystem path for the node
    filesystem  (required)  filesystem on which the node resides
    ctype       (required)  content type of data stored on the node, used by host/agent86 to determine appropriate forwarding strategy.
                            Value must be one of the following:
                                cmd         command infofiles are read by agent86 for controlling remote isatss applications.
                                data        data files
                                info        infofiles that communicate between applications
                                log         application logging files
                                resp        command response infofiles are written by agent86 containing status feedback from remote isatss applications.
    stype       (required)  storage type of the node
                            Value must be one of the following:
                                attached    the node is on a filesystem directly attached to the host, and inotify can be used to detect new files
                                network     the node is on a shared filesystem (i.e. NFS) and inotify cannot be relied upon.
    root        (required)  the 'top' path controlled entirely by ISatSS.  When the host/isatss 'clean' command is executed, all files and directories below this level are deleted.
    incinerator (optional)  dictionary containing the groupid and job idea of the host/incinerator instance responsible for managing the data stored on the node
                            format:  {'gid':g, 'jid'j}

Regardless of configuration, nodes are required for the following system defaults (defined in isatss_config.defaults)

"""
fstypes = {}
fstypes['fastest'] = {'root':'/dev/shm/isatss_data', 'filesystem':'/dev/shm', 'stype':'attached'}
fstypes['local']   = {'root':'/scratch/isatss_data', 'filesystem':'/',        'stype':'attached'}
fstypes['data']    = {'root':'/data/isatss_data',    'filesystem':'/data',    'stype':'attached'}

nodes = {}
nodes[0]  = {'path':'info/default_info',		       'fstype':'local',   'ctype':'info'}
nodes[1]  = {'path':'001_log',                         'fstype':'local',   'ctype':'log'}
nodes[2]  = {'path':'info/02_agent86_commands_out',    'fstype':'local',   'ctype':'cmd'}
nodes[3]  = {'path':'info/03_agent86_response',        'fstype':'local',   'ctype':'resp'}
nodes[72] = {'path':'info/72_agent86_commands_out',    'fstype':'local',   'ctype':'cmd'}
nodes[73] = {'path':'info/73_agent86_response',        'fstype':'local',   'ctype':'resp'}
nodes[18] = {'path':'work',		                       'fstype':'local',   'ctype':'data'}
nodes[19] = {'path':'fault_cache',                     'fstype':'local',   'ctype':'data'}

nodes[4]  = {'path':'data/04_incoming/grb_lhcp',       'fstype':'fastest', 'ctype':'data'}
nodes[5]  = {'path':'data/05_incoming/grb_rhcp',       'fstype':'fastest', 'ctype':'data'}
nodes[15] = {'path':'data/15_grb_l1b_data_in',         'fstype':'fastest', 'ctype':'data'}
nodes[16] = {'path':'status',		                   'fstype':'local',   'ctype':'data'}
nodes[17] = {'path':'data/17_hcast_data_in',           'fstype':'fastest', 'ctype':'data'}
nodes[25] = {'path':'data/25_ldm_out_replicate_in',    'fstype':'fastest', 'ctype':'data'}
nodes[32] = {'path':'monitor_output',                  'fstype':'local',   'ctype':'data'}

nodes[42] = {'path':'data/42_ldm_arch',                'fstype':'data',    'ctype':'data'}
nodes[43] = {'path':'data/43_star_in',                 'fstype':'fastest', 'ctype':'data'}
nodes[44] = {'path':'data/44_h8_ncm_data_in',          'fstype':'fastest', 'ctype':'data'}
nodes[45] = {'path':'data/45_h8_fdgrg_data_in',        'fstype':'fastest', 'ctype':'data'}
nodes[46] = {'path':'data/46_h8_tiles_data',           'fstype':'fastest', 'ctype':'data'}
nodes[47] = {'path':'data/47_g16_tiles_data',          'fstype':'fastest', 'ctype':'data'}
nodes[48] = {'path':'data/48_g16_fcgrg_data_in',       'fstype':'fastest', 'ctype':'data'}
nodes[49] = {'path':'data/49_g16_mgrg_data_in',        'fstype':'fastest', 'ctype':'data'}
nodes[50] = {'path':'data/50_h8_mgrg_data_in',         'fstype':'fastest', 'ctype':'data'}
nodes[51] = {'path':'data/51_g16_ncm_data_in',         'fstype':'fastest', 'ctype':'data'}
nodes[53] = {'path':'data/53_ldm_out_data_in',         'fstype':'fastest', 'ctype':'data'}

nodes[14] = {'path':'incoming',		                   'fstype':'data',    'ctype':'data'}
nodes[24] = {'path':'products/h8_tiles',               'fstype':'data',    'ctype':'data'}
nodes[30] = {'path':'products/h8_slabs',               'fstype':'data',    'ctype':'data'}
nodes[39] = {'path':'products/g16_area',               'fstype':'data',    'ctype':'data'}
nodes[40] = {'path':'products/g16_tiles',              'fstype':'data',    'ctype':'data'}
nodes[62] = {'path':'esearch_cache',                   'fstype':'data',    'ctype':'data'}

nodes[7]  = {'path':'info/07_ldmer_in_cntl',           'fstype':'fastest', 'ctype':'cntl'}
nodes[9]  = {'path':'info/09_ldm_in_dispatch_cntl',    'fstype':'fastest', 'ctype':'cntl'}
nodes[11] = {'path':'info/11_ldm_in_replicate_cntl',   'fstype':'fastest', 'ctype':'cntl'}
nodes[13] = {'path':'info/13_incinerator_cntl',        'fstype':'fastest', 'ctype':'cntl'}
nodes[20] = {'path':'info/20_agent86_cntl',            'fstype':'fastest', 'ctype':'cntl'}
nodes[22] = {'path':'info/22_mi6_cntl',                'fstype':'fastest', 'ctype':'cntl'}
nodes[23] = {'path':'info/23_g16_grg_l1b_cntl',        'fstype':'fastest', 'ctype':'cntl'}
nodes[26] = {'path':'info/26_g16_tile_rep_cntl',       'fstype':'fastest', 'ctype':'cntl'}
nodes[28] = {'path':'info/28_g16_fdco_cntl',           'fstype':'fastest', 'ctype':'cntl'}
nodes[29] = {'path':'info/29_g16_meso_cntl',           'fstype':'fastest', 'ctype':'cntl'}
nodes[52] = {'path':'info/52_g16_ncm_cntl',            'fstype':'fastest', 'ctype':'cntl'}
nodes[55] = {'path':'info/55_ldm_out_repl_cntl',       'fstype':'fastest', 'ctype':'cntl'}
nodes[56] = {'path':'info/56_ldm_out_cntl',            'fstype':'fastest', 'ctype':'cntl'}
nodes[57] = {'path':'info/57_star_dispatcher_cntl',    'fstype':'fastest', 'ctype':'cntl'}

nodes[6]  = {'path':'info/06_ldm_out_replicator_in',   'fstype':'fastest', 'ctype':'info'}
nodes[8]  = {'path':'info/08_g16ncm_input',            'fstype':'fastest', 'ctype':'info'}
nodes[10] = {'path':'info/10_g16mgrg_input',           'fstype':'fastest', 'ctype':'info'}
nodes[12] = {'path':'info/12_g16fcgrg_input',          'fstype':'fastest', 'ctype':'info'}
nodes[21] = {'path':'info/21_star_input',              'fstype':'fastest', 'ctype':'info'}
nodes[27] = {'path':'info/27_g16_tile_replicator_in',  'fstype':'fastest', 'ctype':'info'}
nodes[31] = {'path':'info/31_deaddrop',                'fstype':'local',   'ctype':'info'}
nodes[33] = {'path':'info/33_h8_ncm_input',            'fstype':'fastest', 'ctype':'info'}
nodes[34] = {'path':'info/34_h8_mgrg_input',           'fstype':'fastest', 'ctype':'info'}
nodes[35] = {'path':'info/35_h8_fdgrg_input',          'fstype':'fastest', 'ctype':'info'}
nodes[36] = {'path':'info/36_h8_replicator_input',     'fstype':'fastest', 'ctype':'info'}
nodes[37] = {'path':'info/37_g16l1bgrg_input',         'fstype':'fastest', 'ctype':'info'}
nodes[38] = {'path':'info/38_hcast_input',             'fstype':'fastest', 'ctype':'info'}
nodes[41] = {'path':'info/41_ldm_arch_input',          'fstype':'fastest', 'ctype':'info'}
nodes[54] = {'path':'info/54_ldm_out_input',           'fstype':'fastest', 'ctype':'info'}

nodes[58] = {'path':'58_pda',                          'fstype':'fastest', 'ctype':'data'}
nodes[59] = {'path':'59_pda_replicator_in',            'fstype':'fastest', 'ctype':'info'}
nodes[60] = {'path':'decoders',                        'fstype':'data',    'ctype':'data'}
nodes[61] = {'path':'ledgers',                         'fstype':'data',    'ctype':'data'}

nodes[64] = {'path':'info/64_amsr2_cutter_cntl',       'fstype':'fastest', 'ctype':'cntl'}
nodes[65] = {'path':'info/65_amsr2_cutter_info',       'fstype':'fastest', 'ctype':'info'}
nodes[66] = {'path':'data/66_amsr2_cutter_data',       'fstype':'data',    'ctype':'data'}

nodes[67] = {'path':'info/67_amsr2_cntl',              'fstype':'fastest', 'ctype':'cntl'}
nodes[68] = {'path':'info/68_amsr2_info',              'fstype':'fastest', 'ctype':'info'}
nodes[69] = {'path':'data/69_amsr2_data',              'fstype':'data',    'ctype':'data'}

nodes[70] = {'path':'info/70_gcom_cntl',               'fstype':'fastest', 'ctype':'cntl'}
nodes[71] = {'path':'info/71_gcom_info',               'fstype':'fastest', 'ctype':'info'}
nodes[74] = {'path':'data/74_gcom_data',               'fstype':'data',    'ctype':'data'}

nodes[75] = {'path':'info/75_h8_dispatch_cntl',        'fstype':'fastest', 'ctype':'cntl'}
nodes[76] = {'path':'info/76_h8_dispatch_info',        'fstype':'fastest', 'ctype':'info'}
nodes[77] = {'path':'data/77_h8_dispatch_data',        'fstype':'data',    'ctype':'data'}
nodes[78] = {'path':'info/78_h8_dispatch_info',        'fstype':'fastest', 'ctype':'info'}

nodes[80] = {'path':'info/80_remote_dispatcher_cntl',  'fstype':'fastest', 'ctype':'cntl'}
nodes[81] = {'path':'info/81_ascat_info',              'fstype':'fastest', 'ctype':'info'}
nodes[82] = {'path':'data/82_ascat_data',              'fstype':'fastest', 'ctype':'data'}
nodes[83] = {'path':'data/83_ascat_ledger',            'fstype':'fastest', 'ctype':'data'}

nodes[85] = {'path':'info/85_fls_cntl',                'fstype':'fastest', 'ctype':'cntl'}
nodes[86] = {'path':'data/86_fls_data',                'fstype':'data',    'ctype':'data'}
nodes[87] = {'path':'info/87_fls_info',                'fstype':'fastest', 'ctype':'info'}
nodes[88] = {'path':'info/88_fls_proc_cntl',           'fstype':'fastest', 'ctype':'cntl'}

nodes[91] = {'path':'info/041_ldm_out_info',           'fstype':'fastest', 'ctype':'info'}
nodes[92] = {'path':'data/042_ldm_out_data',           'fstype':'data',    'ctype':'data'}

nodes[95] = {'path':'info/95_jason_disp_cntl',         'fstype':'fastest', 'ctype':'cntl'}
nodes[96] = {'path':'data/96_jason_disp_data',         'fstype':'data',    'ctype':'data'}
nodes[97] = {'path':'info/97_jason_disp_info',         'fstype':'fastest', 'ctype':'info'}

nodes[93] = {'path':'info/93_jason_proc_cntl',         'fstype':'fastest', 'ctype':'cntl'}
nodes[98] = {'path':'data/98_jason_proc_data',         'fstype':'data',    'ctype':'data'}
nodes[99] = {'path':'info/99_jason_proc_info',         'fstype':'fastest', 'ctype':'info'}

nodes[100] = {'path':'info/100_gpm_puller_cntl',       'fstype':'fastest', 'ctype':'cntl'}
nodes[101] = {'path':'info/101_gpm_puller_info',       'fstype':'fastest', 'ctype':'info'}
nodes[102] = {'path':'data/102_gpm_puller_data',       'fstype':'data',    'ctype':'data'}

nodes[104] = {'path':'info/104_atms_puller_cntl',      'fstype':'fastest', 'ctype':'cntl'}
nodes[105] = {'path':'info/105_atms_puller_info',      'fstype':'fastest', 'ctype':'info'}
nodes[106] = {'path':'data/106_atms_puller_data',      'fstype':'data',    'ctype':'data'}

nodes[107] = {'path':'info/107_atms_cutter_cntl',      'fstype':'fastest', 'ctype':'cntl'}
nodes[108] = {'path':'info/108_atms_cutter_info',      'fstype':'fastest', 'ctype':'info'}
nodes[109] = {'path':'data/109_atms_cutter_data',      'fstype':'data',    'ctype':'data'}
nodes[110] = {'path':'info/110_atms_proj_cntl',        'fstype':'fastest', 'ctype':'cntl'}

nodes[111] = {'path':'info/111_gpm_cutter_cntl',       'fstype':'fastest', 'ctype':'cntl'}
nodes[112] = {'path':'info/112_gpm_cutter_info',       'fstype':'fastest', 'ctype':'info'}
nodes[113] = {'path':'data/113_gpm_cutter_data',       'fstype':'data',    'ctype':'data'}
nodes[114] = {'path':'info/114_gpm_proj_cntl',         'fstype':'fastest', 'ctype':'cntl'}

nodes[120] = {'path':'info/120_cryosat_disp_cntl',     'fstype':'fastest', 'ctype':'cntl'}
nodes[121] = {'path':'data/121_cryosat_disp_data',     'fstype':'data',    'ctype':'data'}
nodes[122] = {'path':'info/122_cryosat_disp_info',     'fstype':'fastest', 'ctype':'info'}

nodes[123] = {'path':'info/123_cryosat_proc_cntl',     'fstype':'fastest', 'ctype':'cntl'}
nodes[124] = {'path':'data/124_cryosat_proc_data',     'fstype':'data',    'ctype':'data'}
nodes[125] = {'path':'info/125_cryosat_proc_info',     'fstype':'fastest', 'ctype':'info'}

nodes[130] = {'path':'info/130_altika_disp_cntl',      'fstype':'fastest', 'ctype':'cntl'}
nodes[131] = {'path':'data/131_altika_disp_data',      'fstype':'data',    'ctype':'data'}
nodes[132] = {'path':'info/132_altika_disp_info',      'fstype':'fastest', 'ctype':'info'}

nodes[133] = {'path':'info/133_altika_proc_cntl',      'fstype':'fastest', 'ctype':'cntl'}
nodes[134] = {'path':'data/134_altika_proc_data',      'fstype':'data',    'ctype':'data'}
nodes[135] = {'path':'info/135_altika_proc_info',      'fstype':'fastest', 'ctype':'info'}

nodes[140] = {'path':'info/140_sentinel_disp_cntl',    'fstype':'fastest', 'ctype':'cntl'}
nodes[141] = {'path':'data/141_sentinel_disp_data',    'fstype':'data',    'ctype':'data'}
nodes[142] = {'path':'info/142_sentinel_disp_info',    'fstype':'fastest', 'ctype':'info'}
nodes[143] = {'path':'info/143_sentinel_proc_cntl',    'fstype':'fastest', 'ctype':'cntl'}
nodes[144] = {'path':'data/144_sentinel_proc_data',    'fstype':'data',    'ctype':'data'}
nodes[145] = {'path':'info/145_sentinel_proc_info',    'fstype':'fastest', 'ctype':'info'}

nodes[150] = {'path':'info/150_vice_puller_cntl',      'fstype':'fastest', 'ctype':'cntl'}
nodes[151] = {'path':'info/151_vice_puller_info',      'fstype':'fastest', 'ctype':'info'}
nodes[152] = {'path':'data/152_vice_puller_data',      'fstype':'data',    'ctype':'data'}

nodes[153] = {'path':'info/153_vice_stitcher_cntl',    'fstype':'fastest', 'ctype':'cntl'}
nodes[154] = {'path':'info/154_vice_stitcher_info',    'fstype':'fastest', 'ctype':'info'}
nodes[155] = {'path':'data/155_vice_stitcher_data',    'fstype':'data',    'ctype':'data'}
nodes[156] = {'path':'info/156_vice_proj_cntl',        'fstype':'fastest', 'ctype':'cntl'}
nodes[157] = {'path':'viirs_ice_cache',                'fstype':'data',    'ctype':'data'}


nodes[700] = {'path':'info/700_dmsp_f15_cut_cntl',     'fstype':'fastest', 'ctype':'cntl'}
nodes[702] = {'path':'info/702_dmsp_f15_cut_input',    'fstype':'fastest', 'ctype':'info'}
nodes[703] = {'path':'data/703_dmsp_f15_cut_data',     'fstype':'data',    'ctype':'data'}
nodes[704] = {'path':'info/704_dmsp_f15_cut_info_out', 'fstype':'fastest', 'ctype':'info'}

nodes[705] = {'path':'info/705_reproject_cntl',        'fstype':'fastest', 'ctype':'cntl'}
nodes[706] = {'path':'info/706_reproject_input',       'fstype':'fastest', 'ctype':'info'}
nodes[707] = {'path':'data/707_reproject_data',        'fstype':'data',    'ctype':'data'}
nodes[708] = {'path':'info/708_reproject_info_out',    'fstype':'fastest', 'ctype':'info'}

# system defaults
defaults = {}
defaults['log']             = 'isatss_log'	  			# default log file name
defaults['log_node']        = 1							# path to storage area for log files
defaults['loglevel']        = 5							# V_STATUS logging level
defaults['work_node']       = 18							# path to storage area for temporary work
defaults['fault_node']      = 1							# path to storage area for stored faulty data files
defaults['loopsleep']       = 0                           # im_daemon loop delay
defaults['pidpath']         = '/scratch/isatss_data/pid'  # path to storage area for pid files
defaults['node']            = 0                     		# default station to write and read info messages
defaults['traceprint']      = False				  		# default exception printing to include traceback or not
defaults['shutdown_wait']   = 60					  		# default time to wait for an application to shutdown
defaults['command_node']    = 2                     		# default station to write command messages
defaults['response_node']   = 3                     		# default station to read command responses
defaults['user']            = 'brapp'
defaults['vlab']            = {}
defaults['vlab']['url']     = 'https://vlab.ncep.noaa.gov'
defaults['vlab']['company'] = 10132
defaults['vlab']['group']   = 1334496		# ISatSS community group ID
defaults['sudocmd']         = 'sudo -Su'
defaults['cluster_log']     = True
defaults['doc_cfg']         = 'doc_cfg'                  # documentation configuration file

#groups
groups = {}

groups[0] = {}
groups[0]['name']     = 'default'
groups[0]['jobs']     = {}
groups[0]['jobs'][0]  = {'host':-1,'cfg':'default'}

groups[1] = {}
groups[1]['name']     = 'agent86ers'
groups[1]['description'] = """
The agent86ers group provides message routing and data flow
between all hosts in the system.
"""
groups[1]['cluster_action'] = ['init','shutdown']
groups[1]['jobs']     = {}
groups[1]['jobs'][1]  = {'host':1, 'cfg':'agent86_config'}
groups[1]['jobs'][2]  = {'host':2, 'cfg':'agent86_config'}

groups[2] = {}
groups[2]['name']     = 'incinerators'
groups[2]['description'] = """
The incinerators group includes an incinerator job for each host
in the system.
"""
groups[2]['jobs']     = {}
groups[2]['jobs'][1]  = {'host':1, 'cfg':'incinerator_config'}
groups[2]['jobs'][2]  = {'host':2, 'cfg':'incinerator_config'}

groups[3] = {}
groups[3]['name']     = 'monitor'
groups[3]['description'] = """
The monitor group provides monitoring services for all hosts in the system.
An mi6 application running on each host collects server performance metrics, and
scrapes the log files of all applications, preparing condensed summary information
based on each application's agent86 class.

The mi6 applications write info messages to node 31 on each host, which are forwarded
by agent86 to node 31 on host 0.  An instance of the gchq application running on host 0
consumes the messages, and writes them to a file named system_tm.YYYYMMDD on node 32.
"""
groups[3]['jobs']     = {}
groups[3]['jobs'][1]  = {'host':1, 'cfg':'mi6_config'}
groups[3]['jobs'][2]  = {'host':2, 'cfg':'mi6_config'}
groups[3]['jobs'][3]  = {'host':1, 'cfg':'gchq_config'}

groups[4]                = {}
groups[4]['name']        = 'LDM'
groups[4]['description'] = """
Jobs for configuring and managing LDM instances
"""
groups[4]['jobs']        = {}
groups[4]['jobs'][1]     = {'host':2, 'cfg':'isatss_ldm_manager'}
groups[4]['jobs'][2]     = {'host':1, 'cfg':'ldm_in_dispatcher'}
#groups[4]['jobs'][3]     = {'host':1, 'cfg':'goes_stats_processor'}


groups[5]                = {}
groups[5]['name']        = 'FLS Processing'
groups[5]['instance']    = ['ROCK', 'NAPO']
groups[5]['description'] = """
Job processing Fog and Low Stratus products
"""
groups[5]['jobs']        = {}
groups[5]['jobs'][1]     = {'host':1, 'cfg':'fls_puller'}
'''
groups[6]                = {}
groups[6]['name']        = 'GCOM Processing'
groups[6]['description'] = """
Jobs for ingesting, processing, and pushing GCOM products
"""
groups[6]['jobs']        = {}
groups[6]['jobs'][1]     = {'host':1, 'cfg':'amsr2_ocean_puller'}
groups[6]['jobs'][2]     = {'host':1, 'cfg':'amsr2_ocean_processor', 'icfg':{'io':{'x':2000,'y':3200}}}


groups[8]                = {}
groups[8]['name']        = 'Himawari Tile Processing'
groups[8]['description'] = """
Jobs for ingesting, processing, and pushing Himawari tiles
"""
groups[8]['jobs']        = {}
groups[8]['jobs'][1]     = {'host':1, 'cfg':'star_dispatcher'}
groups[8]['jobs'][2]     = {'host':1, 'cfg':'h8_slab2tile'}
'''

groups[9]                = {}
groups[9]['name']        = 'DMSP SSMI Processing'
groups[9]['description'] = """
Jobs for ingesting, processing, and pushing DMSP SSMI data
"""
groups[9]['jobs']        = {}
groups[9]['jobs'][1]     = {'host':1, 'cfg':'dmsp_f15_cutter_config'}
groups[9]['jobs'][2]     = {'host':1, 'cfg':'ssmi_projector'}

groups[10]                = {}
groups[10]['name']        = 'Jason2/3 Altimetry Processing'
groups[10]['description'] = """
Jobs for ingesting, processing, and pushing Altimetry data from Jason2/3
"""
groups[10]['jobs']        = {}
groups[10]['jobs'][1]     = {'host':1, 'cfg':'jason_dispatcher'}
groups[10]['jobs'][2]     = {'host':1, 'cfg':'jason_processor'}

'''
groups[11]                = {}
groups[11]['name']        = 'AMSR2 Imagery Processing'
groups[11]['description'] = """
Jobs for ingesting, processing, and pushing AMSR2 Imagery
"""
groups[11]['jobs']        = {}
groups[11]['jobs'][1]     = {'host':1, 'cfg':'amsr2_puller'}
groups[11]['jobs'][2]     = {'host':1, 'cfg':'amsr2_cutter'}
groups[11]['jobs'][3]     = {'host':1, 'cfg':'amsr2_projector'}
'''

groups[12]                = {}
groups[12]['name']        = 'ATMS Imagery Processing'
groups[12]['description'] = """
Jobs for ingesting, processing, and pushing ATMS Imagery
"""
groups[12]['jobs']        = {}
groups[12]['jobs'][1]     = {'host':1, 'cfg':'atms_dispatcher'}
groups[12]['jobs'][2]     = {'host':1, 'cfg':'atms_cutter'}
groups[12]['jobs'][3]     = {'host':1, 'cfg':'atms_projector'}

groups[13] = {}
groups[13]['name']     = 'GPM GMI'
groups[13]['description'] = """
GPM GMI processing jobs
"""
groups[13]['jobs']     = {}
groups[13]['jobs'][1] = {'host':1, 'cfg':'gpm_dispatcher'}
groups[13]['jobs'][2] = {'host':1, 'cfg':'gpm_gmi_cutter'}
groups[13]['jobs'][3] = {'host':1, 'cfg':'gpm_gmi_projector'}

groups[14] = {}
groups[14]['name']     = 'CryoSat processing'
groups[14]['description'] = """
CryoSat processing chain
"""
groups[14]['jobs']     = {}
groups[14]['jobs'][1]  = {'host':1,'cfg':'cryosat_dispatcher'}
groups[14]['jobs'][2]  = {'host':1,'cfg':'cryosat_processor'}

groups[15] = {}
groups[15]['name']     = 'Altika processing'
groups[15]['description'] = """
Altika processing chain
"""
groups[15]['jobs']     = {}
groups[15]['jobs'][1]  = {'host':1,'cfg':'altika_dispatcher'}
groups[15]['jobs'][2]  = {'host':1,'cfg':'altika_processor'}

groups[16] = {}
groups[16]['name']     = 'Sentinel-3 processing'
groups[16]['description'] = """
Sentinel-3 processing chain
"""
groups[16]['jobs']     = {}
groups[16]['jobs'][1]  = {'host':1,'cfg':'sentinel_dispatcher'}
groups[16]['jobs'][2]  = {'host':1,'cfg':'sentinel_processor'}

'''
groups[17] = {}
groups[17]['name']     = 'VIIRS ice concentration processing'
groups[17]['description'] = """
VIIRS ice concentration processing chain
"""
groups[17]['jobs']     = {}
groups[17]['jobs'][2]  = {'host':1,'cfg':'viirs_ice_stitcher'}
groups[17]['jobs'][3]  = {'host':1,'cfg':'viirs_ice_projector'}
'''

groups[18] = {}
groups[18]['name']        = 'h8-tileproc'
groups[18]['description'] = """
The h8-tileproc group archives incoming h8 tiles, forwards them to ldm, and creates area files
"""
groups[18]['jobs']     = {}
groups[18]['jobs'][1]  = {'host':1,'cfg':'star_dispatcher'}
