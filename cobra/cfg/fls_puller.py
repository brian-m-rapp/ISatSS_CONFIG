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
job['name']     = 'fls_puller'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'fls_puller_log'
job['log_node'] = 1

job['notifications']   = {}
job['notifications']['fls']   = {'node':54, 'enabled':True, 'fields':['file', 'node'], 'prefix':'fls'}

job['data'] = {}
job['data']['flsfiles']                = {}
job['data']['flsfiles']['location']    = {'node':86}
job['data']['flsfiles']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['flsfiles']['method']      = {'technique':'stage', 'path':'incinerator'}
job['data']['flsfiles']['activeonly']  = True                                                            # check pidfile
job['data']['flsfiles']['schedule']    = {'interval':600}

job['data']['flsledger']               = {}
job['data']['flsledger']['location']   = {'node':61}
job['data']['flsledger']['aging']      = {'window':86400*10, 'mode':'creationtime'}
job['data']['flsledger']['method']     = {'technique':'inplace'}
job['data']['flsledger']['activeonly'] = True
job['data']['flsledger']['schedule']   = {'interval':600}

job['data']['log']                     = {}
job['data']['log']['location']         = {'node':1}
job['data']['log']['aging']            = {'window':2,'mode':'count'}
job['data']['log']['archive']          = {'window':7,'mode':'count'}
job['data']['log']['roots']            = [job['log']]
job['data']['log']['method']           = {'technique':'inplace'}
job['data']['log']['schedule']         = {'interval':3600}
job['data']['log']['activeonly']       = True

job['loglevel']         = 6
job['cntl_node']        = 85
job['max_sleep']        = 10
job['work_time']        = 60

job['sources'] = {}
job['sources']['star'] =  {'protocol':'FTP', 'host':'ftp.star.nesdis.noaa.gov', 'timeout':10, 'retry':10,'paths':{},'sessions':1}

#fls_args = {'window':3600, 'cyclecount':10}
fls_args = {'window':2*86400, 'cyclecount':5}
fls_args['target'] = {'data':job['data']['flsfiles'], 'notifications':job['notifications']}
fls_args['ledger'] = {'node':job['data']['flsledger']['location']['node'],'name':'fls_status'}
job['sources']['star']['paths']['fls'] = {'path':'/pub/smcd/spb/kurtis.pinkney/goes16_fls/CONUS', 'dirs':{}, 'special':{}}
job['sources']['star']['paths']['fls']['special'] = {'module':'remote_puller','class':'FilePuller','args':fls_args}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include
