# dispatcher configuration for big data project goes-r data

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
for parm in ['cntl','indata','abidata','abiinfo','glmdata','glminfo']:
      if parm not in jobvars:
          jobvars[parm] = 0

if 'loglvl' not in jobvars:
    jobvars['loglvl'] = 5

if 'traceprint' not in jobvars:
    jobvars['traceprint'] = 'disabled'

job = {}
job['name']       = 'g17_replicator'
job['cmd']        = 'mojo'
job['class']      = 'Mojo'
job['log']        = 'g17_replicator_log'
job['log_node']   = 1
job['loglevel']   = jobvars['loglvl']
job['cntl_node']  = jobvars['cntl']
job['traceprint'] = jobvars['traceprint']

job['input_type']  = {}
job['input_type']['type']          = 'awsqueue'
job['input_type']['name']          = 'BMR_ISatSS_GOES17_Queue'
job['input_type']['data_location'] = 'local'
job['input_type']['data_node']     = jobvars['indata']
job['input_type']['aws_region']    = 'us-east-1'
job['input_type']['authid']        = 4
job['input_type']['topic_arn']     = 'arn:aws:sns:us-east-1:123901341784:NewGOES17Object'
job['input_type']['window']        = 3600
job['input_type']['file_retries']  = 400
job['input_type']['suppress_dups'] = True
job['input_type']['delete_file']   = False
job['input_type']['create_info']   = False
job['input_type']['input_filter']  = {'calc':'Get ABI-L1b-Rad StartsWith Get GLM-L2-LCFA StartsWith +'}
job['input_type']['on_exit']       = {'delete_queue':False, 'unsubscribe':True}

job['notifications']   = {}
job['notifications']['abi']     = {'node':jobvars['abiinfo'],  'enabled':True, 'prefix':'abi'}
job['notifications']['glm']     = {'node':jobvars['glminfo'],  'enabled':True, 'prefix':'glm'}

job['data'] = {}

job['data']['log']                 = {}
job['data']['log']['location']    = {'node':job['log_node']}
job['data']['log']['itemlist']    = {'calc':'1 NestedList'}
job['data']['log']['groupfilter'] = {'calc':job['log']+' _  + GetUser + \- + GetHost + 2 7 ArchFilt'}
job['data']['log']['schedule']    = {'calc':'Now 3600 +'}

job['data']['abiinfo']                = {}
job['data']['abiinfo']['location']    = {'node':jobvars['abiinfo']}

job['data']['abidata']                = {}
job['data']['abidata']['location']    = {'node':jobvars['abidata']}

job['data']['glminfo']                = {}
job['data']['glminfo']['location']    = {'node':jobvars['glminfo']}

job['data']['glmdata']                = {}
job['data']['glmdata']['location']    = {'node':jobvars['glmdata']}

pargs = {}
pargs['outputs'] = {}
pargs['outputs']['abi'] = {}
pargs['outputs']['abi']['target']       = 'abidata'
pargs['outputs']['abi']['method']       = 'copy'
pargs['outputs']['abi']['notification'] = 'abi'
pargs['outputs']['abi']['filter']       = {'calc':'file Get Basename _ABI- Contains'}

pargs['outputs']['glm'] = {}
pargs['outputs']['glm']['target']       = 'glmdata'
pargs['outputs']['glm']['method']       = 'copy'
pargs['outputs']['glm']['notification'] = 'glm'
pargs['outputs']['glm']['filter']       = {'calc':'file Get Basename _GLM- Contains'}

job['modclass']          = {'module':'mm_replicator', 'class':'Replicator', 'args':pargs}
job['watcher_timeout']   = 1000
job['files_per_cycle']   = 50

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}   #or include

