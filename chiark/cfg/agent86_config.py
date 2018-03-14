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
job['name']  = 'agent86'
job['cmd']   = 'agent86'
job['class'] = 'Agent86'
job['log']   = 'agent86_log'

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':0,'type':'datapath','path':'log'}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loopsleep']                 = 0
job['loglevel']                  = 5
job['pause_empty']               = 2
job['actions_per_cycle']         = 10
job['listenport']                = 1337
job['msgmap']                    = {}
job['watcher_timeout']           = 1000
