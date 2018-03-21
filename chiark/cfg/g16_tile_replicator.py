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
job['name']     = 'g16_tile_replicator'
job['cmd']      = 'replicator'
job['class']    = 'Replicator'
job['log']      = 'g16_tile_replicator_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']   = {}
job['notifications']['fdco']    = {'node':12, 'enabled':True, 'prefix':'fdco'}
job['notifications']['meso']    = {'node':10, 'enabled':True, 'prefix':'meso'}
job['notifications']['ldm']     = {'node':6,  'enabled':True, 'prefix':'g16tile'}

job['data'] = {}
job['data']['tilearch']             = {}
job['data']['tilearch']['location'] = {'node':40}
job['data']['tilearch']['aging']    = {'window':86400, 'mode':'elapsedname','fmt':'%Y%m%d%H'}
job['data']['tilearch']['method']   = {'technique':'stage','path':'isatss_incinerator'}

job['data']['fdco_data'] = {}
job['data']['fdco_data']['location']     = {'node':48}
job['data']['fdco_data']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['fdco_data']['method']       = {'technique':'inplace'}
job['data']['fdco_data']['activeonly']   = True
job['data']['fdco_data']['schedule']     = {'interval':600}
job['data']['meso_data'] = {}
job['data']['meso_data']['location']     = {'node':49}
job['data']['meso_data']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['meso_data']['method']       = {'technique':'inplace'}
job['data']['meso_data']['activeonly']   = True
job['data']['meso_data']['schedule']     = {'interval':600}
job['data']['ldm_data'] = {}
job['data']['ldm_data']['location']      = {'node':25}
job['data']['ldm_data']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['ldm_data']['method']        = {'technique':'inplace'}
job['data']['ldm_data']['activeonly']    = True
job['data']['ldm_data']['schedule']      = {'interval':600}
job['data']['fdco_info'] = {}
job['data']['fdco_info']['location']     = {'node':12}
job['data']['fdco_info']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['fdco_info']['method']       = {'technique':'inplace'}
job['data']['fdco_info']['activeonly']   = True
job['data']['fdco_info']['schedule']     = {'interval':600}
job['data']['meso_info'] = {}
job['data']['meso_info']['location']     = {'node':10}
job['data']['meso_info']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['meso_info']['method']       = {'technique':'inplace'}
job['data']['meso_info']['activeonly']   = True
job['data']['meso_info']['schedule']     = {'interval':600}
job['data']['ldm_info'] = {}
job['data']['ldm_info']['location']      = {'node':6}
job['data']['ldm_info']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['ldm_info']['method']        = {'technique':'inplace'}
job['data']['ldm_info']['activeonly']    = True
job['data']['ldm_info']['schedule']      = {'interval':600}


job['data']['log']                   = {}
job['data']['log']['location']       = {'node':job['log_node']}
job['data']['log']['aging']          = {'window':2,'mode':'count'}
job['data']['log']['archive']        = {'window':7,'mode':'count'}
job['data']['log']['roots']          = [job['log']]
job['data']['log']['method']         = {'technique':'inplace'}
job['data']['log']['schedule']       = {'interval':3600}
job['data']['log']['activeonly']     = True

job['loglevel']    = 5
job['cntl_node']   = 26

job['input_type']  = {'type':'infofile','node':27,'delete_file':True, 'delete_info':True}

job['outputs'] = {}
job['outputs']['ldm']  = {'dataitem':'ldm_data','hardlink':True,'notifications':['ldm']}

job['outputs']['fdco'] = {'dataitem':'fdco_data','hardlink':True,'filt':[],'notifications':['fdco']}
job['outputs']['fdco']['filt'].append({'filt':'substrings','target':'file','containsany':['FD_','CONUS_'],'name':'FDCO Test'})

job['outputs']['meso'] = {'dataitem':'meso_data','hardlink':True,'filt':[],'notifications':['meso']}
job['outputs']['meso']['filt'].append({'filt':'substrings','target':'file','containsany':['M1_','M2_'],'name':'M1 M2 Test'})

job['outputs']['arch']  = {'dataitem':'tilearch','path':[]}
pathstack = []
pathstack.append({'method':'extract_field','delimiter':'/','field':-1,'name':'basename','target':'file'})
pathstack.append({'method':'extract_field','delimiter':'_','field':3,'start_char':0,'nchar':10,'name':'dtg_extract'})
job['outputs']['arch']['path'].append({'target':'file','stack':pathstack,'name':'yearmodahr'})
