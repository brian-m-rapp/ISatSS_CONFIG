# ldm tracker config


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
job['name']     = 'sbn_ldm_tracker'
job['cmd']      = 'ldmtracker'
job['class']    = 'LDMT'
job['log']      = 'sbn_ldm_tracker_log'
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

job['ldmd_log']     = '/data/ldm/logs/ldmd.log'
job['max_proctime'] = 10
job['maxlines']     = 1000

job['manifest']                = 'sbn_manifest'
job['update_manifest']         = {'on_shutdown':True, 'on_loop':True, 'deltas':'sbn_manifest_deltas'}
#job['tracker_config']          = {'tracker_class':'tracker','args':{}}
product_type_map = {
	'properties': {
		'wmo':       {'type': 'text'},
		'src':       {'type': 'text'},
		'keys':      {'type': 'keyword', 'index': True},
		'rcvstamp':  {'type': 'date'},
		'reftime':   {'type': 'date'},
		'fsize':     {'type': 'long'},
		'clat':      {'type': 'float'},
		'clon':      {'type': 'float'},
		'latency':   {'type': 'long'},
		'layer':     {'type': 'text'},
		'station':   {'type': 'text'},
		'parameter': {'type': 'text'},
		'ntiles':    {'type': 'long'},
		'tileno':    {'type': 'long'}
	}
}

curator_config = {
    'client': {
        'hosts': '127.0.0.1',
        'port': 9200,
#        'url_prefix': null,
        'use_ssl': False,
#        'certificate': null,
#        'client_cert': null,
#		'client_key': null,
        'ssl_no_validate': False,
#        'http_auth': null,
        'timeout': 30,
        'master_only': False
    },
    'logging': {
        'loglevel': 'INFO',
#        'logfile': null,
        'logformat': 'default',
        'blacklist': [
            'elasticsearch',
            'urllib3'
        ]
    }
}

job['tracker_config'] = {'tracker_class':'esearch_tracker', 'args':{}}
job['tracker_config']['args']['connection']       = [{'host':'masaq', 'port':9200, 'use_ssl':False}]
job['tracker_config']['args']['topnode']          = 600
job['tracker_config']['args']['index']            = 'sbn_products'
job['tracker_config']['args']['doc_type']         = 'products'
job['tracker_config']['args']['settings']         = {'number_of_shards':5, 'number_of_replicas':1}
job['tracker_config']['args']['mapping']          = product_type_map
job['tracker_config']['args']['curator_config']   = curator_config

curator_actions = {
	1: {
		'action': 'delete_snapshots',
		'description': 'Delete snapshots from sbn_products repository older than 60 days',
		'options': {
			'repository': 'sbn_products',
			'disable_action': True
		},
		'filters': [
			{
				'filtertype': 'pattern',
				'kind': 'prefix',
				'value': 'products-'
			},
			{
				'filtertype': 'age',
				'source': 'creation_date',
				'direction': 'older',
				'unit': 'days',
				'unit_count': 60
			}
		]
	}
}


job['agents'] = {}
job['agents']['abi_scmi'] = {'class':'abi_agent', 'format':'nc4', 'keys':['ABI', 'SCMI']}
