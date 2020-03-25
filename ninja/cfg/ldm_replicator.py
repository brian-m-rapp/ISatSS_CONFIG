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
    for parm in ['cntl','in','abiarch','glmarch']:
        jobvars[parm] = 0

job = {}
job['name']     = 'ldm_replicator'
job['cmd']      = 'mojo'
job['class']    = 'Mojo'
job['log']      = 'ldm_replicator_log'
job['log_node'] = 1


job['notifications']   = {}

job['data'] = {}
job['data']['abiarch']             = {}
job['data']['abiarch']['location'] = {'node':jobvars['abiarch']}
job['data']['abiarch']['aging']    = {'window':86400, 'mode':'elapsedname','fmt':'%Y%m%d%H'}
job['data']['abiarch']['method']   = {'technique':'stage','path':'isatss_incinerator'}
job['data']['abiarch']['schedule'] = {'interval':600}

job['data']['glmarch']             = {}
job['data']['glmarch']['location'] = {'node':jobvars['glmarch']}
job['data']['glmarch']['aging']    = {'window':86400, 'mode':'elapsedname','fmt':'%Y%m%d%H'}
job['data']['glmarch']['method']   = {'technique':'stage','path':'isatss_incinerator'}
job['data']['glmarch']['schedule'] = {'interval':600}

job['data']['log']                 = {}
job['data']['log']['location']     = {'node':job['log_node']}
job['data']['log']['aging']        = {'window':2,'mode':'count'}
job['data']['log']['archive']      = {'window':7,'mode':'count'}
job['data']['log']['roots']        = [job['log']]
job['data']['log']['method']       = {'technique':'inplace'}
job['data']['log']['schedule']     = {'interval':3600}
job['data']['log']['activeonly']   = True

job['loglevel']    = 5
job['cntl_node']   = jobvars['cntl']

job['input_type']  = {'type':'infofile','node':jobvars['in'],'delete_file':True, 'delete_info':True}

pargs = {}
pargs['outputs'] = {}
pargs['outputs']['abi'] = {}
pargs['outputs']['abi']['target'] = 'abiarch'
pargs['outputs']['abi']['method'] = 'copy'
pargs['outputs']['abi']['path']   = {'calc':'file Get Basename _ 3 Extract 1 9 Substr %Y%j%H %Y%m%d%H TimeReformat'}
pargs['outputs']['abi']['filter'] = {'calc':'file Get Basename _ABI- Contains'}

pargs['outputs']['glm'] = {}
pargs['outputs']['glm']['target'] = 'glmarch'
pargs['outputs']['glm']['method'] = 'copy'
pargs['outputs']['glm']['path']   = {'calc':'file Get Basename _ 3 Extract 1 9 Substr %Y%j%H %Y%m%d%H TimeReformat'}
pargs['outputs']['glm']['filter'] = {'calc':'file Get Basename _GLM- Contains'}

job['modclass']          = {'module':'mm_replicator','class':'Replicator','args':pargs}
job['watcher_timeout']   = 1000
job['files_per_cycle']   = 50

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include

