# dispatcher configuration for h8 data flow

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
job['name']     = 'gcom_ocean_replicator'
job['cmd']      = 'replicator'
job['class']    = 'Replicator'
job['log']      = 'gcom_ocean_replicator_log'
job['log_node'] = 1


job['data'] = {}
job['data']['gdata'] = {}
job['data']['gdata']['location']     = {'node':57}
job['data']['gdata']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['gdata']['method']       = {'technique':'inplace'}
job['data']['gdata']['activeonly']   = True
job['data']['gdata']['schedule']     = {'interval':600}

job['data']['odata'] = {}
job['data']['odata']['location']     = {'node':59}
job['data']['odata']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['odata']['method']       = {'technique':'inplace'}
job['data']['odata']['activeonly']   = True
job['data']['odata']['schedule']     = {'interval':600}

job['data']['ginfo'] = {}
job['data']['ginfo']['location']     = {'node':56}
job['data']['ginfo']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['ginfo']['method']       = {'technique':'inplace'}
job['data']['ginfo']['activeonly']   = True
job['data']['ginfo']['schedule']     = {'interval':600}

job['data']['oinfo'] = {}
job['data']['oinfo']['location']     = {'node':58}
job['data']['oinfo']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['oinfo']['method']       = {'technique':'inplace'}
job['data']['oinfo']['activeonly']   = True
job['data']['oinfo']['schedule']     = {'interval':600}

job['data']['log']                   = {}
job['data']['log']['location']       = {'node':job['log_node']}
job['data']['log']['aging']          = {'window':2,'mode':'count'}
job['data']['log']['archive']        = {'window':7,'mode':'count'}
job['data']['log']['roots']          = [job['log']]
job['data']['log']['method']         = {'technique':'inplace'}
job['data']['log']['schedule']       = {'interval':3600}
job['data']['log']['activeonly']     = True

job['loglevel']    = 5
job['cntl_node']   = 55

job['input_type']  = {'type':'infofile','node':51,'delete_file':True, 'delete_info':True}

job['notifications']   = {}
job['notifications']['gnotif']    = {'node':job['data']['ginfo']['location']['node'], 'enabled':True, 'prefix':'gcomwspd'}
job['notifications']['onotif']    = {'node':job['data']['oinfo']['location']['node'], 'enabled':True, 'prefix':'ocean'}

job['outputs'] = {}
job['outputs']['gfiles'] = {'dataitem':'gdata','hardlink':True, 'notifications':['gnotif']}
job['outputs']['ofiles'] = {'dataitem':'odata','hardlink':True, 'notifications':['onotif']}
