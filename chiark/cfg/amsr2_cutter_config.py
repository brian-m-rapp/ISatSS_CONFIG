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
ncspec['dimensions']['nscans_hires']          = {'src':'nscans/hires'}
ncspec['dimensions']['nscans_lores']          = {'src':'nscans/lores'}
ncspec['dimensions']['points_per_scan_hires'] = {'src':'points/hires'}
ncspec['dimensions']['points_per_scan_lores'] = {'src':'points/hires'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['instrument_name']		= {'src':'meta/instrument_name'}
ncspec['globalmeta']['time_coverage_start'] = {'src':'meta/time_coverage_start', 'timeformat':'%Y-%m-%dT%H:%M:%S.0Z'}
ncspec['globalmeta']['time_coverage_end']   = {'src':'meta/time_coverage_end', 'timeformat':'%Y-%m-%dT%H:%M:%S.0Z'}
ncspec['globalmeta']['production_site']     = {'src':'meta/production_site'}
ncspec['globalmeta']['Metadata_Link']       = {'src':'meta/Metadata_Link'}
ncspec['globalmeta']['dataset_name']        = {'src':'filename'}

ncspec['variables']   = {}

ncspec['variables']['Latitude_for_89A']   = {}
ncspec['variables']['Latitude_for_89A']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_for_89A']['shape']                  = {'default':['nscans_hires','npixel_hires']}
ncspec['variables']['Latitude_for_89A']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_for_89A']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_for_89A']['complevel']              = {'default':1}
ncspec['variables']['Latitude_for_89A']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_for_89A']['data']                   = {'src':'data/lat85'}
ncspec['variables']['Latitude_for_89A']['attrs'] = {}
ncspec['variables']['Latitude_for_89A']['attrs']['standard_name'] = {'default':'Latitude_for_89A'}
ncspec['variables']['Latitude_for_89A']['attrs']['long_name']     = {'default':'Latitude High Resolution'}
ncspec['variables']['Latitude_for_89A']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_for_89A']   = {}
ncspec['variables']['Longitude_for_89A']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_for_89A']['shape']                  = {'default':['nscans_hires','npixel_hires']}
ncspec['variables']['Longitude_for_89A']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_for_89A']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_for_89A']['complevel']              = {'default':1}
ncspec['variables']['Longitude_for_89A']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_for_89A']['data']                   = {'src':'data/lon85'}
ncspec['variables']['Longitude_for_89A']['attrs'] = {}
ncspec['variables']['Longitude_for_89A']['attrs']['standard_name'] = {'default':'Longitude_for_89A'}
ncspec['variables']['Longitude_for_89A']['attrs']['long_name']     = {'default':'Longitude High Resolution'}
ncspec['variables']['Longitude_for_89A']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['Latitude_for_36']   = {}
ncspec['variables']['Latitude_for_36']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_for_36']['shape']                  = {'default':['nscans_lores','npixel_lores']}
ncspec['variables']['Latitude_for_36']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_for_36']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_for_36']['complevel']              = {'default':1}
ncspec['variables']['Latitude_for_36']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_for_36']['data']                   = {'src':'data/lat37'}
ncspec['variables']['Latitude_for_36']['attrs'] = {}
ncspec['variables']['Latitude_for_36']['attrs']['standard_name'] = {'default':'Latitude_for_36'}
ncspec['variables']['Latitude_for_36']['attrs']['long_name']     = {'default':'Latitude Low Resolution'}
ncspec['variables']['Latitude_for_36']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_for_36']   = {}
ncspec['variables']['Longitude_for_36']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_for_36']['shape']                  = {'default':['nscans_lores','npixel_lores']}
ncspec['variables']['Longitude_for_36']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_for_36']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_for_36']['complevel']              = {'default':1}
ncspec['variables']['Longitude_for_36']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_for_36']['data']                   = {'src':'data/lon37'}
ncspec['variables']['Longitude_for_36']['attrs'] = {}
ncspec['variables']['Longitude_for_36']['attrs']['standard_name'] = {'default':'Longitude_for_36'}
ncspec['variables']['Longitude_for_36']['attrs']['long_name']     = {'default':'Longitude Low Resolution'}
ncspec['variables']['Longitude_for_36']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['Temp_37GHz_V']   = {}
ncspec['variables']['Temp_37GHz_V']['fmt']                    = {'default':'f'}
ncspec['variables']['Temp_37GHz_V']['shape']                  = {'default':['nscans_lores','npixel_lores']}
ncspec['variables']['Temp_37GHz_V']['fill_value']             = {'default':-9999.}
ncspec['variables']['Temp_37GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['Temp_37GHz_V']['complevel']              = {'default':1}
ncspec['variables']['Temp_37GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['Temp_37GHz_V']['data']                   = {'src':'data/v37'}
ncspec['variables']['Temp_37GHz_V']['attrs'] = {}
ncspec['variables']['Temp_37GHz_V']['attrs']['coordinates']   = {'default':['Latitude_for_36, Longitude_for_36']}
ncspec['variables']['Temp_37GHz_V']['attrs']['standard_name'] = {'default':'37 GHz V Brightness Temperature'}
ncspec['variables']['Temp_37GHz_V']['attrs']['long_name']     = {'default':'37 GHz V Brightness Temperature'}
ncspec['variables']['Temp_37GHz_V']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Temp_37GHz_H']   = {}
ncspec['variables']['Temp_37GHz_H']['fmt']                    = {'default':'f'}
ncspec['variables']['Temp_37GHz_H']['shape']                  = {'default':['nscans_lores','npixel_lores']}
ncspec['variables']['Temp_37GHz_H']['fill_value']             = {'default':-9999.}
ncspec['variables']['Temp_37GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['Temp_37GHz_H']['complevel']              = {'default':1}
ncspec['variables']['Temp_37GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['Temp_37GHz_H']['data']                   = {'src':'data/h37'}
ncspec['variables']['Temp_37GHz_H']['attrs'] = {}
ncspec['variables']['Temp_37GHz_H']['attrs']['coordinates']   = {'default':['Latitude_for_36, Longitude_for_36']}
ncspec['variables']['Temp_37GHz_H']['attrs']['standard_name'] = {'default':'37 GHz H Brightness Temperature'}
ncspec['variables']['Temp_37GHz_H']['attrs']['long_name']     = {'default':'37 GHz H Brightness Temperature'}
ncspec['variables']['Temp_37GHz_H']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Temp_85GHz_V']   = {}
ncspec['variables']['Temp_85GHz_V']['fmt']                    = {'default':'f'}
ncspec['variables']['Temp_85GHz_V']['shape']                  = {'default':['nscans_hires','npixel_hires']}
ncspec['variables']['Temp_85GHz_V']['fill_value']             = {'default':-9999.}
ncspec['variables']['Temp_85GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['Temp_85GHz_V']['complevel']              = {'default':1}
ncspec['variables']['Temp_85GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['Temp_85GHz_V']['data']                   = {'src':'data/v85'}
ncspec['variables']['Temp_85GHz_V']['attrs'] = {}
ncspec['variables']['Temp_85GHz_V']['attrs']['coordinates']   = {'default':['Latitude_for_89A, Longitude_for_89A']}
ncspec['variables']['Temp_85GHz_V']['attrs']['standard_name'] = {'default':'85 GHz V Brightness Temperature'}
ncspec['variables']['Temp_85GHz_V']['attrs']['long_name']     = {'default':'85 GHz V Brightness Temperature'}
ncspec['variables']['Temp_85GHz_V']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Temp_85GHz_H']   = {}
ncspec['variables']['Temp_85GHz_H']['fmt']                    = {'default':'f'}
ncspec['variables']['Temp_85GHz_H']['shape']                  = {'default':['nscans_hires','npixel_hires']}
ncspec['variables']['Temp_85GHz_H']['fill_value']             = {'default':-9999.}
ncspec['variables']['Temp_85GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['Temp_85GHz_H']['complevel']              = {'default':1}
ncspec['variables']['Temp_85GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['Temp_85GHz_H']['data']                   = {'src':'data/h85'}
ncspec['variables']['Temp_85GHz_H']['attrs'] = {}
ncspec['variables']['Temp_85GHz_H']['attrs']['coordinates']   = {'default':['Latitude_for_89A, Longitude_for_89A']}
ncspec['variables']['Temp_85GHz_H']['attrs']['standard_name'] = {'default':'85 GHz H Brightness Temperature'}
ncspec['variables']['Temp_85GHz_H']['attrs']['long_name']     = {'default':'85 GHz H Brightness Temperature'}
ncspec['variables']['Temp_85GHz_H']['attrs']['units']         = {'default':'K'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'amsr2_points', 'fields':['file','node']}

coordVars = {}
coordVars['Brightness_Temperature_36_GHzV']   = {'lat': 'Latitude_for_36', 'lon': 'Longitude_for_36'}
coordVars['Brightness_Temperature_36_GHzH']   = {'lat': 'Latitude_for_36', 'lon': 'Longitude_for_36'}
coordVars['Brightness_Temperature_89_GHz_AV'] = {'lat': 'Latitude_for_89A', 'lon': 'Longitude_for_89A'}
coordVars['Brightness_Temperature_89_GHz_AH'] = {'lat': 'Latitude_for_89A', 'lon': 'Longitude_for_89A'}

dims = {'scancount':'Number_of_Scans', 'hires_fov':'Number_of_hi_rez_FOVs', 'lores_fov':'Number_of_low_rez_FOVs', 'primary':'Brightness_Temperature_36_GHzV'}
args = {'ncspec':ncspec, 'coords':coordVars, 'dims':dims, 'boundaries':[-60.0, -30.0, 30.0, 60.0], 'overlap':5}

job['modclass'] = {'module':'point_set_cutter', 'class':'PointSetCutter', 'args':args}
