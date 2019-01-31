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
job['name']     = 'gpm_gmi_projector'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'gpm_gmi_project_log'
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
job['cntl_node']            = 114
job['input_type']           = {'type':'infofile','node':112,'delete_file':True, 'delete_info':True}

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
pfields['image']['lats']        = 'Latitude'
pfields['image']['lons']        = 'Longitude'
pfields['image']['proj']        =  projdict
pfields['image']['pixperpoint'] = 1          # Pixels per data point

pimages = {}
pimages['v89'] = {}
pimages['v89']['pfield'] = 'image'
pimages['v89']['lats']   = 'Latitude'
pimages['v89']['lons']   = 'Longitude'
pimages['v89']['vals']   = 'BTemp_89GHz_V'
pimages['v89']['roi']    = 10000             # Radius of Influence (in meters)
pimages['h89'] = {}
pimages['h89']['pfield'] = 'image'
pimages['h89']['lats']   = 'Latitude'
pimages['h89']['lons']   = 'Longitude'
pimages['h89']['vals']   = 'BTemp_89GHz_H'
pimages['h89']['roi']    = 10000			 # Radius of Influence (in meters)
pimages['v37'] = {}
pimages['v37']['pfield'] = 'image'
pimages['v37']['lats']   = 'Latitude'
pimages['v37']['lons']   = 'Longitude'
pimages['v37']['vals']   = 'BTemp_37GHz_V'
pimages['v37']['roi']    = 10000			 # Radius of Influence (in meters)
pimages['h37'] = {}
pimages['h37']['pfield'] = 'image'
pimages['h37']['lats']   = 'Latitude'
pimages['h37']['lons']   = 'Longitude'
pimages['h37']['vals']   = 'BTemp_37GHz_H'
pimages['h37']['roi']    = 10000			 # Radius of Influence (in meters)

"""
odata
	
"""


ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'isatss', 'delimiter':'_'})
ncspec['namedef'].append({'src':'filename'})

ncspec['dimensions'] = {}
ncspec['dimensions']['x']                          = {'src':'dimensions/x'}
ncspec['dimensions']['y']                          = {'src':'dimensions/y'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['platform_ID']                = {'default':'GCOM-W1'}
ncspec['globalmeta']['dataset_name']               = {'src':'meta/Metadata_Link'}
ncspec['globalmeta']['time_coverage_start']        = {'src':'meta/time_coverage_start'}
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

ncspec['variables']['BTemp_89GHz_V'] = {}
ncspec['variables']['BTemp_89GHz_V']['fmt']                     = {'default':'i2'}
ncspec['variables']['BTemp_89GHz_V']['shape']                   = {'default':['y','x']}
ncspec['variables']['BTemp_89GHz_V']['fill_value']              = {'default':-9999}
ncspec['variables']['BTemp_89GHz_V']['zlib']                    = {'default':True}
ncspec['variables']['BTemp_89GHz_V']['complevel']               = {'default':1}
ncspec['variables']['BTemp_89GHz_V']['shuffle']                 = {'default':True}
ncspec['variables']['BTemp_89GHz_V']['data']                    = {'src':'data/BTemp_89GHz_V'}
ncspec['variables']['BTemp_89GHz_V']['attrs'] = {}
ncspec['variables']['BTemp_89GHz_V']['attrs']['standard_name']  = {'default':'89 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_89GHz_V']['attrs']['units']          = {'default':'K'}
ncspec['variables']['BTemp_89GHz_V']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/v89'}
ncspec['variables']['BTemp_89GHz_V']['attrs']['grid_mapping']   = {}

ncspec['variables']['BTemp_89GHz_H'] = {}
ncspec['variables']['BTemp_89GHz_H']['fmt']                     = {'default':'i2'}
ncspec['variables']['BTemp_89GHz_H']['shape']                   = {'default':['y','x']}
ncspec['variables']['BTemp_89GHz_H']['fill_value']              = {'default':-9999}
ncspec['variables']['BTemp_89GHz_H']['zlib']                    = {'default':True}
ncspec['variables']['BTemp_89GHz_H']['complevel']               = {'default':1}
ncspec['variables']['BTemp_89GHz_H']['shuffle']                 = {'default':True}
ncspec['variables']['BTemp_89GHz_H']['data']                    = {'src':'data/BTemp_89GHz_H'}
ncspec['variables']['BTemp_89GHz_H']['attrs'] = {}
ncspec['variables']['BTemp_89GHz_H']['attrs']['standard_name']  = {'default':'89 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_89GHz_H']['attrs']['units']          = {'default':'K'}
ncspec['variables']['BTemp_89GHz_H']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/h89'}
ncspec['variables']['BTemp_89GHz_H']['attrs']['grid_mapping']   = {}

ncspec['variables']['BTemp_37GHz_V'] = {}
ncspec['variables']['BTemp_37GHz_V']['fmt']                     = {'default':'i2'}
ncspec['variables']['BTemp_37GHz_V']['shape']                   = {'default':['y','x']}
ncspec['variables']['BTemp_37GHz_V']['fill_value']              = {'default':-9999}
ncspec['variables']['BTemp_37GHz_V']['zlib']                    = {'default':True}
ncspec['variables']['BTemp_37GHz_V']['complevel']               = {'default':1}
ncspec['variables']['BTemp_37GHz_V']['shuffle']                 = {'default':True}
ncspec['variables']['BTemp_37GHz_V']['data']                    = {'src':'data/BTemp_37GHz_V'}
ncspec['variables']['BTemp_37GHz_V']['attrs'] = {}
ncspec['variables']['BTemp_37GHz_V']['attrs']['standard_name']  = {'default':'36.5 GHz V Brightness Temperature'}
ncspec['variables']['BTemp_37GHz_V']['attrs']['units']          = {'default':'K'}
ncspec['variables']['BTemp_37GHz_V']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/v37'}
ncspec['variables']['BTemp_37GHz_V']['attrs']['grid_mapping']   = {}

ncspec['variables']['BTemp_37GHz_H'] = {}
ncspec['variables']['BTemp_37GHz_H']['fmt']                     = {'default':'i2'}
ncspec['variables']['BTemp_37GHz_H']['shape']                   = {'default':['y','x']}
ncspec['variables']['BTemp_37GHz_H']['fill_value']              = {'default':-9999}
ncspec['variables']['BTemp_37GHz_H']['zlib']                    = {'default':True}
ncspec['variables']['BTemp_37GHz_H']['complevel']               = {'default':1}
ncspec['variables']['BTemp_37GHz_H']['shuffle']                 = {'default':True}
ncspec['variables']['BTemp_37GHz_H']['data']                    = {'src':'data/BTemp_37GHz_H'}
ncspec['variables']['BTemp_37GHz_H']['attrs'] = {}
ncspec['variables']['BTemp_37GHz_H']['attrs']['standard_name']  = {'default':'36.5 GHz H Brightness Temperature'}
ncspec['variables']['BTemp_37GHz_H']['attrs']['units']          = {'default':'K'}
ncspec['variables']['BTemp_37GHz_H']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/h37'}
ncspec['variables']['BTemp_37GHz_H']['attrs']['grid_mapping']   = {}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'gpm_gmi_projection', 'fields':['file','node']}

job['modclass'] = {'module':'swathbuckler', 'class':'GeoRGE', 'args':{'pfields':pfields,'pimages':pimages,'ncspec':ncspec, 'projections':proj_spec}}
