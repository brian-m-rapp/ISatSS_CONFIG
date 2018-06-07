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
job['update_manifest']         = {'on_shutdown':True, 'on_loop':True,'deltas':'sbn_manifest_deltas'}
#job['tracker_config']          = {'tracker_class':'tracker','args':{}}
product_type_map = {
	'properties': {
		'wmo':      {'type':'text'},
		'src':      {'type':'text'},
		'rcvstamp': {'type': 'double'},
		'fsize':    {'type':'long'}
	}
}

job['tracker_config'] = {'tracker_class':'esearch_tracker','args':{}}
job['tracker_config']['args']['connection'] = [{'host':'isatss', 'port':9200, 'use_ssl':False}]
job['tracker_config']['args']['topnode']    = 600
job['tracker_config']['args']['index']      = 'sbn_products'
job['tracker_config']['args']['doc_type']   = 'products'
job['tracker_config']['args']['settings']   = {'number_of_shards':5, 'number_of_replicas':0}
job['tracker_config']['args']['mapping']    = product_type_map
