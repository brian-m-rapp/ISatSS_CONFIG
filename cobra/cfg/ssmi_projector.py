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
job['name']     = 'ssmi_project'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'ssmi_project_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':707}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':708}
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

job['loglevel']             = 6

job['cntl_node']            = 705

job['input_type']           = {'type':'infofile','node':706,'delete_file':True, 'delete_info':True}

projStereo = {'proj':'stere','lat_0':None,'lon_0':None,'lat_ts':None, 'a':6371200, 'b':6371200}
projLambCC = {'proj':'lcc','lat_0':None,'lon_0':None,'lat_1':None,'lat_2':None, 'a':6371200, 'b':6371200}
projMerc   = {'proj':'merc','lon_0':None, 'a':6371200, 'b':6371200}

proj_spec = {}

proj_spec['lambert_projection'] = {}
proj_spec['lambert_projection']['fmt']                                     = {'default':'i'}
proj_spec['lambert_projection']['shape']                                   = {'default':[]}
proj_spec['lambert_projection']['attrs'] = {}
proj_spec['lambert_projection']['attrs']['grid_mapping_name']              = {'default':'lambert_conformal_conic'}
proj_spec['lambert_projection']['attrs']['standard_parallel']              = {'default':0.}
proj_spec['lambert_projection']['attrs']['longitude_of_central_meridian']  = {'src':'parms/center_lon'}
proj_spec['lambert_projection']['attrs']['latitude_of_projection_origin']  = {'src':'parms/center_lat'}
proj_spec['lambert_projection']['attrs']['false_easting']                  = {'default':0}
proj_spec['lambert_projection']['attrs']['false_northing']                 = {'default':0}
proj_spec['lambert_projection']['attrs']['semi_major']                     = {'default':6371200}
proj_spec['lambert_projection']['attrs']['semi_minor']                     = {'default':6371200}

proj_spec['mercator_projection'] = {}
proj_spec['mercator_projection']['fmt']                                     = {'default':'i'}
proj_spec['mercator_projection']['shape']                                   = {'default':[]}
proj_spec['mercator_projection']['attrs'] = {}
proj_spec['mercator_projection']['attrs']['grid_mapping_name']              = {'default':'mercator'}
proj_spec['mercator_projection']['attrs']['standard_parallel']              = {'default':0.}
proj_spec['mercator_projection']['attrs']['longitude_of_projection_origin'] = {'src':'parms/center_lon'}
proj_spec['mercator_projection']['attrs']['false_easting']                  = {'default':0}
proj_spec['mercator_projection']['attrs']['false_northing']                 = {'default':0}
proj_spec['mercator_projection']['attrs']['semi_major']                     = {'default':6371200}
proj_spec['mercator_projection']['attrs']['semi_minor']                     = {'default':6371200}

proj_spec['polar_projection'] = {}
proj_spec['polar_projection']['fmt']                                            = {'default':'i'}
proj_spec['polar_projection']['shape']                                          = {'default':[]}
proj_spec['polar_projection']['attrs'] = {}
proj_spec['polar_projection']['attrs']['grid_mapping_name']                     = {'default':'polar_stereographic'}
proj_spec['polar_projection']['attrs']['standard_parallel']                     = {'default':0.}
proj_spec['polar_projection']['attrs']['straight_vertical_longitude_from_pole'] = {'src':'parms/center_lon'}
proj_spec['polar_projection']['attrs']['latitude_of_projection_origin']         = {'src':'parms/center_lat'}
proj_spec['polar_projection']['attrs']['false_easting']                         = {'default':0}
proj_spec['polar_projection']['attrs']['false_northing']                        = {'default':0}
proj_spec['polar_projection']['attrs']['semi_major']                            = {'default':6371200}
proj_spec['polar_projection']['attrs']['semi_minor']                            = {'default':6371200}

projdict = {}
#None means to use the (lat or lon) center derived from the data
projdict['southpolar'] = {'minlat':-100, 'maxlat':-60, 'roi': 15000, 'projdef':projStereo, 'projspec':'polar_projection'}
projdict['southlamb']  = {'minlat':-60,  'maxlat':-30, 'roi': 15000, 'projdef':projLambCC, 'projspec':'lambert_projection'}
projdict['merc']       = {'minlat':-30,  'maxlat':30,  'roi': 15000, 'projdef':projMerc, 'projspec':'mercator_projection'}
projdict['northlamb']  = {'minlat':30,   'maxlat':60,  'roi': 15000, 'projdef':projLambCC, 'projspec':'lambert_projection'}
projdict['northpolar'] = {'minlat':60,   'maxlat':100, 'roi': 15000, 'projdef':projStereo, 'projspec':'polar_projection'}

# projected fields
pfields = {}
pfields['image'] = {}
pfields['image']['lats']        = 'Latitude_hires'
pfields['image']['lons']        = 'Longitude_hires'
pfields['image']['proj']        =  projdict
pfields['image']['pixperpoint'] = 4

pimages = {}
pimages['v85'] = {}
pimages['v85']['pfield'] = 'image'
pimages['v85']['lats']   = 'Latitude_hires'
pimages['v85']['lons']   = 'Longitude_hires'
pimages['v85']['vals']   = 'Temp_85GHz_V'
pimages['v85']['roi']    = 15000
pimages['h85'] = {}
pimages['h85']['pfield'] = 'image'
pimages['h85']['lats']   = 'Latitude_hires'
pimages['h85']['lons']   = 'Longitude_hires'
pimages['h85']['vals']   = 'Temp_85GHz_H'
pimages['h85']['roi']    = 15000
pimages['v37'] = {}
pimages['v37']['pfield'] = 'image'
pimages['v37']['lats']   = 'Latitude_lores'
pimages['v37']['lons']   = 'Longitude_lores'
pimages['v37']['vals']   = 'Temp_37GHz_V'
pimages['v37']['roi']    = 30000
pimages['h37'] = {}
pimages['h37']['pfield'] = 'image'
pimages['h37']['lats']   = 'Latitude_lores'
pimages['h37']['lons']   = 'Longitude_lores'
pimages['h37']['vals']   = 'Temp_37GHz_H'
pimages['h37']['roi']    = 30000

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
ncspec['globalmeta']['title']				       = {'src':'meta/title'}
ncspec['globalmeta']['platform']                   = {'src':'meta/platform'}
ncspec['globalmeta']['platform_ID']                = {'src':'meta/platform_ID'}
ncspec['globalmeta']['dataset_name']               = {'src':'filename'}
ncspec['globalmeta']['time_coverage_start']        = {'src':'meta/time_coverage_start'}
ncspec['globalmeta']['time_coverage_end']          = {'src':'meta/time_coverage_end'}
ncspec['globalmeta']['production_site']            = {'src':'meta/production_site'}
ncspec['globalmeta']['Metadata_Conventions']       = {'src':'meta/Metadata_Conventions'}

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

ncspec['variables']['Temp_85GHz_V'] = {}
ncspec['variables']['Temp_85GHz_V']['fmt']                    = {'default':'u2'}
ncspec['variables']['Temp_85GHz_V']['shape']                  = {'default':['y','x']}
ncspec['variables']['Temp_85GHz_V']['fill_value']             = {'default':-9999}
ncspec['variables']['Temp_85GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['Temp_85GHz_V']['complevel']              = {'default':1}
ncspec['variables']['Temp_85GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['Temp_85GHz_V']['data']                   = {'src':'data/Temp_85GHz_V'}
ncspec['variables']['Temp_85GHz_V']['attrs'] = {}
ncspec['variables']['Temp_85GHz_V']['attrs']['standard_name'] = {'default':'85 GHz V Brightness Temperature'}
ncspec['variables']['Temp_85GHz_V']['attrs']['units']         = {'default':'K'}
ncspec['variables']['Temp_85GHz_V']['attrs']['grid_mapping']  = {}

ncspec['variables']['Temp_85GHz_H'] = {}
ncspec['variables']['Temp_85GHz_H']['fmt']                    = {'default':'u2'}
ncspec['variables']['Temp_85GHz_H']['shape']                  = {'default':['y','x']}
ncspec['variables']['Temp_85GHz_H']['fill_value']             = {'default':-9999}
ncspec['variables']['Temp_85GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['Temp_85GHz_H']['complevel']              = {'default':1}
ncspec['variables']['Temp_85GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['Temp_85GHz_H']['data']                   = {'src':'data/Temp_85GHz_H'}
ncspec['variables']['Temp_85GHz_H']['attrs'] = {}
ncspec['variables']['Temp_85GHz_H']['attrs']['standard_name'] = {'default':'85 GHz H Brightness Temperature'}
ncspec['variables']['Temp_85GHz_H']['attrs']['units']         = {'default':'K'}
ncspec['variables']['Temp_85GHz_H']['attrs']['grid_mapping']  = {}

ncspec['variables']['Temp_37GHz_V'] = {}
ncspec['variables']['Temp_37GHz_V']['fmt']                    = {'default':'u2'}
ncspec['variables']['Temp_37GHz_V']['shape']                  = {'default':['y','x']}
ncspec['variables']['Temp_37GHz_V']['fill_value']             = {'default':-9999}
ncspec['variables']['Temp_37GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['Temp_37GHz_V']['complevel']              = {'default':1}
ncspec['variables']['Temp_37GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['Temp_37GHz_V']['data']                   = {'src':'data/Temp_37GHz_V'}
ncspec['variables']['Temp_37GHz_V']['attrs'] = {}
ncspec['variables']['Temp_37GHz_V']['attrs']['standard_name'] = {'default':'37 GHz V Brightness Temperature'}
ncspec['variables']['Temp_37GHz_V']['attrs']['units']         = {'default':'K'}
ncspec['variables']['Temp_37GHz_V']['attrs']['grid_mapping']  = {}

ncspec['variables']['Temp_37GHz_H'] = {}
ncspec['variables']['Temp_37GHz_H']['fmt']                    = {'default':'u2'}
ncspec['variables']['Temp_37GHz_H']['shape']                  = {'default':['y','x']}
ncspec['variables']['Temp_37GHz_H']['fill_value']             = {'default':-9999}
ncspec['variables']['Temp_37GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['Temp_37GHz_H']['complevel']              = {'default':1}
ncspec['variables']['Temp_37GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['Temp_37GHz_H']['data']                   = {'src':'data/Temp_37GHz_H'}
ncspec['variables']['Temp_37GHz_H']['attrs'] = {}
ncspec['variables']['Temp_37GHz_H']['attrs']['standard_name'] = {'default':'37 GHz H Brightness Temperature'}
ncspec['variables']['Temp_37GHz_H']['attrs']['units']         = {'default':'K'}
ncspec['variables']['Temp_37GHz_H']['attrs']['grid_mapping']  = {}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'reproject_points', 'fields':['file','node']}

job['modclass'] = {'module':'swathbuckler','class':'GeoRGE','args':{'pfields':pfields,'pimages':pimages,'ncspec':ncspec, 'projections':proj_spec}}
