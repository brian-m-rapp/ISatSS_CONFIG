# Frank configuration for Jason2 altimetry product

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
"""
    Reformat/tailor jason2 nc4 files (as avail from PDA) into a format for the goes-r dmw
    plugin.  The purpose is to ingest the data into edex via the dmw table for access
    in cave using the point plot resource data, latter plots the values of wave height as text.
    Relies upon modification of im_ncfile.py modification: mapscalefac dictionary to multiply
    incoming data by the incoming data scale factor and add offset if applicable, whenever the i
    data in the array does not match the key in mapscalefac.

    
"""

job = {}
job['name']     = 'viirs_active_fires_processor'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'viirs_active_fires_processing_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':42}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':41}
job['data']['info']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['info']['method']      = {'technique':'inplace'}
job['data']['info']['activeonly']  = False
job['data']['info']['schedule']    = {'interval':600}
job['data']['info']['cfgorder']    = 1

job['data']['log']                 = {}
job['data']['log']['location']     = {'node':job['log_node']}
job['data']['log']['aging']        = {'window':2,'mode':'count'}
job['data']['log']['archive']      = {'window':7,'mode':'count'}
job['data']['log']['roots']        = [job['log']]
job['data']['log']['method']       = {'technique':'inplace'}
job['data']['log']['schedule']     = {'interval':3600}
job['data']['log']['activeonly']   = True

job['loglevel']             = 5

job['cntl_node']            = 163

job['input_type']           = {'type':'infofile','node':162,'delete_file':False, 'delete_info':False}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

#inncf
ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'isatss','delimiter':'_'})
ncspec['namedef'].append({'src':'inncf/globalmeta/Metadata_Link'})

ncspec['dimensions'] = {}
ncspec['dimensions']['nfire']        = {'src':'inncf/dimensions/(Fire Pixels)nfire'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['instrument_name']             = {'src':'inncf/globalmeta/instrument_name'}
ncspec['globalmeta']['time_coverage_start']         = {'src':'inncf/globalmeta/time_coverage_start'}
ncspec['globalmeta']['production_site']             = {'default':'NAPO'}

ncspec['variables']   = {}
ncspec['variables']['lat']   = {}
ncspec['variables']['lat']['fmt']                    = {'default':'f8'}
ncspec['variables']['lat']['shape']                  = {'default':['nfire']}
ncspec['variables']['lat']['zlib']                   = {'default':True}
ncspec['variables']['lat']['complevel']              = {'default':1}
ncspec['variables']['lat']['shuffle']                = {'default':True}
ncspec['variables']['lat']['data']                   = {'src':'data/(Fire Pixels)FP_latitude'}
ncspec['variables']['lat']['attrs'] = {}
ncspec['variables']['lat']['attrs']['long_name']     = {'default':'latitude'}
ncspec['variables']['lat']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['lon']   = {}
ncspec['variables']['lon']['fmt']                    = {'default':'f8'}
ncspec['variables']['lon']['shape']                  = {'default':['nfire']}
ncspec['variables']['lon']['zlib']                   = {'default':True}
ncspec['variables']['lon']['complevel']              = {'default':1}
ncspec['variables']['lon']['shuffle']                = {'default':True}
ncspec['variables']['lon']['data']                   = {'src':'data/(Fire Pixels)FP_longitude'}
ncspec['variables']['lon']['attrs'] = {}
ncspec['variables']['lon']['attrs']['long_name']     = {'default':'longitude'}
ncspec['variables']['lon']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['FP_power']   = {}
ncspec['variables']['FP_power']['fmt']                    = {'default':'f4'}
ncspec['variables']['FP_power']['shape']                  = {'default':['nfire']}
ncspec['variables']['FP_power']['zlib']                   = {'default':True}
ncspec['variables']['FP_power']['complevel']              = {'default':1}
ncspec['variables']['FP_power']['shuffle']                = {'default':True}
ncspec['variables']['FP_power']['data']                   = {'src':'data/(Fire Pixels)FP_power'}
ncspec['variables']['FP_power']['attrs'] = {}
ncspec['variables']['FP_power']['attrs']['units']         = {'default':'MW'}
ncspec['variables']['FP_power']['attrs']['long_name']     = {'default':'Fire radiative power'}

ncspec['variables']['FP_confidence']   = {}
ncspec['variables']['FP_confidence']['fmt']                    = {'default':'f4'}
ncspec['variables']['FP_confidence']['shape']                  = {'default':['nfire']}
ncspec['variables']['FP_confidence']['zlib']                   = {'default':True}
ncspec['variables']['FP_confidence']['complevel']              = {'default':1}
ncspec['variables']['FP_confidence']['shuffle']                = {'default':True}
ncspec['variables']['FP_confidence']['data']                   = {'src':'data/(Fire Pixels)FP_confidence'}
ncspec['variables']['FP_confidence']['attrs'] = {}
ncspec['variables']['FP_confidence']['attrs']['units']         = {'default':'%'}
ncspec['variables']['FP_confidence']['attrs']['long_name']     = {'default':'Detection confidence'}


ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'viirs', 'fields':['file','node']}

job['modclass'] = {'module':'nc_convert','class':'NCCon','args':{'ncspec':ncspec}}
