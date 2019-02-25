"""
    IDP Satellite Support Subsystem
    Copyright (C) 2016-2019 Joseph K. Zajic (joe.zajic@noaa.gov), Brian M. Rapp (brian.rapp@noaa.gov)

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
    Reformat/tailor Cryosat text files (as avail from star) into a format for the goes-r dmw
    plugin.  The purpose is to ingest the data into edex via the dmw table for access
    in cave using the point plot resource data, latter plots the values of wave height as text.

    These files do not flow over SBN, but can be found on the star anonymous ftp:
    ftp://ftp.star.nesdis.noaa.gov/pub/socd/lsa/johnl/c2
    example file name: c2_20190212T14_swh.txt
"""

job = {}
job['name']     = 'altika_processor'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'altika_processor_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':134}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':135}
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

job['cntl_node']            = 133

job['input_type']           = {'type':'infofile','node':132,'delete_file':True, 'delete_info':True}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'altika_pass', 'delimiter':'_'})
ncspec['namedef'].append({'src':'meta/absolute_pass_number', 'delimiter':'_rev_'})
ncspec['namedef'].append({'src':'meta/absolute_rev_number', 'delimiter':'.nc'})

ncspec['dimensions'] = {}
ncspec['dimensions']['time']      = {'src':'inncf/dimensions/time'}
ncspec['dimensions']['dmw_band']  = {'default':1}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['production_site']       = {'src':'isatss/site'}
ncspec['globalmeta']['mission_name']          = {'src':'meta/mission_name'}
ncspec['globalmeta']['altimeter_sensor_name'] = {'src':'meta/altimeter_sensor_name'}
ncspec['globalmeta']['coverage_start_time']   = {'src':'meta/first_meas_time', 'timereformat':{'in':'%Y-%m-%d %H:%M:%S','out':'%Y-%m-%dT%H:%M:%S','start':0,'nchar':19}}
ncspec['globalmeta']['coverage_end_time']     = {'src':'meta/last_meas_time', 'timereformat':{'in':'%Y-%m-%d %H:%M:%S','out':'%Y-%m-%dT%H:%M:%S','start':0,'nchar':19}}

ncspec['variables']   = {}
ncspec['variables']['lat']   = {}
ncspec['variables']['lat']['fmt']                    = {'default':'f4'}
ncspec['variables']['lat']['shape']                  = {'default':['time']}
ncspec['variables']['lat']['zlib']                   = {'default':True}
ncspec['variables']['lat']['complevel']              = {'default':1}
ncspec['variables']['lat']['shuffle']                = {'default':True}
ncspec['variables']['lat']['data']                   = {'src':'data/lat', 'mapscalefac':{-999:{'scale':1e-6}}, 'fmt':'f4'}
ncspec['variables']['lat']['attrs'] = {}
ncspec['variables']['lat']['attrs']['long_name']     = {'default':'latitude'}
ncspec['variables']['lat']['attrs']['standard_name'] = {'default':'latitude'}
ncspec['variables']['lat']['attrs']['units']         = {'default':'degrees_north'}
ncspec['variables']['lat']['attrs']['comment']       = {'default':'Positive latitude is North latitude, negative latitude is South latitude. See SARAL User Handbook.'}

ncspec['variables']['lon']   = {}
ncspec['variables']['lon']['fmt']                    = {'default':'f4'}
ncspec['variables']['lon']['shape']                  = {'default':['time']}
ncspec['variables']['lon']['zlib']                   = {'default':True}
ncspec['variables']['lon']['complevel']              = {'default':1}
ncspec['variables']['lon']['shuffle']                = {'default':True}
ncspec['variables']['lon']['data']                   = {'src':'data/lon', 'mapscalefac':{-999:{'scale':1e-6, 'longt180neg':True}}, 'fmt':'f4'}
ncspec['variables']['lon']['attrs'] = {}
ncspec['variables']['lon']['attrs']['long_name']     = {'default':'longitude'}
ncspec['variables']['lon']['attrs']['standard_name'] = {'default':'longitude'}
ncspec['variables']['lon']['attrs']['units']         = {'default':'degrees_east'}
ncspec['variables']['lon']['attrs']['comment']       = {'default':'East longitude relative to Greenwich meridian. See SARAL User Handbook.'}

ncspec['variables']['time']   = {}
ncspec['variables']['time']['fmt']                         = {'default':'f8'}
ncspec['variables']['time']['shape']                       = {'default':['time']}
ncspec['variables']['time']['zlib']                        = {'default':True}
ncspec['variables']['time']['complevel']                   = {'default':1}
ncspec['variables']['time']['shuffle']                     = {'default':True}
ncspec['variables']['time']['data']                        = {'src':'data/time', 'truncate':1800}
ncspec['variables']['time']['attrs'] = {}
ncspec['variables']['time']['attrs']['standard_name']      = {'default':'time'}
ncspec['variables']['time']['attrs']['long_name']          = {'default':'time (sec. since 2000-01-01)'}
ncspec['variables']['time']['attrs']['units']              = {'default':'seconds since 2000-01-01 00:00:00.0'}

ncspec['variables']['swh']   = {}
ncspec['variables']['swh']['fmt']                    = {'default':'f4'}
ncspec['variables']['swh']['shape']                  = {'default':['time']}
ncspec['variables']['swh']['fill_value']             = {'default':-999.0}
ncspec['variables']['swh']['zlib']                   = {'default':True}
ncspec['variables']['swh']['complevel']              = {'default':1}
ncspec['variables']['swh']['shuffle']                = {'default':True}
ncspec['variables']['swh']['data']                   = {'src':'data/swh', 'mapscalefac':{-999:{'scale':.001}}, 'map':{32767:-999}, 'fmt':'f4'}
ncspec['variables']['swh']['attrs'] = {}
ncspec['variables']['swh']['attrs']['units']         = {'default':'m'}
ncspec['variables']['swh']['attrs']['standard_name'] = {'default':'sea_surface_wave_significant_height'}
ncspec['variables']['swh']['attrs']['long_name']     = {'default':'Corrected significant waveheight'}
ncspec['variables']['swh']['attrs']['coordinates']   = {'default':['lon, lat']}
ncspec['variables']['swh']['attrs']['comment']       = {'default':'All instrumental corrections included, i.e. modeled instrumental errors correction (modeled_instr_corr_swh) and system bias'}

ncspec['variables']['surface_type']   = {}
ncspec['variables']['surface_type']['fmt']                    = {'default':'i1'}
ncspec['variables']['surface_type']['shape']                  = {'default':['time']}
ncspec['variables']['surface_type']['fill_value']             = {'default':127}
ncspec['variables']['surface_type']['zlib']                   = {'default':True}
ncspec['variables']['surface_type']['complevel']              = {'default':1}
ncspec['variables']['surface_type']['shuffle']                = {'default':True}
ncspec['variables']['surface_type']['data']                   = {'src':'data/surface_type'}
ncspec['variables']['surface_type']['attrs'] = {}
ncspec['variables']['surface_type']['attrs']['flag_values']   = {'default':[0, 1, 2, 3]}
ncspec['variables']['surface_type']['attrs']['flag_meanings'] = {'default':'ocean lake_enclosed_sea ice land'}
ncspec['variables']['surface_type']['attrs']['long_name']     = {'default':'surface type'}
ncspec['variables']['surface_type']['attrs']['coordinates']   = {'default':['lon, lat']}
ncspec['variables']['surface_type']['attrs']['comment']       = {'default':'Computed using a DTM2000 file: 0 = open oceans or semi-enclosed seas; 1 = enclosed seas or lakes; 2 = continental ice; 3 = land. See SARAL User Handbook'}

ncspec['variables']['wind_speed_alt']   = {}
ncspec['variables']['wind_speed_alt']['fmt']                    = {'default':'f4'}
ncspec['variables']['wind_speed_alt']['shape']                  = {'default':['time']}
ncspec['variables']['wind_speed_alt']['fill_value']             = {'default':-999.0}
ncspec['variables']['wind_speed_alt']['zlib']                   = {'default':True}
ncspec['variables']['wind_speed_alt']['complevel']              = {'default':1}
ncspec['variables']['wind_speed_alt']['shuffle']                = {'default':True}
ncspec['variables']['wind_speed_alt']['data']                   = {'src':'data/wind_speed_alt', 'mapscalefac':{-999:{'scale':.01}}, 'map':{32767:-999}, 'fmt':'f4'}
ncspec['variables']['wind_speed_alt']['attrs'] = {}
ncspec['variables']['wind_speed_alt']['attrs']['long_name']     = {'default':'altimeter wind speed'}
ncspec['variables']['wind_speed_alt']['attrs']['standard_name'] = {'default':'wind_speed'}
ncspec['variables']['wind_speed_alt']['attrs']['source']        = {'default':'John Lillibridge and co [2013] - One and Two-Dimensional Wind Speed Models for Ka-band Altimetry - JTECH-D-13-00167.1'}
ncspec['variables']['wind_speed_alt']['attrs']['units']         = {'default':'m/s'}
ncspec['variables']['wind_speed_alt']['attrs']['coordinates']   = {'default':['lon, lat']}
ncspec['variables']['wind_speed_alt']['attrs']['comment']       = {'default':'Should not be used over land. See SARAL User Handbook'}

ncspec['variables']['band_id']   = {}
ncspec['variables']['band_id']['fmt']                    = {'default':'i1'}
ncspec['variables']['band_id']['shape']                  = {'default':['dmw_band']}
ncspec['variables']['band_id']['zlib']                   = {'default':True}
ncspec['variables']['band_id']['complevel']              = {'default':1}
ncspec['variables']['band_id']['shuffle']                = {'default':True}
ncspec['variables']['band_id']['data']                   = {'default':12}
ncspec['variables']['band_id']['attrs'] = {}
ncspec['variables']['band_id']['attrs']['long_name']     = {'default':'Generic band identifier for use in AWIPS DMW plug-in'}
ncspec['variables']['band_id']['attrs']['units']         = {'default':'1'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'altika', 'fields':['file','node']}

job['modclass'] = {'module':'nc_convert','class':'NCCon','args':{'ncspec':ncspec}}

