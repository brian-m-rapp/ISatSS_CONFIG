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
site = 'ROCK'

hosts = {}
hosts[1] = {'host':'shelby.napo.nws.noaa.gov', 'shortname':'shelby'}
hosts[2] = {'host':'shelby.napo.nws.noaa.gov', 'shortname':'ldm', 'sudocmd':'sudo -iu', 'user':'ldm', 'ext':1338, 'cmd':74, 'resp':75}

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
nodes[74] = {'path':'/scratch/isatss_data/info/74_agent86_commands_out',  'filesystem': '/scratch', 'ctype':'cmd', 'stype':'attached','root':'/scratch/isatss_data'}
nodes[75] = {'path':'/scratch/isatss_data/info/75_agent86_response',      'filesystem': '/scratch', 'ctype':'resp','stype':'attached','root':'/scratch/isatss_data'}
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
#nodes[42] = {'path':'/dev/shm/isatss_data/info/42_ldm_arch_input',        'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'} #
nodes[42] = {'path':'/home/brapp/data/isatss_data/042_ldm_out_data',      'filesystem':'/raftr',   'ctype':'data', 'stype':'attached', 'root':'/raftr/isatss_data', 'incinerator':{'gid':2,'jid':1}}
nodes[54] = {'path':'/dev/shm/isatss_data/info/54_ldm_out_input',         'filesystem': '/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[58] = {'path':'/dev/shm/isatss_data/58_pda',                        'filesystem': '/dev/shm',  'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[59] = {'path':'/dev/shm/isatss_data/59_pda_replicator_in',          'filesystem': '/dev/shm',  'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[60] = {'path':'/mnt/ldm2/decoders',                                 'filesystem': '/mnt/ldm2', 'ctype':'data','stype':'network', 'root':'/mnt/ldm2', 'incinerator':{'gid':2,'jid':1}} 

nodes[70] = {'path':'/dev/shm/isatss_data/info/70_gcom_cntl',             'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[71] = {'path':'/dev/shm/isatss_data/info/71_gcom_info',             'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[72] = {'path':'/dev/shm/isatss_data/data/72_gcom_data',             'filesystem':'/dev/shm','ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[73] = {'path':'/scratch/isatss_data/data/73_gcom_ledger',           'filesystem':'/scratch','ctype':'data','stype':'attached','root':'/scratch/isatss_data'}

nodes[80] = {'path':'/dev/shm/isatss_data/info/80_remote_dispatcher_cntl','filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[81] = {'path':'/dev/shm/isatss_data/info/81_ascat_info',            'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[82] = {'path':'/dev/shm/isatss_data/data/82_ascat_data',            'filesystem':'/dev/shm','ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[83] = {'path':'/scratch/isatss_data/data/83_ascat_ledger',          'filesystem':'/scratch','ctype':'data','stype':'attached','root':'/scratch/isatss_data'}

nodes[84] = {'path':'/dev/shm/isatss_data/info/84_amsr2_cutter_cntl',     'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[85] = {'path':'/dev/shm/isatss_data/info/85_amsr2_cutter_info',     'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[86] = {'path':'/home/brapp/data/isatss_data/86_amsr2_cutter_data',  'filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}

nodes[87] = {'path':'/dev/shm/isatss_data/info/87_amsr2_puller_cntl',     'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[88] = {'path':'/dev/shm/isatss_data/info/88_amsr2_puller_info',     'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[89] = {'path':'/home/brapp/data/isatss_data/89_amsr2_puller_data',  'filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}

nodes[90] = {'path':'/dev/shm/isatss_data/info/90_amsr2_proj_cntl',       'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[91] = {'path':'/dev/shm/isatss_data/info/91_amsr2_proj_info',       'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[92] = {'path':'/home/brapp/data/isatss_data/92_amsr2_projdata',     'filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}

nodes[93] = {'path':'/dev/shm/isatss_data/info/93_atms_puller_cntl',      'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[94] = {'path':'/dev/shm/isatss_data/info/94_atms_puller_info',      'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[95] = {'path':'/home/brapp/data/isatss_data/95_atms_puller_data',   'filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}

nodes[96] = {'path':'/dev/shm/isatss_data/info/96_atms_cutter_cntl',      'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[97] = {'path':'/dev/shm/isatss_data/info/97_atms_cutter_info',      'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[98] = {'path':'/home/brapp/data/isatss_data/98_atms_cutter_data',   'filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}
nodes[99] = {'path':'/dev/shm/isatss_data/info/99_atms_proj_cntl',        'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[100] = {'path':'/scratch/isatss_data/ledgers',                      'filesystem':'/scratch','ctype':'data','stype':'attached','root':'/scratch/isatss_data'}
nodes[101] = {'path':'/dev/shm/isatss_data/info/101_jason_puller_cntl',   'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[102] = {'path':'/dev/shm/isatss_data/info/102_jason_puller_info',   'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[103] = {'path':'/home/brapp/data/isatss_data/103_jason_puller_data','filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}

nodes[104] = {'path':'/dev/shm/isatss_data/info/104_atms_puller_cntl',    'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[105] = {'path':'/dev/shm/isatss_data/info/105_atms_puller_info',    'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[106] = {'path':'/home/brapp/data/isatss_data/106_atms_puller_data', 'filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}

nodes[107] = {'path':'/dev/shm/isatss_data/info/107_atms_cutter_cntl',    'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[108] = {'path':'/dev/shm/isatss_data/info/108_atms_cutter_info',    'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[109] = {'path':'/home/brapp/data/isatss_data/109_atms_cutter_data', 'filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}

nodes[110] = {'path':'/dev/shm/isatss_data/info/110_atms_proj_cntl',      'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[120] = {'path':'/dev/shm/isatss_data/info/120_gpm_puller_cntl',     'filesystem':'/dev/shm','ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[121] = {'path':'/dev/shm/isatss_data/info/121_gpm_puller_info',     'filesystem':'/dev/shm','ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[122] = {'path':'/home/brapp/data/isatss_data/122_gpm_puller_data',  'filesystem':'/home/brapp/data','ctype':'data','stype':'attached','root':'/home'}

nodes[700] = {'path':'/dev/shm/isatss_data/info/700_ssmi_cut_cntl',       'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[702] = {'path':'/dev/shm/isatss_data/info/702_ssmi_cut_input',      'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[703] = {'path':'/home/brapp/data/isatss_data/703_ssmi_cut_data',    'filesystem':'/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[704] = {'path':'/dev/shm/isatss_data/info/704_ssmi_cut_info_out',   'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

nodes[705] = {'path':'/dev/shm/isatss_data/info/705_reproject_cntl',     'filesystem':'/dev/shm', 'ctype':'cntl','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[706] = {'path':'/dev/shm/isatss_data/info/706_reproject_input',    'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[707] = {'path':'/home/brapp/data/isatss_data/707_reproject_data',     'filesystem':'/dev/shm', 'ctype':'data','stype':'attached','root':'/dev/shm/isatss_data'}
nodes[708] = {'path':'/dev/shm/isatss_data/info/708_reproject_info_out', 'filesystem':'/dev/shm', 'ctype':'info','stype':'attached','root':'/dev/shm/isatss_data'}

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
defaults['sudocmd']         = 'sudo -iu'

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
#groups[1]['jobs'][3]  = {'host':1, 'cfg':'thread_test_config'}

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
groups[4]['jobs'][3]  = {'host':1,'cfg':'gcom_puller'}

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
groups[6]['jobs'][2]  = {'host':2,'cfg':'g16_tile_replicator'}



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

# g17_packets
groups[8] = {}
groups[8]['name']     = 'goes-17_grb_pkt_l1b_processing'
groups[8]['description'] = """
The pkt_l1b_processing group generates AWIPS-II compatible reflectance and brightness temperature
tiles from incoming GRB CCSDS packets.
"""
groups[8]['jobs']     = {}
"""
groups[8]['jobs'][1]  = {'host':1,'cfg':'g17_gpacket_config',        'icfg':{'io':{'x':200,'y':1200}}}
groups[8]['jobs'][2]  = {'host':1,'cfg':'g17_grb_abi_lhcp_proc',     'icfg':{'io':{'x':1400,'y':600}}}
groups[8]['jobs'][3]  = {'host':1,'cfg':'g17_grb_abi_rhcp_proc',     'icfg':{'io':{'x':1400,'y':200}}}
groups[8]['jobs'][4]  = {'host':1,'cfg':'g17_grb_abi_bnd2_proc',     'icfg':{'io':{'x':1400,'y':1000}}}
groups[8]['jobs'][5]  = {'host':1,'cfg':'g17_grb_glm_proc',          'icfg':{'io':{'x':1400,'y':1800}}}
"""

groups[9] = {}
groups[9]['name']     = 'pda'
groups[9]['description'] = """
PDA product group
"""
groups[9]['jobs']     = {}
groups[9]['jobs'][1] = {'host':2,'cfg':'pda_dispatcher'}
groups[9]['jobs'][2] = {'host':2,'cfg':'pda_replicator'}


groups[10] = {}
groups[10]['name']     = 'misc_retrieval'
groups[10]['description'] = """
Miscellaneous remote retrieval jobs
"""
groups[10]['jobs']     = {}
groups[10]['jobs'][1] = {'host':1, 'cfg':'remote_dispatcher'}
groups[10]['jobs'][2] = {'host':1, 'cfg':'amsr2_puller'}
groups[10]['jobs'][3] = {'host':1, 'cfg':'jason_dispatcher'}
groups[10]['jobs'][4] = {'host':1, 'cfg':'atms_dispatcher'}

groups[11] = {}
groups[11]['name']     = 'Cutters'
groups[11]['description'] = """
Miscellaneous file cutter jobs
"""
groups[11]['jobs']     = {}
groups[11]['jobs'][1] = {'host':1, 'cfg':'atms_cutter'}

groups[12] = {}
groups[12]['name']     = 'ATMS'
groups[12]['description'] = """
ATMS processing jobs
"""
groups[12]['jobs']     = {}
groups[12]['jobs'][1] = {'host':1, 'cfg':'atms_dispatcher'}
groups[12]['jobs'][2] = {'host':1, 'cfg':'atms_cutter'}
groups[12]['jobs'][3] = {'host':1, 'cfg':'atms_projector'}

groups[13] = {}
groups[13]['name']     = 'GPM GMI'
groups[13]['description'] = """
GPM GMI processing jobs
"""
groups[13]['jobs']     = {}
groups[13]['jobs'][1] = {'host':1, 'cfg':'gpm_dispatcher'}
