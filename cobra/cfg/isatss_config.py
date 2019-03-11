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

import socket
ipaddr = socket.gethostbyname(socket.gethostname())
if ipaddr.startswith('140.90.141'):
	site = 'NAPO'
elif ipaddr.startswith('192.168'):
	site = 'ROCK'
else:
	site = 'unknown'

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
if site == 'NAPO':
	hosts[1] = {'host':'cobra.napo.nws.noaa.gov', 'shortname':'cobra', 'sudocmd':'sudo -iu'}
	hosts[2] = {'host':'cobra.napo.nws.noaa.gov', 'shortname':'ldm', 'sudocmd':'sudo -iu', 'user':'ldm', 'ext':1338, 'cmd':72, 'resp':73}
elif site == 'ROCK':
	hosts[1] = {'host':'chiark.dilireum.org', 'shortname':'chiark'}
	hosts[2] = {'host':'masaq.dilireum.org',  'shortname':'masaq'}
else:
	print('Unknown site')
	import sys
	sys.exit(1)

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
nodes[0]  = {'path':'/scratch/isatss_data/info/default_info',		      'filesystem': '/scratch', 'ctype':'info','stype':'attached','root':'/scratch/isatss_data'}
nodes[1]  = {'path':'/scratch/isatss_data/log',                           'filesystem': '/scratch', 'ctype':'log', 'stype':'attached','root':'/scratch/isatss_data'}
nodes[2]  = {'path':'/scratch/isatss_data/info/02_agent86_commands_out',  'filesystem': '/scratch', 'ctype':'cmd', 'stype':'attached','root':'/scratch/isatss_data'}
nodes[3]  = {'path':'/scratch/isatss_data/info/03_agent86_response',      'filesystem': '/scratch', 'ctype':'resp','stype':'attached','root':'/scratch/isatss_data'}
nodes[72] = {'path':'/scratch/isatss_data/info/72_agent86_commands_out',  'filesystem': '/scratch', 'ctype':'cmd', 'stype':'attached','root':'/scratch/isatss_data'}
nodes[73] = {'path':'/scratch/isatss_data/info/73_agent86_response',      'filesystem': '/scratch', 'ctype':'resp','stype':'attached','root':'/scratch/isatss_data'}
nodes[18] = {'path':'/scratch/isatss_data/work',		                  'filesystem': '/scratch', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'}
nodes[19] = {'path':'/scratch/isatss_data/fault_cache',                   'filesystem': '/scratch', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'}

nodes[4]  = {'path':'/dev/shm/isatss_data/data/04_incoming/grb_lhcp',     'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'}
nodes[5]  = {'path':'/dev/shm/isatss_data/data/05_incoming/grb_rhcp',     'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[15] = {'path':'/dev/shm/isatss_data/data/15_grb_l1b_data_in',       'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[16] = {'path':'/scratch/isatss_data/status',		                  'filesystem': '/scratch', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'}
nodes[17] = {'path':'/dev/shm/isatss_data/data/17_hcast_data_in',         'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[25] = {'path':'/dev/shm/isatss_data/data/25_ldm_out_replicate_in',  'filesystem': '/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[32] = {'path':'/scratch/isatss_data/monitor_output',                'filesystem': '/scratch', 'ctype':'data','stype':'attached','root':'/scratch/isatss_data'} #

nodes[42] = {'path':'/data/isatss_data/data/42_ldm_arch',                 'filesystem': '/data',    'ctype':'data','stype':'attached','root':'/data'} #
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

nodes[14] = {'path':'/data/isatss_data/incoming',		                  'filesystem': '/data',    'ctype':'data','stype':'attached', 'root':'/data/isatss_data'} #
nodes[24] = {'path':'/data/isatss_data/products/h8_tiles',		          'filesystem': '/data',    'ctype':'data','stype':'attached', 'root':'/data/isatss_data'}  #
nodes[30] = {'path':'/data/isatss_data/products/h8_slabs',		          'filesystem': '/data',    'ctype':'data','stype':'attached', 'root':'/data/isatss_data'}  #
nodes[39] = {'path':'/data/isatss_data/products/g16_area',	              'filesystem': '/data',    'ctype':'data','stype':'attached', 'root':'/data/isatss_data'}  #
nodes[40] = {'path':'/data/isatss_data/products/g16_tiles',		          'filesystem': '/data',    'ctype':'data','stype':'attached', 'root':'/data/isatss_data'}  #
nodes[62] = {'path':'/data/isatss_data/esearch_cache',		              'filesystem': '/data',    'ctype':'data','stype':'attached', 'root':'/data/isatss_data'}  #

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
nodes[41] = {'path':'/dev/shm/isatss_data/info/41_ldm_arch_input',        'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[54] = {'path':'/dev/shm/isatss_data/info/54_ldm_out_input',         'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[58] = {'path':'/dev/shm/isatss_data/58_pda',                        'filesystem': '/dev/shm',  'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[59] = {'path':'/dev/shm/isatss_data/59_pda_replicator_in',          'filesystem': '/dev/shm',  'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[60] = {'path':'/mnt/ldm2/decoders',                                 'filesystem': '/mnt/ldm2', 'ctype':'data','stype':'network', 'root':'/mnt/ldm2', 'incinerator':{'gid':2,'jid':1}} 
nodes[61] = {'path':'/data/isatss_data/ledgers',                          'filesystem':' /data',     'ctype':'data','stype':'attached','root':'/data/isatss_data'}

nodes[64] = {'path':'/dev/shm/isatss_data/info/64_amsr2_cutter_cntl',     'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[65] = {'path':'/dev/shm/isatss_data/info/65_amsr2_cutter_info',     'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[66] = {'path':'/data/isatss_data/data/66_amsr2_cutter_data',        'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data/isatss_data'}

nodes[67] = {'path':'/dev/shm/isatss_data/info/67_amsr2_cntl',            'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[68] = {'path':'/dev/shm/isatss_data/info/68_amsr2_info',            'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[69] = {'path':'/data/isatss_data/data/69_amsr2_data',               'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data/isatss_data'}

nodes[70] = {'path':'/dev/shm/isatss_data/info/70_gcom_cntl',             'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[71] = {'path':'/dev/shm/isatss_data/info/71_gcom_info',             'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[74] = {'path':'/data/isatss_data/data/74_gcom_data',                'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data/isatss_data'}

nodes[75] = {'path':'/dev/shm/isatss_data/info/75_h8_dispatch_cntl',      'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[76] = {'path':'/dev/shm/isatss_data/info/76_h8_dispatch_info',      'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[77] = {'path':'/data/isatss_data/data/77_h8_dispatch_data',         'filesystem':'/ddata',  'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[78] = {'path':'/dev/shm/isatss_data/info/78_h8_dispatch_info',      'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[80] = {'path':'/dev/shm/isatss_data/info/80_remote_dispatcher_cntl','filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[81] = {'path':'/dev/shm/isatss_data/info/81_ascat_info',            'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[82] = {'path':'/dev/shm/isatss_data/data/82_ascat_data',            'filesystem':'/dev/shm','ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[83] = {'path':'/dev/shm/isatss_data/data/83_ascat_ledger',          'filesystem':'/dev/shm','ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[85] = {'path':'/dev/shm/isatss_data/info/85_fls_cntl',              'filesystem':'/dev/shm', 'ctype':'cntl', 'stype':'attached', 'root':'/dev/shm/isatss_data', 'incinerator':{'gid':2,'jid':1}}
nodes[86] = {'path':'/data/isatss_data/data/86_fls_data',                 'filesystem':'/data',    'ctype':'data', 'stype':'attached', 'root':'/data/isatss_data', 'incinerator':{'gid':2,'jid':1}}
nodes[87] = {'path':'/dev/shm/isatss_data/info/87_fls_info',              'filesystem':'/dev/shm', 'ctype':'info', 'stype':'attached', 'root':'/dev/shm/isatss_data'}
nodes[88] = {'path':'/dev/shm/isatss_data/info/88_fls_proc_cntl',         'filesystem':'/dev/shm', 'ctype':'cntl', 'stype':'attached', 'root':'/dev/shm/isatss_data', 'incinerator':{'gid':2,'jid':1}}

nodes[91] = {'path':'/dev/shm/isatss_data/info/041_ldm_out_info',         'filesystem':'/dev/shm', 'ctype':'info', 'stype':'attached', 'root':'/dev/shm/isatss_data', 'incinerator':{'gid':2,'jid':1}}
nodes[92] = {'path':'/data/isatss_data/data/042_ldm_out_data',            'filesystem':'/data',    'ctype':'data', 'stype':'attached', 'root':'/data/isatss_data', 'incinerator':{'gid':2,'jid':1}}

nodes[95] = {'path':'/dev/shm/isatss_data/info/95_jason_disp_cntl',       'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[96] = {'path':'/data/isatss_data/data/96_jason_disp_data',          'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[97] = {'path':'/dev/shm/isatss_data/info/97_jason_disp_info',       'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[93] = {'path':'/dev/shm/isatss_data/info/93_jason_proc_cntl',       'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[98] = {'path':'/data/isatss_data/data/98_jason_proc_data',          'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[99] = {'path':'/dev/shm/isatss_data/info/99_jason_proc_info',       'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[100] = {'path':'/dev/shm/isatss_data/info/100_gpm_puller_cntl',     'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[101] = {'path':'/dev/shm/isatss_data/info/101_gpm_puller_info',     'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[102] = {'path':'/data/isatss_data/data/102_gpm_puller_data',        'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data/isatss_data'}

nodes[104] = {'path':'/dev/shm/isatss_data/info/104_atms_puller_cntl',    'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[105] = {'path':'/dev/shm/isatss_data/info/105_atms_puller_info',    'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[106] = {'path':'/data/isatss_data/data/106_atms_puller_data',       'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data/isatss_data'}

nodes[107] = {'path':'/dev/shm/isatss_data/info/107_atms_cutter_cntl',    'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[108] = {'path':'/dev/shm/isatss_data/info/108_atms_cutter_info',    'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[109] = {'path':'/data/isatss_data/data/109_atms_cutter_data',       'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data'}
nodes[110] = {'path':'/dev/shm/isatss_data/info/110_atms_proj_cntl',      'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[111] = {'path':'/dev/shm/isatss_data/info/111_gpm_cutter_cntl',     'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[112] = {'path':'/dev/shm/isatss_data/info/112_gpm_cutter_info',     'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[113] = {'path':'/data/isatss_data/data/113_gpm_cutter_data',        'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data'}
nodes[114] = {'path':'/dev/shm/isatss_data/info/114_gpm_proj_cntl',       'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[120] = {'path':'/dev/shm/isatss_data/info/120_cryosat_disp_cntl',   'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[121] = {'path':'/data/isatss_data/data/121_cryosat_disp_data',      'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[122] = {'path':'/dev/shm/isatss_data/info/122_cryosat_disp_info',   'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[123] = {'path':'/dev/shm/isatss_data/info/123_cryosat_proc_cntl',   'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[124] = {'path':'/data/isatss_data/data/124_cryosat_proc_data',      'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[125] = {'path':'/dev/shm/isatss_data/info/125_cryosat_proc_info',   'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[130] = {'path':'/dev/shm/isatss_data/info/130_altika_disp_cntl',    'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[131] = {'path':'/data/isatss_data/data/131_altika_disp_data',       'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[132] = {'path':'/dev/shm/isatss_data/info/132_altika_disp_info',    'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[133] = {'path':'/dev/shm/isatss_data/info/133_altika_proc_cntl',    'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[134] = {'path':'/data/isatss_data/data/134_altika_proc_data',       'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[135] = {'path':'/dev/shm/isatss_data/info/135_altika_proc_info',    'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[140] = {'path':'/dev/shm/isatss_data/info/140_sentinel_disp_cntl',  'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[141] = {'path':'/data/isatss_data/data/141_sentinel_disp_data',     'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[142] = {'path':'/dev/shm/isatss_data/info/142_sentinel_disp_info',  'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[143] = {'path':'/dev/shm/isatss_data/info/143_sentinel_proc_cntl',  'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[144] = {'path':'/data/isatss_data/data/144_sentinel_proc_data',     'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[145] = {'path':'/dev/shm/isatss_data/info/145_sentinel_proc_info',  'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[150] = {'path':'/dev/shm/isatss_data/info/150_vice_puller_cntl',    'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[151] = {'path':'/dev/shm/isatss_data/info/151_vice_puller_info',    'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[152] = {'path':'/data/isatss_data/data/152_vice_puller_data',       'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data/isatss_data'}

nodes[153] = {'path':'/dev/shm/isatss_data/info/153_vice_stitcher_cntl',  'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[154] = {'path':'/dev/shm/isatss_data/info/154_vice_stitcher_info',  'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[155] = {'path':'/data/isatss_data/data/155_vice_stitcher_data',     'filesystem':'/data',   'ctype':'data','stype':'attached','root':'/data'}
nodes[156] = {'path':'/dev/shm/isatss_data/info/156_vice_proj_cntl',      'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[270] = {'path':'/home/brapp/checkisatss/pullFromPDA/Global/ASCAT/metopa',         'filesystem':'/home',       'ctype':'data','stype':'attached','root':'/home/lbyerle/checkisatss/pullFromPDA'}
nodes[271] = {'path':'/home/brapp/checkisatss/pullFromPDA/Global/ASCAT/metopb',         'filesystem':'/home',       'ctype':'data','stype':'attached','root':'/home/lbyerle/checkisatss/pullFromPDA'}
nodes[272] = {'path':'/dev/shm/isatss_data/info/272_ascat_dispatch_cntl',                 'filesystem':'/dev/shm',    'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[273] = {'path':'/dev/shm/isatss_data/info/273_ascat_dispatch_info',                 'filesystem':'/dev/shm',    'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[274] = {'path':'/home/brapp/isatss_data/274_ascat_dispatch_data',                 'filesystem':'/home',       'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}


nodes[700] = {'path':'/dev/shm/isatss_data/info/700_dmsp_f15_cut_cntl',     'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[702] = {'path':'/dev/shm/isatss_data/info/702_dmsp_f15_cut_input',    'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[703] = {'path':'/data/isatss_data/data/703_dmsp_f15_cut_data',        'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[704] = {'path':'/dev/shm/isatss_data/info/704_dmsp_f15_cut_info_out', 'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[705] = {'path':'/dev/shm/isatss_data/info/705_reproject_cntl',      'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[706] = {'path':'/dev/shm/isatss_data/info/706_reproject_input',     'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[707] = {'path':'/data/isatss_data/data/707_reproject_data',         'filesystem':'/data',    'ctype':'data','stype':'attached','root':'/data/isatss_data'}
nodes[708] = {'path':'/dev/shm/isatss_data/info/708_reproject_info_out',  'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

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
defaults['cluster_log']     = False

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
groups[4]['jobs'][3]     = {'host':1, 'cfg':'goes_stats_processor'}


groups[5]                = {}
groups[5]['name']        = 'FLS Processing'
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
'''
groups[7]                = {}
groups[7]['name']        = 'Cryosat Altimetry Processing'
groups[7]['description'] = """
Jobs for ingesting, processing, and pushing Cryosat altimetry products
"""
groups[7]['jobs']        = {}
groups[7]['jobs'][1]     = {'host':1, 'cfg':'cryosat_dispatcher'}
groups[7]['jobs'][2]     = {'host':1, 'cfg':'cryosat_processor'}

groups[8]                = {}
groups[8]['name']        = 'Himawari Tile Processing'
groups[8]['description'] = """
Jobs for ingesting, processing, and pushing Himawari tiles
"""
groups[8]['jobs']        = {}
groups[8]['jobs'][1]     = {'host':1, 'cfg':'star_dispatcher'}
groups[8]['jobs'][2]     = {'host':1, 'cfg':'h8_slab2tile'}


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


groups[11]                = {}
groups[11]['name']        = 'AMSR2 Imagery Processing'
groups[11]['description'] = """
Jobs for ingesting, processing, and pushing AMSR2 Imagery
"""
groups[11]['jobs']        = {}
groups[11]['jobs'][1]     = {'host':1, 'cfg':'amsr2_puller'}
groups[11]['jobs'][2]     = {'host':1, 'cfg':'amsr2_cutter'}
groups[11]['jobs'][3]     = {'host':1, 'cfg':'amsr2_projector'}


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
#groups[16]['jobs'][2]  = {'host':1,'cfg':'sentinel_processor'}

groups[17] = {}
groups[17]['name']     = 'VIIRS ice concentration processing'
groups[17]['description'] = """
VIIRS ice concentration processing chain
"""
groups[17]['jobs']     = {}
groups[17]['jobs'][1]  = {'host':1,'cfg':'ascat_dispatcher'}
groups[17]['jobs'][2]  = {'host':1,'cfg':'viirs_ice_stitcher'}
groups[17]['jobs'][3]  = {'host':1,'cfg':'viirs_ice_projector'}


