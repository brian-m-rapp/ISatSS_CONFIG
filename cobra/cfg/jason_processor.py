# Frank configuration for Jason2 altimetry product

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
    Reformat/tailor jason2 nc4 files (as avail from PDA) into a format for the goes-r dmw
    plugin.  The purpose is to ingest the data into edex via the dmw table for access
    in cave using the point plot resource data, latter plots the values of wave height as text.
    Relies upon modification of im_ncfile.py modification: mapscalefac dictionary to multiply
    incoming data by the incoming data scale factor and add offset if applicable, whenever the i
    data in the array does not match the key in mapscalefac.

    These files do not flow over SBN, but can be found on PDA or anonymous ftp:
    ftp://ftp.nodc.noaa.gov/pub/data.nodc/jason2/ogdr/ogdr/
    example: JA2_OPN_2PdS311_254_20161215_195917_20161215_213728.nc
"""

job = {}
job['name']     = 'jason_processing'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'jason_processing_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':98}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':99}
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

job['cntl_node']            = 93

job['input_type']           = {'type':'infofile','node':92,'delete_file':False, 'delete_info':False}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

#inncf
ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'jason_napo','delimiter':'_'})
ncspec['namedef'].append({'src':'inncf/globalmeta/cycle_number','delimiter':'_'})
ncspec['namedef'].append({'src':'inncf/globalmeta/pass_number','delimiter':'.nc'})

ncspec['dimensions'] = {}
ncspec['dimensions']['time']        = {'src':'inncf/dimensions/time'}
ncspec['dimensions']['dmw_band']     = {'default':1}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['mission_name']                = {'src':'inncf/globalmeta/mission_name'}
ncspec['globalmeta']['first_meas_time']             = {'src':'inncf/globalmeta/first_meas_time'}
ncspec['globalmeta']['last_meas_time']              = {'src':'inncf/globalmeta/last_meas_time'}
ncspec['globalmeta']['production_site']             = {'default':'NAPO'}

ncspec['variables']   = {}
ncspec['variables']['lat']   = {}
ncspec['variables']['lat']['fmt']                    = {'default':'f8'}
ncspec['variables']['lat']['shape']                  = {'default':['time']}
ncspec['variables']['lat']['zlib']                   = {'default':True}
ncspec['variables']['lat']['complevel']              = {'default':1}
ncspec['variables']['lat']['shuffle']                = {'default':True}
ncspec['variables']['lat']['data']                   = {'src':'data/lat','mapscalefac':{-9.99e07:{'scale':1e-06}},'fmt':'f8'}
ncspec['variables']['lat']['attrs'] = {}
ncspec['variables']['lat']['attrs']['long_name']     = {'default':'latitude'}
ncspec['variables']['lat']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['lon']   = {}
ncspec['variables']['lon']['fmt']                    = {'default':'f8'}
ncspec['variables']['lon']['shape']                  = {'default':['time']}
ncspec['variables']['lon']['zlib']                   = {'default':True}
ncspec['variables']['lon']['complevel']              = {'default':1}
ncspec['variables']['lon']['shuffle']                = {'default':True}
ncspec['variables']['lon']['data']                   = {'src':'data/lon','mapscalefac':{-999.:{'scale':1e-06, 'longt180neg':True}},'fmt':'f8'}
ncspec['variables']['lon']['attrs'] = {}
ncspec['variables']['lon']['attrs']['long_name']     = {'default':'longitude'}
ncspec['variables']['lon']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['swh_ku']   = {}
ncspec['variables']['swh_ku']['fmt']                    = {'default':'f4'}
ncspec['variables']['swh_ku']['shape']                  = {'default':['time']}
#ncspec['variables']['swh_ku']['fill_value']             = {'default':-999.}
ncspec['variables']['swh_ku']['fill_value']             = {'default':32767}
ncspec['variables']['swh_ku']['zlib']                   = {'default':True}
ncspec['variables']['swh_ku']['complevel']              = {'default':1}
ncspec['variables']['swh_ku']['shuffle']                = {'default':True}
ncspec['variables']['swh_ku']['data']                   = {'src':'data/swh_ku','mapscalefac':{32767:{'scale':1e-03, 'offset':0}},'fmt':'f4'}
ncspec['variables']['swh_ku']['attrs'] = {}
ncspec['variables']['swh_ku']['attrs']['units']         = {'default':'m'}
ncspec['variables']['swh_ku']['attrs']['long_name']     = {'default':'Ku band corrected significant waveheight'}

ncspec['variables']['time']   = {}
ncspec['variables']['time']['fmt']                    = {'default':'f8'}
ncspec['variables']['time']['shape']                  = {'default':['time']}
ncspec['variables']['time']['zlib']                   = {'default':True}
ncspec['variables']['time']['complevel']              = {'default':1}
ncspec['variables']['time']['shuffle']                = {'default':True}
ncspec['variables']['time']['data']                   = {'src':'data/time'}
ncspec['variables']['time']['attrs'] = {}
ncspec['variables']['time']['attrs']['standard_name'] = {'default':'time'}
ncspec['variables']['time']['attrs']['long_name']     = {'default':'Jason scan start time, seconds since 2000-01-01 00:00:00'}
ncspec['variables']['time']['attrs']['units']         = {'default':'s'}

ncspec['variables']['DQF']   = {}
ncspec['variables']['DQF']['fmt']                    = {'default':'i1'}
ncspec['variables']['DQF']['shape']                  = {'default':['time']}
ncspec['variables']['DQF']['fill_value']             = {'default':-1}
ncspec['variables']['DQF']['zlib']                   = {'default':True}
ncspec['variables']['DQF']['complevel']              = {'default':1}
ncspec['variables']['DQF']['shuffle']                = {'default':True}
ncspec['variables']['DQF']['data']                   = {'src':'data/qual_alt_1hz_swh_ku'}
ncspec['variables']['DQF']['attrs'] = {}
ncspec['variables']['DQF']['attrs']['units']         = {'default':'1'}
ncspec['variables']['DQF']['attrs']['long_name']     = {'default':'quality flag for 1 Hz altimeter data: Ku band SWH'}
ncspec['variables']['DQF']['attrs']['flag_values']   = {'default':[0,1]}
ncspec['variables']['DQF']['attrs']['flag_meanings'] = {'default':'good, bad'}

ncspec['variables']['band_id']   = {}
ncspec['variables']['band_id']['fmt']                    = {'default':'i1'}
ncspec['variables']['band_id']['shape']                  = {'default':['dmw_band']}
ncspec['variables']['band_id']['zlib']                   = {'default':True}
ncspec['variables']['band_id']['complevel']              = {'default':1}
ncspec['variables']['band_id']['shuffle']                = {'default':True}
ncspec['variables']['band_id']['data']                   = {'default':10}
ncspec['variables']['band_id']['attrs'] = {}
ncspec['variables']['band_id']['attrs']['long_name']     = {'default':'Generic band identifier for use in AWIPS dmw plugin'}
ncspec['variables']['band_id']['attrs']['units']         = {'default':'1'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'jason', 'fields':['file','node']}

job['modclass'] = {'module':'nc_convert','class':'NCCon','args':{'ncspec':ncspec}}
