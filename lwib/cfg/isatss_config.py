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

"""hosts[1] = {'host':'lwib.napo.nws.gov', 'shortname':'lwib', 'sudocmd':'sudo -iu'}
"""

hosts[1] = {'host':'unallocated.barefruit.co.uk', 'shortname':'lwib', 'sudocmd':'sudo -iu'}

hattr = {}
hattr[1] = {'nics': [('netname', 'eth0')],   'filesystems': []}

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
nodes[0]  = {'path':'/home/lbyerle/scratch/isatss_data/info/default_info',		      'filesystem': '/home', 'ctype':'info','stype':'attached','root':'/home/lbyerle/scratch/isatss_data'}
nodes[1]  = {'path':'/home/lbyerle/scratch/isatss_data/log',                          'filesystem': '/home', 'ctype':'log', 'stype':'attached','root':'/home/lbyerle/scratch/isatss_data'}
nodes[2]  = {'path':'/home/lbyerle/scratch/isatss_data/info/02_agent86_commands_out', 'filesystem': '/home', 'ctype':'cmd', 'stype':'attached','root':'/home/lbyerle/scratch/isatss_data'}
nodes[3]  = {'path':'/home/lbyerle/scratch/isatss_data/info/03_agent86_response',     'filesystem': '/home', 'ctype':'resp','stype':'attached','root':'/home/lbyerle/scratch/isatss_data'}
nodes[10] = {'path':'/home/lbyerle/scratch/isatss_data/ledgers',                      'filesystem':' /home', 'ctype':'data','stype':'attached','root':'/home/lbyerle/scratch/isatss_data'}
nodes[11] = {'path':'/home/lbyerle/scratch/isatss_data/monitor_output',               'filesystem': '/home', 'ctype':'data','stype':'attached','root':'/home/lbyerle/scratch/isatss_data'}

nodes[41] = {'path':'/dev/shm/isatss_data/info/041_ldm_out_info',                   'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[42] = {'path':'/home/lbyerle/scratch/isatss_data/042_ldm_out_data',           'filesystem':'/home',  'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}

nodes[50] = {'path':'/dev/shm/isatss_data/info/050_gcom_puller_cntl',              'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[51] = {'path':'/dev/shm/isatss_data/info/051_gcom_puller_info',              'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[52] = {'path':'/home/lbyerle/isatss_data/052_gcom_puller_data',              'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[54] = {'path':'/dev/shm/isatss_data/info/054_gcom_wspd_pro_cntl',            'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[55] = {'path':'/dev/shm/isatss_data/info/055_gcom_rep_cntl',                 'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[56] = {'path':'/dev/shm/isatss_data/info/056_gcom_wspd_rep_info',            'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[57] = {'path':'/home/lbyerle/isatss_data/057_gcom_wspd_rep_data',            'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[58] = {'path':'/dev/shm/isatss_data/info/058_gcom_ocean_rep_info',           'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[59] = {'path':'/home/lbyerle/isatss_data/059_gcom_ocean_rep_data',           'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}

nodes[120] = {'path':'/dev/shm/isatss_data/info/120_amsr2_ocean_cut_info',           'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[121] = {'path':'/home/lbyerle/isatss_data/121_amsr2_ocean_cut_data',           'filesystem':'/home',  'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[122] = {'path':'/dev/shm/isatss_data/info/122_amsr2_ocean_cut_cntl',           'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[123] = {'path':'/dev/shm/isatss_data/info/123_amsr2_ocean_proj_cntl',          'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[240] = {'path':'/dev/shm/isatss_data/info/240_gcom_puller_nhcprep_cntl',              'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[241] = {'path':'/dev/shm/isatss_data/info/241_gcom_puller_nhcprep_info',              'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[242] = {'path':'/home/lbyerle/isatss_data/242_gcom_puller_nhcprep_data',              'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[243] = {'path':'/dev/shm/isatss_data/info/243_amsr2_ocean_nhcprep_cut_cntl',          'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[244] = {'path':'/dev/shm/isatss_data/info/244_amsr2_ocean_nhcprep_cut_info',          'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[245] = {'path':'/home/lbyerle/isatss_data/245_amsr2_ocean_nhcprep_cut_data',          'filesystem':'/home',  'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[246] = {'path':'/dev/shm/isatss_data/info/246_amsr2_ocean_nhcprep_proj_cntl',         'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[270] = {'path':'/home/lbyerle/checkisatss/pullFromPDA/Global/ASCAT/metopa',         'filesystem':'/home',       'ctype':'data','stype':'attached','root':'/home/lbyerle/checkisatss/pullFromPDA'}
nodes[271] = {'path':'/home/lbyerle/checkisatss/pullFromPDA/Global/ASCAT/metopb',         'filesystem':'/home',       'ctype':'data','stype':'attached','root':'/home/lbyerle/checkisatss/pullFromPDA'}
nodes[272] = {'path':'/dev/shm/isatss_data/info/272_ascat_dispatch_cntl',                 'filesystem':'/dev/shm',    'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[273] = {'path':'/dev/shm/isatss_data/info/273_ascat_dispatch_info',                 'filesystem':'/dev/shm',    'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[274] = {'path':'/home/lbyerle/isatss_data/274_ascat_dispatch_data',                 'filesystem':'/home',       'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}

nodes[90] = {'path':'/dev/shm/isatss_data/info/90_jason_disp_cntl',     'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[91] = {'path':'/home/lbyerle/isatss_data/91_jason_disp_data',       'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[92] = {'path':'/dev/shm/isatss_data/info/92_jason_disp_info',     'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[93] = {'path':'/dev/shm/isatss_data/info/93_jason_proc_cntl',     'filesystem':'/home', 'ctype':'cntl','stype':'attached','root':'/home/lbyerle/isatss_data'}

nodes[135] = {'path':'/dev/shm/isatss_data/info/135_S3A_disp_cntl',     'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[136] = {'path':'/home/lbyerle/isatss_data/136_S3A_disp_data',       'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[137] = {'path':'/dev/shm/isatss_data/info/137_S3A_disp_info',     'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[138] = {'path':'/dev/shm/isatss_data/info/138_S3A_proc_cntl',     'filesystem':'/home', 'ctype':'cntl','stype':'attached','root':'/home/lbyerle/isatss_data'}

nodes[140] = {'path':'/dev/shm/isatss_data/info/140_S3B_disp_cntl',     'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[141] = {'path':'/home/lbyerle/isatss_data/141_S3B_disp_data',       'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[142] = {'path':'/dev/shm/isatss_data/info/142_S3B_disp_info',     'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[143] = {'path':'/dev/shm/isatss_data/info/143_S3B_proc_cntl',     'filesystem':'/home', 'ctype':'cntl','stype':'attached','root':'/home/lbyerle/isatss_data'}

nodes[145] = {'path':'/dev/shm/isatss_data/info/145_blend_tpw_disp_cntl',     'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[146] = {'path':'/home/lbyerle/isatss_data/146_blend_tpw_disp_data',       'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[147] = {'path':'/dev/shm/isatss_data/info/147_blend_tpw_disp_info',     'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[148] = {'path':'/dev/shm/isatss_data/info/148_blend_tpw_proc_cntl',     'filesystem':'/home', 'ctype':'cntl','stype':'attached','root':'/home/lbyerle/isatss_data'}

nodes[150] = {'path':'/dev/shm/isatss_data/info/150_blend_rr_disp_cntl',     'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[151] = {'path':'/home/lbyerle/isatss_data/151_blend_rr_disp_data',       'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[152] = {'path':'/dev/shm/isatss_data/info/152_blend_rr_disp_info',     'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[153] = {'path':'/dev/shm/isatss_data/info/153_blend_rr_proc_cntl',     'filesystem':'/home', 'ctype':'cntl','stype':'attached','root':'/home/lbyerle/isatss_data'}

nodes[155] = {'path':'/dev/shm/isatss_data/info/155_blend_pct_disp_cntl',     'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[156] = {'path':'/home/lbyerle/isatss_data/156_blend_pct_disp_data',       'filesystem':'/home',   'ctype':'data','stype':'attached','root':'/home/lbyerle/isatss_data'}
nodes[157] = {'path':'/dev/shm/isatss_data/info/157_blend_pct_disp_info',     'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[158] = {'path':'/dev/shm/isatss_data/info/158_blend_pct_proc_cntl',     'filesystem':'/home', 'ctype':'cntl','stype':'attached','root':'/home/lbyerle/isatss_data'}

# system default

defaults = {}
defaults['log']             = 'isatss_log'	  			# default log file name
defaults['log_node']        = 1							# path to storage area for log files
defaults['loglevel']        = 5							# V_STATUS logging level
defaults['work_node']       = 18							# path to storage area for temporary work
defaults['fault_node']      = 1							# path to storage area for stored faulty data files
defaults['loopsleep']       = 0                           # im_daemon loop delay
defaults['pidpath']         = '/home/lbyerle/scratch/isatss_data/pid'  # path to storage area for pid files
defaults['node']            = 0                     		# default station to write and read info messages
defaults['traceprint']      = False				  		# default exception printing to include traceback or not
defaults['shutdown_wait']   = 60					  		# default time to wait for an application to shutdown
defaults['command_node']    = 2                     		# default station to write command messages
defaults['response_node']   = 3                     		# default station to read command responses
defaults['user']            = 'lbyerle'
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
'''
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
'''

groups[2] = {}
groups[2]['name']     = 'incinerators'
groups[2]['description'] = """
The incinerators group includes an incinerator job for each host
in the system.
"""
groups[2]['jobs']     = {}
groups[2]['jobs'][1]  = {'host':1, 'cfg':'incinerator_config'}

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
groups[3]['jobs'][3]  = {'host':1, 'cfg':'gchq_config'}

groups[4]                = {}
groups[4]['name']        = 'GCOM AMSR2 OCEAN Processing'
groups[4]['description'] = """
Jobs for ingesting, processing, and pushing AMSR2 Ocean products
"""
groups[4]['jobs']        = {}
groups[4]['jobs'][1]     = {'host':1, 'cfg':'gcom_puller'}
groups[4]['jobs'][2]     = {'host':1, 'cfg':'gcom_ocean_replicator'}
groups[4]['jobs'][3]     = {'host':1, 'cfg':'gcom_processor'}
groups[4]['jobs'][4]     = {'host':1, 'cfg':'amsr2_ocean_cutter'}
groups[4]['jobs'][5]     = {'host':1, 'cfg':'amsr2_ocean_projector'}

groups[5]                = {}
groups[5]['name']        = 'GCOM AMSR2 OCEAN Processing NHC Prep'
groups[5]['description'] = """
Jobs for ingesting, processing, and pushing AMSR2 Ocean products, NHC Prep
"""
groups[5]['jobs']        = {}
groups[5]['jobs'][1]     = {'host':1, 'cfg':'gcom_puller_nhcprep'}
groups[5]['jobs'][2]     = {'host':1, 'cfg':'amsr2_ocean_cutter_nhcprep'}
groups[5]['jobs'][3]     = {'host':1, 'cfg':'amsr2_ocean_projector_nhcprep'}

groups[6]                = {}
groups[6]['name']        = 'ASCAT Processing'
groups[6]['description'] = """
Job processing ASCAT products 
"""
groups[6]['jobs']        = {}
groups[6]['jobs'][1]     = {'host':1,'cfg':'ascat_dispatcher'}

groups[7]                = {}
groups[7]['name']        = 'Jason2/3 Altimetry Processing'
groups[7]['description'] = """
Jobs for ingesting, processing, and pushing Altimetry data from Jason2/3
"""
groups[7]['jobs']        = {}
groups[7]['jobs'][1]     = {'host':1, 'cfg':'jason_dispatcher'}
groups[7]['jobs'][2]     = {'host':1, 'cfg':'jason_processor'}

groups[8]                = {}
groups[8]['name']        = 'Sentinel 3A Altimetry Processing'
groups[8]['description'] = """
Jobs for ingesting, processing, and pushing Altimetry data from Sentinel 3A
"""
groups[8]['jobs']        = {}
groups[8]['jobs'][1]     = {'host':1, 'cfg':'S3A_dispatcher_placeholder'}
groups[8]['jobs'][2]     = {'host':1, 'cfg':'S3A_processor'}

groups[9]                = {}
groups[9]['name']        = 'Sentinel 3B Altimetry Processing'
groups[9]['description'] = """
Jobs for ingesting, processing, and pushing Altimetry data from Sentinel 3B
"""
groups[9]['jobs']        = {}
groups[9]['jobs'][1]     = {'host':1, 'cfg':'S3B_dispatcher_placeholder'}
groups[9]['jobs'][2]     = {'host':1, 'cfg':'S3B_processor'}

groups[10]                = {}
groups[10]['name']        = 'Blended hydro TPW Processing'
groups[10]['description'] = """
Jobs for ingesting, processing, and pushing Blended hydro TPW products
"""
groups[10]['jobs']        = {}
groups[10]['jobs'][1]     = {'host':1, 'cfg':'blended_tpw_dispatcher'}
groups[10]['jobs'][2]     = {'host':1, 'cfg':'blended_tpw_processor'}

groups[11]                = {}
groups[11]['name']        = 'Blended hydro Rain Rate Processing'
groups[11]['description'] = """
Jobs for ingesting, processing, and pushing Blended hydro Rain Rate products
"""
groups[11]['jobs']        = {}
groups[11]['jobs'][1]     = {'host':1, 'cfg':'blended_rr_dispatcher'}
groups[11]['jobs'][2]     = {'host':1, 'cfg':'blended_rr_processor'}

groups[12]                = {}
groups[12]['name']        = 'Blended hydro Percent TPW Normal Processing'
groups[12]['description'] = """
Jobs for ingesting, processing, and pushing Blended hydro Rain PCT products
"""
groups[12]['jobs']        = {}
groups[12]['jobs'][1]     = {'host':1, 'cfg':'blended_pct_dispatcher'}
groups[12]['jobs'][2]     = {'host':1, 'cfg':'blended_pct_processor'}
