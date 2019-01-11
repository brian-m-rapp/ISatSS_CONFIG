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

ncspec['variables']['Latitude_hires']   = {}
ncspec['variables']['Latitude_hires']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_hires']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Latitude_hires']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_hires']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_hires']['complevel']              = {'default':1}
ncspec['variables']['Latitude_hires']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_hires']['data']                   = {'src':'data/Latitude_hires'}
ncspec['variables']['Latitude_hires']['attrs'] = {}
ncspec['variables']['Latitude_hires']['attrs']['standard_name'] = {'default':'Latitude_hires'}
ncspec['variables']['Latitude_hires']['attrs']['long_name']     = {'default':'Latitude High Resolution'}
ncspec['variables']['Latitude_hires']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_hires']   = {}
ncspec['variables']['Longitude_hires']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_hires']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Longitude_hires']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_hires']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_hires']['complevel']              = {'default':1}
ncspec['variables']['Longitude_hires']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_hires']['data']                   = {'src':'data/Longitude_hires'}
ncspec['variables']['Longitude_hires']['attrs'] = {}
ncspec['variables']['Longitude_hires']['attrs']['standard_name'] = {'default':'Longitude_hires'}
ncspec['variables']['Longitude_hires']['attrs']['long_name']     = {'default':'Longitude High Resolution'}
ncspec['variables']['Longitude_hires']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['Latitude_lores']   = {}
ncspec['variables']['Latitude_lores']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_lores']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['Latitude_lores']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_lores']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_lores']['complevel']              = {'default':1}
ncspec['variables']['Latitude_lores']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_lores']['data']                   = {'src':'data/Latitude_lores'}
ncspec['variables']['Latitude_lores']['attrs'] = {}
ncspec['variables']['Latitude_lores']['attrs']['standard_name'] = {'default':'Latitude_lores'}
ncspec['variables']['Latitude_lores']['attrs']['long_name']     = {'default':'Latitude Low Resolution'}
ncspec['variables']['Latitude_lores']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_lores']   = {}
ncspec['variables']['Longitude_lores']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_lores']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['Longitude_lores']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_lores']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_lores']['complevel']              = {'default':1}
ncspec['variables']['Longitude_lores']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_lores']['data']                   = {'src':'data/Longitude_lores'}
ncspec['variables']['Longitude_lores']['attrs'] = {}
ncspec['variables']['Longitude_lores']['attrs']['standard_name'] = {'default':'Longitude_lores'}
ncspec['variables']['Longitude_lores']['attrs']['long_name']     = {'default':'Longitude Low Resolution'}
ncspec['variables']['Longitude_lores']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['BTemp_36_GHzV']   = {}
ncspec['variables']['BTemp_36_GHzV']['fmt']                    = {'default':'f'}
ncspec['variables']['BTemp_36_GHzV']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['BTemp_36_GHzV']['fill_value']             = {'default':-9999.}
ncspec['variables']['BTemp_36_GHzV']['zlib']                   = {'default':True}
ncspec['variables']['BTemp_36_GHzV']['complevel']              = {'default':1}
ncspec['variables']['BTemp_36_GHzV']['shuffle']                = {'default':True}
ncspec['variables']['BTemp_36_GHzV']['data']                   = {'src':'data/BTemp_36_GHzV'}
ncspec['variables']['BTemp_36_GHzV']['attrs'] = {}
ncspec['variables']['BTemp_36_GHzV']['attrs']['coordinates']   = {'default':['Latitude_lores, Longitude_lores']}
ncspec['variables']['BTemp_36_GHzV']['attrs']['standard_name'] = {'default':'37 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_36_GHzV']['attrs']['long_name']     = {'default':'37 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_36_GHzV']['attrs']['units']         = {'default':'K'}

ncspec['variables']['BTemp_36_GHzH']   = {}
ncspec['variables']['BTemp_36_GHzH']['fmt']                    = {'default':'f'}
ncspec['variables']['BTemp_36_GHzH']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['BTemp_36_GHzH']['fill_value']             = {'default':-9999.}
ncspec['variables']['BTemp_36_GHzH']['zlib']                   = {'default':True}
ncspec['variables']['BTemp_36_GHzH']['complevel']              = {'default':1}
ncspec['variables']['BTemp_36_GHzH']['shuffle']                = {'default':True}
ncspec['variables']['BTemp_36_GHzH']['data']                   = {'src':'data/BTemp_36_GHzH'}
ncspec['variables']['BTemp_36_GHzH']['attrs'] = {}
ncspec['variables']['BTemp_36_GHzH']['attrs']['coordinates']   = {'default':['Latitude_lores, Longitude_lores']}
ncspec['variables']['BTemp_36_GHzH']['attrs']['standard_name'] = {'default':'37 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_36_GHzH']['attrs']['long_name']     = {'default':'37 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_36_GHzH']['attrs']['units']         = {'default':'K'}

ncspec['variables']['BTemp_89_GhzAV']   = {}
ncspec['variables']['BTemp_89_GhzAV']['fmt']                    = {'default':'f'}
ncspec['variables']['BTemp_89_GhzAV']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['BTemp_89_GhzAV']['fill_value']             = {'default':-9999.}
ncspec['variables']['BTemp_89_GhzAV']['zlib']                   = {'default':True}
ncspec['variables']['BTemp_89_GhzAV']['complevel']              = {'default':1}
ncspec['variables']['BTemp_89_GhzAV']['shuffle']                = {'default':True}
ncspec['variables']['BTemp_89_GhzAV']['data']                   = {'src':'data/BTemp_89_GhzAV'}
ncspec['variables']['BTemp_89_GhzAV']['attrs'] = {}
ncspec['variables']['BTemp_89_GhzAV']['attrs']['coordinates']   = {'default':['Latitude_hires, Longitude_hires']}
ncspec['variables']['BTemp_89_GhzAV']['attrs']['standard_name'] = {'default':'85 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_89_GhzAV']['attrs']['long_name']     = {'default':'85 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_89_GhzAV']['attrs']['units']         = {'default':'K'}

ncspec['variables']['BTemp_89_GhzAH']   = {}
ncspec['variables']['BTemp_89_GhzAH']['fmt']                    = {'default':'f'}
ncspec['variables']['BTemp_89_GhzAH']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['BTemp_89_GhzAH']['fill_value']             = {'default':-9999.}
ncspec['variables']['BTemp_89_GhzAH']['zlib']                   = {'default':True}
ncspec['variables']['BTemp_89_GhzAH']['complevel']              = {'default':1}
ncspec['variables']['BTemp_89_GhzAH']['shuffle']                = {'default':True}
ncspec['variables']['BTemp_89_GhzAH']['data']                   = {'src':'data/BTemp_89_GhzAH'}
ncspec['variables']['BTemp_89_GhzAH']['attrs'] = {}
ncspec['variables']['BTemp_89_GhzAH']['attrs']['coordinates']   = {'default':['Latitude_hires, Longitude_hires']}
ncspec['variables']['BTemp_89_GhzAH']['attrs']['standard_name'] = {'default':'85 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_89_GhzAH']['attrs']['long_name']     = {'default':'85 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_89_GhzAH']['attrs']['units']         = {'default':'K'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'amsr2_points', 'fields':['file','node']}

coordVars = {}
coordVars['BTemp_36_GHzV']  = {'lat': 'Latitude_lores', 'lon': 'Longitude_lores'}
coordVars['BTemp_36_GHzH']  = {'lat': 'Latitude_lores', 'lon': 'Longitude_lores'}
coordVars['BTemp_89_GhzAV'] = {'lat': 'Latitude_hires', 'lon': 'Longitude_hires'}
coordVars['BTemp_89_GhzAH'] = {'lat': 'Latitude_hires', 'lon': 'Longitude_hires'}

varmap = {}
varmap['BTemp_36_GHzV'] = 'Brightness_Temperature_36_GHzV'
varmap['BTemp_36_GHzH'] = 'Brightness_Temperature_36_GHzH'
varmap['BTemp_89_GhzAV'] = 'Brightness_Temperature_89_GHz_AV'
varmap['BTemp_89_GhzAH'] = 'Brightness_Temperature_89_GHz_AH'
varmap['Latitude_lores'] = 'Latitude_for_36'
varmap['Longitude_lores'] = 'Longitude_for_36'
varmap['Latitude_hires'] = 'Latitude_for_89A'
varmap['Longitude_hires'] = 'Longitude_for_89A'

dims = {'scans':{'scancount':'Number_of_Scans'}, 'resolutions':{'hires':'Number_of_hi_rez_FOVs', 'lores':'Number_of_low_rez_FOVs'}}
args = {'ncspec':ncspec, 'coords':coordVars, 'dims':dims, 'boundaries':[-60.0, -30.0, 30.0, 60.0], 'overlap':5, 'varmap':varmap}

job['modclass'] = {'module':'point_set_cutter', 'class':'PointSetCutter', 'args':args}
