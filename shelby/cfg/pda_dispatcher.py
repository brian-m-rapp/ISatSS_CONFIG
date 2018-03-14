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
job['name']     = 'pda_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'pda_dispatch_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']['slab']   = {'node':21, 'enabled':True,'fields':['file','node'],'prefix':'h8_slab'}	# Need to modify

job['data'] = {}	# Need to modify
job['data']['h8slab']                 = {}
job['data']['h8slab']['location']       = {'node':43}
job['data']['h8slab']['aging']          = {'window':3600, 'mode':'creationtime'}
job['data']['h8slab']['method']         = {'technique':'stage', 'path':'incinerator'}
job['data']['h8slab']['activeonly']     = True                                                            # check pidfile
job['data']['h8slab']['schedule']       = {'interval':600}

job['data']['infoslab']                = {}
job['data']['infoslab']['location']    = {'node':21}
job['data']['infoslab']['filter']      = {'type':'starts','test':job['notifications']['slab']['prefix']}
job['data']['infoslab']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['infoslab']['method']      = {'technique':'inplace'}
job['data']['infoslab']['activeonly']  = True
job['data']['infoslab']['schedule']    = {'interval':600}

job['data']['log']                    = {}
job['data']['log']['location']        = {'node':job['log_node']}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 6
job['cntl_node']        = 20	# Need to modify
job['max_sleep']        = 10	# Need to modify
job['work_time']        = 60	# Need to modify

windsFilter = []
windsFilter.append({'criteria':'substring', 'requires':{'parms':{'contains':'metopa', 'endswith':'l2_winds-lite'}}})

ambigFilter = []
ambigFilter.append({'criteria':'substring', 'requires':{'parms':{'contains':'metopa', 'contains':'l2_winds-lite_ambiguity'}}})

job['sources'] = {}
job['sources']['pda'] = {'protocol':'FTPS', 'host':'140.90.190.143', 'authid':1, 'timeout':30, 'paths':{}, 'sessions':1}
job['sources']['pda']['paths']['ascat'] = {'path':'/PDAFileLinks/GLOBAL/ASCAT'}

job['sources']['pda']['paths']['ascat']['files'] = {}
job['sources']['pda']['paths']['ascat']['files']['winds'] = {'filt':windsFilter}
job['sources']['pda']['paths']['ascat']['files']['ambig'] = {'filt':ambigFilter}

"""
slabcyclefilt = []	# Need to modify
slabcyclefilt.append({'criteria':'closeout'})
slabcyclefilt.append({'criteria':'age','method':'tstring','parms':{'tfmt':'%Y%m%d_%H%M'},'age':3600,'closeout_on_fail':True})

slabfilt = []	# Need to modify
slabfilt.append({'criteria':'substring', 'requires':{'parms':{'endswith':'.bz2','contains':'FLDK'},'closeout_on_fail':False},'exclude':{'parms':{'endswith':'.sha256'},'closeout_on_fail':True}})
slabfilt.append({'criteria':'trigger', 'endswith':'.x'})

job['sources']['star'] = {'protocol':'AFTP', 'host':'ftp.star.nesdis.noaa.gov', 'authid':1, 'timeout':30, 'paths':{},'ledger':{'node':23,'name':'star_status'},'sessions':1}
job['sources']['star']['paths']['ahi'] = {'path':'AHI', 'dirs':{}}
job['sources']['star']['paths']['ahi']['dirs']['slabcycle'] = {'filt':slabcyclefilt,'pathdef':'slabcycle'}
job['sources']['star']['paths']['slabcycle'] = {'files':{},'closeout':[]}
job['sources']['star']['paths']['slabcycle']['files']['slabfile'] = {'filt':slabfilt}
job['sources']['star']['paths']['slabcycle']['files']['slabfile']['notifications'] = ['slab']
job['sources']['star']['paths']['slabcycle']['files']['slabfile']['retrieve']      = 'prod'
job['sources']['star']['paths']['slabcycle']['files']['slabfile']['delete']        = False
job['sources']['star']['paths']['slabcycle']['files']['slabfile']['trigger']       = {'defn':{'endswith':'.x'},'delete':False,'retrieve':False}
job['sources']['star']['paths']['slabcycle']['closeout'].append({'criteria':'count','count':320})
job['sources']['star']['paths']['slabcycle']['closeout'].append({'criteria':'age','method':'tstring','parms':{'tfmt':'%Y%m%d_%H%M'},'age':86400})
"""

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include

