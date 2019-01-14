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
job['name']     = 'amsr2_cutter'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'amsr2_cutter_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':86}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':85}
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

job['cntl_node']            = 84

job['input_type']           = {'type':'infofile','node':88,'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'src':'filename'})

ncspec['dimensions'] = {}
ncspec['dimensions']['scanlines'] = {'src':'nscans/scancount'}
ncspec['dimensions']['fov_hires'] = {'src':'fov/hires'}
ncspec['dimensions']['fov_lores'] = {'src':'fov/lores'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['instrument_name']		= {'src':'meta/instrument_name'}
ncspec['globalmeta']['time_coverage_start'] = {'src':'meta/time_coverage_start'}
ncspec['globalmeta']['time_coverage_end']   = {'src':'meta/time_coverage_end'}
ncspec['globalmeta']['production_site']     = {'default':'NWS/NAPO'}
ncspec['globalmeta']['Metadata_Link']       = {'src':'meta/Metadata_Link'}

ncspec['variables']   = {}
ncspec['variables']['Latitude_for_89A']   = {}
ncspec['variables']['Latitude_for_89A']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_for_89A']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Latitude_for_89A']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_for_89A']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_for_89A']['complevel']              = {'default':1}
ncspec['variables']['Latitude_for_89A']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_for_89A']['data']                   = {'src':'data/Latitude_for_89A'}
ncspec['variables']['Latitude_for_89A']['attrs'] = {}
ncspec['variables']['Latitude_for_89A']['attrs']['standard_name'] = {'default':'Latitude_for_89A'}
ncspec['variables']['Latitude_for_89A']['attrs']['long_name']     = {'default':'Latitude High Resolution'}
ncspec['variables']['Latitude_for_89A']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_for_89A']   = {}
ncspec['variables']['Longitude_for_89A']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_for_89A']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Longitude_for_89A']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_for_89A']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_for_89A']['complevel']              = {'default':1}
ncspec['variables']['Longitude_for_89A']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_for_89A']['data']                   = {'src':'data/Longitude_for_89A'}
ncspec['variables']['Longitude_for_89A']['attrs'] = {}
ncspec['variables']['Longitude_for_89A']['attrs']['standard_name'] = {'default':'Longitude_for_89A'}
ncspec['variables']['Longitude_for_89A']['attrs']['long_name']     = {'default':'Longitude High Resolution'}
ncspec['variables']['Longitude_for_89A']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['Latitude_for_36']   = {}
ncspec['variables']['Latitude_for_36']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_for_36']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['Latitude_for_36']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_for_36']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_for_36']['complevel']              = {'default':1}
ncspec['variables']['Latitude_for_36']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_for_36']['data']                   = {'src':'data/Latitude_for_36'}
ncspec['variables']['Latitude_for_36']['attrs'] = {}
ncspec['variables']['Latitude_for_36']['attrs']['standard_name'] = {'default':'Latitude_for_36'}
ncspec['variables']['Latitude_for_36']['attrs']['long_name']     = {'default':'Latitude Low Resolution'}
ncspec['variables']['Latitude_for_36']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_for_36']   = {}
ncspec['variables']['Longitude_for_36']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_for_36']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['Longitude_for_36']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_for_36']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_for_36']['complevel']              = {'default':1}
ncspec['variables']['Longitude_for_36']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_for_36']['data']                   = {'src':'data/Longitude_for_36'}
ncspec['variables']['Longitude_for_36']['attrs'] = {}
ncspec['variables']['Longitude_for_36']['attrs']['standard_name'] = {'default':'Longitude_for_36'}
ncspec['variables']['Longitude_for_36']['attrs']['long_name']     = {'default':'Longitude Low Resolution'}
ncspec['variables']['Longitude_for_36']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['Brightness_Temperature_36_GHzV']   = {}
ncspec['variables']['Brightness_Temperature_36_GHzV']['fmt']                    = {'default':'f'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['Brightness_Temperature_36_GHzV']['fill_value']             = {'default':-9999.}
ncspec['variables']['Brightness_Temperature_36_GHzV']['zlib']                   = {'default':True}
ncspec['variables']['Brightness_Temperature_36_GHzV']['complevel']              = {'default':1}
ncspec['variables']['Brightness_Temperature_36_GHzV']['shuffle']                = {'default':True}
ncspec['variables']['Brightness_Temperature_36_GHzV']['data']                   = {'src':'data/Brightness_Temperature_36_GHzV'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs'] = {}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs']['coordinates']   = {'default':['Latitude_for_36, Longitude_for_36']}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs']['standard_name'] = {'default':'36 GHz V Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs']['long_name']     = {'default':'36 GHz V Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Brightness_Temperature_36_GHzH']   = {}
ncspec['variables']['Brightness_Temperature_36_GHzH']['fmt']                    = {'default':'f'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['Brightness_Temperature_36_GHzH']['fill_value']             = {'default':-9999.}
ncspec['variables']['Brightness_Temperature_36_GHzH']['zlib']                   = {'default':True}
ncspec['variables']['Brightness_Temperature_36_GHzH']['complevel']              = {'default':1}
ncspec['variables']['Brightness_Temperature_36_GHzH']['shuffle']                = {'default':True}
ncspec['variables']['Brightness_Temperature_36_GHzH']['data']                   = {'src':'data/Brightness_Temperature_36_GHzH'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs'] = {}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs']['coordinates']   = {'default':['Latitude_for_36, Longitude_for_36']}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs']['standard_name'] = {'default':'36 GHz H Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs']['long_name']     = {'default':'36 GHz H Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Brightness_Temperature_89_GHz_AV']   = {}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['fmt']                    = {'default':'f'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['fill_value']             = {'default':-9999.}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['zlib']                   = {'default':True}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['complevel']              = {'default':1}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['shuffle']                = {'default':True}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['data']                   = {'src':'data/Brightness_Temperature_89_GHz_AV'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs'] = {}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs']['coordinates']   = {'default':['Latitude_for_89A, Longitude_for_89A']}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs']['standard_name'] = {'default':'89 GHz A V Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs']['long_name']     = {'default':'89 GHz A V Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Brightness_Temperature_89_GHz_AH']   = {}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['fmt']                    = {'default':'f'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['fill_value']             = {'default':-9999.}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['zlib']                   = {'default':True}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['complevel']              = {'default':1}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['shuffle']                = {'default':True}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['data']                   = {'src':'data/Brightness_Temperature_89_GHz_AH'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs'] = {}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs']['coordinates']   = {'default':['Latitude_for_89A, Longitude_for_89A']}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs']['standard_name'] = {'default':'89 GHz A H Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs']['long_name']     = {'default':'89 GHz A H Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs']['units']         = {'default':'K'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'amsr2_points', 'fields':['file','node']}

# Coordinate attributes (variables) for each output data variable
coordVars = {}
coordVars['Brightness_Temperature_36_GHzV']  = {'lat': 'Latitude_for_36', 'lon': 'Longitude_for_36'}
coordVars['Brightness_Temperature_36_GHzH']  = {'lat': 'Latitude_for_36', 'lon': 'Longitude_for_36'}
coordVars['Brightness_Temperature_89_GHz_AV'] = {'lat': 'Latitude_for_89A', 'lon': 'Longitude_for_89A'}
coordVars['Brightness_Temperature_89_GHz_AH'] = {'lat': 'Latitude_for_89A', 'lon': 'Longitude_for_89A'}

# For renaming variables from the input file.  Keys are the new variable names, values are the old.
varmap = {}
"""
varmap['BTemp_36_GHzV'] = 'Brightness_Temperature_36_GHzV'
varmap['BTemp_36_GHzH'] = 'Brightness_Temperature_36_GHzH'
varmap['BTemp_89_GhzAV'] = 'Brightness_Temperature_89_GHz_AV'
varmap['BTemp_89_GhzAH'] = 'Brightness_Temperature_89_GHz_AH'
varmap['Latitude_lores'] = 'Latitude_for_36'
varmap['Longitude_lores'] = 'Longitude_for_36'
varmap['Latitude_hires'] = 'Latitude_for_89A'
varmap['Longitude_hires'] = 'Longitude_for_89A'
"""

# Map of dimensions to convert from the input file to the output file
dimmap = {}
dimmap['scans']       = {'scancount':'Number_of_Scans'}
dimmap['resolutions'] = {'hires':'Number_of_hi_rez_FOVs', 'lores':'Number_of_low_rez_FOVs'}
dimmap['primary']     = 'Brightness_Temperature_89_GHz_AV'

# Map the variable row dimension back to odata row dimension
scanmap = {'scanlines':'scancount'}

args = {'ncspec':ncspec, 'coords':coordVars, 'dimmap':dimmap, 'scanmap':scanmap, 'boundaries':[-60.0, -30.0, 30.0, 60.0], 'overlap':5, 'varmap':varmap}

job['modclass'] = {'module':'point_set_cutter', 'class':'PointSetCutter', 'args':args}
