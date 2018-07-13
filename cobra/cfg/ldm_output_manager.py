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

job = {}
job['name']     = 'ldm_output_manager'
job['cmd']      = 'ldmer'
job['class']    = 'LDMer'
job['log']      = 'ldm_output_log'
job['log_node'] = 1

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':job['log_node']}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 5

job['cntl_node']        = 56

job['ldm_monitor']      = {'active':True, 'interval':60, 'restart':True}
job['verbose_ldmd_log'] = False
job['ldm_lib']          = '/usr/local/ldm/lib64'
job['ldmadmin']         = '/usr/local/ldm/bin/ldmadmin'
job['pqcat']            = '/usr/local/ldm/bin/pqcat'
job['pqcheck']          = '/usr/local/ldm/bin/pqcheck'

job['ldmd_cfg_file']    = '/usr/local/ldm/etc/ldmd.conf'
job['pqact_cfg_file']   = '/usr/local/ldm/etc/pqact.conf'
job['queue_file']       = '/usr/local/ldm/var/queues/ldm.pq'

job['ldmd_config']      = {}
job['ldmd_config']['allow'] = []
job['ldmd_config']['allow'].append({'feedset':'ANY', 'hostname':'^140.90.141.190$', 'OK':'', 'not':'','desc':['NAPO Lab']})
job['ldmd_config']['allow'].append({'feedset':'ANY', 'hostname':'^10.90.80.10$',    'OK':'', 'not':'','desc':['Unknown']})
job['ldmd_config']['allow'].append({'feedset':'ANY', 'hostname':'^165.92.60.60$',   'OK':'', 'not':'','desc':['Unknown']})

job['input_type']       = {'type':'infofile','node':54, 'delete_info':True, 'delete_file':True}
job['files_per_cycle']	= 50
job['watcher_timeout']  = 1000

