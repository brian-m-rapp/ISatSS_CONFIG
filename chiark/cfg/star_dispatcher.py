# dispatcher configuration for h8 data flow

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
job['name']     = 'star_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'star_dispatch_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']['slab']   = {'node':71, 'enabled':True,'fields':['file','node'],'prefix':'h8_slab'}

job['data'] = {}
job['data']['h8slab']                 = {}
job['data']['h8slab']['location']       = {'node':72}
job['data']['h8slab']['aging']          = {'window':3600, 'mode':'creationtime'}
job['data']['h8slab']['method']         = {'technique':'stage', 'path':'incinerator'}
job['data']['h8slab']['activeonly']     = True                                                            # check pidfile
job['data']['h8slab']['schedule']       = {'interval':600}

job['data']['infoslab']                = {}
job['data']['infoslab']['location']    = {'node':71}
job['data']['infoslab']['filter']      = {'type':'starts','test':job['notifications']['slab']['prefix']}
job['data']['infoslab']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['infoslab']['method']      = {'technique':'inplace'}
job['data']['infoslab']['activeonly']  = True
job['data']['infoslab']['schedule']    = {'interval':600}

job['data']['slabledger']                = {}
job['data']['slabledger']['location']    = {'node':73}
job['data']['slabledger']['aging']       = {'window':86400*10, 'mode':'creationtime'}
job['data']['slabledger']['method']      = {'technique':'inplace'}
job['data']['slabledger']['activeonly']  = True
job['data']['slabledger']['schedule']    = {'interval':600}

job['data']['log']                    = {}
job['data']['log']['location']        = {'node':1}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 5
job['cntl_node']        = 70
job['max_sleep']        = 10
job['work_time']        = 60

job['sources'] = {}
job['sources']['star'] = {'protocol':'AFTP', 'host':'ftp.star.nesdis.noaa.gov', 'authid':3, 'timeout':10, 'retry':10,'paths':{},'sessions':1}
ahiargs = {'window':3600,'scenes':['FLDK'],'bands':['B03','B07','B08','B09','B10','B13','B14'],'cyclecount':70}
ahiargs['target'] = {'data':job['data']['h8slab'],'notifications':job['notifications']}
ahiargs['ledger'] = {'node':job['data']['slabledger']['location']['node'],'name':'star_status'}
job['sources']['star']['paths']['ahi'] = {'path':'AHI','dirs':{},'special':{'module':'starserver','class':'AHIPuller','args':ahiargs}}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include

