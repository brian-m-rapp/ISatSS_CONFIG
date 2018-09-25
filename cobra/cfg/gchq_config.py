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
job['handler_pool_size']            = 1
job['watcher_timeout']              = 1000
job['queue_timeout']                = 2
job['telemetry_aggregation_period'] = 60

# Define each publisher with required connection parameters
"""
The 'publishers' dictionary defines site-specific parameters for all of the gchq publishers defined in ISatSS/cfg/gchq_defaults.py.
There is a separate dictionary for each publishers data type ('telemetry', 'alert', and 'notification').  Each publisher data type
dictionary contains a dictionary for each instance of that data type.  Each publisher instance dictionary contains the following:
Dictionary fields
	'provider'	(required)	Type for the publisher.  Valid types are 'vlabesearch', 'file', and 'vlabforum'.  'vlabesearch' signifies
							the publisher is an elasticSearch database hosted on VLab.  'file' is a flat file stored on a node defined
							in isatss_config, and 'vlabforum' is for a forum hosted on VLab.
	'enabled'	(required)	Indicates whether or not the provider instance is enabled.  Values are True of False.
	'parms'		(required)	Dictionary of provider-type-specific parameters.  For 'vlabesearch' providers, possible keys are:
							'url'			URL for accessing the publisher.
							'company'		Liferay companyID value for the elasticSearch instance.
							'group'			Liferay groupID value for the elasticSearch instance.
							'sslnoverify'	Specifies whether or not to validate the reported SSL certificate.  Value are True or False.
	'include'	(optional)	List of messages to publish.  If specified, this must be all inclusive.  Only those messages listed will be
							published
	'exclude'	(optional)	List of messages to exclude from publishing.  If specified, all message except those in the exclude list
							will be published.
	'defaults'	(optional)	Publisher-type-specific default values dictionary.  For vlabesearch, the key can be 'index', which is the
							name of the default index for this esearch publisher.  The default value can be overridden by a specific
							message index value from gchq_defaults.  For a vlabforum publisher, the key can be the default 'forumid'.
							There are no defaults for 'file' publishers.
"""
job['publishers'] = {}
job['publishers']['telemetry'] = {}

job['publishers']['telemetry'][0] = {}
job['publishers']['telemetry'][0]['provider'] = 'vlabesearch'
job['publishers']['telemetry'][0]['enabled']  = True
job['publishers']['telemetry'][0]['parms']    = {'url':'https://vlab-dev.ncep.noaa.gov', 'company':10132, 'group':67059, 'sslnoverify':True}
job['publishers']['telemetry'][0]['exclude']  = ['BB_Monitor', 'GOES_Radiance_Monitor'] 

job['publishers']['telemetry'][1] = {}
job['publishers']['telemetry'][1]['provider'] = 'vlabesearch'
job['publishers']['telemetry'][1]['enabled']  = False
job['publishers']['telemetry'][1]['parms']    = {'url':'https://vlab.ncep.noaa.gov', 'company':10132, 'group':67059, 'sslnoverify':False}
job['publishers']['telemetry'][1]['exclude']  = ['BB_Monitor', 'GOES_Radiance_Monitor'] 

job['publishers']['telemetry'][2] = {}
job['publishers']['telemetry'][2]['provider'] = 'file'
job['publishers']['telemetry'][2]['enabled']  = True
job['publishers']['telemetry'][2]['parms']    = {'node':job['monitor_node'], 'rootname':'system_tm', 'mode':'daily'}
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
indexes['abi_meta_stats']['batch_period']  = 60         # If <= 0, then batches are disabled, else submit batches this often (in seconds)
indexes['abi_meta_stats']['use_curator']   = True
indexes['abi_meta_stats']['curator_args']  = {}
indexes['abi_meta_stats']['curator_args']['use_threading']   = True
indexes['abi_meta_stats']['curator_args']['snapshot_maxage'] = 60
indexes['abi_meta_stats']['curator_args']['index_maxage']    = 30
indexes['abi_meta_stats']['curator_args']['age_units']       = 'days'
indexes['abi_meta_stats']['curator_args']['time_template']   = indexes['abi_meta_stats']['time_template']

job['publishers']['telemetry'][4] = {}
job['publishers']['telemetry'][4]['provider']            = 'esearch'
job['publishers']['telemetry'][4]['enabled']             = True
job['publishers']['telemetry'][4]['parms']               = {}
job['publishers']['telemetry'][4]['parms']['connection'] = [{'host':'isatss', 'port':9200, 'use_ssl': False}]
job['publishers']['telemetry'][4]['parms']['indexes']    = indexes
job['publishers']['telemetry'][4]['include']             = ['GOES_Radiance_Monitor']

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

"""
The 'intel' dictionary defines agent13 processing agent classes that will be used and instantiated to perform
additional processing on specific messages.  Each key is a unique convenience name with the following dictionary keys:
'enabled'	(Required)	Whether or not this intel agent is enabled.  Values are True or False.
'module'	(Required)	Name of the module containing the Agent13 subclass.
'class'		(Required)	Name of the agent13 class to instantiate.  On creation, a list of registered messages is
						created for the message types this agent will respond to.  When a message of one of the registered
						types is found, the agent13.update() method will be called to operate on that message and
						submit the results to the publisher at the appropriate point.
"""
job['intel'] = {}
job['intel']['pmd_telemetry']       = {'enabled':True,  'module':'im_daemon',             'class':'PMDTelemetry'}
job['intel']['abi_summary']         = {'enabled':True,  'module':'agent99_grb',           'class':'ABISummary'}
job['intel']['host_telemetry']      = {'enabled':True,  'module':'mi6',                   'class':'HostTelemetry'}
job['intel']['goes_telemetry']      = {'enabled':True,  'module':'goes_telemetry',        'class':'GoesStatusOutput','args':{}}
job['intel']['radiance_aggregator'] = {'enabled':True,  'module':'g17_radiance_analysis', 'class':'RadianceAggregator'}
job['intel']['big_brother']         = {'enabled':False, 'module':'bbmon',                 'class':'BBMon', 'args':{'excluded_jobs':{3:[11]}}}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}	#or include
