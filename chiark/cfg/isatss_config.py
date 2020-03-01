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
optional variables used by lib/im_cssh for authenticating the ops user

For Redhat and Centos, the default 'sudo -Su' works.
For openSUSE, use 'sudo -iu'.
"""

sudocmd = 'sudo -iu'    # defaults to 'sudo -Su'

"""
Name of the ISatSS Processing facility - MI6 includes this in telemetry, notifications, and alerts
"""

"""
The instance_attrs dictionary allows arbitrary variables to be defined based on an 'instance' key.
This is useful here since this same isatss_config file defines two separate instance of ISatSS.
The instance applied is determined by resolving the host name at runtime and matching it against
the hosts defined in the 'hosts' dictionary.  This in turn determines the instance_id to be applied
to define the hosts, groups, jobs, site ID, and tier in the current instance.
"""

instance_attrs = {}
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
hosts[2] = {'host':'grb01.nhc.noaa.gov','user':'ldm', 'ext':1336,'cmd':4,'resp':5}
"""
hosts = {'ROCK': {}}
hosts['ROCK'][1] = {'host':['ninja.dilireum.org'], 'shortname':'ninja'}
hosts['ROCK'][2] = {'host':['masaq.dilireum.org'], 'shortname':'masaq'}
hosts['ROCK'][3] = {'host':['masaq.dilireum.org'], 'shortname':'masaq', 'user':'ldm', 'ext':1338, 'cmd':4, 'resp':5}

"""
The nodes dictionary defines all filesystem locations that are accessed (read, write, delete) by ISatSS applications.  For clustered configurations, it is
assumed
that all hosts are configured with identical local file systems, and the same access to shared filesystems.  isatss_config.nodes is used in conjunction with
the
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
    root        (required)  the 'top' path controlled entirely by ISatSS.  When the host/isatss 'clean' command is executed, all files and directories below
this level are deleted.
    incinerator (optional)  dictionary containing the groupid and job idea of the host/incinerator instance responsible for managing the data stored on the
node
                            format:  {'gid':g, 'jid'j}

Regardless of configuration, nodes are required for the following system defaults (defined in isatss_config.defaults)

"""

fstypes = {}
fstypes['fastest'] = {'root':'/dev/shm/isatss_data', 'filesystem':'/dev/shm',     'stype':'attached'}
fstypes['local']   = {'root':'/scratch/isatss_data', 'filesystem':'/',            'stype':'attached'}

nodes = {}
nodes[0]   = {'path':'info/000_default_info',           'fstype':'local',   'ctype':'info'}
nodes[1]   = {'path':'001_log',                         'fstype':'local',   'ctype':'log', 'cutoff':100e6}
nodes[2]   = {'path':'info/002_agent86_cmd_out',        'fstype':'fastest', 'ctype':'cmd'}
nodes[3]   = {'path':'info/003_agent86_cmd_resp',       'fstype':'fastest', 'ctype':'resp'}
nodes[4]   = {'path':'info/004_ldm_agent86_cmd_out',    'fstype':'fastest', 'ctype':'cmd'}
nodes[5]   = {'path':'info/005_ldm_agent86_cmd_resp',   'fstype':'fastest', 'ctype':'resp'}
nodes[6]   = {'path':'006_work',                        'fstype':'local',   'ctype':'data'}
nodes[7]   = {'path':'007_agent86_cntl',                'fstype':'fastest', 'ctype':'cntl'}
nodes[8]   = {'path':'cntl/008_incinerator_cntl',       'fstype':'fastest', 'ctype':'cntl'}
nodes[9]   = {'path':'cntl/009_incinerator_ldm_cntl',   'fstype':'fastest', 'ctype':'cntl'}
nodes[10]  = {'path':'info/010_deaddrop_info',          'fstype':'local',   'ctype':'info'}
nodes[11]  = {'path':'cntl/011_mi6_cntl',               'fstype':'fastest', 'ctype':'cntl'}
nodes[12]  = {'path':'monitor_data',                    'fstype':'local',   'ctype':'data'}
nodes[13]  = {'path':'cntl/013_gchq_cntl',              'fstype':'fastest', 'ctype':'cntl'}
nodes[14]  = {'path':'cntl/014_mi6_ldm_cntl',           'fstype':'fastest', 'ctype':'cntl'}
nodes[15]  = {'path':'esearch_cache',                   'fstype':'local',   'ctype':'data'}

nodes[20]  = {'path':'info/20_ldmer_cntl',              'fstype':'fastest',  'ctype':'cntl'}
nodes[21]  = {'path':'data/21_pqact_dropzone',          'fstype':'local',    'ctype':'data'}
nodes[22]  = {'path':'info/22_ldm_queue_info_in',       'fstype':'fastest',  'ctype':'info'}
nodes[23]  = {'path':'data/23_ldm_queue_in',            'fstype':'local',    'ctype':'data'}

nodes[30]  = {'path':'info/30_ldm_dispatch_cntl',       'fstype':'fastest',  'ctype':'cntl'}
nodes[31]  = {'path':'data/31_input_archive',           'fstype':'local',    'ctype':'data'}
nodes[32]  = {'path':'data/32_abi_l1b',                 'fstype':'local',    'ctype':'data'}
nodes[33]  = {'path':'info/33_abi_l1b_info',            'fstype':'fastest',  'ctype':'info'}
nodes[34]  = {'path':'data/34_glm_l1b',                 'fstype':'local',    'ctype':'data'}
nodes[35]  = {'path':'info/35_glm_l1b',                 'fstype':'fastest',  'ctype':'info'}
nodes[36]  = {'path':'info/36_input_archive_info',      'fstype':'local',    'ctype':'info'}

nodes[40] = {'path':'info/40_ldm_repl_cntl',            'fstype':'fastest',  'ctype':'cntl'}
nodes[41] = {'path':'data/41_abil1b_archive',           'fstype':'local',    'ctype':'data'}
nodes[42] = {'path':'data/42_glml1b_archive',           'fstype':'local',    'ctype':'data'}

# system defaults
defaults = {}
defaults['log']             = 'isatss_log'               # default log file name
defaults['log_node']        = 1                              # path to storage area for log files
defaults['loglevel']        = 5                              # V_STATUS logging level
defaults['work_node']       = 6                             # path to storage area for temporary work
defaults['fault_node']      = 7                             # path to storage area for stored faulty data files
defaults['loopsleep']       = 0                            # im_daemon loop delay
defaults['pidpath']         = '/dev/shm/isatss_data/pid'   # path to storage area for pid files
defaults['node']            = 0                            # default station to write and read info messages
defaults['traceprint']      = False               # default exception printing to include traceback or not
defaults['shutdown_wait']   = 60                   # default time to wait for an application to shutdown
defaults['command_node']    = 2                   # default station to write command messages    (hosts[i]['cmd']
defaults['response_node']   = 3                   # default station to read command responses (hosts[i]['resp']
defaults['user']            = 'brapp'
defaults['sudocmd']         = 'sudo -Su'
defaults['vlab']            = {}
defaults['vlab']['url']     = 'https://vlab.ncep.noaa.gov'
defaults['vlab']['company'] = 10132
defaults['vlab']['group']   = 1334496        # ISatSS community group ID
defaults['logLockSize']     = '1G'

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
groups[1]['jobs'][3]  = {'host':3, 'cfg':'agent86_config'}

groups[2] = {}
groups[2]['name']     = 'incinerators'
groups[2]['description'] = """
The incinerators group includes an incinerator job for each host
in the system. 
"""
groups[2]['jobs']     = {}
groups[2]['jobs'][1]  = {'host':1, 'cfg':'incinerator_config', 'vars':{'cntl':8}}
groups[2]['jobs'][2]  = {'host':2, 'cfg':'incinerator_config', 'vars':{'cntl':8}}
groups[2]['jobs'][3]  = {'host':3, 'cfg':'incinerator_config', 'vars':{'cntl':9}}

groups[3] = {}
groups[3]['name']     = 'monitor'
groups[3]['description'] = """
The monitor group provides monitoring services for all hosts in the system.
An mi6 application running on each host collects server performance metrics, and
scrapes the log files of all applications, preparing condensed summary information
based on each application's agent86 class.

The mi6 applications write info messages to node 36 on each host, which are forwarded
by agent86 to node 36 on host 1.  An instance of the gchq application running on host 1
consumes the messages, and writes them to a file named system_tm.YYYYMMDD on node 37. 
"""
groups[3]['jobs']     = {}
groups[3]['jobs'][1]  = {'host':1,'cfg':'mi6_config',  'vars':{'deaddrop':10, 'cntl':11}}
groups[3]['jobs'][2]  = {'host':2,'cfg':'mi6_config',  'vars':{'deaddrop':10, 'cntl':11}}
groups[3]['jobs'][3]  = {'host':3,'cfg':'mi6_config',  'vars':{'deaddrop':10, 'cntl':14}}
groups[3]['jobs'][4]  = {'host':2,'cfg':'gchq_config', 'vars':{'deaddrop':10, 'cntl':13, 'monitor':12, 'cache':15}}

# io1_ldm
groups[4] = {}
groups[4]['name']     = 'ldm'
groups[4]['description'] = """
The io1_ldm group provides i/o services for host #1 including ldm based ingest, and  output queue insertion.
"""
groups[4]['jobs']     = {}
groups[4]['jobs'][1]  = {'host':3,'cfg':'ldm_manager',    'vars':{'cntl':20, 'in':22, 'outdata':21}}
groups[4]['jobs'][2]  = {'host':2,'cfg':'ldm_dispatcher', 'vars':{'cntl':30, 'in':21, 'abiinfo':33, 'abidata':32, 'glminfo':35, 'glmdata':34, 'archinfo':36, 'archdata':31}}
groups[4]['jobs'][3]  = {'host':2,'cfg':'ldm_replicator', 'vars':{'cntl':40, 'in':36, 'abiarch':41, 'glmarch':42}}
