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
job['name']     = 'viirs_ice_projector'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'viirs_ice_project_log'
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
job['cntl_node']            = 110
job['input_type']           = {'type':'infofile','node':154,'delete_file':False, 'delete_info':False}

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
projdict['southpole']  = {'ignore': True,  'minlat':-100, 'maxlat':-85, 'projdef':projLambCC,  'projspec':'lambert_projection'}
projdict['southpolar'] = {'ignore': False, 'minlat':-85,  'maxlat':-60, 'projdef':projLambCC,  'projspec':'lambert_projection'}
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
pimages['iceconc'] = {}
pimages['iceconc']['pfield'] = 'image'
pimages['iceconc']['lats']   = 'Latitude'
pimages['iceconc']['lons']   = 'Longitude'
pimages['iceconc']['vals']   = 'IceConc'
pimages['iceconc']['roi']    = 750             # Radius of Influence (in meters)

pimages['icemap'] = {}
pimages['icemap']['pfield'] = 'image'
pimages['icemap']['lats']   = 'Latitude'
pimages['icemap']['lons']   = 'Longitude'
pimages['icemap']['vals']   = 'IceMap'
pimages['icemap']['roi']    = 750             # Radius of Influence (in meters)

pimages['dqf'] = {}
pimages['dqf']['pfield'] = 'image'
pimages['dqf']['lats']   = 'Latitude'
pimages['dqf']['lons']   = 'Longitude'
pimages['dqf']['vals']   = 'SummaryQC_Ice_Concentration'
pimages['dqf']['roi']    = 750             # Radius of Influence (in meters)

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
ncspec['globalmeta']['time_coverage_start'] = {'src':'meta/time_coverage_start'}
ncspec['globalmeta']['time_coverage_end']   = {'src':'meta/time_coverage_end'}
ncspec['globalmeta']['production_site']     = {'src':'meta/production_site'}
ncspec['globalmeta']['instrument_name']		= {'src':'meta/instrument_name'}
ncspec['globalmeta']['Metadata_Link']       = {'src':'meta/Metadata_Link'}
ncspec['globalmeta']['satellite_name']      = {'src':'meta/satellite_name'}

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

ncspec['variables']['IceConc'] = {}
ncspec['variables']['IceConc']['fmt']                     = {'default':'f4'}
ncspec['variables']['IceConc']['shape']                   = {'default':['y','x']}
ncspec['variables']['IceConc']['fill_value']              = {'default':-999.}
ncspec['variables']['IceConc']['zlib']                    = {'default':True}
ncspec['variables']['IceConc']['complevel']               = {'default':1}
ncspec['variables']['IceConc']['shuffle']                 = {'default':True}
ncspec['variables']['IceConc']['data']                    = {'src':'data/IceConc'}
ncspec['variables']['IceConc']['attrs'] = {}
ncspec['variables']['IceConc']['attrs']['standard_name']  = {'default':'Ice Concentration'}
ncspec['variables']['IceConc']['attrs']['units']          = {'default':'%'}
ncspec['variables']['IceConc']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/iceconc'}
ncspec['variables']['IceConc']['attrs']['grid_mapping']   = {}

ncspec['variables']['IceMap'] = {}
ncspec['variables']['IceMap']['fmt']                     = {'default':'i1'}
ncspec['variables']['IceMap']['shape']                   = {'default':['y','x']}
ncspec['variables']['IceMap']['fill_value']              = {'default':-3}
ncspec['variables']['IceMap']['zlib']                    = {'default':True}
ncspec['variables']['IceMap']['complevel']               = {'default':1}
ncspec['variables']['IceMap']['shuffle']                 = {'default':True}
ncspec['variables']['IceMap']['data']                    = {'src':'data/IceMap'}
ncspec['variables']['IceMap']['attrs'] = {}
ncspec['variables']['IceMap']['attrs']['standard_name']  = {'default':'Ice Cover map codes'}
ncspec['variables']['IceMap']['attrs']['units']          = {'default':'1'}
ncspec['variables']['IceMap']['attrs']['radius_of_infl'] = {'src':'parms/rad_of_infl/icemap'}
ncspec['variables']['IceMap']['attrs']['grid_mapping']   = {}

ncspec['variables']['SummaryQC_Ice_Concentration']   = {}
ncspec['variables']['SummaryQC_Ice_Concentration']['fmt']                    = {'default':'i1'}
ncspec['variables']['SummaryQC_Ice_Concentration']['shape']                  = {'default':['y','x']}
ncspec['variables']['SummaryQC_Ice_Concentration']['fill_value']             = {'default':-128}
ncspec['variables']['SummaryQC_Ice_Concentration']['zlib']                   = {'default':True}
ncspec['variables']['SummaryQC_Ice_Concentration']['complevel']              = {'default':1}
ncspec['variables']['SummaryQC_Ice_Concentration']['shuffle']                = {'default':True}
ncspec['variables']['SummaryQC_Ice_Concentration']['data']                   = {'src':'data/SummaryQC_Ice_Concentration'}
ncspec['variables']['SummaryQC_Ice_Concentration']['attrs'] = {}
ncspec['variables']['SummaryQC_Ice_Concentration']['attrs']['units']         = {'default':'1'}
ncspec['variables']['SummaryQC_Ice_Concentration']['attrs']['long_name']     = {'default':'User-level summary QC: 0=Normal, 1=Uncertain, 2=Non-Retrievable, 3=Bad'}
ncspec['variables']['SummaryQC_Ice_Concentration']['attrs']['flag_values']   = {'default':[0,1,2,3]}
ncspec['variables']['SummaryQC_Ice_Concentration']['attrs']['flag_meanings'] = {'default':'Normal, Uncertain, Non-Retrievable, Bad'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'viirs_ice', 'fields':['file','node']}

job['modclass'] = {'module':'swathbuckler', 'class':'GeoRGE', 'args':{'pfields':pfields,'pimages':pimages,'ncspec':ncspec, 'projections':proj_spec}}
