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
job['name']  = 'gpacket'
job['cmd']   = 'gpacket'
job['class'] = 'GPacket'
job['log']   = 'gpacket_log'

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':1,'path':'log'}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log'], 'grbPacketProcessor', 'grbPacketServer']
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['interval'] = 65.0

job['ports'] = {}
job['ports']['rhcp'] = {'port':'50020'}
job['ports']['lhcp'] = {'port':'50010'}

job['cmds']  = {}
job['cmds']['grbPacketServer']    = {'path':'/data/isatss/mcast-bridge/forwarding_server'}
job['cmds']['grbPacketProcessor'] = {'path':'/data/isatss/mcast-bridge/isatss'}

job['site']  = 'cprk'

job['uproddirs'] = {}
job['uproddirs']['abi']           = 3600
job['uproddirs']['glm']           = 0
job['uproddirs']['space_weather'] = 0

job['translate'] = {}
job['translate']['ip-address']   = 'sites/ip-address'
job['translate']['fanout-hosts'] = 'sites/ip-address'
job['translate']['port']         = 'ports/port'

job['searchdef'] = {'cmd':True,'args':['port'],'switches':[]}

job['sites'] = {}
job['sites']['annex']   = {'ip-address':'10.90.190.123','apps':{}}
job['sites']['cprkant'] = {'ip-address':'10.70.14.95','apps':{}}
job['sites']['nannex']  = {'ip-address':'192.168.124.2','apps':{}}
job['sites']['nannex']['apps']['server_rhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'nannex', 'fanout-hosts':['local'],'port':'rhcp'},'switches':['udp']}
job['sites']['nannex']['apps']['server_lhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'nannex', 'fanout-hosts':['local'],'port':'lhcp'},'switches':['udp']}
job['sites']['nannex']['apps']['process_rhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/mnt/ramdisk/grb_rhcp','port':'rhcp'},'switches':[]}
job['sites']['nannex']['apps']['process_lhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/mnt/ramdisk/grb_lhcp','port':'lhcp'},'switches':[]}
job['sites']['local']  = {'ip-address':'127.0.0.1','apps':{}}
job['sites']['napo']   = {'ip-address':'140.90.141.250','apps':{}}
job['sites']['napo']['apps']['server_rhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'nannex', 'fanout-hosts':['local'],'port':'rhcp'},'switches':['tcp']}
job['sites']['napo']['apps']['server_lhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'nannex', 'fanout-hosts':['local'],'port':'lhcp'},'switches':['tcp']}
job['sites']['napo']['apps']['process_rhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/mnt/ramdisk/grb_live','port':'rhcp'},'switches':[]}
job['sites']['napo']['apps']['process_lhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/mnt/ramdisk/grb_live','port':'lhcp'},'switches':[]}
job['sites']['cprk']   = {'ip-address':'10.60.116.76','apps':{}}
job['sites']['cprk']['apps']['server_rhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'cprkant', 'fanout-hosts':['local'],'port':'rhcp'},'switches':['tcp']}
job['sites']['cprk']['apps']['server_lhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'cprkant', 'fanout-hosts':['local'],'port':'lhcp'},'switches':['tcp']}
job['sites']['cprk']['apps']['process_rhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/scratch/isatss_data/incoming/grb_rhcp','port':'rhcp'},'switches':[]}
job['sites']['cprk']['apps']['process_lhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/scratch/isatss_data/incoming/grb_lhcp','port':'lhcp'},'switches':[]}
job['sites']['awc']   = {'ip-address':'172.16.251.46','apps':{}}
#job['sites']['awc']['apps']['server_rhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'cprk', 'fanout-hosts':['local'],'port':'rhcp'},'switches':['tcp']}
#job['sites']['awc']['apps']['server_lhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'cprk', 'fanout-hosts':['local'],'port':'lhcp'},'switches':['tcp']}
job['sites']['awc']['apps']['server_rhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'awc', 'fanout-hosts':['local'],'port':'rhcp'},'switches':['udp']}
job['sites']['awc']['apps']['server_lhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'awc', 'fanout-hosts':['local'],'port':'lhcp'},'switches':['udp']}
job['sites']['awc']['apps']['process_rhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/scratch/isatss_data/grb_live','port':'rhcp'},'switches':[]}
job['sites']['awc']['apps']['process_lhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/scratch/isatss_data/grb_live','port':'lhcp'},'switches':[]}
job['sites']['nhc']   = {'ip-address':'140.90.176.108','apps':{}}
job['sites']['nhc']['apps']['server_rhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'nhc', 'fanout-hosts':['local'],'port':'rhcp'},'switches':['udp']}
job['sites']['nhc']['apps']['server_lhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'nhc', 'fanout-hosts':['local'],'port':'lhcp'},'switches':['udp']}
job['sites']['nhc']['apps']['process_rhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/home/isatss/isatss_data/grb_live','port':'rhcp'},'switches':[]}
job['sites']['nhc']['apps']['process_lhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local',  'output-directory':'/home/isatss/isatss_data/grb_live','port':'lhcp'},'switches':[]}
job['sites']['spc']   = {'ip-address':'140.90.173.70','apps':{}}
job['sites']['spc']['apps']['server_rhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'spc', 'fanout-hosts':['local'],'port':'rhcp'},'switches':['udp']}
job['sites']['spc']['apps']['server_lhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'spc', 'fanout-hosts':['local'],'port':'lhcp'},'switches':['udp']}
#job['sites']['spc']['apps']['server_rhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'cprk','fanout-hosts':['local'],'port':'rhcp'},'switches':['tcp']}
#job['sites']['spc']['apps']['server_lhcp']  = {'cmd':'grbPacketServer',   'args':{'ip-address':'cprk','fanout-hosts':['local'],'port':'lhcp'},'switches':['tcp']}
job['sites']['spc']['apps']['process_rhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local', 'output-directory':'/mnt/ramdisk/grb_live','port':'rhcp'},'switches':[]}
job['sites']['spc']['apps']['process_lhcp'] = {'cmd':'grbPacketProcessor','args':{'ip-address':'local', 'output-directory':'/mnt/ramdisk/grb_live','port':'lhcp'},'switches':[]}

