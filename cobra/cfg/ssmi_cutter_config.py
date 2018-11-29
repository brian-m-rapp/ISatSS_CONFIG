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
job['name']     = 'ssmicutter'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'ssmicutter_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':703}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':704}
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

job['cntl_node']            = 700

job['input_type']           = {'type':'infofile','node':702,'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'src':'filename'})
#ncspec['namedef'].append({'src':'ncfs/02/globalmeta/satellite_id','translate':{'GOES-16':'G16'},'delimiter':'_proxyvis_'})
#ncspec['namedef'].append({'src':'tileno','fmt':'str','pad':{'len':2,'val':'0','just':'r'},'delimiter':'_'})
#ncspec['namedef'].append({'src':'stamp','delimiter':'.nc'})

ncspec['dimensions'] = {}
ncspec['dimensions']['nscans']       = {'src':'nscans'}
ncspec['dimensions']['npixel_hires'] = {'default':256}
ncspec['dimensions']['npixel_lores'] = {'default':64}

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
ncspec['globalmeta']['keywords']         		   = {'default':'EARTH SCIENCE > SPECTRAL/ENGINEERING > MICROWAVE > ANTENNA TEMPERATURE'}
ncspec['globalmeta']['time_coverage_end']          = {'src':'times/end','timeformat':'%Y-%m-%dT%H:%M:%S.0Z'}
ncspec['globalmeta']['time_coverage_start']        = {'src':'times/start','timeformat':'%Y-%m-%dT%H:%M:%S.0Z'}
ncspec['globalmeta']['title']                      = {'default':'DMSP F15 SSM/I Microwave Temperatures'}

ncspec['variables']   = {}

ncspec['variables']['Latitude_hires']   = {}
ncspec['variables']['Latitude_hires']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_hires']['shape']                  = {'default':['nscans','npixel_hires']}
ncspec['variables']['Latitude_hires']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_hires']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_hires']['complevel']              = {'default':1}
ncspec['variables']['Latitude_hires']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_hires']['data']                   = {'src':'data/lat85'}
ncspec['variables']['Latitude_hires']['attrs'] = {}
ncspec['variables']['Latitude_hires']['attrs']['standard_name'] = {'default':'Latitude_hires'}
ncspec['variables']['Latitude_hires']['attrs']['long_name']     = {'default':'Latitude High Resolution'}
ncspec['variables']['Latitude_hires']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_hires']   = {}
ncspec['variables']['Longitude_hires']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_hires']['shape']                  = {'default':['nscans','npixel_hires']}
ncspec['variables']['Longitude_hires']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_hires']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_hires']['complevel']              = {'default':1}
ncspec['variables']['Longitude_hires']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_hires']['data']                   = {'src':'data/lon85'}
ncspec['variables']['Longitude_hires']['attrs'] = {}
ncspec['variables']['Longitude_hires']['attrs']['standard_name'] = {'default':'Longitude_hires'}
ncspec['variables']['Longitude_hires']['attrs']['long_name']     = {'default':'Longitude High Resolution'}
ncspec['variables']['Longitude_hires']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['Latitude_lores']   = {}
ncspec['variables']['Latitude_lores']['fmt']                    = {'default':'f'}
ncspec['variables']['Latitude_lores']['shape']                  = {'default':['nscans','npixel_lores']}
ncspec['variables']['Latitude_lores']['fill_value']             = {'default':-9999.}
ncspec['variables']['Latitude_lores']['zlib']                   = {'default':True}
ncspec['variables']['Latitude_lores']['complevel']              = {'default':1}
ncspec['variables']['Latitude_lores']['shuffle']                = {'default':True}
ncspec['variables']['Latitude_lores']['data']                   = {'src':'data/lat37'}
ncspec['variables']['Latitude_lores']['attrs'] = {}
ncspec['variables']['Latitude_lores']['attrs']['standard_name'] = {'default':'Latitude_lores'}
ncspec['variables']['Latitude_lores']['attrs']['long_name']     = {'default':'Latitude Low Resolution'}
ncspec['variables']['Latitude_lores']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['Longitude_lores']   = {}
ncspec['variables']['Longitude_lores']['fmt']                    = {'default':'f'}
ncspec['variables']['Longitude_lores']['shape']                  = {'default':['nscans','npixel_lores']}
ncspec['variables']['Longitude_lores']['fill_value']             = {'default':-9999.}
ncspec['variables']['Longitude_lores']['zlib']                   = {'default':True}
ncspec['variables']['Longitude_lores']['complevel']              = {'default':1}
ncspec['variables']['Longitude_lores']['shuffle']                = {'default':True}
ncspec['variables']['Longitude_lores']['data']                   = {'src':'data/lon37'}
ncspec['variables']['Longitude_lores']['attrs'] = {}
ncspec['variables']['Longitude_lores']['attrs']['standard_name'] = {'default':'Longitude_lores'}
ncspec['variables']['Longitude_lores']['attrs']['long_name']     = {'default':'Longitude Low Resolution'}
ncspec['variables']['Longitude_lores']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['Temp_37GHz_V']   = {}
ncspec['variables']['Temp_37GHz_V']['fmt']                    = {'default':'f'}
ncspec['variables']['Temp_37GHz_V']['shape']                  = {'default':['nscans','npixel_lores']}
ncspec['variables']['Temp_37GHz_V']['fill_value']             = {'default':-9999.}
ncspec['variables']['Temp_37GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['Temp_37GHz_V']['complevel']              = {'default':1}
ncspec['variables']['Temp_37GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['Temp_37GHz_V']['data']                   = {'src':'data/v37'}
ncspec['variables']['Temp_37GHz_V']['attrs'] = {}
ncspec['variables']['Temp_37GHz_V']['attrs']['coordinates']   = {'default':['Latitude_lores ','Longitude_lores']}
ncspec['variables']['Temp_37GHz_V']['attrs']['standard_name'] = {'default':'37 GHz V Brightness Temperature'}
ncspec['variables']['Temp_37GHz_V']['attrs']['long_name']     = {'default':'37 GHz V Brightness Temperature'}
ncspec['variables']['Temp_37GHz_V']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Temp_37GHz_H']   = {}
ncspec['variables']['Temp_37GHz_H']['fmt']                    = {'default':'f'}
ncspec['variables']['Temp_37GHz_H']['shape']                  = {'default':['nscans','npixel_lores']}
ncspec['variables']['Temp_37GHz_H']['fill_value']             = {'default':-9999.}
ncspec['variables']['Temp_37GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['Temp_37GHz_H']['complevel']              = {'default':1}
ncspec['variables']['Temp_37GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['Temp_37GHz_H']['data']                   = {'src':'data/h37'}
ncspec['variables']['Temp_37GHz_H']['attrs'] = {}
ncspec['variables']['Temp_37GHz_H']['attrs']['coordinates']   = {'default':['Latitude_lores ','Longitude_lores']}
ncspec['variables']['Temp_37GHz_H']['attrs']['standard_name'] = {'default':'37 GHz H Brightness Temperature'}
ncspec['variables']['Temp_37GHz_H']['attrs']['long_name']     = {'default':'37 GHz H Brightness Temperature'}
ncspec['variables']['Temp_37GHz_H']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Temp_85GHz_V']   = {}
ncspec['variables']['Temp_85GHz_V']['fmt']                    = {'default':'f'}
ncspec['variables']['Temp_85GHz_V']['shape']                  = {'default':['nscans','npixel_hires']}
ncspec['variables']['Temp_85GHz_V']['fill_value']             = {'default':-9999.}
ncspec['variables']['Temp_85GHz_V']['zlib']                   = {'default':True}
ncspec['variables']['Temp_85GHz_V']['complevel']              = {'default':1}
ncspec['variables']['Temp_85GHz_V']['shuffle']                = {'default':True}
ncspec['variables']['Temp_85GHz_V']['data']                   = {'src':'data/v85'}
ncspec['variables']['Temp_85GHz_V']['attrs'] = {}
ncspec['variables']['Temp_85GHz_V']['attrs']['coordinates']   = {'default':['Latitude_hires ','Longitude_hires']}
ncspec['variables']['Temp_85GHz_V']['attrs']['standard_name'] = {'default':'85 GHz V Brightness Temperature'}
ncspec['variables']['Temp_85GHz_V']['attrs']['long_name']     = {'default':'85 GHz V Brightness Temperature'}
ncspec['variables']['Temp_85GHz_V']['attrs']['units']         = {'default':'K'}

ncspec['variables']['Temp_85GHz_H']   = {}
ncspec['variables']['Temp_85GHz_H']['fmt']                    = {'default':'f'}
ncspec['variables']['Temp_85GHz_H']['shape']                  = {'default':['nscans','npixel_hires']}
ncspec['variables']['Temp_85GHz_H']['fill_value']             = {'default':-9999.}
ncspec['variables']['Temp_85GHz_H']['zlib']                   = {'default':True}
ncspec['variables']['Temp_85GHz_H']['complevel']              = {'default':1}
ncspec['variables']['Temp_85GHz_H']['shuffle']                = {'default':True}
ncspec['variables']['Temp_85GHz_H']['data']                   = {'src':'data/h85'}
ncspec['variables']['Temp_85GHz_H']['attrs'] = {}
ncspec['variables']['Temp_85GHz_H']['attrs']['coordinates']   = {'default':['Latitude_hires ','Longitude_hires']}
ncspec['variables']['Temp_85GHz_H']['attrs']['standard_name'] = {'default':'85 GHz H Brightness Temperature'}
ncspec['variables']['Temp_85GHz_H']['attrs']['long_name']     = {'default':'85 GHz H Brightness Temperature'}
ncspec['variables']['Temp_85GHz_H']['attrs']['units']         = {'default':'K'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'ssmi_points', 'fields':['file','node']}

#breakpoints = {}
#breakpoints['s_ps'] = -60
#breakpoints['s_ps'] = -60
#breakpoints['s_ps'] = -60
#breakpoints['s_ps'] = -60
#overlap = 3
breakpoints = [-60, 30, -30, 60]
#job['modclass'] = {'module':'ssmicon','class':'SSMI2NC','args':{'ncspec':ncspec, breakpoints, overlap}}
job['modclass'] = {'module':'ssmicutter','class':'SSMI2NC','args':{'ncspec':ncspec, 'breakpoints':breakpoints, 'regions':[-60.0, -30.0, 30.0, 60.0], 'overlap':5}}

