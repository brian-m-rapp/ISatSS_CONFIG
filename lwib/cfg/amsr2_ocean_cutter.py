# Place AMSR2 Ocean products into files by geog lat, pointset compatible format

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
job['name']     = 'amsr2_ocean_cutter'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'amsr2_ocean_cutter_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':121}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':120}
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

job['cntl_node']            = 122

job['input_type']           = {'type':'infofile','node':58,'delete_file':True, 'delete_info':True}

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
ncspec['variables']['Latitude_for_High_Resolution']   = {}
ncspec['variables']['Latitude_for_High_Resolution']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_for_High_Resolution']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Latitude_for_High_Resolution']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_for_High_Resolution']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_for_High_Resolution']['complevel']              = {'default':1}
ncspec['variables']['Latitude_for_High_Resolution']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_for_High_Resolution']['data']                   = {'src':'data/Latitude_for_High_Resolution'}
ncspec['variables']['Latitude_for_High_Resolution']['attrs'] = {}
ncspec['variables']['Latitude_for_High_Resolution']['attrs']['long_name']     = {'default':'Latitude High Resolution'}
ncspec['variables']['Latitude_for_High_Resolution']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_for_High_Resolution']   = {}
ncspec['variables']['Longitude_for_High_Resolution']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_for_High_Resolution']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Longitude_for_High_Resolution']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_for_High_Resolution']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_for_High_Resolution']['complevel']              = {'default':1}
ncspec['variables']['Longitude_for_High_Resolution']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_for_High_Resolution']['data']                   = {'src':'data/Longitude_for_High_Resolution'}
ncspec['variables']['Longitude_for_High_Resolution']['attrs'] = {}
ncspec['variables']['Longitude_for_High_Resolution']['attrs']['long_name']     = {'default':'Longitude High Resolution'}
ncspec['variables']['Longitude_for_High_Resolution']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['Latitude_for_Low_Resolution']   = {}
ncspec['variables']['Latitude_for_Low_Resolution']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_for_Low_Resolution']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['Latitude_for_Low_Resolution']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_for_Low_Resolution']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_for_Low_Resolution']['complevel']              = {'default':1}
ncspec['variables']['Latitude_for_Low_Resolution']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_for_Low_Resolution']['data']                   = {'src':'data/Latitude_for_Low_Resolution'}
ncspec['variables']['Latitude_for_Low_Resolution']['attrs'] = {}
ncspec['variables']['Latitude_for_Low_Resolution']['attrs']['long_name']     = {'default':'Latitude Low Resolution'}
ncspec['variables']['Latitude_for_Low_Resolution']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_for_Low_Resolution']   = {}
ncspec['variables']['Longitude_for_Low_Resolution']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_for_Low_Resolution']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['Longitude_for_Low_Resolution']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_for_Low_Resolution']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_for_Low_Resolution']['complevel']              = {'default':1}
ncspec['variables']['Longitude_for_Low_Resolution']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_for_Low_Resolution']['data']                   = {'src':'data/Longitude_for_Low_Resolution'}
ncspec['variables']['Longitude_for_Low_Resolution']['attrs'] = {}
ncspec['variables']['Longitude_for_Low_Resolution']['attrs']['long_name']     = {'default':'Longitude Low Resolution'}
ncspec['variables']['Longitude_for_Low_Resolution']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['WSPD']   = {}
ncspec['variables']['WSPD']['fmt']                    = {'default':'f'}
ncspec['variables']['WSPD']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['WSPD']['fill_value']             = {'default':-9999.}
ncspec['variables']['WSPD']['zlib']                   = {'default':True}
ncspec['variables']['WSPD']['complevel']              = {'default':1}
ncspec['variables']['WSPD']['shuffle']                = {'default':True}
ncspec['variables']['WSPD']['data']                   = {'src':'data/WSPD'}
ncspec['variables']['WSPD']['attrs'] = {}
ncspec['variables']['WSPD']['attrs']['coordinates']   = {'default':['Latitude_for_Low_Resolution, Longitude_for_Low_Resolution']}
ncspec['variables']['WSPD']['attrs']['long_name']     = {'default':'Wind Speed'}
ncspec['variables']['WSPD']['attrs']['units']         = {'default':'m/s'}

ncspec['variables']['TPW']   = {}
ncspec['variables']['TPW']['fmt']                    = {'default':'f'}
ncspec['variables']['TPW']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['TPW']['fill_value']             = {'default':-9999.}
ncspec['variables']['TPW']['zlib']                   = {'default':True}
ncspec['variables']['TPW']['complevel']              = {'default':1}
ncspec['variables']['TPW']['shuffle']                = {'default':True}
ncspec['variables']['TPW']['data']                   = {'src':'data/TPW'}
ncspec['variables']['TPW']['attrs'] = {}
ncspec['variables']['TPW']['attrs']['coordinates']   = {'default':['Latitude_for_Low_Resolution, Longitude_for_Low_Resolution']}
ncspec['variables']['TPW']['attrs']['long_name']     = {'default':'Total Precipitable Water'}
ncspec['variables']['TPW']['attrs']['units']         = {'default':'mm'}

ncspec['variables']['CLW']   = {}
ncspec['variables']['CLW']['fmt']                    = {'default':'f'}
ncspec['variables']['CLW']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['CLW']['fill_value']             = {'default':-9999.}
ncspec['variables']['CLW']['zlib']                   = {'default':True}
ncspec['variables']['CLW']['complevel']              = {'default':1}
ncspec['variables']['CLW']['shuffle']                = {'default':True}
ncspec['variables']['CLW']['data']                   = {'src':'data/CLW'}
ncspec['variables']['CLW']['attrs'] = {}
ncspec['variables']['CLW']['attrs']['coordinates']   = {'default':['Latitude_for_Low_Resolution, Longitude_for_Low_Resolution']}
ncspec['variables']['CLW']['attrs']['long_name']     = {'default':'Cloud Liquid Water'}
ncspec['variables']['CLW']['attrs']['units']         = {'default':'mm'}

ncspec['variables']['SST']   = {}
ncspec['variables']['SST']['fmt']                    = {'default':'f'}
ncspec['variables']['SST']['shape']                  = {'default':['scanlines','fov_lores']}
ncspec['variables']['SST']['fill_value']             = {'default':-9999.}
ncspec['variables']['SST']['zlib']                   = {'default':True}
ncspec['variables']['SST']['complevel']              = {'default':1}
ncspec['variables']['SST']['shuffle']                = {'default':True}
ncspec['variables']['SST']['data']                   = {'src':'data/SST'}
ncspec['variables']['SST']['attrs'] = {}
ncspec['variables']['SST']['attrs']['coordinates']   = {'default':['Latitude_for_Low_Resolution, Longitude_for_Low_Resolution']}
ncspec['variables']['SST']['attrs']['long_name']     = {'default':'Sea Surface Temperature'}
ncspec['variables']['SST']['attrs']['units']         = {'default':'Kelvin'}

ncspec['variables']['Rain_Rate']   = {}
ncspec['variables']['Rain_Rate']['fmt']                    = {'default':'f'}
ncspec['variables']['Rain_Rate']['shape']                  = {'default':['scanlines','fov_hires']}
ncspec['variables']['Rain_Rate']['fill_value']             = {'default':-9999.}
ncspec['variables']['Rain_Rate']['zlib']                   = {'default':True}
ncspec['variables']['Rain_Rate']['complevel']              = {'default':1}
ncspec['variables']['Rain_Rate']['shuffle']                = {'default':True}
ncspec['variables']['Rain_Rate']['data']                   = {'src':'data/Rain_Rate'}
ncspec['variables']['Rain_Rate']['attrs'] = {}
ncspec['variables']['Rain_Rate']['attrs']['coordinates']   = {'default':['Latitude_for_High_Resolution, Longitude_for_High_Resolution']}
ncspec['variables']['Rain_Rate']['attrs']['long_name']     = {'default':'Surface Rain Rate'}
ncspec['variables']['Rain_Rate']['attrs']['units']         = {'default':'mm/hr'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'amsr2_ocean_points', 'fields':['file','node']}

# Coordinate attributes (variables) for each output data variable
coordVars = {}
coordVars['WSPD']       = {'lat': 'Latitude_for_Low_Resolution', 'lon': 'Longitude_for_Low_Resolution'}
coordVars['TPW']        = {'lat': 'Latitude_for_Low_Resolution', 'lon': 'Longitude_for_Low_Resolution'}
coordVars['CLW']        = {'lat': 'Latitude_for_Low_Resolution', 'lon': 'Longitude_for_Low_Resolution'}
coordVars['SST']        = {'lat': 'Latitude_for_Low_Resolution', 'lon': 'Longitude_for_Low_Resolution'}
coordVars['Rain_Rate']  = {'lat': 'Latitude_for_High_Resolution','lon': 'Longitude_for_High_Resolution'}

# For renaming variables from the input file.  Keys are the new variable names, values are the old.
varmap = {}
"""
varmap['WSPD'] = 'WSPD'
varmap['TPW'] = 'TPW'
varmap['CLW'] = 'CLW'
varmap['SST'] = 'SST'
varmap['Rain_Rate'] = 'Rain_Rate'
varmap['Latitude_lores'] = 'Latitude_for_Low_Resolution'
varmap['Longitude_lores'] = 'Longitude_for_Low_Resolution'
varmap['Latitude_hires'] = 'Latitude_for_High_Resolution'
varmap['Longitude_hires'] = 'Longitude_for_High_Resolution'
"""

# Map of dimensions to convert from the input file to the output file
dimmap = {}
dimmap['scans']       = {'scancount':'Number_of_Scans'}
dimmap['resolutions'] = {'hires':'Number_of_hi_rez_FOVs', 'lores':'Number_of_low_rez_FOVs'}
dimmap['primary']     = 'Rain_Rate'

# Map the variable row dimension back to odata row dimension
scanmap = {'scanlines':'scancount'}

args = {'ncspec':ncspec, 'coords':coordVars, 'dimmap':dimmap, 'scanmap':scanmap, 'boundaries':[-60.0, -30.0, 30.0, 60.0], 'overlap':5, 'varmap':varmap}

job['modclass'] = {'module':'point_set_cutter', 'class':'PointSetCutter', 'args':args}
