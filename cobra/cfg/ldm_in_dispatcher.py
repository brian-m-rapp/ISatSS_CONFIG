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
job['name']     = 'ldm_in_dispatcher'
job['cmd']      = 'dispatcher'
job['class']    = 'Dispatcher'
job['log']      = 'ldm_in_dispatch_log'
job['log_node'] = 1


job['notifications']   = {}
job['notifications']['grbl1b']   = {'node':37, 'enabled':True,'fields':['file','node'],'prefix':'grbl1b'}
job['notifications']['hcast']    = {'node':38, 'enabled':True,'fields':['file','node'],'prefix':'hcast'}
job['notifications']['ldmarch']  = {'node':42, 'enabled':True,'fields':['file','node'],'prefix':'ldmarch'}

job['data'] = {}
job['data']['prodgrbl1b']                  = {}
job['data']['prodgrbl1b']['location']      = {'node':15}
job['data']['prodgrbl1b']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['prodgrbl1b']['method']        = {'technique':'inplace'}
job['data']['prodgrbl1b']['activeonly']    = True                                                            # check pidfile
job['data']['prodgrbl1b']['schedule']      = {'interval':600}
job['data']['prodhcast']                   = {}
job['data']['prodhcast']['location']       = {'node':17}
job['data']['prodhcast']['aging']          = {'window':3600, 'mode':'creationtime'}
job['data']['prodhcast']['method']         = {'technique':'inplace'}
job['data']['prodhcast']['activeonly']     = True                                                            # check pidfile
job['data']['prodhcast']['schedule']       = {'interval':600}
job['data']['prodldmarch']                 = {}
job['data']['prodldmarch']['location']     = {'node':41}
job['data']['prodldmarch']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['prodldmarch']['method']       = {'technique':'inplace'}
job['data']['prodldmarch']['activeonly']   = True                                                            # check pidfile
job['data']['prodldmarch']['schedule']     = {'interval':600}

job['data']['infogrbl1b']                  = {}
job['data']['infogrbl1b']['location']      = {'node':37}
job['data']['infogrbl1b']['aging']         = {'window':3600, 'mode':'creationtime'}
job['data']['infogrbl1b']['method']        = {'technique':'inplace'}
job['data']['infogrbl1b']['activeonly']    = True                                                            # check pidfile
job['data']['infogrbl1b']['schedule']      = {'interval':600}
job['data']['infohcast']                   = {}
job['data']['infohcast']['location']       = {'node':38}
job['data']['infohcast']['aging']          = {'window':3600, 'mode':'creationtime'}
job['data']['infohcast']['method']         = {'technique':'inplace'}
job['data']['infohcast']['activeonly']     = True                                                            # check pidfile
job['data']['infohcast']['schedule']       = {'interval':600}
job['data']['infoldmarch']                 = {}
job['data']['infoldmarch']['location']     = {'node':42}
job['data']['infoldmarch']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['infoldmarch']['method']       = {'technique':'inplace'}
job['data']['infoldmarch']['activeonly']   = True                                                            # check pidfile
job['data']['infoldmarch']['schedule']     = {'interval':600}

job['data']['log']                    = {}
job['data']['log']['location']        = {'node':job['log_node']}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 5
job['cntl_node']        = 9
job['max_sleep']        = 10
job['work_time']        = 60

job['monitor'] = {'agents':{},'mi6':{}}
job['monitor']['agents']['grb_receipt_summary']      = {'enabled':True, 'module':'agent99_grb', 'class':'GRBReceipt'}
job['monitor']['agents']['pmd_admin']                = {'enabled':False, 'module':'im_daemon', 'class':'PMDAdmin', 'args':{'alerts':[27,28], 'telemetry':[26,27,28]}}
job['monitor']['mi6']['non_isatss']                  = {'enabled':True, 'lockout':1800}
job['monitor']['mi6']['forward']                     = {'enabled':True, 'types':{}, 'messages':{}}
job['monitor']['mi6']['forward']['types']['ERROR']   = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}
job['monitor']['mi6']['forward']['types']['WARNING'] = {'enabled':True, 'alert':{'enabled':True, 'lockout':1800}, 'tm':{'enabled':False}}	#or include

grbfiltdef = []
grbfiltdef.append({'filt':'substring','target':'name','contains':'_ABI-','name':'ABI Test'})
hcastfiltdef = []
hcastfiltdef.append({'filt':'substring','target':'name','contains':'_AHI-','name':'AHI Test'})

job['sources'] = {}
job['sources']['ldm'] = {'protocol':'CP', 'paths':{}}
job['sources']['ldm']['paths']['dropzone'] = {'node':25,'files':{},'delete':True}
job['sources']['ldm']['paths']['dropzone']['files']['grbl1b']  = {'retrieve':{},'filt':grbfiltdef}
job['sources']['ldm']['paths']['dropzone']['files']['grbl1b']['retrieve']['proc'] = {'enabled':True,'dataitem':'prodgrbl1b','notifications':['grbl1b']}
job['sources']['ldm']['paths']['dropzone']['files']['grbl1b']['retrieve']['arch'] = {'enabled':True,'dataitem':'prodldmarch','notifications':['ldmarch'],'hardlink':'proc'}
job['sources']['ldm']['paths']['dropzone']['files']['hcast']  = {'retrieve':{},'filt':hcastfiltdef}
job['sources']['ldm']['paths']['dropzone']['files']['hcast']['retrieve']['proc'] = {'enabled':True,'dataitem':'prodhcast','notifications':['hcast']}
job['sources']['ldm']['paths']['dropzone']['files']['hcast']['retrieve']['arch'] = {'enabled':True,'dataitem':'prodldmarch','notifications':['ldmarch'],'hardlink':'proc'}
