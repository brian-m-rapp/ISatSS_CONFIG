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
job['name']  = 'mi6'
job['cmd']   = 'mi6'
job['class'] = 'MI6'
job['log']   = 'mi6_log'

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':0,'type':'datapath','path':'log'}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['loopsleep']                 = 1
job['loglevel']                  = 6
job['handler_pool_size']         = 3

job['statslogging'] = {'filesystems': {'period': 60,              'aggregate': 15, 'method': 'abs'},
                       'cpu':         {'period': 10, 'rolling':6, 'aggregate': 90, 'method': 'abs'},
                       'memory':      {'period': 10, 'rolling':6, 'aggregate': 90, 'method': 'abs'},
                       'network':     {'period': 60,              'aggregate': 15, 'method': 'diff'}}

# host attributes
job['hattr'] = {}

job['hattr'][0] = {'nics': [('netname', 'eth0')]}
job['hattr'][0]['filesystems'] = []
job['hattr'][0]['filesystems'].append({'fs': '/'})
job['hattr'][0]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][0]['filesystems'].append({'fs': '/home'})

job['hattr'][1] = {'nics': [('netname', 'bond0'), ('netname', 'eth1')]}
job['hattr'][1]['filesystems'] = []
job['hattr'][1]['filesystems'].append({'fs': '/'})
job['hattr'][1]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][1]['filesystems'].append({'fs': '/home'})
