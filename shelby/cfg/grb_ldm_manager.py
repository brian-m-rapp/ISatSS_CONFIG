# ldm configuration for grb data flow

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
job['name']  = 'grb_ldm_manager'
job['cmd']   = 'ldmer'
job['class'] = 'LDMer'
job['log']   = 'grb_ldm_log'

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':1,'type':'datapath','path':'log'}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loglevel']         = 4

job['cntl_node']        = 7

job['defaults'] = {}
job['input_type']       = {'type':'infofile','node':6,'delete_file':False, 'delete_info':True}
job['pause']		    = 2
job['files_per_cycle']	= 50
job['ldm_home']         = '/usr/local/ldm'
job['watcher_timeout']  = 1000

