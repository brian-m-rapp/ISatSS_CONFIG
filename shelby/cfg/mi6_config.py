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
job['name']     = 'mi6'
job['cmd']      = 'mi6'
job['class']    = 'MI6'
job['log']      = 'mi6_log'
job['log_node'] = 1

job['notifications'] = {}
job['notifications']['deaddrop']      = {'node':31,'enabled':True}

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':job['log_node']}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['cntl_node']                 = 22

job['loopsleep']                 = 1
job['loglevel']                  = 6
job['handler_pool_size']         = 3

# These are common telemetry classes for every host at this site
job['host_telemetry'] = {'filesystems': {'period': 60,              'aggregate': 15, 'method': 'abs'},
						 'cpu':         {'period': 10, 'rolling':6, 'aggregate': 90, 'method': 'abs'},
						 'memory':      {'period': 10, 'rolling':6, 'aggregate': 90, 'method': 'abs'},
						 'network':     {'period': 60,              'aggregate': 15, 'method': 'diff'}}

# host attributes
job['hattr'] = {}

job['hattr'][1] = {}
job['hattr'][1]['collect']     = []
job['hattr'][1]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][1]['network']     = [('netpref', 'eno')]
job['hattr'][1]['filesystems'] = []
job['hattr'][1]['filesystems'].append({'fs': '/'})
job['hattr'][1]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][1]['filesystems'].append({'fs': '/opt'})
job['hattr'][1]['filesystems'].append({'fs': '/scratch'})
job['hattr'][1]['filesystems'].append({'fs': '/tmp'})
job['hattr'][1]['filesystems'].append({'fs': '/usr'})
job['hattr'][1]['filesystems'].append({'fs': '/usr1'})
job['hattr'][1]['filesystems'].append({'fs': '/var'})
job['hattr'][1]['filesystems'].append({'fs': '/var/log'})
job['hattr'][1]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][2] = {}
job['hattr'][1]['collect']     = []
job['hattr'][2]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][2]['network']     = [('netpref', 'eno')]
job['hattr'][2]['filesystems'] = []
job['hattr'][2]['filesystems'].append({'fs': '/'})
job['hattr'][2]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][2]['filesystems'].append({'fs': '/opt'})
job['hattr'][2]['filesystems'].append({'fs': '/scratch'})
job['hattr'][2]['filesystems'].append({'fs': '/tmp'})
job['hattr'][2]['filesystems'].append({'fs': '/usr'})
job['hattr'][2]['filesystems'].append({'fs': '/usr1'})
job['hattr'][2]['filesystems'].append({'fs': '/var'})
job['hattr'][2]['filesystems'].append({'fs': '/var/log'})
job['hattr'][2]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][3] = {}
job['hattr'][3]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][3]['network']     = [('netpref', 'eno')]
job['hattr'][3]['filesystems'] = []
job['hattr'][3]['filesystems'].append({'fs': '/'})
job['hattr'][3]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][3]['filesystems'].append({'fs': '/opt'})
job['hattr'][3]['filesystems'].append({'fs': '/scratch'})
job['hattr'][3]['filesystems'].append({'fs': '/tmp'})
job['hattr'][3]['filesystems'].append({'fs': '/usr'})
job['hattr'][3]['filesystems'].append({'fs': '/usr1'})
job['hattr'][3]['filesystems'].append({'fs': '/var'})
job['hattr'][3]['filesystems'].append({'fs': '/var/log'})
job['hattr'][3]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][4] = {}
job['hattr'][4]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][4]['network']     = [('netpref', 'eno')]
job['hattr'][4]['filesystems'] = []
job['hattr'][4]['filesystems'].append({'fs': '/'})
job['hattr'][4]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][4]['filesystems'].append({'fs': '/opt'})
job['hattr'][4]['filesystems'].append({'fs': '/scratch'})
job['hattr'][4]['filesystems'].append({'fs': '/tmp'})
job['hattr'][4]['filesystems'].append({'fs': '/usr'})
job['hattr'][4]['filesystems'].append({'fs': '/usr1'})
job['hattr'][4]['filesystems'].append({'fs': '/var'})
job['hattr'][4]['filesystems'].append({'fs': '/var/log'})
job['hattr'][4]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][5] = {}
job['hattr'][5]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][5]['network']     = [('netpref', 'eno')]
job['hattr'][5]['filesystems'] = []
job['hattr'][5]['filesystems'].append({'fs': '/'})
job['hattr'][5]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][5]['filesystems'].append({'fs': '/opt'})
job['hattr'][5]['filesystems'].append({'fs': '/scratch'})
job['hattr'][5]['filesystems'].append({'fs': '/tmp'})
job['hattr'][5]['filesystems'].append({'fs': '/usr'})
job['hattr'][5]['filesystems'].append({'fs': '/usr1'})
job['hattr'][5]['filesystems'].append({'fs': '/var'})
job['hattr'][5]['filesystems'].append({'fs': '/var/log'})
job['hattr'][5]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][6] = {}
job['hattr'][6]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][6]['network']     = [('netpref', 'eno')]
job['hattr'][6]['filesystems'] = []
job['hattr'][6]['filesystems'].append({'fs': '/'})
job['hattr'][6]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][6]['filesystems'].append({'fs': '/opt'})
job['hattr'][6]['filesystems'].append({'fs': '/scratch'})
job['hattr'][6]['filesystems'].append({'fs': '/tmp'})
job['hattr'][6]['filesystems'].append({'fs': '/usr'})
job['hattr'][6]['filesystems'].append({'fs': '/usr1'})
job['hattr'][6]['filesystems'].append({'fs': '/var'})
job['hattr'][6]['filesystems'].append({'fs': '/var/log'})
job['hattr'][6]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][7] = {}
job['hattr'][7]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][7]['network']     = [('netpref', 'eno')]
job['hattr'][7]['filesystems'] = []
job['hattr'][7]['filesystems'].append({'fs': '/'})
job['hattr'][7]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][7]['filesystems'].append({'fs': '/opt'})
job['hattr'][7]['filesystems'].append({'fs': '/scratch'})
job['hattr'][7]['filesystems'].append({'fs': '/tmp'})
job['hattr'][7]['filesystems'].append({'fs': '/usr'})
job['hattr'][7]['filesystems'].append({'fs': '/usr1'})
job['hattr'][7]['filesystems'].append({'fs': '/var'})
job['hattr'][7]['filesystems'].append({'fs': '/var/log'})
job['hattr'][7]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][8] = {}
job['hattr'][8]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][8]['network']     = [('netpref', 'eno')]
job['hattr'][8]['filesystems'] = []
job['hattr'][8]['filesystems'].append({'fs': '/'})
job['hattr'][8]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][8]['filesystems'].append({'fs': '/opt'})
job['hattr'][8]['filesystems'].append({'fs': '/scratch'})
job['hattr'][8]['filesystems'].append({'fs': '/tmp'})
job['hattr'][8]['filesystems'].append({'fs': '/usr'})
job['hattr'][8]['filesystems'].append({'fs': '/usr1'})
job['hattr'][8]['filesystems'].append({'fs': '/var'})
job['hattr'][8]['filesystems'].append({'fs': '/var/log'})
job['hattr'][8]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][9] = {}
job['hattr'][9]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][9]['network']     = [('netpref', 'eno')]
job['hattr'][9]['filesystems'] = []
job['hattr'][9]['filesystems'].append({'fs': '/'})
job['hattr'][9]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][9]['filesystems'].append({'fs': '/opt'})
job['hattr'][9]['filesystems'].append({'fs': '/scratch'})
job['hattr'][9]['filesystems'].append({'fs': '/tmp'})
job['hattr'][9]['filesystems'].append({'fs': '/usr'})
job['hattr'][9]['filesystems'].append({'fs': '/usr1'})
job['hattr'][9]['filesystems'].append({'fs': '/var'})
job['hattr'][9]['filesystems'].append({'fs': '/var/log'})
job['hattr'][9]['filesystems'].append({'fs': '/var/log/audit'})

job['hattr'][10] = {}
job['hattr'][10]['collect']     = ['filesystems', 'cpu', 'memory', 'network']
job['hattr'][10]['network']     = [('netpref', 'eno')]
job['hattr'][10]['filesystems'] = []
job['hattr'][10]['filesystems'].append({'fs': '/'})
job['hattr'][10]['filesystems'].append({'fs': '/data'})
job['hattr'][10]['filesystems'].append({'fs': '/dev/shm', 'collect': True})
job['hattr'][10]['filesystems'].append({'fs': '/miniconda'})
job['hattr'][10]['filesystems'].append({'fs': '/opt'})
job['hattr'][10]['filesystems'].append({'fs': '/scratch'})
job['hattr'][10]['filesystems'].append({'fs': '/tmp'})
job['hattr'][10]['filesystems'].append({'fs': '/usr'})
job['hattr'][10]['filesystems'].append({'fs': '/usr1'})
job['hattr'][10]['filesystems'].append({'fs': '/var'})
job['hattr'][10]['filesystems'].append({'fs': '/var/log'})
job['hattr'][10]['filesystems'].append({'fs': '/var/log/audit'})
