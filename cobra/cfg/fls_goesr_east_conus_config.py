# Frank configuration for G-16 Fog and Low Stratus product

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
"""
	Add goes imagery projection, not found in originating file
"""

job = {}
job['name']     = 'fls_processing'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'fls_processing_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':92}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':91}
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

job['cntl_node']            = 88

job['input_type']           = {'type':'infofile', 'node':87, 'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

#inncf
ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'IXTE99_napo','delimiter':'_'})
ncspec['namedef'].append({'src':'inncf/globalmeta/Metadata_Link'})

ncspec['dimensions'] = {}
#ncspec['dimensions']['y']        = {'default':1500}
#ncspec['dimensions']['x']        = {'default':2500}
ncspec['dimensions']['y']        = {'src':'inncf/dimensions/Rows'}
ncspec['dimensions']['x']        = {'src':'inncf/dimensions/Columns'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['scene_id']                = {'src':'inncf/globalmeta/scene_id'}
ncspec['globalmeta']['orbital_slot']            = {'src':'inncf/globalmeta/orbital_slot'}
ncspec['globalmeta']['time_coverage_start']     = {'src':'inncf/globalmeta/time_coverage_start'}
ncspec['globalmeta']['dataset_name']            = {'src':'inncf/globalmeta/Metadata_Link'}
ncspec['globalmeta']['platform_ID']             = {'default':'G16'}
ncspec['globalmeta']['production_site']         = {'default':'NAPO'}


ncspec['variables']   = {}
ncspec['variables']['goes_imager_projection']   = {}
ncspec['variables']['goes_imager_projection']['fmt']                                       = {'default':'i'}
ncspec['variables']['goes_imager_projection']['shape']                                     = {'default':[]}
ncspec['variables']['goes_imager_projection']['attrs'] = {}
ncspec['variables']['goes_imager_projection']['attrs']['long_name']                        = {'default':'GOES-R ABI fixed grid projection'}
ncspec['variables']['goes_imager_projection']['attrs']['grid_mapping_name']                = {'default':'geostationary'}
ncspec['variables']['goes_imager_projection']['attrs']['perspective_point_height']         = {'default':35786023.0}
ncspec['variables']['goes_imager_projection']['attrs']['semi_major_axis']                  = {'default':6378137}
ncspec['variables']['goes_imager_projection']['attrs']['semi_minor_axis']                  = {'default':6356752.31414}
ncspec['variables']['goes_imager_projection']['attrs']['inverse_flattening']               = {'default':298.2572221}
ncspec['variables']['goes_imager_projection']['attrs']['latitude_of_projection_origin']    = {'default':0.0}
ncspec['variables']['goes_imager_projection']['attrs']['longitude_of_projection_origin']   = {'default':-75.0}
ncspec['variables']['goes_imager_projection']['attrs']['sweep_angle_axis']                 = {'default':'x'}


ncspec['variables']['y']  = {}
ncspec['variables']['y']['fmt']                    = {'default':'i2'}
ncspec['variables']['y']['shape']                  = {'default':['y']}
ncspec['variables']['y']['start']                  = {'default':0}
ncspec['variables']['y']['delta']                  = {'default':1}
ncspec['variables']['y']['attrs'] = {}
ncspec['variables']['y']['attrs']['long_name']     = {'default':'GOES fixed grid projection y-coordinate'}
ncspec['variables']['y']['attrs']['standard_name'] = {'default':'projection_y_coordinate'}
ncspec['variables']['y']['attrs']['units']         = {'default':'rad'}
ncspec['variables']['y']['attrs']['axis']          = {'default':'Y'}
ncspec['variables']['y']['attrs']['add_offset']    = {'default':0.128212}
ncspec['variables']['y']['attrs']['scale_factor']  = {'default':-5.6e-5}


ncspec['variables']['x']  = {}
ncspec['variables']['x']['fmt']                    = {'default':'i2'}
ncspec['variables']['x']['shape']                  = {'default':['x']}
ncspec['variables']['x']['start']                  = {'default':0}
ncspec['variables']['x']['delta']                  = {'default':1}
ncspec['variables']['x']['attrs'] = {}
ncspec['variables']['x']['attrs']['long_name']     = {'default':'GOES fixed grid projection x-coordinate'}
ncspec['variables']['x']['attrs']['standard_name'] = {'default':'projection_x_coordinate'}
ncspec['variables']['x']['attrs']['axis']          = {'default':'X'}
ncspec['variables']['x']['attrs']['units']         = {'default':'rad'}
ncspec['variables']['x']['attrs']['add_offset']    = {'default':-0.101332}
ncspec['variables']['x']['attrs']['scale_factor']  = {'default':5.6e-5}

ncspec['variables']['Fog_Depth']   = {}
ncspec['variables']['Fog_Depth']['fmt']                    = {'default':'u2'}
ncspec['variables']['Fog_Depth']['shape']                  = {'default':['y','x']}
ncspec['variables']['Fog_Depth']['fill_value']             = {'default':65535}
ncspec['variables']['Fog_Depth']['zlib']                   = {'default':True}
ncspec['variables']['Fog_Depth']['complevel']              = {'default':1}
ncspec['variables']['Fog_Depth']['shuffle']                = {'default':True}
ncspec['variables']['Fog_Depth']['data']                   = {'src':'data/Fog_Depth','mapnegfill':{0:65535},'fmt':'u2'}
#ncspec['variables']['Fog_Depth']['data']                   = {'src':'data/Fog_Depth','map':{-999.0:65535},'fmt':'u2'}
ncspec['variables']['Fog_Depth']['attrs'] = {}
ncspec['variables']['Fog_Depth']['attrs']['units']         = {'default':'m'}
ncspec['variables']['Fog_Depth']['attrs']['long_name']     = {'default':'Fog_Depth'}
ncspec['variables']['Fog_Depth']['attrs']['grid_mapping']  = {'default':'goes_imager_projection'}
ncspec['variables']['Fog_Depth']['attrs']['_Unsigned']     = {'default':'true'}
ncspec['variables']['Fog_Depth']['attrs']['coordinates']   = {'default':'y x'}

ncspec['variables']['IFR_Fog_Prob']   = {}
ncspec['variables']['IFR_Fog_Prob']['fmt']                    = {'default':'u2'}
ncspec['variables']['IFR_Fog_Prob']['shape']                  = {'default':['y','x']}
ncspec['variables']['IFR_Fog_Prob']['fill_value']             = {'default':65535}
ncspec['variables']['IFR_Fog_Prob']['zlib']                   = {'default':True}
ncspec['variables']['IFR_Fog_Prob']['complevel']              = {'default':1}
ncspec['variables']['IFR_Fog_Prob']['shuffle']                = {'default':True}
ncspec['variables']['IFR_Fog_Prob']['data']                   = {'src':'data/IFR_Fog_Prob','map':{-999.0:65535},'fmt':'u2'}
ncspec['variables']['IFR_Fog_Prob']['attrs'] = {}
ncspec['variables']['IFR_Fog_Prob']['attrs']['units']         = {'default':'%'}
ncspec['variables']['IFR_Fog_Prob']['attrs']['long_name']     = {'default':'IFR_Fog_Prob'}
ncspec['variables']['IFR_Fog_Prob']['attrs']['grid_mapping']  = {'default':'goes_imager_projection'}
ncspec['variables']['IFR_Fog_Prob']['attrs']['_Unsigned']     = {'default':'true'}
ncspec['variables']['IFR_Fog_Prob']['attrs']['coordinates']   = {'default':'y x'}

ncspec['variables']['LIFR_Fog_Prob']   = {}
ncspec['variables']['LIFR_Fog_Prob']['fmt']                    = {'default':'u2'}
ncspec['variables']['LIFR_Fog_Prob']['shape']                  = {'default':['y','x']}
ncspec['variables']['LIFR_Fog_Prob']['fill_value']             = {'default':65535}
ncspec['variables']['LIFR_Fog_Prob']['zlib']                   = {'default':True}
ncspec['variables']['LIFR_Fog_Prob']['complevel']              = {'default':1}
ncspec['variables']['LIFR_Fog_Prob']['shuffle']                = {'default':True}
ncspec['variables']['LIFR_Fog_Prob']['data']                   = {'src':'data/LIFR_Fog_Prob','map':{-999.0:65535},'fmt':'u2'}
ncspec['variables']['LIFR_Fog_Prob']['attrs'] = {}
ncspec['variables']['LIFR_Fog_Prob']['attrs']['units']         = {'default':'%'}
ncspec['variables']['LIFR_Fog_Prob']['attrs']['long_name']     = {'default':'LIFR_Fog_Prob'}
ncspec['variables']['LIFR_Fog_Prob']['attrs']['grid_mapping']  = {'default':'goes_imager_projection'}
ncspec['variables']['LIFR_Fog_Prob']['attrs']['_Unsigned']     = {'default':'true'}
ncspec['variables']['LIFR_Fog_Prob']['attrs']['coordinates']   = {'default':'y x'}

ncspec['variables']['MVFR_Fog_Prob']   = {}
ncspec['variables']['MVFR_Fog_Prob']['fmt']                    = {'default':'u2'}
ncspec['variables']['MVFR_Fog_Prob']['shape']                  = {'default':['y','x']}
ncspec['variables']['MVFR_Fog_Prob']['fill_value']             = {'default':65535}
ncspec['variables']['MVFR_Fog_Prob']['zlib']                   = {'default':True}
ncspec['variables']['MVFR_Fog_Prob']['complevel']              = {'default':1}
ncspec['variables']['MVFR_Fog_Prob']['shuffle']                = {'default':True}
ncspec['variables']['MVFR_Fog_Prob']['data']                   = {'src':'data/MVFR_Fog_Prob','map':{-999.0:65535},'fmt':'u2'}
ncspec['variables']['MVFR_Fog_Prob']['attrs'] = {}
ncspec['variables']['MVFR_Fog_Prob']['attrs']['units']         = {'default':'%'}
ncspec['variables']['MVFR_Fog_Prob']['attrs']['long_name']     = {'default':'MVFR_Fog_Prob'}
ncspec['variables']['MVFR_Fog_Prob']['attrs']['grid_mapping']  = {'default':'goes_imager_projection'}
ncspec['variables']['MVFR_Fog_Prob']['attrs']['_Unsigned']     = {'default':'true'}
ncspec['variables']['MVFR_Fog_Prob']['attrs']['coordinates']   = {'default':'y x'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'aaw', 'fields':['file','node']}

job['modclass'] = {'module':'nc_convert','class':'NCCon','args':{'ncspec':ncspec}}

