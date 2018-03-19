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
"""
site = 'NAPO'

tier = 'dev'	# dev/qa/ops - unique to IDP deployment, not used outside of this configuration file

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
hosts[2] = {'host':'grb01.nhc.noaa.gov','user':'ldm', 'ext':1336,'cmd':4,'resp':5}
"""
hosts = {}

hosts[1] = {'host':'shelby.napo.nws.noaa.gov', 'shortname':'shelby'}
hosts[2] = {'host':'dev1.napo.nws.noaa.gov',   'shortname':'dev1', 'connecteas':'140.90.141.140', 'resolvenames':False}

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


nodes = {}
nodes[0]  = {'path':'/scratch/isatss_data/info/default_info',		  'filesystem': '/scratch', 'ctype':'info','stype':'attached','root':'/scratch/isatss_data'}
nodes[1]  = {'path':'/scratch/isatss_data/log',                           'filesystem': '/scratch', 'ctype':'log', 'stype':'attached','root':'/scratch/isatss_data'}
nodes[2]  = {'path':'/scratch/isatss_data/info/02_agent86_commands_out',  'filesystem': '/scratch', 'ctype':'cmd', 'stype':'attached','root':'/scratch/isatss_data'}
nodes[3]  = {'path':'/scratch/isatss_data/info/03_agent86_response',      'filesystem': '/scratch', 'ctype':'resp','stype':'attached','root':'/scratch/isatss_data'}
nodes[18] = {'path':'/scratch/isatss_data/work',		          'filesystem': '/scratch', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'}
nodes[19] = {'path':'/scratch/isatss_data/fault_cache',                   'filesystem': '/scratch', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'}

nodes[4]  = {'path':'/dev/shm/isatss_data/data/04_incoming/grb_lhcp',     'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'}
nodes[5]  = {'path':'/dev/shm/isatss_data/data/05_incoming/grb_rhcp',     'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[15] = {'path':'/dev/shm/isatss_data/data/15_grb_l1b_data_in',       'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[16] = {'path':'/scratch/isatss_data/status',		          'filesystem': '/scratch', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'}
nodes[17] = {'path':'/dev/shm/isatss_data/data/17_hcast_data_in',         'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[25] = {'path':'/dev/shm/isatss_data/data/25_ldm_out_replicate_in',  'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[32] = {'path':'/scratch/isatss_data/monitor_output',                'filesystem': '/scratch', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'} #

nodes[41] = {'path':'/dev/shm/isatss_data/data/41_ldm_arch',              'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[43] = {'path':'/dev/shm/isatss_data/data/43_star_in',               'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[44] = {'path':'/dev/shm/isatss_data/data/44_h8_ncm_data_in',        'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[45] = {'path':'/dev/shm/isatss_data/data/45_h8_fdgrg_data_in',      'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[46] = {'path':'/dev/shm/isatss_data/data/46_h8_tiles_data',         'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[47] = {'path':'/dev/shm/isatss_data/data/47_g16_tiles_data',        'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[48] = {'path':'/dev/shm/isatss_data/data/48_g16_fcgrg_data_in',     'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[49] = {'path':'/dev/shm/isatss_data/data/49_g16_mgrg_data_in',      'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[50] = {'path':'/dev/shm/isatss_data/data/50_h8_mgrg_data_in',       'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[51] = {'path':'/dev/shm/isatss_data/data/51_g16_ncm_data_in',       'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[53] = {'path':'/dev/shm/isatss_data/data/53_ldm_out_data_in',       'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #

nodes[14] = {'path':'/data/isatss_data/incoming',		          'filesystem': '/data',    'ctype':'data','stype':'network', 'root':'/data/isatss_data','incinerator':{'gid':2,'jid':10}} #
nodes[24] = {'path':'/data/isatss_data/products/h8_tiles',		  'filesystem': '/data',    'ctype':'data','stype':'network', 'root':'/data/isatss_data','incinerator':{'gid':2,'jid':2}}  #
nodes[30] = {'path':'/data/isatss_data/products/h8_slabs',		  'filesystem': '/data',    'ctype':'data','stype':'network', 'root':'/data/isatss_data','incinerator':{'gid':2,'jid':2}}  #
nodes[39] = {'path':'/data/isatss_data/products/g16_area',	      'filesystem': '/data',    'ctype':'data','stype':'network', 'root':'/data/isatss_data','incinerator':{'gid':2,'jid':9}}  #
nodes[40] = {'path':'/data/isatss_data/products/g16_tiles',		  'filesystem': '/data',    'ctype':'data','stype':'network', 'root':'/data/isatss_data','incinerator':{'gid':2,'jid':1}}  #

nodes[7]  = {'path':'/dev/shm/isatss_data/info/07_ldmer_in_cntl',         'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[9]  = {'path':'/dev/shm/isatss_data/info/09_ldm_in_dispatch_cntl',  'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[11] = {'path':'/dev/shm/isatss_data/info/11_ldm_in_replicate_cntl', 'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[13] = {'path':'/dev/shm/isatss_data/info/13_incinerator_cntl',      'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[20] = {'path':'/dev/shm/isatss_data/info/20_agent86_cntl',          'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[22] = {'path':'/dev/shm/isatss_data/info/22_mi6_cntl',              'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[23] = {'path':'/dev/shm/isatss_data/info/23_g16_grg_l1b_cntl',      'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[26] = {'path':'/dev/shm/isatss_data/info/26_g16_tile_rep_cntl',     'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[28] = {'path':'/dev/shm/isatss_data/info/28_g16_fdco_cntl',         'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[29] = {'path':'/dev/shm/isatss_data/info/29_g16_meso_cntl',         'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[52] = {'path':'/dev/shm/isatss_data/info/52_g16_ncm_cntl',          'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[55] = {'path':'/dev/shm/isatss_data/info/55_ldm_out_repl_cntl',     'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[56] = {'path':'/dev/shm/isatss_data/info/56_ldm_out_cntl',          'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[57] = {'path':'/dev/shm/isatss_data/info/57_star_dispatcher_cntl',  'filesystem': '/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[6]  = {'path':'/dev/shm/isatss_data/info/06_ldm_out_replicator_in', 'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[8]  = {'path':'/dev/shm/isatss_data/info/08_g16ncm_input',          'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[10] = {'path':'/dev/shm/isatss_data/info/10_g16mgrg_input',         'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[12] = {'path':'/dev/shm/isatss_data/info/12_g16fcgrg_input',        'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[21] = {'path':'/dev/shm/isatss_data/info/21_star_input',            'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[27] = {'path':'/dev/shm/isatss_data/info/27_g16_tile_replicator_in','filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[31] = {'path':'/scratch/isatss_data/info/31_deaddrop',              'filesystem': '/scratch', 'ctype':'info','stype':'attached','root':'/scratch/isatss_data'} #
nodes[33] = {'path':'/dev/shm/isatss_data/info/33_h8_ncm_input',          'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[34] = {'path':'/dev/shm/isatss_data/info/34_h8_mgrg_input',         'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[35] = {'path':'/dev/shm/isatss_data/info/35_h8_fdgrg_input',        'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[36] = {'path':'/dev/shm/isatss_data/info/36_h8_replicator_input',   'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[37] = {'path':'/dev/shm/isatss_data/info/37_g16l1bgrg_input',       'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[38] = {'path':'/dev/shm/isatss_data/info/38_hcast_input',           'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[42] = {'path':'/dev/shm/isatss_data/info/42_ldm_arch_input',        'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[54] = {'path':'/dev/shm/isatss_data/info/54_ldm_out_input',         'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[58] = {'path':'/dev/shm/isatss_data/58_pda',                        'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[59] = {'path':'/dev/shm/isatss_data/59_pda_replicator_in',          'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}


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

groups[4] = {}
groups[4]['name']     = 'ldmout'
groups[4]['description'] = """
ISatSS LDM Output Group
"""
groups[4]['jobs']     = {}
groups[4]['jobs'][1]  = {'host':2,'cfg':'ldm_output_replicator'}
groups[4]['jobs'][2]  = {'host':2,'cfg':'ldm_output_manager'}

groups[5] = {}
groups[5]['name']     = 'ldmin'
groups[5]['description'] = """
ISatSS LDM Input Group
ldm_input_manager runs an instance of LDMer on the LDM Input Server, placing data in node 25
ldm_dispatch_manager runs an instance of Dispatcher on the LDM Input Server, 
"""
groups[5]['jobs']     = {}
groups[5]['jobs'][1]  = {'host':1,'cfg':'ldm_input_manager'}
groups[5]['jobs'][2]  = {'host':1,'cfg':'ldm_in_dispatcher'}
groups[5]['jobs'][3]  = {'host':1,'cfg':'ldm_in_replicator'}

groups[6] = {}
groups[6]['name']     = 'goes-16_grb_ldm_l1b_processing'
groups[6]['description'] = """
The ldm_l1b_processing group generates AWIPS-II compatible reflectance and brightness temperature
tiles from full scene ABI L1B scene files.
"""
groups[6]['jobs']     = {}
groups[6]['jobs'][1]  = {'host':1,'cfg':'g16_george_l1b'}
groups[6]['jobs'][2]  = {'host':1,'cfg':'g16_tile_replicator'}



groups[7] = {}
groups[7]['name']     = 'goes-16_grb_pkt_l1b_processing'
groups[7]['description'] = """
The pkt_l1b_processing group generates AWIPS-II compatible reflectance and brightness temperature
tiles from incoming GRB CCSDS packets.
"""
groups[7]['jobs']     = {}
groups[7]['jobs'][1]  = {'host':1,'cfg':'gpacket_config'}
groups[7]['jobs'][2]  = {'host':1,'cfg':'grb_abi_lhcp_processor'}
groups[7]['jobs'][3]  = {'host':1,'cfg':'grb_abi_rhcp_processor'}
groups[7]['jobs'][4]  = {'host':1,'cfg':'grb_abi_band2_processor'}

groups[8] = {}
groups[8]['name']     = 'goes-16_grb_nawips_imagery'
groups[8]['description'] = """
The ncp_imagery group translates incoming ABI tiles into NAWIPS compatible McIDAS Area Files
"""
groups[8]['jobs']     = {}
groups[8]['jobs'][1]  = {'host':1,'cfg':'g16_george_fdco'}
groups[8]['jobs'][2]  = {'host':1,'cfg':'g16_george_meso'}
groups[8]['jobs'][3]  = {'host':1,'cfg':'g16_ncm'}

groups[9] = {}
groups[9]['name']     = 'pda'
groups[9]['description'] = """
PDA product group
"""
groups[9]['jobs']     = {}
groups[9]['jobs'][1] = {'host':1,'cfg':'pda_dispatcher'}
