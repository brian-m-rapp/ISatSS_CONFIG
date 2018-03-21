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
job['name']     = 'ldm_in_replicator'
job['cmd']      = 'replicator'
job['class']    = 'Replicator'
job['log']      = 'ldm_in_replicator_log'
job['log_node'] = 1


job['notifications']   = {}

job['data'] = {}
job['data']['ldminarch']             = {}
job['data']['ldminarch']['location'] = {'node':14}
job['data']['ldminarch']['aging']    = {'window':86400, 'mode':'elapsedname','fmt':'abi_%Y%m%d%H'}
job['data']['ldminarch']['method']   = {'technique':'stage','path':'isatss_incinerator'}

job['data']['log']                   = {}
job['data']['log']['location']       = {'node':job['log_node']}
job['data']['log']['aging']          = {'window':2,'mode':'count'}
job['data']['log']['archive']        = {'window':7,'mode':'count'}
job['data']['log']['roots']          = [job['log']]
job['data']['log']['method']         = {'technique':'inplace'}
job['data']['log']['schedule']       = {'interval':3600}
job['data']['log']['activeonly']     = True

job['loglevel']    = 5
job['cntl_node']   = 11

job['input_type']  = {'type':'infofile','node':42,'delete_file':True, 'delete_info':True}

job['outputs'] = {}
job['outputs']['abi'] = {'dataitem':'ldminarch','filt':[], 'path':[]}
job['outputs']['abi']['filt'].append({'filt':'substring','target':'file','contains':'_ABI-','name':'ABI Test'})
pathstack = []
pathstack.append({'method':'extract_field','delimiter':'/','field':-1,'name':'basename','target':'file'})
pathstack.append({'method':'extract_field','delimiter':'_','field':3,'start_char':1,'nchar':9,'name':'startfieldextract'})
pathstack.append({'method':'date_reformat','inspec':'%Y%j%H','outspec':'%Y%m%d%H','name':'startfieldreformat'})
job['outputs']['abi']['path'].append({'default':'abi_','name':'prefix'})
job['outputs']['abi']['path'].append({'target':'file','stack':pathstack,'name':'yearmodahr'})


