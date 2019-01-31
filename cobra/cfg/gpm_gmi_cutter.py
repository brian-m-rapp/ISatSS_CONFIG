# Points into GLM Grid configuration

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
job['name']     = 'gpm_gmi_cutter'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'gpm_gmi_cutter_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':113}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':112}
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

job['cntl_node']            = 111

job['input_type']           = {'type':'infofile', 'node':101, 'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'src':'filename'})

ncspec['dimensions'] = {}
ncspec['dimensions']['Scanline']      = {'src':'nscans/scancount'}
ncspec['dimensions']['Field_of_view'] = {'src':'fov/fov'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['instrument_name']		= {'src':'meta/instrument_name'}
ncspec['globalmeta']['time_coverage_start'] = {'src':'meta/time_coverage_start'}
ncspec['globalmeta']['time_coverage_end']   = {'src':'meta/time_coverage_end'}
ncspec['globalmeta']['production_site']     = {'default':'NWS/NAPO'}
ncspec['globalmeta']['Metadata_Link']       = {'src':'meta/Metadata_Link'}

ncspec['variables']   = {}

ncspec['variables']['Latitude']   = {}
ncspec['variables']['Latitude']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude']['shape']                  = {'default':['Scanline','Field_of_view']}
ncspec['variables']['Latitude']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude']['zlib']                   = {'default':True}
ncspec['variables']['Latitude']['complevel']              = {'default':1}
ncspec['variables']['Latitude']['shuffle']                = {'default':True}
ncspec['variables']['Latitude']['data']                   = {'src':'data/Latitude'}
ncspec['variables']['Latitude']['attrs'] = {}
ncspec['variables']['Latitude']['attrs']['standard_name'] = {'default':'Latitude'}
ncspec['variables']['Latitude']['attrs']['long_name']     = {'default':'Latitude'}
ncspec['variables']['Latitude']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude']   = {}
ncspec['variables']['Longitude']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude']['shape']                  = {'default':['Scanline','Field_of_view']}
ncspec['variables']['Longitude']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude']['zlib']                   = {'default':True}
ncspec['variables']['Longitude']['complevel']              = {'default':1}
ncspec['variables']['Longitude']['shuffle']                = {'default':True}
ncspec['variables']['Longitude']['data']                   = {'src':'data/Longitude'}
ncspec['variables']['Longitude']['attrs'] = {}
ncspec['variables']['Longitude']['attrs']['standard_name'] = {'default':'Longitude'}
ncspec['variables']['Longitude']['attrs']['long_name']     = {'default':'Longitude'}
ncspec['variables']['Longitude']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['BTemp_37GHz_V']   = {}
ncspec['variables']['BTemp_37GHz_V']['fmt']                    = {'default':'f'}
ncspec['variables']['BTemp_37GHz_V']['shape']                  = {'default':['Scanline','Field_of_view']}
ncspec['variables']['BTemp_37GHz_V']['fill_value']             = {'default':-9999.}
ncspec['variables']['BTemp_37GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['BTemp_37GHz_V']['complevel']              = {'default':1}
ncspec['variables']['BTemp_37GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['BTemp_37GHz_V']['data']                   = {'src':'data/BTemp_37GHz_V'}
ncspec['variables']['BTemp_37GHz_V']['attrs'] = {}
ncspec['variables']['BTemp_37GHz_V']['attrs']['coordinates']   = {'default':['Latitude, Longitude']}
ncspec['variables']['BTemp_37GHz_V']['attrs']['standard_name'] = {'default':'36.5 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_37GHz_V']['attrs']['long_name']     = {'default':'36.5 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_37GHz_V']['attrs']['units']         = {'default':'K'}

ncspec['variables']['BTemp_37GHz_H']   = {}
ncspec['variables']['BTemp_37GHz_H']['fmt']                    = {'default':'f'}
ncspec['variables']['BTemp_37GHz_H']['shape']                  = {'default':['Scanline','Field_of_view']}
ncspec['variables']['BTemp_37GHz_H']['fill_value']             = {'default':-9999.}
ncspec['variables']['BTemp_37GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['BTemp_37GHz_H']['complevel']              = {'default':1}
ncspec['variables']['BTemp_37GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['BTemp_37GHz_H']['data']                   = {'src':'data/BTemp_37GHz_H'}
ncspec['variables']['BTemp_37GHz_H']['attrs'] = {}
ncspec['variables']['BTemp_37GHz_H']['attrs']['coordinates']   = {'default':['Latitude, Longitude']}
ncspec['variables']['BTemp_37GHz_H']['attrs']['standard_name'] = {'default':'36.5 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_37GHz_H']['attrs']['long_name']     = {'default':'36.5 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_37GHz_H']['attrs']['units']         = {'default':'K'}

ncspec['variables']['BTemp_89GHz_V']   = {}
ncspec['variables']['BTemp_89GHz_V']['fmt']                    = {'default':'f'}
ncspec['variables']['BTemp_89GHz_V']['shape']                  = {'default':['Scanline','Field_of_view']}
ncspec['variables']['BTemp_89GHz_V']['fill_value']             = {'default':-9999.}
ncspec['variables']['BTemp_89GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['BTemp_89GHz_V']['complevel']              = {'default':1}
ncspec['variables']['BTemp_89GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['BTemp_89GHz_V']['data']                   = {'src':'data/BTemp_89GHz_V'}
ncspec['variables']['BTemp_89GHz_V']['attrs'] = {}
ncspec['variables']['BTemp_89GHz_V']['attrs']['coordinates']   = {'default':['Latitude, Longitude']}
ncspec['variables']['BTemp_89GHz_V']['attrs']['standard_name'] = {'default':'89 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_89GHz_V']['attrs']['long_name']     = {'default':'89 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_89GHz_V']['attrs']['units']         = {'default':'K'}

ncspec['variables']['BTemp_89GHz_H']   = {}
ncspec['variables']['BTemp_89GHz_H']['fmt']                    = {'default':'f'}
ncspec['variables']['BTemp_89GHz_H']['shape']                  = {'default':['Scanline','Field_of_view']}
ncspec['variables']['BTemp_89GHz_H']['fill_value']             = {'default':-9999.}
ncspec['variables']['BTemp_89GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['BTemp_89GHz_H']['complevel']              = {'default':1}
ncspec['variables']['BTemp_89GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['BTemp_89GHz_H']['data']                   = {'src':'data/BTemp_89GHz_H'}
ncspec['variables']['BTemp_89GHz_H']['attrs'] = {}
ncspec['variables']['BTemp_89GHz_H']['attrs']['coordinates']   = {'default':['Latitude, Longitude']}
ncspec['variables']['BTemp_89GHz_H']['attrs']['standard_name'] = {'default':'89 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_89GHz_H']['attrs']['long_name']     = {'default':'89 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_89GHz_H']['attrs']['units']         = {'default':'K'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'gpm_swath', 'fields':['file','node']}

# Coordinate attributes (variables) for each output data variable
coordVars = {}
coordVars['BTemp_37GHz_V']  = {'lat': 'Latitude', 'lon': 'Longitude', 'offset':5}
coordVars['BTemp_37GHz_H']  = {'lat': 'Latitude', 'lon': 'Longitude', 'offset':6}
coordVars['BTemp_89GHz_V']  = {'lat': 'Latitude', 'lon': 'Longitude', 'offset':7}
coordVars['BTemp_89GHz_H']  = {'lat': 'Latitude', 'lon': 'Longitude', 'offset':8}

# For renaming variables from the input file.  Keys are the new variable names; values are the original variable names.
varmap = {}
varmap['BTemp_37GHz_V'] = '/S1/Tb'
varmap['BTemp_37GHz_H'] = '/S1/Tb'
varmap['BTemp_89GHz_V'] = '/S1/Tb'
varmap['BTemp_89GHz_H'] = '/S1/Tb'
varmap['Latitude']      = '/S1/Latitude'
varmap['Longitude']     = '/S1/Longitude'
varmap['Year']          = '/S1/ScanTime/Year'
varmap['Month']         = '/S1/ScanTime/Month'
varmap['Day']           = '/S1/ScanTime/DayOfMonth'
varmap['Hour']          = '/S1/ScanTime/Hour'
varmap['Minute']        = '/S1/ScanTime/Minute'
varmap['Second']        = '/S1/ScanTime/Second'

# Map of dimensions to convert from the input file to the output file
dimmap = {}
dimmap['scans']       = {'scancount':'Scanline'}
dimmap['resolutions'] = {'fov':'Field_of_view'}
dimmap['primary']     = 'BTemp_37GHz_V'

# Map the variable row dimension back to odata row dimension
scanmap = {'Scanline':'scancount'}

bounds = [-60.0, -30.0, 30.0, 60.0]
args = {'ncspec':ncspec, 'coords':coordVars, 'dimmap':dimmap, 'scanmap':scanmap, 'boundaries':bounds, 'overlap':5, 'varmap':varmap, 'by_orbit': False}

job['modclass'] = {'module':'gpm_gmi_tailor', 'class':'GpmGmiTailor', 'args':args}
