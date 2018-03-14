# isatss job definition for grb packet management

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
job['name']     = 'gpacket'
job['cmd']      = 'gpacket'
job['class']    = 'GPacket'
job['log']      = 'gpacket_log'
job['log_node'] = 1

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':job['log_node']}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log'], 'grbPacketProcessor', 'caduReader', 'statusFanout', 'statusReader']
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

'''
job['data']  = {}
job['data']['products'] = {}
job['data']['products']['location']   = {'node':47}
job['data']['products']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['products']['method']     = {'technique':'inplace'}
job['data']['products']['activeonly'] = True
job['data']['products']['schedule']   = {'interval':600}
'''

job['interval'] = 65.0

job['searchdef'] = {'cmd': True}

job['cmds']  = {}
job['cmds']['grbPacketServer']    = {'path':'/home/brapp/git/grb_processing/forwarding_server'}
job['cmds']['grbPacketProcessor'] = {'path':'/home/brapp/git/grb_processing/isatss'}
job['cmds']['caduReader']         = {'path':'/home/brapp/git/grb_processing/mcast'}
job['cmds']['statusFanout']       = {'path':'/home/brapp/git/grb_processing/mcast'}
job['cmds']['statusReader']       = {'path':'/home/brapp/git/grb_processing/isatss'}

'''
Make these nodes for incinerator to purge <output-directory>/...
Also, create these if they don't exist in setup()
'''
job['uproddirs'] = {}
job['uproddirs']['abi']           = 3600
job['uproddirs']['glm']           = 3600
job['uproddirs']['space_weather'] = 0

job['translate'] = {}
job['translate']['ip-address']       = 'addrs'
job['translate']['fanout-hosts']     = 'addrs'
job['translate']['port']             = 'ports'
job['translate']['output-directory'] = 'node_lookup'
job['translate']['mcast-address']    = 'addrs'
job['translate']['mcast-port']       = 'ports'
job['translate']['mcast-interface']  = 'addrs'

job['addrs'] = {}
job['addrs']['ip']           = '140.90.141.167'
job['addrs']['mcast']        = '224.70.14.21'
job['addrs']['local']        = '127.0.0.1'
job['addrs']['local_rhcp']   = '127.0.0.1:50010'
job['addrs']['local_lhcp']   = '127.0.0.1:50020'
job['addrs']['local_status'] = '127.0.0.1:50030'

job['ports'] = {}
job['ports']['rhcp']   = '50010'
job['ports']['lhcp']   = '50020'
job['ports']['status'] = '50030'

job['apps'] = {}
job['apps']['cadu_rhcp']     = {'cmd':'caduReader',        'args':{'mcast-address':'mcast', 'mcast-port':'rhcp', 'mcast-interface':'ip', 'fanout-hosts':['local_rhcp']},'switches':[]}
job['apps']['cadu_lhcp']     = {'cmd':'caduReader',        'args':{'mcast-address':'mcast', 'mcast-port':'lhcp', 'mcast-interface':'ip', 'fanout-hosts':['local_lhcp']},'switches':[]}
job['apps']['process_rhcp']  = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':42, 'port':'rhcp'}, 'switches':['udp']}
job['apps']['process_lhcp']  = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':41, 'port':'lhcp'}, 'switches':['udp']}
job['apps']['fanout_status'] = {'cmd':'statusFanout',      'args':{'mcast-address':'mcast', 'mcast-port':'status', 'mcast-interface':'ip', 'fanout-hosts':['local_status']},'switches':[]}
job['apps']['reader_status'] = {'cmd':'statusReader',      'args':{'ip-address':'local', 'port':'status'},'switches':[]}
