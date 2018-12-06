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
job['name']     = 'reproject_convert'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'reproject_convert_log'
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

ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'src':'filename'})
#ncspec['namedef'].append({'src':'ncfs/02/globalmeta/satellite_id','translate':{'GOES-16':'G16'},'delimiter':'_proxyvis_'})
#ncspec['namedef'].append({'src':'tileno','fmt':'str','pad':{'len':2,'val':'0','just':'r'},'delimiter':'_'})
#ncspec['namedef'].append({'src':'stamp','delimiter':'.nc'})

ncspec['dimensions'] = {}
ncspec['dimensions']['x_hires']       = {'src':'nscans/xhires'}
ncspec['dimensions']['y_hires']       = {'src':'nscans/yhires'}
ncspec['dimensions']['x_lores']	      = {'src':'nscans/xlores'}
ncspec['dimensions']['y_lores']	      = {'src':'nscans/ylores'}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['instrument_name']            = {'default':'SSMI'}
ncspec['globalmeta']['instrument_type']            = {'default':'Microwave Radiometer'}
ncspec['globalmeta']['Metadata_Conventions']       = {'default':'Unidata Dataset Discovery v1.0'}
ncspec['globalmeta']['platform']                   = {'default':'DMSP 5D-3/F15 > Defense Meteorological Satellite Program-F15'}
ncspec['globalmeta']['platform_ID']                = {'default':'F15'}
ncspec['globalmeta']['processing_level']           = {'default':'NOAA Level 1'}
ncspec['globalmeta']['production_data_source']     = {'default':'Realtime'}
ncspec['globalmeta']['production_site']            = {'default':'NWS/NAPO'}
ncspec['globalmeta']['standard_name_vocabulary']   = {'default':'CF Standard Name Table (v25, 05 July 2013)'}
ncspec['globalmeta']['summary']                    = {'default':'Special Sensor Microwave/Imager (SSM/I) file containing 37GHz and 87GHz V & H antenna temperature from orbitized TDR data'}
ncspec['globalmeta']['keywords']                   = {'default':'EARTH SCIENCE > SPECTRAL/ENGINEERING > MICROWAVE > ANTENNA TEMPERATURE'}
#ncspec['globalmeta']['time_coverage_end']          = {'src':'times/end','timeformat':'%Y-%m-%dT%H:%M:%S.0Z'}
ncspec['globalmeta']['time_coverage_end']          = {'src':'time_coverage_end'}
ncspec['globalmeta']['time_coverage_start']        = {'src':'time_coverage_start'}
ncspec['globalmeta']['title']                      = {'default':'DMSP F15 SSM/I Microwave Temperatures'}
ncspec['globalmeta']['dataset_name']               = {'src':'filename'}

ncspec['variables']   = {}
ncspec['variables']['x_85coord']   = {}
ncspec['variables']['x_85coord']['fmt']                    = {'default':'i2'}
ncspec['variables']['x_85coord']['shape']                  = {'default':'x_hires'}
ncspec['variables']['x_85coord']['start']                  = {'default':0}
ncspec['variables']['x_85coord']['delta']                  = {'default':1}
ncspec['variables']['x_85coord']['data']                   = {'src':'data/x_85coord'}
ncspec['variables']['x_85coord']['attrs'] = {}
ncspec['variables']['x_85coord']['attrs']['standard_name'] = {'default':'projection_x_hires_coordinates'}
ncspec['variables']['x_85coord']['attrs']['units']         = {'default':'m'}
ncspec['variables']['x_85coord']['attrs']['add_offset']    = {'default':0}
ncspec['variables']['x_85coord']['attrs']['scale_factor']  = {'default':0}

ncspec['variables']['y_85coord']   = {}
ncspec['variables']['y_85coord']['fmt']                    = {'default':'i2'}
ncspec['variables']['y_85coord']['shape']                  = {'default':'y_hires'}
ncspec['variables']['y_85coord']['start']                  = {'default':0}
ncspec['variables']['y_85coord']['delta']                  = {'default':1}
ncspec['variables']['y_85coord']['data']                   = {'src':'data/y_85coord'}
ncspec['variables']['y_85coord']['attrs'] = {}
ncspec['variables']['y_85coord']['attrs']['standard_name'] = {'default':'projection_y_hires_coordinates'}
ncspec['variables']['y_85coord']['attrs']['units']         = {'default':'m'}
ncspec['variables']['y_85coord']['attrs']['add_offset']    = {'default':0}
ncspec['variables']['y_85coord']['attrs']['scale_factor']  = {'default':0}

ncspec['variables']['x_37coord']   = {}
ncspec['variables']['x_37coord']['fmt']                    = {'default':'i2'}
ncspec['variables']['x_37coord']['shape']                  = {'default':'x_lores'}
ncspec['variables']['x_37coord']['start']                  = {'default':0}
ncspec['variables']['x_37coord']['delta']                  = {'default':1}
ncspec['variables']['x_37coord']['data']                   = {'src':'data/x_37coord'}
ncspec['variables']['x_37coord']['attrs'] = {}
ncspec['variables']['x_37coord']['attrs']['standard_name'] = {'default':'projection_x_lores_coordinates'}
ncspec['variables']['x_37coord']['attrs']['units']         = {'default':'m'}
ncspec['variables']['x_37coord']['attrs']['add_offset']    = {'default':0}
ncspec['variables']['x_37coord']['attrs']['scale_factor']  = {'default':0}

ncspec['variables']['y_37coord']   = {}
ncspec['variables']['y_37coord']['fmt']                    = {'default':'i2'}
ncspec['variables']['y_37coord']['shape']                  = {'default':'y_lores'}
ncspec['variables']['y_37coord']['start']                  = {'default':0}
ncspec['variables']['y_37coord']['delta']                  = {'default':1}
ncspec['variables']['y_37coord']['data']                   = {'src':'data/y_37coord'}
ncspec['variables']['y_37coord']['attrs'] = {}
ncspec['variables']['y_37coord']['attrs']['standard_name'] = {'default':'projection_y_lores_coordinates'}
ncspec['variables']['y_37coord']['attrs']['units']         = {'default':'m'}
ncspec['variables']['y_37coord']['attrs']['add_offset']    = {'default':0}
ncspec['variables']['y_37coord']['attrs']['scale_factor']  = {'default':0}

ncspec['variables']['Temp_37GHz_V']   = {}
ncspec['variables']['Temp_37GHz_V']['fmt']                    = {'default':'u1'}
ncspec['variables']['Temp_37GHz_V']['shape']                  = {'default':['y_lores','x_lores']}
ncspec['variables']['Temp_37GHz_V']['fill_value']             = {'default':0}
ncspec['variables']['Temp_37GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['Temp_37GHz_V']['complevel']              = {'default':1}
ncspec['variables']['Temp_37GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['Temp_37GHz_V']['data']                   = {'src':'data/v37'}
ncspec['variables']['Temp_37GHz_V']['attrs'] = {}
ncspec['variables']['Temp_37GHz_V']['attrs']['standard_name'] = {'default':'37vTb'}
ncspec['variables']['Temp_37GHz_V']['attrs']['long_name']     = {'default':'37 GHz V Brightness Temperature'}
ncspec['variables']['Temp_37GHz_V']['attrs']['units']         = {'default':'K'}
ncspec['variables']['Temp_37GHz_V']['attrs']['grid_mapping']  = {'default':'goes_imager_projection'}
ncspec['variables']['Temp_37GHz_V']['attrs']['_Unsigned']     = {'default':'true'}
ncspec['variables']['Temp_37GHz_V']['attrs']['valid_min']     = {'default':0}
ncspec['variables']['Temp_37GHz_V']['attrs']['valid_max']     = {'default':255}

ncspec['variables']['Temp_37GHz_H']   = {}
ncspec['variables']['Temp_37GHz_H']['fmt']                    = {'default':'u1'}
ncspec['variables']['Temp_37GHz_H']['shape']                  = {'default':['y_lores','x_lores']}
ncspec['variables']['Temp_37GHz_H']['fill_value']             = {'default':0}
ncspec['variables']['Temp_37GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['Temp_37GHz_H']['complevel']              = {'default':1}
ncspec['variables']['Temp_37GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['Temp_37GHz_H']['data']                   = {'src':'data/h37'}
ncspec['variables']['Temp_37GHz_H']['attrs'] = {}
ncspec['variables']['Temp_37GHz_H']['attrs']['standard_name'] = {'default':'37hTb'}
ncspec['variables']['Temp_37GHz_H']['attrs']['long_name']     = {'default':'37 GHz H Brightness Temperature'}
ncspec['variables']['Temp_37GHz_H']['attrs']['units']         = {'default':'K'}
ncspec['variables']['Temp_37GHz_V']['attrs']['grid_mapping']  = {'default':'goes_imager_projection'}
ncspec['variables']['Temp_37GHz_V']['attrs']['_Unsigned']     = {'default':'true'}
ncspec['variables']['Temp_37GHz_V']['attrs']['valid_min']     = {'default':0}
ncspec['variables']['Temp_37GHz_V']['attrs']['valid_max']     = {'default':255}

ncspec['variables']['Temp_85GHz_V']   = {}
ncspec['variables']['Temp_85GHz_V']['fmt']                    = {'default':'u1'}
ncspec['variables']['Temp_85GHz_V']['shape']                  = {'default':['y_hires','x_hires']}
ncspec['variables']['Temp_85GHz_V']['fill_value']             = {'default':0}
ncspec['variables']['Temp_85GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['Temp_85GHz_V']['complevel']              = {'default':1}
ncspec['variables']['Temp_85GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['Temp_85GHz_V']['data']                   = {'src':'data/v85'}
ncspec['variables']['Temp_85GHz_V']['attrs'] = {}
ncspec['variables']['Temp_85GHz_V']['attrs']['standard_name'] = {'default':'85vTb'}
ncspec['variables']['Temp_85GHz_V']['attrs']['long_name']     = {'default':'85 GHz V Brightness Temperature'}
ncspec['variables']['Temp_85GHz_V']['attrs']['units']         = {'default':'K'}
ncspec['variables']['Temp_37GHz_V']['attrs']['grid_mapping']  = {'default':'goes_imager_projection'}
ncspec['variables']['Temp_37GHz_V']['attrs']['_Unsigned']     = {'default':'true'}
ncspec['variables']['Temp_37GHz_V']['attrs']['valid_min']     = {'default':0}
ncspec['variables']['Temp_37GHz_V']['attrs']['valid_max']     = {'default':255}

ncspec['variables']['Temp_85GHz_H']   = {}
ncspec['variables']['Temp_85GHz_H']['fmt']                    = {'default':'u1'}
ncspec['variables']['Temp_85GHz_H']['shape']                  = {'default':['y_hires','x_hires']}
ncspec['variables']['Temp_85GHz_H']['fill_value']             = {'default':0}
ncspec['variables']['Temp_85GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['Temp_85GHz_H']['complevel']              = {'default':1}
ncspec['variables']['Temp_85GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['Temp_85GHz_H']['data']                   = {'src':'data/h85'}
ncspec['variables']['Temp_85GHz_H']['attrs'] = {}
ncspec['variables']['Temp_85GHz_H']['attrs']['standard_name'] = {'default':'85hTb'}
ncspec['variables']['Temp_85GHz_H']['attrs']['long_name']     = {'default':'85 GHz H Brightness Temperature'}
ncspec['variables']['Temp_85GHz_H']['attrs']['units']         = {'default':'K'}
ncspec['variables']['Temp_37GHz_V']['attrs']['grid_mapping']  = {'default':'goes_imager_projection'}
ncspec['variables']['Temp_37GHz_V']['attrs']['_Unsigned']     = {'default':'true'}
ncspec['variables']['Temp_37GHz_V']['attrs']['valid_min']     = {'default':0}
ncspec['variables']['Temp_37GHz_V']['attrs']['valid_max']     = {'default':255}

ncspec['variables']['goes_imager_projection'] = {}
ncspec['variables']['goes_imager_projection']['fmt']                                     = {'default':'i'}
ncspec['variables']['goes_imager_projection']['shape']                                   = {'default':[]}
ncspec['variables']['goes_imager_projection']['attrs'] = {}
ncspec['variables']['goes_imager_projection']['attrs']['long_name']                      = {'default':'SSMI projection'}
ncspec['variables']['goes_imager_projection']['attrs']['grid_mapping_name']              = {'default':'geostationary'}
ncspec['variables']['goes_imager_projection']['attrs']['latitude_of_projection_origin']  = {'default':0.0}
ncspec['variables']['goes_imager_projection']['attrs']['longitude_of_projection_origin'] = {'default':-75.0}
ncspec['variables']['goes_imager_projection']['attrs']['semi_major_axis']                = {'default':6378137}
ncspec['variables']['goes_imager_projection']['attrs']['semi_minor_axis']                = {'default':6356752.31414}
ncspec['variables']['goes_imager_projection']['attrs']['perspective_point_height']       = {'default':35786023.0}
ncspec['variables']['goes_imager_projection']['attrs']['inverse_flattening']             = {'default':298.2572221}
ncspec['variables']['goes_imager_projection']['attrs']['sweep_angle_axis']               = {'default':'x'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'reproject_points', 'fields':['file','node']}

job['modclass'] = {'module':'reproject','class':'RPJT2NC','args':{'ncspec':ncspec}}

