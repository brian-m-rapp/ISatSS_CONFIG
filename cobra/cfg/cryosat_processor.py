# Frank configuration for Jason2 altimetry product

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
job['name']     = 'cryosat_processor'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'cryosat_processor_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':124}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':125}
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

job['input_type']           = {'type':'infofile','node':122,'delete_file':False, 'delete_info':False}

job['watcher_timeout']      = 1000
job['files_per_cycle']      = 50

ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'default':'cryosat2', 'delimiter':'_'})
ncspec['namedef'].append({'src':'indata/filetime', 'delimiter':'.nc'})

ncspec['dimensions'] = {}
ncspec['dimensions']['data_rows'] = {'src':'indata/data_rows'}
ncspec['dimensions']['dmw_band']  = {'default':1}

ncspec['globalmeta'] = {}
ncspec['globalmeta']['mission_name']        = {'default':'CryoSat-2'}
ncspec['globalmeta']['production_site']     = {'src':'indata/production_site'}
ncspec['globalmeta']['coverage_start_time'] = {'src':'indata/start_time', 'timeformat':'%Y-%m-%dT%H:%M:%S'}
ncspec['globalmeta']['coverage_end_time']   = {'src':'indata/end_time', 'timeformat':'%Y-%m-%dT%H:%M:%S'}

ncspec['variables']   = {}
ncspec['variables']['lat']   = {}
ncspec['variables']['lat']['fmt']                    = {'default':'f4'}
ncspec['variables']['lat']['shape']                  = {'default':['data_rows']}
ncspec['variables']['lat']['zlib']                   = {'default':True}
ncspec['variables']['lat']['complevel']              = {'default':1}
ncspec['variables']['lat']['shuffle']                = {'default':True}
ncspec['variables']['lat']['data']                   = {'src':'data/lat'}
ncspec['variables']['lat']['attrs'] = {}
ncspec['variables']['lat']['attrs']['long_name']     = {'default':'latitude'}
ncspec['variables']['lat']['attrs']['units']         = {'default':'degrees_north'}

ncspec['variables']['lon']   = {}
ncspec['variables']['lon']['fmt']                    = {'default':'f4'}
ncspec['variables']['lon']['shape']                  = {'default':['data_rows']}
ncspec['variables']['lon']['zlib']                   = {'default':True}
ncspec['variables']['lon']['complevel']              = {'default':1}
ncspec['variables']['lon']['shuffle']                = {'default':True}
ncspec['variables']['lon']['data']                   = {'src':'data/lon'}
ncspec['variables']['lon']['attrs'] = {}
ncspec['variables']['lon']['attrs']['long_name']     = {'default':'longitude'}
ncspec['variables']['lon']['attrs']['units']         = {'default':'degrees_east'}

ncspec['variables']['time']   = {}
ncspec['variables']['time']['fmt']                    = {'default':'f8'}
ncspec['variables']['time']['shape']                  = {'default':['data_rows']}
ncspec['variables']['time']['zlib']                   = {'default':True}
ncspec['variables']['time']['complevel']              = {'default':1}
ncspec['variables']['time']['shuffle']                = {'default':True}
ncspec['variables']['time']['data']                   = {'src':'data/time'}
ncspec['variables']['time']['attrs'] = {}
ncspec['variables']['time']['attrs']['standard_name'] = {'default':'time'}
ncspec['variables']['time']['attrs']['long_name']     = {'default':'CryoSat-2 scan start time, seconds since 1970-01-01 00:00:00'}
ncspec['variables']['time']['attrs']['units']         = {'default':'s'}

ncspec['variables']['swh']   = {}
ncspec['variables']['swh']['fmt']                    = {'default':'f4'}
ncspec['variables']['swh']['shape']                  = {'default':['data_rows']}
#ncspec['variables']['swh']['fill_value']             = {'default':32767}
ncspec['variables']['swh']['zlib']                   = {'default':True}
ncspec['variables']['swh']['complevel']              = {'default':1}
ncspec['variables']['swh']['shuffle']                = {'default':True}
ncspec['variables']['swh']['data']                   = {'src':'data/swh'}
ncspec['variables']['swh']['attrs'] = {}
ncspec['variables']['swh']['attrs']['units']         = {'default':'m'}
ncspec['variables']['swh']['attrs']['standard_name'] = {'default':'swh'}
ncspec['variables']['swh']['attrs']['long_name']     = {'default':'Significant wave height'}

ncspec['variables']['wspd']   = {}
ncspec['variables']['wspd']['fmt']                    = {'default':'f4'}
ncspec['variables']['wspd']['shape']                  = {'default':['data_rows']}
ncspec['variables']['wspd']['zlib']                   = {'default':True}
ncspec['variables']['wspd']['complevel']              = {'default':1}
ncspec['variables']['wspd']['shuffle']                = {'default':True}
ncspec['variables']['wspd']['data']                   = {'src':'data/wspd'}
ncspec['variables']['wspd']['attrs'] = {}
ncspec['variables']['wspd']['attrs']['long_name']     = {'default':'Wind speed'}
ncspec['variables']['wspd']['attrs']['units']         = {'default':'m/s'}

ncspec['variables']['DQF']   = {}
ncspec['variables']['DQF']['fmt']                    = {'default':'i1'}
ncspec['variables']['DQF']['shape']                  = {'default':['data_rows']}
ncspec['variables']['DQF']['fill_value']             = {'default':-1}
ncspec['variables']['DQF']['zlib']                   = {'default':True}
ncspec['variables']['DQF']['complevel']              = {'default':1}
ncspec['variables']['DQF']['shuffle']                = {'default':True}
ncspec['variables']['DQF']['data']                   = {'default':0}
ncspec['variables']['DQF']['attrs'] = {}
ncspec['variables']['DQF']['attrs']['units']         = {'default':'1'}
ncspec['variables']['DQF']['attrs']['long_name']     = {'default':'quality flag for SWH (forced to 0)'}
ncspec['variables']['DQF']['attrs']['flag_values']   = {'default':[0,1]}
ncspec['variables']['DQF']['attrs']['flag_meanings'] = {'default':'good, bad'}

ncspec['variables']['band_id']   = {}
ncspec['variables']['band_id']['fmt']                    = {'default':'i1'}
ncspec['variables']['band_id']['shape']                  = {'default':['dmw_band']}
ncspec['variables']['band_id']['zlib']                   = {'default':True}
ncspec['variables']['band_id']['complevel']              = {'default':1}
ncspec['variables']['band_id']['shuffle']                = {'default':True}
ncspec['variables']['band_id']['data']                   = {'default':11}
ncspec['variables']['band_id']['attrs'] = {}
ncspec['variables']['band_id']['attrs']['long_name']     = {'default':'Generic band identifier for use in AWIPS DMW plug-in'}
ncspec['variables']['band_id']['attrs']['units']         = {'default':'1'}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'cryosat2', 'fields':['file','node']}

job['modclass'] = {'module':'cryosat_convert','class':'CryosatConvert','args':{'ncspec':ncspec}}
