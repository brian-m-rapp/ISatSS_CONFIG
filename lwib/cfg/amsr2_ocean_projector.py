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
job['name']     = 'amsr2_ocean_projector'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'amsr2_ocean_project_log'
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
job['cntl_node']            = 123
job['input_type']           = {'type':'infofile','node':120,'delete_file':True, 'delete_info':True}

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
pfields['image']['lats']        = 'Latitude_for_High_Resolution'
pfields['image']['lons']        = 'Longitude_for_High_Resolution'
pfields['image']['proj']        =  projdict
pfields['image']['pixperpoint'] = 1          # Pixels per data point

pimages = {}
pimages['rrim'] = {}
pimages['rrim']['pfield'] = 'image'
pimages['rrim']['lats']   = 'Latitude_for_High_Resolution'
pimages['rrim']['lons']   = 'Longitude_for_High_Resolution'
pimages['rrim']['vals']   = 'Rain_Rate'
pimages['rrim']['roi']    = 10000             # Radius of Influence (in meters)
pimages['wspdim'] = {}
pimages['wspdim']['pfield'] = 'image'
pimages['wspdim']['lats']   = 'Latitude_for_Low_Resolution'
pimages['wspdim']['lons']   = 'Longitude_for_Low_Resolution'
pimages['wspdim']['vals']   = 'WSPD'
pimages['wspdim']['roi']    = 20000			 # Radius of Influence (in meters)
pimages['tpwim'] = {}
pimages['tpwim']['pfield'] = 'image'
pimages['tpwim']['lats']   = 'Latitude_for_Low_Resolution'
pimages['tpwim']['lons']   = 'Longitude_for_Low_Resolution'
pimages['tpwim']['vals']   = 'TPW'
pimages['tpwim']['roi']    = 20000			 # Radius of Influence (in meters)
pimages['clwim'] = {}
pimages['clwim']['pfield'] = 'image'
pimages['clwim']['lats']   = 'Latitude_for_Low_Resolution'
pimages['clwim']['lons']   = 'Longitude_for_Low_Resolution'
pimages['clwim']['vals']   = 'CLW'
pimages['clwim']['roi']    = 20000			 # Radius of Influence (in meters)
pimages['sstim'] = {}
pimages['sstim']['pfield'] = 'image'
pimages['sstim']['lats']   = 'Latitude_for_Low_Resolution'
pimages['sstim']['lons']   = 'Longitude_for_Low_Resolution'
pimages['sstim']['vals']   = 'SST'
pimages['sstim']['roi']    = 20000			 # Radius of Influence (in meters)

"""
odata
	
"""


ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'isatss','delimiter':'_'})
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

ncspec['variables']['Rain_Rate'] = {}
ncspec['variables']['Rain_Rate']['fmt']                     = {'default':'f4'}
ncspec['variables']['Rain_Rate']['shape']                   = {'default':['y','x']}
ncspec['variables']['Rain_Rate']['fill_value']              = {'default':-9999.}
ncspec['variables']['Rain_Rate']['zlib']                    = {'default':True}
ncspec['variables']['Rain_Rate']['complevel']               = {'default':1}
ncspec['variables']['Rain_Rate']['shuffle']                 = {'default':True}
ncspec['variables']['Rain_Rate']['data']                    = {'src':'data/Rain_Rate','map':{0:-9999.},'fmt':'f4'}
ncspec['variables']['Rain_Rate']['attrs'] = {}
ncspec['variables']['Rain_Rate']['attrs']['standard_name']  = {'default':'Surface Rain Rate'}
ncspec['variables']['Rain_Rate']['attrs']['units']          = {'default':'mm/hr'}
ncspec['variables']['Rain_Rate']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/rrim'}
ncspec['variables']['Rain_Rate']['attrs']['grid_mapping']   = {}

ncspec['variables']['WSPD'] = {}
ncspec['variables']['WSPD']['fmt']                     = {'default':'f4'}
ncspec['variables']['WSPD']['shape']                   = {'default':['y','x']}
ncspec['variables']['WSPD']['fill_value']              = {'default':-9999.}
ncspec['variables']['WSPD']['zlib']                    = {'default':True}
ncspec['variables']['WSPD']['complevel']               = {'default':1}
ncspec['variables']['WSPD']['shuffle']                 = {'default':True}
ncspec['variables']['WSPD']['data']                    = {'src':'data/WSPD','map':{0:-9999.},'fmt':'f4'}
ncspec['variables']['WSPD']['attrs'] = {}
ncspec['variables']['WSPD']['attrs']['standard_name']  = {'default':'Wind Speed'}
ncspec['variables']['WSPD']['attrs']['units']          = {'default':'m/s'}
ncspec['variables']['WSPD']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/wspdim'}
ncspec['variables']['WSPD']['attrs']['grid_mapping']   = {}

ncspec['variables']['TPW'] = {}
ncspec['variables']['TPW']['fmt']                     = {'default':'f4'}
ncspec['variables']['TPW']['shape']                   = {'default':['y','x']}
ncspec['variables']['TPW']['fill_value']              = {'default':-9999.}
ncspec['variables']['TPW']['zlib']                    = {'default':True}
ncspec['variables']['TPW']['complevel']               = {'default':1}
ncspec['variables']['TPW']['shuffle']                 = {'default':True}
ncspec['variables']['TPW']['data']                    = {'src':'data/TPW','map':{0:-9999.},'fmt':'f4'}
ncspec['variables']['TPW']['attrs'] = {}
ncspec['variables']['TPW']['attrs']['standard_name']  = {'default':'Total Precipitable Water'}
ncspec['variables']['TPW']['attrs']['units']          = {'default':'mm'}
ncspec['variables']['TPW']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/tpwim'}
ncspec['variables']['TPW']['attrs']['grid_mapping']   = {}

ncspec['variables']['CLW'] = {}
ncspec['variables']['CLW']['fmt']                     = {'default':'f4'}
ncspec['variables']['CLW']['shape']                   = {'default':['y','x']}
ncspec['variables']['CLW']['fill_value']              = {'default':-9999.}
ncspec['variables']['CLW']['zlib']                    = {'default':True}
ncspec['variables']['CLW']['complevel']               = {'default':1}
ncspec['variables']['CLW']['shuffle']                 = {'default':True}
ncspec['variables']['CLW']['data']                    = {'src':'data/CLW','map':{0:-9999.},'fmt':'f4'}
ncspec['variables']['CLW']['attrs'] = {}
ncspec['variables']['CLW']['attrs']['standard_name']  = {'default':'Cloud Liquid Water'}
ncspec['variables']['CLW']['attrs']['units']          = {'default':'mm'}
ncspec['variables']['CLW']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/clwim'}
ncspec['variables']['CLW']['attrs']['grid_mapping']   = {}

ncspec['variables']['SST'] = {}
ncspec['variables']['SST']['fmt']                     = {'default':'f4'}
ncspec['variables']['SST']['shape']                   = {'default':['y','x']}
ncspec['variables']['SST']['fill_value']              = {'default':-9999.}
ncspec['variables']['SST']['zlib']                    = {'default':True}
ncspec['variables']['SST']['complevel']               = {'default':1}
ncspec['variables']['SST']['shuffle']                 = {'default':True}
ncspec['variables']['SST']['data']                    = {'src':'data/SST','map':{0:-9999.},'fmt':'f4'}
ncspec['variables']['SST']['attrs'] = {}
ncspec['variables']['SST']['attrs']['standard_name']  = {'default':'Sea Surface Temperature'}
ncspec['variables']['SST']['attrs']['units']          = {'default':'K'}
ncspec['variables']['SST']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/sstim'}
ncspec['variables']['SST']['attrs']['grid_mapping']   = {}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'reproject_points', 'fields':['file','node']}

job['modclass'] = {'module':'swathbuckler', 'class':'GeoRGE', 'args':{'pfields':pfields,'pimages':pimages,'ncspec':ncspec, 'projections':proj_spec}}
