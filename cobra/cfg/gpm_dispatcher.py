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
job['name']     = 'gpm_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'gpm_dispatch_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']['gpm']   = {'node':101, 'enabled':True, 'fields':['file', 'node'], 'prefix':'gpm'}

job['data'] = {}
job['data']['afiles']                 = {}
job['data']['afiles']['location']       = {'node':102}
job['data']['afiles']['aging']          = {'window':3600, 'mode':'creationtime'}
job['data']['afiles']['method']         = {'technique':'stage', 'path':'incinerator'}
job['data']['afiles']['activeonly']     = True                                                            # check pidfile
job['data']['afiles']['schedule']       = {'interval':600}

job['data']['aledger']                = {}
job['data']['aledger']['location']    = {'node':61}
job['data']['aledger']['aging']       = {'window':86400*2, 'mode':'creationtime'}
job['data']['aledger']['method']      = {'technique':'inplace'}
job['data']['aledger']['activeonly']  = True
job['data']['aledger']['schedule']    = {'interval':600}

job['data']['log']                    = {}
job['data']['log']['location']        = {'node':1}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 5
job['cntl_node']        = 100
job['max_sleep']        = 10
job['work_time']        = 60

job['sources'] = {}
job['sources']['satepsanone'] =  {'protocol':'HTTPS', 'host':'satepsanone.nesdis.noaa.gov', 'timeout':10, 'retry':10,'paths':{},'sessions':1}

gpm_args = {'window':86400}
gpm_args['target'] = {'data':job['data']['afiles'], 'notifications':job['notifications']}
gpm_args['ledger'] = {'node':job['data']['aledger']['location']['node'],'name':job['name']+'.ledger'}
gpm_args['filter'] = {'filt':'substring','target':'name','startswith':'1B.GPM.GMI.','name':'GPM GIM imagery'}

job['sources']['satepsanone']['paths']['gpm'] = {'path':'/pub/product/gpm/gmi/L1B', 'dirs':{}, 'special':{}}
job['sources']['satepsanone']['paths']['gpm']['special'] = {'module':'satepsanone_puller','class':'FilePuller','args':gpm_args}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include
