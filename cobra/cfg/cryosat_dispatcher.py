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
job['name']     = 'cryosat_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'cryosat_dispatcher_log'
job['log_node'] = 1

job['notifications']   = {}
job['notifications']['cryosat']   = {'node':122, 'enabled':True, 'fields':['file', 'node'], 'prefix':'cryosat'}

job['data'] = {}
job['data']['cryfiles']                = {}
job['data']['cryfiles']['location']    = {'node':121}
job['data']['cryfiles']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['cryfiles']['method']      = {'technique':'stage', 'path':'incinerator'}
job['data']['cryfiles']['activeonly']  = True                                                            # check pidfile
job['data']['cryfiles']['schedule']    = {'interval':600}

job['data']['cryledger']               = {}
job['data']['cryledger']['location']   = {'node':61}
job['data']['cryledger']['aging']      = {'window':86400*10, 'mode':'creationtime'}
job['data']['cryledger']['method']     = {'technique':'inplace'}
job['data']['cryledger']['activeonly'] = True
job['data']['cryledger']['schedule']   = {'interval':600}

job['data']['log']                     = {}
job['data']['log']['location']         = {'node':1}
job['data']['log']['aging']            = {'window':2,'mode':'count'}
job['data']['log']['archive']          = {'window':7,'mode':'count'}
job['data']['log']['roots']            = [job['log']]
job['data']['log']['method']           = {'technique':'inplace'}
job['data']['log']['schedule']         = {'interval':3600}
job['data']['log']['activeonly']       = True

job['loglevel']         = 5
job['cntl_node']        = 120
job['max_sleep']        = 10
job['work_time']        = 60

job['sources'] = {}
job['sources']['star'] =  {'protocol':'FTP', 'host':'ftp.star.nesdis.noaa.gov', 'timeout':10, 'retry':10,'paths':{},'sessions':1}

cryo_args = {'window':43200, 'cyclecount':20}
cryo_args['target'] = {'data':job['data']['cryfiles'], 'notifications':job['notifications']}
cryo_args['ledger'] = {'node':job['data']['cryledger']['location']['node'],'name':job['name']+'.ledger'}
job['sources']['star']['paths']['cryosat'] = {'path':'/pub/socd/lsa/johnl/c2', 'dirs':{}, 'special':{}}
job['sources']['star']['paths']['cryosat']['special'] = {'module':'im_file_retriever','class':'FilePuller','args':cryo_args}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include
