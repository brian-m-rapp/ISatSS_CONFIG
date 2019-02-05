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
job['name']     = 'gcom_puller'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'gcom_dispatch_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']['gcom']   = {'node':53, 'enabled':True, 'fields':['file', 'node'], 'prefix':'gcom'}

job['data'] = {}
job['data']['gfiles']                 = {}
job['data']['gfiles']['location']       = {'node':74}
job['data']['gfiles']['aging']          = {'window':3600, 'mode':'creationtime'}
job['data']['gfiles']['method']         = {'technique':'stage', 'path':'incinerator'}
job['data']['gfiles']['activeonly']     = True                                                            # check pidfile
job['data']['gfiles']['schedule']       = {'interval':600}

job['data']['gledger']                = {}
job['data']['gledger']['location']    = {'node':61}
job['data']['gledger']['aging']       = {'window':86400*2, 'mode':'creationtime'}
job['data']['gledger']['method']      = {'technique':'inplace'}
job['data']['gledger']['activeonly']  = True
job['data']['gledger']['schedule']    = {'interval':600}

job['data']['log']                    = {}
job['data']['log']['location']        = {'node':1}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 6
job['cntl_node']        = 70
job['max_sleep']        = 10
job['work_time']        = 60

job['sources'] = {}
job['sources']['satepsanone'] =  {'protocol':'HTTPS', 'host':'satepsanone.nesdis.noaa.gov', 'authid':0, 'timeout':10, 'retry':10,'paths':{},'sessions':1}
job['sources']['satepsanone']['decompress'] = 'byext'

gcom_args = {'window':86400}
gcom_args['target'] = {'data':job['data']['gfiles'], 'notifications':job['notifications']}
gcom_args['ledger'] = {'node':job['data']['gledger']['location']['node'],'name':job['name']+'.ledger'}
gcom_args['filter'] = {'filt':'substring','target':'name','startswith':'AMSR2-OCEAN','name':'AMSR2 Ocean Test'}

job['sources']['satepsanone']['paths']['gcom'] = {'path':'/pub/product/nde/amsr2/L2', 'dirs':{}, 'special':{}}
job['sources']['satepsanone']['paths']['gcom']['special'] = {'module':'satepsanone_puller','class':'FilePuller','args':gcom_args}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include
