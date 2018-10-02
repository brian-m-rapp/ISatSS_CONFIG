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
job['name']      = 'g17_gpacket'
job['cmd']       = 'gpacket'
job['class']     = 'GPacket'
job['log']       = 'g17_gpacket_log'
job['log_node']  = 1
job['cntl_node'] = 580
job['loopsleep'] = 1

job['data'] = {}
job['data']['log']                       = {}
job['data']['log']['location']           = {'node':job['log_node']}
job['data']['log']['aging']              = {'window':2,'mode':'count'}
job['data']['log']['archive']            = {'window':7,'mode':'count'}
job['data']['log']['roots']              = [job['log'], 'grbPacketProcessor', 'grbPacketServer']
job['data']['log']['method']             = {'technique':'inplace'}
job['data']['log']['schedule']           = {'interval':3600}
job['data']['log']['activeonly']         = True
job['data']['log']['cfgorder']           = -1

job['apps'] = {}
job['apps']['ipdu_g17_rhcp'] = {}	# goes-17 rhcp
job['apps']['ipdu_g17_rhcp']['path'] = '/home/brapp/git/grb_processing/mcast'
job['apps']['ipdu_g17_rhcp']['app']  = 'ipduReader'
job['apps']['ipdu_g17_rhcp']['keys'] = {}
job['apps']['ipdu_g17_rhcp']['keys']['mcast-address']   = '239.1.148.31'
job['apps']['ipdu_g17_rhcp']['keys']['mcast-port']      = '11031'
job['apps']['ipdu_g17_rhcp']['keys']['mcast-interface'] = '10.90.190.123'
job['apps']['ipdu_g17_rhcp']['keys']['fanout-hosts']    = '127.0.0.1:50010'

job['apps']['ipdu_g17_lhcp'] = {}	# goes-17 lhcp
job['apps']['ipdu_g17_lhcp']['path'] = '/home/brapp/git/grb_processing/mcast'
job['apps']['ipdu_g17_lhcp']['app']  = 'ipduReader'
job['apps']['ipdu_g17_lhcp']['keys'] = {}
job['apps']['ipdu_g17_lhcp']['keys']['mcast-address']   = '239.1.148.31'
job['apps']['ipdu_g17_lhcp']['keys']['mcast-port']      = '11032'
job['apps']['ipdu_g17_lhcp']['keys']['mcast-interface'] = '10.90.190.123'
job['apps']['ipdu_g17_lhcp']['keys']['fanout-hosts']    = '127.0.0.1:50020'

job['apps']['ipdu_g16_lhcp'] = {}	# goes-16 lhcp
job['apps']['ipdu_g16_lhcp']['path'] = '/home/brapp/git/grb_processing/mcast'
job['apps']['ipdu_g16_lhcp']['app']  = 'ipduReader'
job['apps']['ipdu_g16_lhcp']['keys'] = {}
job['apps']['ipdu_g16_lhcp']['keys']['mcast-address']   = '239.1.145.31'
job['apps']['ipdu_g16_lhcp']['keys']['mcast-port']      = '11031'
job['apps']['ipdu_g16_lhcp']['keys']['mcast-interface'] = '10.90.190.123'
job['apps']['ipdu_g16_lhcp']['keys']['fanout-hosts']    = '127.0.0.1:60010'

job['apps']['ipdu_g16_rhcp'] = {}	# goes-16 rhcp
job['apps']['ipdu_g16_rhcp']['path'] = '/home/brapp/git/grb_processing/mcast'
job['apps']['ipdu_g16_rhcp']['app']  = 'ipduReader'
job['apps']['ipdu_g16_rhcp']['keys'] = {}
job['apps']['ipdu_g16_rhcp']['keys']['mcast-address']   = '239.1.145.31'
job['apps']['ipdu_g16_rhcp']['keys']['mcast-port']      = '11032'
job['apps']['ipdu_g16_rhcp']['keys']['mcast-interface'] = '10.90.190.123'
job['apps']['ipdu_g16_rhcp']['keys']['fanout-hosts']    = '127.0.0.1:60020'

job['apps']['packets_g17_rhcp'] = {}	# goes-17 rhcp
job['apps']['packets_g17_rhcp']['path'] = '/home/brapp/git/grb_processing/forwarding_server'
job['apps']['packets_g17_rhcp']['app']  = 'grbPacketServer'
job['apps']['packets_g17_rhcp']['keys'] = {}
job['apps']['packets_g17_rhcp']['keys']['udp']          = ''
job['apps']['packets_g17_rhcp']['keys']['ip-address']   = '127.0.0.1'
job['apps']['packets_g17_rhcp']['keys']['port']         = '50010'
job['apps']['packets_g17_rhcp']['keys']['fanout-hosts'] = '140.90.141.250:50010' 

job['apps']['packets_g17_lhcp'] = {}	# goes-17 lhcp
job['apps']['packets_g17_lhcp']['path'] = '/home/brapp/git/grb_processing/forwarding_server'
job['apps']['packets_g17_lhcp']['app']  = 'grbPacketServer'
job['apps']['packets_g17_lhcp']['keys'] = {}
job['apps']['packets_g17_lhcp']['keys']['udp']          = ''
job['apps']['packets_g17_lhcp']['keys']['ip-address']   = '127.0.0.1'
job['apps']['packets_g17_lhcp']['keys']['port']         = '50020'
job['apps']['packets_g17_lhcp']['keys']['fanout-hosts'] = '140.90.141.250:50020'

job['apps']['packets_g16_lhcp'] = {}	# goes-16 lhcp
job['apps']['packets_g16_lhcp']['path'] = '/home/brapp/git/grb_processing/forwarding_server'
job['apps']['packets_g16_lhcp']['app']  = 'grbPacketServer'
job['apps']['packets_g16_lhcp']['keys'] = {}
job['apps']['packets_g16_lhcp']['keys']['udp']          = ''
job['apps']['packets_g16_lhcp']['keys']['ip-address']   = '127.0.0.1'
job['apps']['packets_g16_lhcp']['keys']['port']         = '60010'
job['apps']['packets_g16_lhcp']['keys']['fanout-hosts'] = '140.90.141.250:60010'

job['apps']['packets_g16_rhcp'] = {}	# goes-16 rhcp
job['apps']['packets_g16_rhcp']['path'] = '/home/brapp/git/grb_processing/forwarding_server'
job['apps']['packets_g16_rhcp']['app']  = 'grbPacketServer'
job['apps']['packets_g16_rhcp']['keys'] = {}
job['apps']['packets_g16_rhcp']['keys']['udp']          = ''
job['apps']['packets_g16_rhcp']['keys']['ip-address']   = '127.0.0.1'
job['apps']['packets_g16_rhcp']['keys']['port']         = '60020'
job['apps']['packets_g16_rhcp']['keys']['fanout-hosts'] = '140.90.141.250:60020'

job['interval'] = 60

