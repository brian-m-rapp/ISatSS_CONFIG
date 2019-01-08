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
job['name']     = 'amsr2_projector'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'amsr2_project_log'
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
job['cntl_node']            = 29
job['input_type']           = {'type':'infofile','node':27,'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

semi_major_radius = 6371200
semi_minor_radius = 6371200

projStereoN = {'proj':'stere', 'a':semi_major_radius, 'b':semi_minor_radius, 'lat_0':None,  'lon_0':None, 'lat_ts':None}
projStereoS = {'proj':'stere', 'a':semi_major_radius, 'b':semi_minor_radius, 'lat_0':None,  'lon_0':None, 'lat_ts':None}
projLambCC  = {'proj':'lcc',   'a':semi_major_radius, 'b':semi_minor_radius, 'lat_0':None,  'lon_0':None, 'lat_1':None, 'lat_2':None}
projMerc    = {'proj':'merc',  'a':semi_major_radius, 'b':semi_minor_radius, 'lon_0':None}

proj_spec = {}

proj_spec['lambert_projection'] = {}
proj_spec['lambert_projection']['fmt']                                     = {'default':'i'}
proj_spec['lambert_projection']['shape']                                   = {'default':[]}
proj_spec['lambert_projection']['attrs'] = {}
proj_spec['lambert_projection']['attrs']['grid_mapping_name']              = {'default':'lambert_conformal_conic'}
proj_spec['lambert_projection']['attrs']['standard_parallel']              = {'src':'parms/std_par'}
proj_spec['lambert_projection']['attrs']['longitude_of_central_meridian']  = {'src':'parms/center_lon'}
proj_spec['lambert_projection']['attrs']['latitude_of_projection_origin']  = {'src':'parms/center_lat'}
proj_spec['lambert_projection']['attrs']['false_easting']                  = {'default':0}
proj_spec['lambert_projection']['attrs']['false_northing']                 = {'default':0}
proj_spec['lambert_projection']['attrs']['semi_major']                     = {'default':semi_major_radius}
proj_spec['lambert_projection']['attrs']['semi_minor']                     = {'default':semi_minor_radius}

proj_spec['mercator_projection'] = {}
proj_spec['mercator_projection']['fmt']                                     = {'default':'i'}
proj_spec['mercator_projection']['shape']                                   = {'default':[]}
proj_spec['mercator_projection']['attrs'] = {}
proj_spec['mercator_projection']['attrs']['grid_mapping_name']              = {'default':'mercator'}
proj_spec['mercator_projection']['attrs']['standard_parallel']              = {'default':0.}
proj_spec['mercator_projection']['attrs']['longitude_of_projection_origin'] = {'src':'parms/center_lon'}
proj_spec['mercator_projection']['attrs']['false_easting']                  = {'default':0}
proj_spec['mercator_projection']['attrs']['false_northing']                 = {'default':0}
proj_spec['mercator_projection']['attrs']['semi_major']                     = {'default':semi_major_radius}
proj_spec['mercator_projection']['attrs']['semi_minor']                     = {'default':semi_minor_radius}

proj_spec['polar_projection'] = {}
proj_spec['polar_projection']['fmt']                                            = {'default':'i'}
proj_spec['polar_projection']['shape']                                          = {'default':[]}
proj_spec['polar_projection']['attrs'] = {}
proj_spec['polar_projection']['attrs']['grid_mapping_name']                     = {'default':'polar_stereographic'}
proj_spec['polar_projection']['attrs']['standard_parallel']                     = {'default':0.}
proj_spec['polar_projection']['attrs']['straight_vertical_longitude_from_pole'] = {'src':'parms/lon_0'}
proj_spec['polar_projection']['attrs']['latitude_of_projection_origin']         = {'src':'parms/lat_0'}
proj_spec['polar_projection']['attrs']['false_easting']                         = {'default':0}
proj_spec['polar_projection']['attrs']['false_northing']                        = {'default':0}
proj_spec['polar_projection']['attrs']['semi_major']                            = {'default':semi_major_radius}
proj_spec['polar_projection']['attrs']['semi_minor']                            = {'default':semi_minor_radius}

projdict = {}
#None means to use the (lat or lon) center derived from the data
'''
projdict['southpolar'] = {'ignore': False, 'minlat':-100, 'maxlat':-60, 'projdef':projStereoS, 'projspec':'polar_projection'}
projdict['southlamb']  = {'ignore': False, 'minlat':-60,  'maxlat':-30, 'projdef':projLambCC,  'projspec':'lambert_projection'}
projdict['merc']       = {'ignore': False, 'minlat':-30,  'maxlat':30,  'projdef':projMerc,    'projspec':'mercator_projection'}
projdict['northlamb']  = {'ignore': False, 'minlat':30,   'maxlat':60,  'projdef':projLambCC,  'projspec':'lambert_projection'}
projdict['northpolar'] = {'ignore': False, 'minlat':60,   'maxlat':100, 'projdef':projStereoN, 'projspec':'polar_projection'}
'''
projdict['southpolar'] = {'ignore': True,  'minlat':-100, 'maxlat':-60, 'projdef':projLambCC,  'projspec':'lambert_projection'}
projdict['southlamb']  = {'ignore': False, 'minlat':-60,  'maxlat':-30, 'projdef':projLambCC,  'projspec':'lambert_projection'}
projdict['merc']       = {'ignore': False, 'minlat':-30,  'maxlat':30,  'projdef':projMerc,    'projspec':'mercator_projection'}
projdict['northlamb']  = {'ignore': False, 'minlat':30,   'maxlat':60,  'projdef':projLambCC,  'projspec':'lambert_projection'}
projdict['northpolar'] = {'ignore': False, 'minlat':60,   'maxlat':100, 'projdef':projLambCC,  'projspec':'lambert_projection'}

# projected fields
pfields = {}
pfields['image'] = {}
pfields['image']['lats']        = 'Latitude_for_89A'
pfields['image']['lons']        = 'Longitude_for_89A'
pfields['image']['proj']        =  projdict
pfields['image']['pixperpoint'] = 1          # Pixels per data point

pimages = {}
pimages['v89'] = {}
pimages['v89']['pfield'] = 'image'
pimages['v89']['lats']   = 'Latitude_for_89A'
pimages['v89']['lons']   = 'Longitude_for_89A'
pimages['v89']['vals']   = 'Brightness_Temperature_89_GHz_AV'
pimages['v89']['roi']    = 10000             # Radius of Influence (in meters)
pimages['h89'] = {}
pimages['h89']['pfield'] = 'image'
pimages['h89']['lats']   = 'Latitude_for_89A'
pimages['h89']['lons']   = 'Longitude_for_89A'
pimages['h89']['vals']   = 'Brightness_Temperature_89_GHz_AH'
pimages['h89']['roi']    = 10000			 # Radius of Influence (in meters)
pimages['v36'] = {}
pimages['v36']['pfield'] = 'image'
pimages['v36']['lats']   = 'Latitude_for_36'
pimages['v36']['lons']   = 'Longitude_for_36'
pimages['v36']['vals']   = 'Brightness_Temperature_36_GHzV'
pimages['v36']['roi']    = 20000			 # Radius of Influence (in meters)
pimages['h36'] = {}
pimages['h36']['pfield'] = 'image'
pimages['h36']['lats']   = 'Latitude_for_36'
pimages['h36']['lons']   = 'Longitude_for_36'
pimages['h36']['vals']   = 'Brightness_Temperature_36_GHzH'
pimages['h36']['roi']    = 20000			 # Radius of Influence (in meters)

"""
odata
	
"""


ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'src':'filename'})

ncspec['dimensions'] = {}
ncspec['dimensions']['x']                          = {'src':'dimensions/x'}
ncspec['dimensions']['y']                          = {'src':'dimensions/y'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['platform_ID']                = {'default':'GCOM-W1'}
ncspec['globalmeta']['dataset_name']               = {'src':'meta/Metadata_Link'}
ncspec['globalmeta']['time_coverage_start']        = {'src':'meta/time_coverage_start'}
ncspec['globalmeta']['time_coverage_end']          = {'src':'meta/time_coverage_end'}
ncspec['globalmeta']['production_site']            = {'src':'meta/production_site'}
ncspec['globalmeta']['pixels_per_point']           = {'src':'parms/pixperpoint'}

ncspec['variables'] = {}
ncspec['variables']['x'] = {}
ncspec['variables']['x']['fmt']                    = {'default':'u2'}
ncspec['variables']['x']['shape']                  = {'default':['x']}
ncspec['variables']['x']['start']                  = {'default':0}
ncspec['variables']['x']['delta']                  = {'default':1}
ncspec['variables']['x']['attrs'] = {}
ncspec['variables']['x']['attrs']['standard_name'] = {'default':'projection_x_coordinate'}
ncspec['variables']['x']['attrs']['units']         = {'default':'meters'}
ncspec['variables']['x']['attrs']['add_offset']    = {'src':'parms/x_offset'}
ncspec['variables']['x']['attrs']['scale_factor']  = {'src':'parms/x_scale'}

ncspec['variables']['y'] = {}
ncspec['variables']['y']['fmt']                    = {'default':'u2'}
ncspec['variables']['y']['shape']                  = {'default':['y']}
ncspec['variables']['y']['start']                  = {'default':0}
ncspec['variables']['y']['delta']                  = {'default':1}
ncspec['variables']['y']['attrs'] = {}
ncspec['variables']['y']['attrs']['standard_name'] = {'default':'projection_y_coordinate'}
ncspec['variables']['y']['attrs']['units']         = {'default':'meters'}
ncspec['variables']['y']['attrs']['add_offset']    = {'src':'parms/y_offset'}
ncspec['variables']['y']['attrs']['scale_factor']  = {'src':'parms/y_scale'}

ncspec['variables']['Brightness_Temperature_89_GHz_AV'] = {}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['fmt']                     = {'default':'i2'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['shape']                   = {'default':['y','x']}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['fill_value']              = {'default':-9999}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['zlib']                    = {'default':True}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['complevel']               = {'default':1}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['shuffle']                 = {'default':True}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['data']                    = {'src':'data/Brightness_Temperature_89_GHz_AV'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs'] = {}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs']['standard_name']  = {'default':'89 GHz V Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs']['units']          = {'default':'K'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/v89'}
ncspec['variables']['Brightness_Temperature_89_GHz_AV']['attrs']['grid_mapping']   = {}

ncspec['variables']['Brightness_Temperature_89_GHz_AH'] = {}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['fmt']                     = {'default':'i2'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['shape']                   = {'default':['y','x']}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['fill_value']              = {'default':-9999}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['zlib']                    = {'default':True}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['complevel']               = {'default':1}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['shuffle']                 = {'default':True}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['data']                    = {'src':'data/Brightness_Temperature_89_GHz_AH'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs'] = {}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs']['standard_name']  = {'default':'89 GHz H Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs']['units']          = {'default':'K'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/h89'}
ncspec['variables']['Brightness_Temperature_89_GHz_AH']['attrs']['grid_mapping']   = {}

ncspec['variables']['Brightness_Temperature_36_GHzV'] = {}
ncspec['variables']['Brightness_Temperature_36_GHzV']['fmt']                     = {'default':'i2'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['shape']                   = {'default':['y','x']}
ncspec['variables']['Brightness_Temperature_36_GHzV']['fill_value']              = {'default':-9999}
ncspec['variables']['Brightness_Temperature_36_GHzV']['zlib']                    = {'default':True}
ncspec['variables']['Brightness_Temperature_36_GHzV']['complevel']               = {'default':1}
ncspec['variables']['Brightness_Temperature_36_GHzV']['shuffle']                 = {'default':True}
ncspec['variables']['Brightness_Temperature_36_GHzV']['data']                    = {'src':'data/Brightness_Temperature_36_GHzV'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs'] = {}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs']['standard_name']  = {'default':'36 GHz V Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs']['units']          = {'default':'K'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/v36'}
ncspec['variables']['Brightness_Temperature_36_GHzV']['attrs']['grid_mapping']   = {}

ncspec['variables']['Brightness_Temperature_36_GHzH'] = {}
ncspec['variables']['Brightness_Temperature_36_GHzH']['fmt']                     = {'default':'i2'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['shape']                   = {'default':['y','x']}
ncspec['variables']['Brightness_Temperature_36_GHzH']['fill_value']              = {'default':-9999}
ncspec['variables']['Brightness_Temperature_36_GHzH']['zlib']                    = {'default':True}
ncspec['variables']['Brightness_Temperature_36_GHzH']['complevel']               = {'default':1}
ncspec['variables']['Brightness_Temperature_36_GHzH']['shuffle']                 = {'default':True}
ncspec['variables']['Brightness_Temperature_36_GHzH']['data']                    = {'src':'data/Brightness_Temperature_36_GHzH'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs'] = {}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs']['standard_name']  = {'default':'36 GHz H Brightness Temperature'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs']['units']          = {'default':'K'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/h36'}
ncspec['variables']['Brightness_Temperature_36_GHzH']['attrs']['grid_mapping']   = {}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'reproject_points', 'fields':['file','node']}

job['modclass'] = {'module':'swathbuckler', 'class':'GeoRGE', 'args':{'pfields':pfields,'pimages':pimages,'ncspec':ncspec, 'projections':proj_spec}}
