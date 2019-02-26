"""
Config file for pulling Fog and Low Stratus (FLS) data from the NESDIS STAR 
FTP site.
"""
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
job['name']     = 'altika_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'altika_dispatcher_log'
job['log_node'] = 1

job['notifications']   = {}
job['notifications']['altika']   = {'node':132, 'enabled':True, 'fields':['file', 'node'], 'prefix':'altika'}

job['data'] = {}
job['data']['altfiles']                = {}
job['data']['altfiles']['location']    = {'node':131}
job['data']['altfiles']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['altfiles']['method']      = {'technique':'stage', 'path':'incinerator'}
job['data']['altfiles']['activeonly']  = True                                                            # check pidfile
job['data']['altfiles']['schedule']    = {'interval':600}

job['data']['altledger']               = {}
job['data']['altledger']['location']   = {'node':61}
job['data']['altledger']['aging']      = {'window':86400*10, 'mode':'creationtime'}
job['data']['altledger']['method']     = {'technique':'inplace'}
job['data']['altledger']['activeonly'] = True
job['data']['altledger']['schedule']   = {'interval':600}

job['data']['log']                     = {}
job['data']['log']['location']         = {'node':1}
job['data']['log']['aging']            = {'window':2,'mode':'count'}
job['data']['log']['archive']          = {'window':7,'mode':'count'}
job['data']['log']['roots']            = [job['log']]
job['data']['log']['method']           = {'technique':'inplace'}
job['data']['log']['schedule']         = {'interval':3600}
job['data']['log']['activeonly']       = True

job['loglevel']         = 5
job['cntl_node']        = 130
job['max_sleep']        = 10
job['work_time']        = 60

job['sources'] = {}
job['sources']['altika'] =  {'protocol':'FTP', 'host':'avisoftp.cnes.fr', 'timeout':10, 'retry':10,'paths':{},'sessions':1}
job['sources']['altika']['decompress'] = {'method':'byext'}

altika_args = {'window':43200, 'cyclecount':20}
altika_args['target'] = {'data':job['data']['altfiles'], 'notifications':job['notifications']}
altika_args['ledger'] = {'node':job['data']['altledger']['location']['node'],'name':job['name']+'.ledger'}
job['sources']['altika']['paths']['altika'] = {'path':'AVISO/pub/saral/ssha_ogdr_t', 'dirs':{}, 'special':{}}
job['sources']['altika']['paths']['altika']['special'] = {'module':'remote_puller','class':'FilePuller','args':altika_args}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include
