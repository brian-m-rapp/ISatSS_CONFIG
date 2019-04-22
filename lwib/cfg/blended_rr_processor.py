# Frank configuration for ASCAT Ambiguities

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
job['name']     = 'blended_rr_processor'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'blended_rr_processor_log'
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

job['cntl_node']            = 153

job['input_type']           = {'type':'infofile','node':152,'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

#inncf
ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'isatss','delimiter':'_'})
ncspec['namedef'].append({'src':'inncf/globalmeta/Metadata_Link'})

ncspec['dimensions'] = {}
ncspec['dimensions']['lon']        = {'src':'inncf/dimensions/lon'}
ncspec['dimensions']['lat']        = {'src':'inncf/dimensions/lat'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['time_coverage_start']      =   {'src':'inncf/globalmeta/time_coverage_start'}
ncspec['globalmeta']['time_coverage_end']        =   {'src':'inncf/globalmeta/time_coverage_end'}
ncspec['globalmeta']['Metadata_Link']            =   {'src':'inncf/globalmeta/Metadata_Link'}
ncspec['globalmeta']['production_site']          =   {'default':'NAPO'}

ncspec['variables']   = {}
ncspec['variables']['lon']   = {}
ncspec['variables']['lon']['fmt']                    = {'default':'f4'}
ncspec['variables']['lon']['shape']                  = {'default':['lon']}
ncspec['variables']['lon']['fill_value']             = {'default':-999.}
ncspec['variables']['lon']['zlib']                   = {'default':True}
ncspec['variables']['lon']['complevel']              = {'default':1}
ncspec['variables']['lon']['shuffle']                = {'default':True}
ncspec['variables']['lon']['data']                   = {'src':'data/lon'}
ncspec['variables']['lon']['attrs'] = {}
ncspec['variables']['lon']['attrs']['long_name']     = {'default':'Longitude'}
ncspec['variables']['lon']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['lat']   = {}
ncspec['variables']['lat']['fmt']                    = {'default':'f4'}
ncspec['variables']['lat']['shape']                  = {'default':['lat']}
ncspec['variables']['lat']['fill_value']             = {'default':-999.}
ncspec['variables']['lat']['zlib']                   = {'default':True}
ncspec['variables']['lat']['complevel']              = {'default':1}
ncspec['variables']['lat']['shuffle']                = {'default':True}
ncspec['variables']['lat']['data']                   = {'src':'data/lat'}
ncspec['variables']['lat']['attrs'] = {}
ncspec['variables']['lat']['attrs']['long_name']     = {'default':'Latitude'}
ncspec['variables']['lat']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['RR']   = {}
ncspec['variables']['RR']['fmt']                    = {'default':'f4'}
ncspec['variables']['RR']['shape']                  = {'default':['lat','lon']}
ncspec['variables']['RR']['fill_value']             = {'default':-999.}
ncspec['variables']['RR']['zlib']                   = {'default':True}
ncspec['variables']['RR']['complevel']              = {'default':1}
ncspec['variables']['RR']['shuffle']                = {'default':True}
ncspec['variables']['RR']['data']                   = {'src':'data/RR'}
ncspec['variables']['RR']['attrs'] = {}
ncspec['variables']['RR']['attrs']['coordinates']   = {'default':['Latitude Longitude']}
ncspec['variables']['RR']['attrs']['long_name']     = {'default':'Blended Rain Rate'}
ncspec['variables']['RR']['attrs']['units']         = {'default':'mm/hr'}

ncspec['variables']['observation_age']   = {}
ncspec['variables']['observation_age']['fmt']                    = {'default':'f4'}
ncspec['variables']['observation_age']['shape']                  = {'default':['lat','lon']}
ncspec['variables']['observation_age']['fill_value']             = {'default':-999.}
ncspec['variables']['observation_age']['zlib']                   = {'default':True}
ncspec['variables']['observation_age']['complevel']              = {'default':1}
ncspec['variables']['observation_age']['shuffle']                = {'default':True}
ncspec['variables']['observation_age']['data']                   = {'src':'data/observation_age'}
ncspec['variables']['observation_age']['attrs'] = {}
ncspec['variables']['observation_age']['attrs']['coordinates']   = {'default':['Latitude Longitude']}
ncspec['variables']['observation_age']['attrs']['long_name']     = {'default':'age of obs analysis time minus obs time'}
ncspec['variables']['observation_age']['attrs']['units']         = {'default':'hours'}

ncspec['variables']['Satellite_Number']   = {}
ncspec['variables']['Satellite_Number']['fmt']                    = {'default':'f4'}
ncspec['variables']['Satellite_Number']['shape']                  = {'default':['lat','lon']}
ncspec['variables']['Satellite_Number']['fill_value']             = {'default':-999.}
ncspec['variables']['Satellite_Number']['zlib']                   = {'default':True}
ncspec['variables']['Satellite_Number']['complevel']              = {'default':1}
ncspec['variables']['Satellite_Number']['shuffle']                = {'default':True}
ncspec['variables']['Satellite_Number']['data']                   = {'src':'data/Satellite_Number'}
ncspec['variables']['Satellite_Number']['attrs'] = {}
ncspec['variables']['Satellite_Number']['attrs']['coordinates']   = {'default':['Latitude Longitude']}
ncspec['variables']['Satellite_Number']['attrs']['long_name']     = {'default':'the ID number of the satellite which made the observation'}
ncspec['variables']['Satellite_Number']['attrs']['units']         = {'default':'none'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'aaw', 'fields':['file','node']}

job['modclass'] = {'module':'nc_convert','class':'NCCon','args':{'ncspec':ncspec}}

