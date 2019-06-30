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

job = {}
job['name']     = 'sentinel_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'sentinel_dispatcher_log'
job['log_node'] = 1

job['notifications']   = {}
job['notifications']['sentinel']   = {'node':142, 'enabled':True, 'fields':['file', 'node'], 'prefix':'sentinel'}

job['data'] = {}
job['data']['sentinel_files']                = {}
job['data']['sentinel_files']['location']    = {'node':141}
job['data']['sentinel_files']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['sentinel_files']['method']      = {'technique':'stage', 'path':'incinerator'}
job['data']['sentinel_files']['activeonly']  = True                                                            # check pidfile
job['data']['sentinel_files']['schedule']    = {'interval':600}

job['data']['sentinel_ledger']               = {}
job['data']['sentinel_ledger']['location']   = {'node':61}
job['data']['sentinel_ledger']['aging']      = {'window':86400*10, 'mode':'creationtime'}
job['data']['sentinel_ledger']['method']     = {'technique':'inplace'}
job['data']['sentinel_ledger']['activeonly'] = True
job['data']['sentinel_ledger']['schedule']   = {'interval':600}

job['data']['log']                     = {}
job['data']['log']['location']         = {'node':1}
job['data']['log']['aging']            = {'window':2,'mode':'count'}
job['data']['log']['archive']          = {'window':7,'mode':'count'}
job['data']['log']['roots']            = [job['log']]
job['data']['log']['method']           = {'technique':'inplace'}
job['data']['log']['schedule']         = {'interval':3600}
job['data']['log']['activeonly']       = True

job['loglevel']         = 5
job['cntl_node']        = 140
job['max_sleep']        = 10
job['work_time']        = 60

job['sources'] = {}
job['sources']['star'] =  {'protocol':'FTP', 'host':'ftp.star.nesdis.noaa.gov', 'timeout':10, 'retry':10,'paths':{},'sessions':1}

sentinel3A_args = {'window':7200, 'cyclecount':40}
sentinel3A_args['target']  = {'data':job['data']['sentinel_files'], 'notifications':job['notifications']}
sentinel3A_args['ledger']  = {'node':job['data']['sentinel_ledger']['location']['node'],'name':'sentinel3A.ledger'}
sentinel3A_args['extract'] = {'method':'tar', 'delete_archive':True, 'files':[{'dirname_is_sourcename':True, 'add_dname_to_fname':True, 'filename':{'is':'standard_measurement.nc'}}]}
job['sources']['star']['paths']['sentinel3A'] = {'path':'/pub/socd3/coastwatch/sral/L2', 'dirs':{}, 'special':{}, 'manifest':{}}
manifest3A_desc = {'name':'S3A_SR_2_WAT_NRT_manifest', 'node':61, 'fields':{'filename':{'index':0}, 'date':{'index':1, 'format':'%Y-%m-%d'}, 'time':{'index':2, 'format':'%H:%M:%S'}}}
job['sources']['star']['paths']['sentinel3A']['manifest']['sentinel'] = manifest3A_desc
#job['sources']['star']['paths']['sentinel3A']['decompress'] = {'method':None}
job['sources']['star']['paths']['sentinel3A']['special'] = {'module':'im_file_retriever','class':'FilePuller','args':sentinel3A_args}

sentinel3B_args = {'window':7200, 'cyclecount':40}
sentinel3B_args['target']  = {'data':job['data']['sentinel_files'], 'notifications':job['notifications']}
sentinel3B_args['ledger']  = {'node':job['data']['sentinel_ledger']['location']['node'],'name':'sentinel3B.ledger'}
sentinel3B_args['extract'] = {'method':'tar', 'delete_archive':True, 'files':[{'dirname_is_sourcename':True, 'add_dname_to_fname':True, 'filename':{'is':'standard_measurement.nc'}}]}
job['sources']['star']['paths']['sentinel3B'] = {'path':'/pub/socd3/coastwatch/sral/s3b/L2', 'dirs':{}, 'special':{}, 'manifest':{}}
manifest3B_desc = {'name':'S3B_SR_2_WAT_NRT_manifest', 'node':61, 'fields':{'filename':{'index':0}, 'date':{'index':1, 'format':'%Y-%m-%d'}, 'time':{'index':2, 'format':'%H:%M:%S'}}}
job['sources']['star']['paths']['sentinel3B']['manifest']['sentinel'] = manifest3B_desc
#job['sources']['star']['paths']['sentinel3B']['decompress'] = {'method':None}
job['sources']['star']['paths']['sentinel3B']['special'] = {'module':'im_file_retriever','class':'FilePuller','args':sentinel3B_args}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include
