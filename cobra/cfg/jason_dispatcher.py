# dispatcher configuration for remote ASCAT file retrieval from NHC 

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
job['name']     = 'jason_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'jason_dispatch_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']['jason']   = {'node':97, 'enabled':True, 'fields':['file', 'node'], 'prefix':'jason'}

job['data'] = {}
job['data']['jfiles']                 = {}
job['data']['jfiles']['location']       = {'node':96}
job['data']['jfiles']['aging']          = {'window':3600, 'mode':'creationtime'}
job['data']['jfiles']['method']         = {'technique':'stage', 'path':'incinerator'}
job['data']['jfiles']['activeonly']     = True                                                            # check pidfile
job['data']['jfiles']['schedule']       = {'interval':600}

job['data']['jledger']                = {}
job['data']['jledger']['location']    = {'node':61}
job['data']['jledger']['aging']       = {'window':86400*10, 'mode':'creationtime'}
job['data']['jledger']['method']      = {'technique':'inplace'}
job['data']['jledger']['activeonly']  = True
job['data']['jledger']['schedule']    = {'interval':600}

job['data']['log']                    = {}
job['data']['log']['location']        = {'node':1}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 5
job['cntl_node']        = 95
job['max_sleep']        = 10
job['work_time']        = 60

job['sources'] = {}
job['sources']['nodc'] =  {'protocol':'FTP', 'host':'ftp.nodc.noaa.gov', 'authid':2, 'timeout':10, 'retry':10,'paths':{},'sessions':1}

jason2_args = {'window':86400, 'cyclecount':None, 'date_from':'stamp', 'date_format':None}
jason2_args['target'] = {'data':job['data']['jfiles'], 'notifications':job['notifications']}
jason2_args['ledger'] = {'node':job['data']['jledger']['location']['node'], 'name':'jason2.ledger'}
jason3_args = {'window':86400, 'cyclecount':None}
jason3_args['target'] = {'data':job['data']['jfiles'], 'notifications':job['notifications']}
jason3_args['ledger'] = {'node':job['data']['jledger']['location']['node'], 'name':'jason3.ledger'}
job['sources']['nodc']['paths']['jason2'] = {'path':'/pub/data.nodc/jason2/ogdr/ogdr', 'dirs':{}, 'special':{}}
job['sources']['nodc']['paths']['jason2']['special'] = {'module':'pull_subdirs', 'class':'SubDirPuller', 'args':jason2_args}
job['sources']['nodc']['paths']['jason3'] = {'path':'/pub/data.nodc/jason3/ogdr/ogdr', 'dirs':{}, 'special':{}}
job['sources']['nodc']['paths']['jason3']['special'] = {'module':'pull_subdirs', 'class':'SubDirPuller', 'args':jason3_args}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include
