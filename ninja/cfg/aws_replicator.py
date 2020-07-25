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
for parm in ['cntl','indata']:
      if parm not in jobvars:
          jobvars[parm] = 0

if 'loglvl' not in jobvars:
    jobvars['loglvl'] = 5

if 'traceprint' not in jobvars:
    jobvars['traceprint'] = 'disabled'

job                = {}
job['name']        = 'aws_replicator'
job['cmd']         = 'mojo'
job['class']       = 'Mojo'
job['log']         = 'aws_replicator_log'
job['log_id']      = 1

job['cache_check'] = 300
job['cache_life']  = 86400
job['cntl_node']   = jobvars['cntl']
job['log_level']   = jobvars['loglvl']
job['maxopen']     = 500
job['pause_empty'] = 5
job['qlimit']      = 500
job['traceprint']  = jobvars['traceprint']

job['input_type']  = {}
job['input_type']['type']          = 'awsqueue'
job['input_type']['name']          = 'NewGOES16ObjectQueue_Test2'
job['input_type']['data_location'] = 'local'
job['input_type']['data_node']     = jobvars['indata']
job['input_type']['aws_region']    = 'us-east-1'
job['input_type']['authid']        = 4
job['input_type']['topic_arn']     = 'arn:aws:sns:us-east-1:123901341784:NewGOES16Object'
job['input_type']['window']        = 3600
job['input_type']['allow_dups']    = False
job['input_type']['delete_file']   = False
job['input_type']['create_info']   = False
job['input_type']['input_filter']  = {'calc':'Get ABI-L1b- StartsWith'}
job['input_type']['on_exit']       = {'delete_queue':False, 'unsubscribe':True}

job['notifications']   = {}

job['data']                              = {}

job['data']['log']                       = {}
job['data']['log']['location']           = {'node':job['log_id']}
job['data']['log']['itemlist']           = {'calc':'1 NestedList'}
job['data']['log']['groupfilter']        = {'calc':job['log']+' _  + GetUser + \- + GetHost + 2 7 ArchFilt'}
job['data']['log']['schedule']           = {'calc':'Now 3600 +'}

pargs = {}
pargs['outputs'] = {}
pargs['outputs']['g16abi']  = {}
pargs['outputs']['g16abi']['target']        = 'abiarchg16'
pargs['outputs']['g16abi']['method']        = 'copy'
pathspec = 'file Get Basename _ 3 Extract 1 11 Substr %Y%j%H%M %Y%m%d%H TimeReformat '
pargs['outputs']['g16abi']['path']          = {'calc':pathspec}
pargs['outputs']['g16abi']['filter']        = {'calc':'G16_ file Get Basename In _ABI- file Get Basename In *'}

pargs['outputs']['g17abi']  = {}
pargs['outputs']['g17abi']['target']        = 'abiarchg17'
pargs['outputs']['g17abi']['method']        = 'copy'
pargs['outputs']['g17abi']['filter']        = {'calc':'G17_ file Get Basename In _ABI- file Get Basename In *'}
pargs['outputs']['g17abi']['path']          = {'calc':pathspec}

pargs['outputs']['g16glm']  = {}
pargs['outputs']['g16glm']['target']        = 'glmarchg16'
pargs['outputs']['g16glm']['method']        = 'copy'
pargs['outputs']['g16glm']['filter']        = {'calc':'G16_ file Get Basename In _GLM- file Get Basename In *'}
pargs['outputs']['g16glm']['path']          = {'calc':pathspec}

pargs['outputs']['g17glm']  = {}
pargs['outputs']['g17glm']['target']        = 'glmarchg17'
pargs['outputs']['g17glm']['method']        = 'copy'
pargs['outputs']['g17glm']['filter']        = {'calc':'G17_ file Get Basename In _GLM- file Get Basename In *'}
pargs['outputs']['g17glm']['path']          = {'calc':pathspec}

job['modclass']          = {'module':'mm_replicator','class':'Replicator','args':pargs}
job['watcher_timeout']   = 1000
job['files_per_cycle']   = 50

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include
