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
job['name']     = 'viirs_ice_processing'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'viirs_ice_processing_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':92}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':91}
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

job['cntl_node']            = 88

job['input_type']           = {'type':'infofile', 'node':87, 'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

#inncf
ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'isatss_viirs_ice', 'delimiter':'_'})
ncspec['namedef'].append({'src':'isatss/filename'})

ncspec['dimensions'] = {}
ncspec['dimensions']['Rows']        = {'src':'inncf/dimensions/Rows'}
ncspec['dimensions']['Columns']     = {'src':'inncf/dimensions/Columns'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['time_coverage_start']     = {'src':'inncf/globalmeta/time_coverage_start'}
ncspec['globalmeta']['time_coverage_end']       = {'src':'inncf/globalmeta/time_coverage_end'}
ncspec['globalmeta']['production_site']         = {'src':'isatss/site'}
ncspec['globalmeta']['Metadata_Link']           = {'default': 'isatss/filename'}
ncspec['globalmeta']['instrument_name']         = {'src':'inncf/globalmeta/instrument_name'}
ncspec['globalmeta']['satellite_name']          = {'src':'inncf/globalmeta/satellite_name'}

ncspec['variables']   = {}
ncspec['variables']['latitude']   = {}
ncspec['variables']['latitude']['fmt']                    = {'default':'f4'}
ncspec['variables']['latitude']['shape']                  = {'default':['Rows','Columns']}
ncspec['variables']['latitude']['fill_value']             = {'default':-999.}
ncspec['variables']['latitude']['zlib']                   = {'default':True}
ncspec['variables']['latitude']['complevel']              = {'default':1}
ncspec['variables']['latitude']['shuffle']                = {'default':True}
ncspec['variables']['latitude']['data']                   = {'src':'data/Latitude'}
ncspec['variables']['latitude']['attrs'] = {}
ncspec['variables']['latitude']['attrs']['standard_name'] = {'default':'latitude'}
ncspec['variables']['latitude']['attrs']['long_name']     = {'default':'Pixel latitude in field Latitude (degree)'}
ncspec['variables']['latitude']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['longitude']   = {}
ncspec['variables']['longitude']['fmt']                    = {'default':'f4'}
ncspec['variables']['longitude']['shape']                  = {'default':['Rows','Columns']}
ncspec['variables']['longitude']['fill_value']             = {'default':-999.}
ncspec['variables']['longitude']['zlib']                   = {'default':True}
ncspec['variables']['longitude']['complevel']              = {'default':1}
ncspec['variables']['longitude']['shuffle']                = {'default':True}
ncspec['variables']['longitude']['data']                   = {'src':'data/Longitude'}
ncspec['variables']['longitude']['attrs'] = {}
ncspec['variables']['longitude']['attrs']['standard_name'] = {'default':'longitude'}
ncspec['variables']['longitude']['attrs']['long_name']     = {'default':'Pixel longitude in field Longitude (degree)'}
ncspec['variables']['longitude']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['IceConc']   = {}
ncspec['variables']['IceConc']['fmt']                    = {'default':'f4'}
ncspec['variables']['IceConc']['shape']                  = {'default':['Rows','Columns']}
ncspec['variables']['IceConc']['fill_value']             = {'default':-999.}
ncspec['variables']['IceConc']['zlib']                   = {'default':True}
ncspec['variables']['IceConc']['complevel']              = {'default':1}
ncspec['variables']['IceConc']['shuffle']                = {'default':True}
ncspec['variables']['IceConc']['data']                   = {'src':'data/IceConc'}
ncspec['variables']['IceConc']['attrs'] = {}
ncspec['variables']['IceConc']['attrs']['standard_name'] = {'default':'Ice Concentration'}
ncspec['variables']['IceConc']['attrs']['coordinates']   = {'default':['longitude latitude']}
ncspec['variables']['IceConc']['attrs']['long_name']     = {'default':'Ice_Concentration'}
ncspec['variables']['IceConc']['attrs']['units']         = {'default':'%'}

ncspec['variables']['IceMap']   = {}
ncspec['variables']['IceMap']['fmt']                    = {'default':'i1'}
ncspec['variables']['IceMap']['shape']                  = {'default':['Rows','Columns']}
ncspec['variables']['IceMap']['fill_value']             = {'default':-3}
ncspec['variables']['IceMap']['zlib']                   = {'default':True}
ncspec['variables']['IceMap']['complevel']              = {'default':1}
ncspec['variables']['IceMap']['shuffle']                = {'default':True}
ncspec['variables']['IceMap']['data']                   = {'src':'data/IceMap'}
ncspec['variables']['IceMap']['attrs'] = {}
ncspec['variables']['IceMap']['attrs']['long_name']     = {'default':'Ice Cover map codes'}
ncspec['variables']['IceMap']['attrs']['coordinates']   = {'default':['longitude latitude']}
ncspec['variables']['IceMap']['attrs']['units']         = {'default':'1'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'viirs_ice', 'fields':['file','node']}

job['modclass'] = {'module':'stitch_swaths','class':'StitchSwaths','args':{'ncspec':ncspec, 'overlap':3, 'length_dim':'Rows'}}

