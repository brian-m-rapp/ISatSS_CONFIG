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
job['name']     = 'ldm_output_replicator'
job['cmd']      = 'replicator'
job['class']    = 'Replicator'
job['log']      = 'ldm_output_replicator_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']   = {}
job['notifications']['ldm']     = {'node':54,  'enabled':True, 'prefix':'oldm'}

job['data'] = {}
job['data']['g16areaarch']             = {}
job['data']['g16areaarch']['location'] = {'node':39}
job['data']['g16areaarch']['aging']    = {'window':86400, 'mode':'elapsedname','fmt':'%Y%m%d%H'}
job['data']['g16areaarch']['method']   = {'technique':'stage','path':'isatss_incinerator'}

job['data']['ldm_data'] = {}
job['data']['ldm_data']['location']    = {'node':53}
job['data']['ldm_data']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['ldm_data']['method']      = {'technique':'inplace'}
job['data']['ldm_data']['activeonly']  = True
job['data']['ldm_data']['schedule']    = {'interval':600}
job['data']['ldm_info'] = {}
job['data']['ldm_info']['location']    = {'node':54}
job['data']['ldm_info']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['ldm_info']['method']      = {'technique':'inplace'}
job['data']['ldm_info']['activeonly']  = True
job['data']['ldm_info']['schedule']    = {'interval':600}

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

job['input_type']  = {'type':'infofile','node':6,'delete_file':True, 'delete_info':True}

job['outputs'] = {}
job['outputs']['ldm']  = {'dataitem':'ldm_data','hardlink':True,'notifications':['ldm']}

job['outputs']['arch']  = {'dataitem':'g16areaarch','path':[],'filt':[]}
job['outputs']['arch']['filt'].append({'filt':'substring','target':'file','notcontains':'.nc','name':'area file test'})
job['outputs']['arch']['filt'].append({'filt':'substring','target':'file','contains':'G16_','name':'satellite test'})
pathstack = []
pathstack.append({'method':'extract_field','delimiter':'/','field':-1,'name':'basename','target':'file'})
pathstack.append({'method':'extract_field','delimiter':'.','field':0,'start_char':0,'nchar':11,'name':'dtg_extract'})
pathstack.append({'method':'date_reformat','inspec':'%Y%m%d_%H','outspec':'%Y%m%d%H','name':'startfieldreformat'})
job['outputs']['arch']['path'].append({'target':'file','stack':pathstack,'name':'yearmodahr'})
