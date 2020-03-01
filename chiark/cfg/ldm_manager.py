# ldm configuration for grb data flow

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
try:
    import jobvarmod
    jobvars = jobvarmod.jobvars.copy()
except:
    jobvars = {}
    for parm in ['cntl','in','outdata']:
        jobvars[parm] = 0

job = {}
job['name']     = 'ldm_manager'
job['cmd']      = 'ldmer'
job['class']    = 'LDMer'
job['log']      = 'ldm_manager_log'
job['log_node'] = 1

job['data'] = {}
job['data']['ldm_data'] = {}
job['data']['ldm_data']['location']   = {'node':jobvars['outdata']}
job['data']['ldm_data']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['ldm_data']['method']     = {'technique':'inplace'}
job['data']['ldm_data']['activeonly'] = False
job['data']['ldm_data']['schedule']   = {'interval':300}

job['data']['log']                    = {}
job['data']['log']['location']        = {'node':job['log_node']}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 5

job['cntl_node']        = jobvars['cntl']

job['input_type']       = {'type':'infofile','node':jobvars['in'], 'delete_info':True, 'delete_file':True}
job['files_per_cycle']  = 50
job['watcher_timeout']  = 1000

job['ldm_monitor']      = {'active':True, 'interval':60, 'restart':True, 'shutdown_on_exit':True, 'restart_on_startup':True}
job['ldm_lib']          = {'ROCK':'/usr/local/ldm/lib64'}
job['ldmadmin']         = {'ROCK':'/usr/local/ldm/bin/ldmadmin'}
job['pqcat']            = {'ROCK':'/usr/local/ldm/bin/pqcat'}
job['pqcheck']          = {'ROCK':'/usr/local/ldm/bin/pqcheck'}
job['ldmd_cfg_file']    = {'ROCK':'/usr/local/ldm/etc/ldmd.conf'}
job['pqact_cfg_file']   = {'ROCK':'/usr/local/ldm/etc/pqact.conf'}
job['queue_file']       = '/usr/local/ldm/var/queues/ldm.pq'

job['ldmd_config'] = {}
job['ldmd_config']['requests'] = []
job['ldmd_config']['requests'].append({'feedset':'ANY', 'pattern':'OR_ABI-L1b.*', 'host':'192.168.2.20', 'desc':['WxConnect East GRB Antenna', 'Rack #1']})
job['ldmd_config']['requests'].append({'feedset':'ANY', 'pattern':'OR_GLM-L2.*',  'host':'192.168.2.20', 'desc':['WxConnect East GRB Antenna', 'Rack #1']})

job['ldmd_config']['allow'] = []
job['ldmd_config']['allow'].append({'feedset':'ANY', 'hostname':'192.168.2.*', 'OK':'', 'not':'', 'desc':['All downstream LDM']})

job['pqact_config'] = []
job['pqact_config'].append({'feedtype':'EXP', 'pattern':'^(\\/.*\\/)(OR_ABI-L1b.*.nc)', 'action':'FILE', 'options':'-overwrite -log -close', 'filename':{'datapath':'ldm_data','spec':'\\2'}, 'desc':['CSPP ABI L1B']})
job['pqact_config'].append({'feedtype':'EXP', 'pattern':'^(\\/.*\\/)(OR_GLM-L2.*.nc)',  'action':'FILE', 'options':'-overwrite -log -close', 'filename':{'datapath':'ldm_data','spec':'\\2'}, 'desc':['CSPP GLM L2']})

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include

