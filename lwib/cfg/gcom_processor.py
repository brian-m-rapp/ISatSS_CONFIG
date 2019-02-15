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
job['name']     = 'gcom_processor'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'gcom_processor_log'
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

job['cntl_node']            = 54

job['input_type']           = {'type':'infofile','node':56,'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

#inncf
ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'src':'inncf/globalmeta/platform_name','delimiter':'_'})
ncspec['namedef'].append({'src':'inncf/globalmeta/instrument_name','delimiter':'_'})
ncspec['namedef'].append({'src':'inncf/globalmeta/start_orbit_number','fmt':'str','delimiter':'.nc'})

ncspec['dimensions'] = {}
ncspec['dimensions']['Number_of_Scans']        = {'src':'inncf/dimensions/Number_of_Scans'}
ncspec['dimensions']['Number_of_low_rez_FOVs'] = {'src':'inncf/dimensions/Number_of_low_rez_FOVs'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['instrument_name']            = {'src':'inncf/globalmeta/instrument_name'}
ncspec['globalmeta']['time_coverage_start']        = {'src':'inncf/globalmeta/time_coverage_start'}
ncspec['globalmeta']['time_coverage_end']        =   {'src':'inncf/globalmeta/time_coverage_end'}
ncspec['globalmeta']['Metadata_Link']        =       {'src':'inncf/globalmeta/Metadata_Link'}
ncspec['globalmeta']['production_site']            = {'default':'NWS/NAPO'}


ncspec['variables']   = {}
ncspec['variables']['latitude']   = {}
ncspec['variables']['latitude']['fmt']                    = {'default':'f4'}
ncspec['variables']['latitude']['shape']                  = {'default':['Number_of_Scans','Number_of_low_rez_FOVs']}
ncspec['variables']['latitude']['fill_value']             = {'default':-9999.}
ncspec['variables']['latitude']['zlib']                   = {'default':True}
ncspec['variables']['latitude']['complevel']              = {'default':1}
ncspec['variables']['latitude']['shuffle']                = {'default':True}
ncspec['variables']['latitude']['data']                   = {'src':'data/Latitude_for_Low_Resolution'}
ncspec['variables']['latitude']['attrs'] = {}
ncspec['variables']['latitude']['attrs']['standard_name'] = {'default':'latitude'}
ncspec['variables']['latitude']['attrs']['long_name']     = {'default':'Latitude for low resolution'}
ncspec['variables']['latitude']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['longitude']   = {}
ncspec['variables']['longitude']['fmt']                    = {'default':'f4'}
ncspec['variables']['longitude']['shape']                  = {'default':['Number_of_Scans','Number_of_low_rez_FOVs']}
ncspec['variables']['longitude']['fill_value']             = {'default':-9999.}
ncspec['variables']['longitude']['zlib']                   = {'default':True}
ncspec['variables']['longitude']['complevel']              = {'default':1}
ncspec['variables']['longitude']['shuffle']                = {'default':True}
ncspec['variables']['longitude']['data']                   = {'src':'data/Longitude_for_Low_Resolution'}
ncspec['variables']['longitude']['attrs'] = {}
ncspec['variables']['longitude']['attrs']['standard_name'] = {'default':'longitude'}
ncspec['variables']['longitude']['attrs']['long_name']     = {'default':'Longitude for low resolution'}
ncspec['variables']['longitude']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['WSPD']   = {}
ncspec['variables']['WSPD']['fmt']                    = {'default':'f8'}
ncspec['variables']['WSPD']['shape']                  = {'default':['Number_of_Scans','Number_of_low_rez_FOVs']}
ncspec['variables']['WSPD']['fill_value']             = {'default':-9999.}
ncspec['variables']['WSPD']['zlib']                   = {'default':True}
ncspec['variables']['WSPD']['complevel']              = {'default':1}
ncspec['variables']['WSPD']['shuffle']                = {'default':True}
ncspec['variables']['WSPD']['data']                   = {'src':'data/WSPD'}
ncspec['variables']['WSPD']['attrs'] = {}
ncspec['variables']['WSPD']['attrs']['standard_name'] = {'default':'Wind Speed'}
ncspec['variables']['WSPD']['attrs']['coordinates']   = {'default':['latitude longitude']}
ncspec['variables']['WSPD']['attrs']['long_name']     = {'default':'Wind Speed'}
ncspec['variables']['WSPD']['attrs']['units']         = {'default':'m s-1'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'aaw', 'fields':['file','node']}

job['modclass'] = {'module':'nc_convert','class':'NCCon','args':{'ncspec':ncspec}}

