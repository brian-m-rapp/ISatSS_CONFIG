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
job['name']     = 'amsr2_ocean_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'amsr2_ocean_dispatcher_log'
job['log_node'] = 1

job['loglevel']         = 5
job['cntl_node']        = 240
job['max_sleep']        = 10
job['work_time']        = 60

job['data'] = {}
job['data']['log']                       = {}
job['data']['log']['location']           = {'node':job['log_node']}
job['data']['log']['aging']              = {'window':2,'mode':'count'}
job['data']['log']['archive']            = {'window':7,'mode':'count'}
job['data']['log']['roots']              = [job['log']]
job['data']['log']['method']             = {'technique':'inplace'}
job['data']['log']['schedule']           = {'interval':3600}
job['data']['log']['activeonly']         = True

job['data']['output'] = {}
job['data']['output']['location']     = {'node':242}
job['data']['output']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']       = {'technique':'inplace'}
job['data']['output']['activeonly']   = True
job['data']['output']['schedule']     = {'interval':600}

job['data']['info'] = {}
job['data']['info']['location']     = {'node':241}
job['data']['info']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['info']['method']       = {'technique':'inplace'}
job['data']['info']['activeonly']   = True
job['data']['info']['schedule']     = {'interval':600}

job['notifications']   = {}
job['notifications']['nhc']    = {'node':job['data']['info']['location']['node'], 'enabled':True, 'fields':['file','node'], 'prefix':'amsr2_'}

amsr2_filtdef = []
amsr2_filtdef.append({'filt':'substring', 'target':'name', 'startswith':'AMSR2-OCEAN', 'name':'AMSR2_OCEAN'})
amsr2_filtdef.append({'filt':'substring', 'target':'name', 'endswith':'.nc', 'name':'AMSR2_OCEAN'})

job['sources'] = {}
job['sources']['amsr2'] = {'protocol':'CP', 'paths':{}}
job['sources']['amsr2']['paths']['dropzone'] = {'node':247, 'files':{}, 'delete':True}
job['sources']['amsr2']['paths']['dropzone']['files']['amsr2']  = {'retrieve':{}, 'filt':amsr2_filtdef}
job['sources']['amsr2']['paths']['dropzone']['files']['amsr2']['retrieve']['nhc']  = {'enabled':True, 'dataitem':'output',  'notifications':['nhc']}

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['grb_fdco_summary']         = {'enabled':True, 'module':'agent99_grb', 'class':'GRBProgGen'}
job['monitor']['agents']['pmd_admin']                = {'enabled':True, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'lockout':1800, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}} #or include

