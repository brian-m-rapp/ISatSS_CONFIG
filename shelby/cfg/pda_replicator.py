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
job['name']     = 'pda_replicator'
job['cmd']      = 'replicator'
job['class']    = 'Replicator'
job['log']      = 'pda_replicator_log'
job['log_node'] = 1


job['notifications']   = {}

job['data'] = {}
job['data']['winds'] = {}
job['data']['winds']['location']     = {'node':60}
job['data']['winds']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['winds']['method']       = {'technique':'inplace'}
job['data']['winds']['activeonly']   = True
job['data']['winds']['schedule']     = {'interval':600}

job['data']['log']                   = {}
job['data']['log']['location']       = {'node':job['log_node']}
job['data']['log']['aging']          = {'window':2,'mode':'count'}
job['data']['log']['archive']        = {'window':7,'mode':'count'}
job['data']['log']['roots']          = [job['log']]
job['data']['log']['method']         = {'technique':'inplace'}
job['data']['log']['schedule']       = {'interval':3600}
job['data']['log']['activeonly']     = True

job['loglevel']    = 5
job['cntl_node']   = 11

job['input_type']  = {'type':'infofile','node':59,'delete_file':True, 'delete_info':True}

datestr = []
datestr.append({'method':'extract_field','delimiter':'/','field':-1,'name':'basename','target':'file'})
datestr.append({'method':'extract_field','delimiter':'_','field':1,'start_char':0,'nchar':8,'name':'datestr'})

timestr = []
timestr.append({'method':'extract_field','delimiter':'/','field':-1,'name':'basename','target':'file'})
timestr.append({'method':'extract_field','delimiter':'_','field':2,'start_char':0,'nchar':4,'name':'datestr'})

instance = []
instance.append({'method':'extract_field','delimiter':'/','field':-1,'start_char':-1,'name':'instance','target':'file'})

job['outputs'] = {}
job['outputs']['winds'] = {'dataitem':'winds','filt':[], 'path':[], 'appendname': False}
job['outputs']['winds']['filt'].append({'filt':'substring', 'target':'file', 'contains':'ascat_',        'name':'contains ascat'})
job['outputs']['winds']['filt'].append({'filt':'substring', 'target':'file', 'contains':'metopa',        'name':'contains metopa'})
job['outputs']['winds']['filt'].append({'filt':'substring', 'target':'file', 'endswith':'l2_winds-lite', 'name':'endswith l2_winds-lite'})
job['outputs']['winds']['path'].append({'default':'ascata_hi/','name':'subdir'})
job['outputs']['winds']['path'].append({'target':'file','stack':datestr,'name':'date'})
job['outputs']['winds']['path'].append({'target':'file','stack':timestr,'name':'time'})
job['outputs']['winds']['path'].append({'default':'.ascat','name':'ext'})

job['outputs']['ambig'] = {'dataitem':'winds','filt':[], 'path':[], 'appendname': False}
job['outputs']['ambig']['filt'].append({'filt':'substring', 'target':'file', 'contains':'ascat_',         'name':'contains ascat'})
job['outputs']['ambig']['filt'].append({'filt':'substring', 'target':'file', 'contains':'metopa',         'name':'contains metopa'})
job['outputs']['ambig']['filt'].append({'filt':'substring', 'target':'file', 'contains':'lite_ambiguity', 'name':'contains lite_ambiguity'})
job['outputs']['ambig']['path'].append({'default':'ascata_hi_ambig','name':'dirprefix'})
job['outputs']['ambig']['path'].append({'target':'file','stack':instance,'name':'inst'})
job['outputs']['ambig']['path'].append({'default':'/','name':'dirchar'})
job['outputs']['ambig']['path'].append({'target':'file','stack':datestr, 'name':'date'})
job['outputs']['ambig']['path'].append({'target':'file','stack':timestr, 'name':'time'})
job['outputs']['ambig']['path'].append({'default':'.ascat','name':'ext'})

