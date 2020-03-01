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

try:
    import jobvarmod
    jobvars = jobvarmod.jobvars.copy()
except:
    jobvars = {}
    for parm in ['cntl','in','abiinfo','glminfo','archinfo','abidata','glmdata','archdata']:
        jobvars[parm] = 0

job = {}
job['name']     = 'ldm_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'ldm_dispatch_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']['abil1b']   = {'node':jobvars['abiinfo'], 'enabled':True,'fields':['file','node'],'prefix':'abil1b'}
job['notifications']['glml1b']   = {'node':jobvars['glminfo'], 'enabled':True,'fields':['file','node'],'prefix':'glml1b'}
job['notifications']['inarch']   = {'node':jobvars['archinfo'], 'enabled':True,'fields':['file','node'],'prefix':'inarch'}

job['data'] = {}
job['data']['prodabil1b']                  = {}
job['data']['prodabil1b']['location']      = {'node':jobvars['abidata']}
job['data']['prodabil1b']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['prodabil1b']['method']        = {'technique':'inplace'}
job['data']['prodabil1b']['activeonly']    = False
job['data']['prodabil1b']['schedule']      = {'interval':600}

job['data']['infoabil1b']                  = {}
job['data']['infoabil1b']['location']      = {'node':job['notifications']['abil1b']['node']}
job['data']['infoabil1b']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['infoabil1b']['method']        = {'technique':'inplace'}
job['data']['infoabil1b']['activeonly']    = False
job['data']['infoabil1b']['schedule']      = {'interval':600}

job['data']['prodglml1b']                  = {}
job['data']['prodglml1b']['location']      = {'node':jobvars['glmdata']}
job['data']['prodglml1b']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['prodglml1b']['method']        = {'technique':'inplace'}
job['data']['prodglml1b']['activeonly']    = False
job['data']['prodglml1b']['schedule']      = {'interval':600}

job['data']['infoglml1b']                  = {}
job['data']['infoglml1b']['location']      = {'node':job['notifications']['glml1b']['node']}
job['data']['infoglml1b']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['infoglml1b']['method']        = {'technique':'inplace'}
job['data']['infoglml1b']['activeonly']    = False
job['data']['infoglml1b']['schedule']      = {'interval':600}

job['data']['prodinarch']                  = {}
job['data']['prodinarch']['location']      = {'node':jobvars['archdata']}
job['data']['prodinarch']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['prodinarch']['method']        = {'technique':'inplace'}
job['data']['prodinarch']['activeonly']    = False
job['data']['prodinarch']['schedule']      = {'interval':600}

job['data']['infoinarch']                  = {}
job['data']['infoinarch']['location']      = {'node':job['notifications']['inarch']['node']}
job['data']['infoinarch']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['infoinarch']['method']        = {'technique':'inplace'}
job['data']['infoinarch']['activeonly']    = False
job['data']['infoinarch']['schedule']      = {'interval':600}

job['data']['log']                         = {}
job['data']['log']['location']             = {'node':job['log_node']}
job['data']['log']['aging']                = {'window':2,'mode':'count'}
job['data']['log']['archive']              = {'window':7,'mode':'count'}
job['data']['log']['roots']                = [job['log']]
job['data']['log']['method']               = {'technique':'inplace'}
job['data']['log']['schedule']             = {'interval':3600}
job['data']['log']['activeonly']           = True

job['loglevel']         = 5
job['cntl_node']        = jobvars['cntl']
job['max_sleep']        = 10
job['work_time']        = 60

abifiltdef = {'name':'GOES L1b SCMI', 'spec':[{'calc':'name Get _ABI-L1b Contains'}]}
glmfiltdef = {'name':'GOES L2 GLM',  'spec':[{'calc':'name Get _GLM-L2 Contains'}]}

job['sources'] = {}
job['sources']['ldm'] = {'protocol':'CP', 'paths':{}}
job['sources']['ldm']['paths']['dropzone'] = {'node':jobvars['in'],'files':{},'delete':True}
job['sources']['ldm']['paths']['dropzone']['files']['abil1b']  = {'retrieve':{},'filt':abifiltdef}
job['sources']['ldm']['paths']['dropzone']['files']['abil1b']['retrieve']['proc'] = {'enabled':True,'dataitem':'prodabil1b','notifications':['abil1b']}
job['sources']['ldm']['paths']['dropzone']['files']['abil1b']['retrieve']['arch'] = {'enabled':True,'dataitem':'prodinarch','notifications':['inarch'],'hardlink':'proc'}
job['sources']['ldm']['paths']['dropzone']['files']['glml1b']  = {'retrieve':{},'filt':glmfiltdef}
job['sources']['ldm']['paths']['dropzone']['files']['glml1b']['retrieve']['proc'] = {'enabled':True,'dataitem':'prodglml1b','notifications':['glml1b']}
job['sources']['ldm']['paths']['dropzone']['files']['glml1b']['retrieve']['arch'] = {'enabled':True,'dataitem':'prodinarch','notifications':['inarch'],'hardlink':'proc'}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include

