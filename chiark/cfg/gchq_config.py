"""
    IDP Satellite Support Subsystem
    Copyright (C) 2017 Joseph K. Zajic (joe.zajic@noaa.gov), Brian M. Rapp (brian.rapp@noaa.gov)

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

'''
The agent99 module knows what type of message is being sent:
	- telemetry
	- notification
	- state change

But, it doesn't know what the outbound interface is for that type of message


GCHQ knows what the outbound interfaces (publishers) are and will define site-wide defaults for each type, 
but the default can be overridden in the mi6 configuration for specific messages GCHQ knows what host 
it's running on and what site it belongs to, so it will add those values to the data where necessary.

mi6 knows how to format the data it gets from each agent99 module for each specific writer, so it will
reformat as necessary for that writer
'''

job = {}
job['name']         = 'gchq'
job['cmd']          = 'gchq'
job['class']        = 'GCHQ'
job['log']          = 'gchq_log'
job['log_node']     = 1
job['monitor_node'] = 32

job['input_type']   = {'type':'infofile', 'node':31}

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':job['log_node']}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loopsleep']                    = 1
job['loglevel']                     = 6
job['pause_empty']                  = 2
job['handler_pool_size']            = 5
job['watcher_timeout']              = 1000
job['queue_timeout']                = 2
job['telemetry_aggregation_period'] = 60

# Define each publisher with required connection parameters
job['publishers'] = {}
job['publishers']['telemetry'] = {}

job['publishers']['telemetry'][0] = {}
job['publishers']['telemetry'][0]['provider'] = 'vlabesearch'
job['publishers']['telemetry'][0]['enabled']  = False
job['publishers']['telemetry'][0]['parms']    = {'url':'https://vlab-dev.ncep.noaa.gov', 'company':10132, 'group':67059, 'sslnoverify':True, 'credid':0}
job['publishers']['telemetry'][0]['exclude']  = ['BB_Monitor', 'GOES_Radiance_Monitor'] 

job['publishers']['telemetry'][1] = {}
job['publishers']['telemetry'][1]['provider'] = 'vlabesearch'
job['publishers']['telemetry'][1]['enabled']  = False
job['publishers']['telemetry'][1]['parms']    = {'url':'https://vlab.ncep.noaa.gov', 'company':10132, 'group':67059, 'sslnoverify':False, 'credid':0}
job['publishers']['telemetry'][1]['exclude']  = ['BB_Monitor', 'GOES_Radiance_Monitor'] 

job['publishers']['telemetry'][2] = {}
job['publishers']['telemetry'][2]['provider'] = 'file'
job['publishers']['telemetry'][2]['enabled']  = True
job['publishers']['telemetry'][2]['parms']    = {'node':job['monitor_node'], 'rootname':'system_tm', 'mode':'daily'}
#job['publishers']['telemetry'][2]['exclude']  = ['BB_Monitor', 'GOES_Scene_Change']
job['publishers']['telemetry'][2]['exclude']  = ['BB_Monitor', 'GOES_Radiance_Monitor']

job['publishers']['telemetry'][3] = {}
job['publishers']['telemetry'][3]['provider'] = 'file'
job['publishers']['telemetry'][3]['enabled']  = False
job['publishers']['telemetry'][3]['parms']    = {'node':job['monitor_node'], 'rootname':'isatss_system_status', 'mode':'daily'}
job['publishers']['telemetry'][3]['include']  = ['BB_Monitor'] 

indexes = {}
indexes['abi_meta_stats'] = {}
indexes['abi_meta_stats']['doc_types']     = ['radiance_variance']
indexes['abi_meta_stats']['settings']      = {'number_of_shards':5, 'number_of_replicas':1}
indexes['abi_meta_stats']['time_template'] = '%Y-%m-%d'
indexes['abi_meta_stats']['time_field']    = 'scene_time'
indexes['abi_meta_stats']['batch_period']  = 30         # If <= 0, then batches are disabled, else submit batches this often (in seconds)
indexes['abi_meta_stats']['use_curator']   = True
indexes['abi_meta_stats']['curator_args']  = {}
indexes['abi_meta_stats']['curator_args']['use_threading']   = True
indexes['abi_meta_stats']['curator_args']['snapshot_maxage'] = 365
indexes['abi_meta_stats']['curator_args']['index_maxage']    = 365
indexes['abi_meta_stats']['curator_args']['age_units']       = 'days'
indexes['abi_meta_stats']['curator_args']['time_template']   = indexes['abi_meta_stats']['time_template']

job['publishers']['telemetry'][4] = {}
job['publishers']['telemetry'][4]['provider']            = 'esearch'
job['publishers']['telemetry'][4]['enabled']             = False
job['publishers']['telemetry'][4]['parms']               = {}
#job['publishers']['telemetry'][4]['parms']['connection'] = [{'host':'isatss', 'port':9200, 'use_ssl': False}, {'host':'lotus', 'port':9200, 'use_ssl':False}]
job['publishers']['telemetry'][4]['parms']['connection'] = [{'host':'isatss', 'port':9200, 'use_ssl': False}]
job['publishers']['telemetry'][4]['parms']['indexes']    = indexes
job['publishers']['telemetry'][4]['parms']['cache']      = {'node': job['cache_node'], 'rootname': 'lotus', 'batch_size':100} # Filename = <node>/<rootname>_<index>.cache
job['publishers']['telemetry'][4]['include']             = ['GOES_Radiance_Monitor']


esearch_connection = [
	{
		'host':    'isatss', 
		'port':    9200, 
		'use_ssl': False
	}
]

indexes = {}
indexes['abi_meta_stats'] = {}
#indexes['abi_meta_stats']['index_alias']   = 'abi_meta_stats'
indexes['abi_meta_stats']['doc_types']     = ['radiance_variance']
indexes['abi_meta_stats']['settings']      = {'number_of_shards':5, 'number_of_replicas':1}
indexes['abi_meta_stats']['time_template'] = '%Y-%m-%d'
indexes['abi_meta_stats']['batch_period']  = 0         # If <= 0, then batches are disabled, else submit batches this often (in seconds)
indexes['abi_meta_stats']['use_curator']   = True
indexes['abi_meta_stats']['curator_args']  = {}
indexes['abi_meta_stats']['curator_args']['use_threading']   = True
indexes['abi_meta_stats']['curator_args']['snapshot_maxage'] = 30
indexes['abi_meta_stats']['curator_args']['index_maxage']    = 7
indexes['abi_meta_stats']['curator_args']['age_units']       = 'days'
indexes['abi_meta_stats']['curator_args']['time_template']   = indexes['abi_meta_stats']['time_template']
#indexes['abi_meta_stats']['curator_args']['es_repo']         = 'abi_meta_stats-backup'
#indexes['abi_meta_stats']['curator_args']['repo_location']   = 'abi_meta_stats-repo'
#indexes['abi_meta_stats']['curator_args']['index_prefix']    = 'abi_meta_stats-'

# index_alias = key
# index_prefix = key+'-'
# es_repo = key+'-backup'
# repo_location = key+'-repo'

job['publishers']['telemetry'][4] = {}
job['publishers']['telemetry'][4]['provider']            = 'esearch'
job['publishers']['telemetry'][4]['enabled']             = True
job['publishers']['telemetry'][4]['parms']               = {}
job['publishers']['telemetry'][4]['parms']['connection'] = esearch_connection
job['publishers']['telemetry'][4]['parms']['indexes']    = indexes
job['publishers']['telemetry'][4]['include']             = ['GOES_Radiance_Values']

job['publishers']['alert'] = {}
job['publishers']['alert'][0] = {}
job['publishers']['alert'][0]['provider'] = 'file'
job['publishers']['alert'][0]['enabled']  = True
job['publishers']['alert'][0]['parms']    = {'node':job['monitor_node'], 'rootname':'alerts', 'mode':'daily'}

job['publishers']['notification'] = {}
job['publishers']['notification'][0] = {}
job['publishers']['notification'][0]['provider'] = 'file'
job['publishers']['notification'][0]['enabled']  = True
job['publishers']['notification'][0]['parms']    = {'node':job['monitor_node'], 'rootname':'notifications', 'mode':'daily'}

# Define default message parameters
job['publishers']['telemetry'][0]['defaults']    = {'index':'isatss_app_telemetry'}
job['publishers']['telemetry'][1]['defaults']    = {'index':'isatss_app_telemetry'}
job['publishers']['alert'][0]['defaults']        = {}
job['publishers']['notification'][0]['defaults'] = {}

# Define products
job['intel'] = {}
job['intel']['pmd_telemetry']  = {'enabled':True,  'module':'im_daemon',      'class':'PMDTelemetry'}
job['intel']['abi_summary']    = {'enabled':True,  'module':'agent99_grb',    'class':'ABISummary'}
job['intel']['host_telemetry'] = {'enabled':True,  'module':'mi6',            'class':'HostTelemetry'}
job['intel']['big_brother']    = {'enabled':False, 'module':'bbmon',          'class':'BBMon','args':{}}
job['intel']['big_brother']['args']['excluded_jobs']      = {3:[11]}
job['intel']['big_brother']['args']['job_thresholds']     = {'latency_yellow':120,'latency_red':240,'restart_yellow':4,'restart_red':8}
job['intel']['big_brother']['args']['input_thresholds']   = {'last_received_yellow':330,'last_received_red':660}
job['intel']['big_brother']['args']['output_thresholds']  = {'last_sent_yellow':330,'last_sent_red':660}
job['intel']['big_brother']['args']['missing_thresholds'] = {'area_count_yellow':283,'area_count_red':566,'in_count_yellow':283,'in_count_red':566,'tile_count_yellow':952,'tile_count_red':1904,'window_start':1200,'window_length':3600}
job['intel']['goes_telemetry'] = {'enabled':True, 'module':'goes_telemetry', 'class':'GoesStatusOutput', 'args':{}}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}	#or include
