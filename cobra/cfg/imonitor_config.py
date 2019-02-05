# imonitor site configuration file

tmfile_node = 32
tmfile_roots = ['system_tm']

tmdefns = []
tmdefns.append('telemetry_descriptions')

alertfile_node = 32
alertfile_roots = ['alerts']

alertdefns = []
alertdefns.append('alert_descriptions')

all_alerts        = ['ERROR', 'WARNING', 'INFO', 'STATUS', 'DEBUG', 'non_isatss']
logging_alerts    = ['ERROR', 'WARNING', 'INFO', 'STATUS', 'DEBUG']
non_isatss_alerts = ['non_isatss']
alert_expansions  = {'faults': ['ERROR', 'WARNING', 'non_isatss']}

sets = {}
sets['general'] = {}
sets['general']['description'] = 'Any of ERROR, WARNING, INFO, STATUS, DEBUG'
sets['general']['fields'] = {}
sets['general']['fields'][1]  = {'key': 'msg', 'label':'Severity', 'prec':7, 'dtype':'s'}
sets['general']['fields'][2]  = {'key': 'stamp', 'label':'Event Time', 'formatter':'formatEventTime', 'prec':26, 'dtype':'s'}
sets['general']['fields'][3]  = {'key': 'site', 'label':'Site', 'prec':8, 'dtype':'s'}
sets['general']['fields'][4]  = {'key': 'host', 'label':'Host', 'formatter':'formatHostShortName', 'prec':8, 'dtype':'s'}
sets['general']['fields'][5]  = {'key': 'gid', 'label':'GID', 'prec':3, 'dtype':'d'}
sets['general']['fields'][6]  = {'key': 'jid', 'label':'JID', 'prec':3, 'dtype':'d'}
sets['general']['fields'][7]  = {'key': 'pid', 'label':'PID', 'prec':3, 'dtype':'d'}
sets['general']['fields'][8]  = {'key': 'thread', 'label':'Thread', 'prec':25, 'dtype':'s'}
sets['general']['fields'][9]  = {'key': 'ident', 'label':'Msg ID', 'prec':8, 'dtype':'s'}
sets['general']['fields'][10] = {'key': 'text', 'label':'', 'prec':3, 'dtype':'s'}

sets['non_isatss'] = {}
sets['non_isatss']['description'] = 'A message not emitted by the im_log module, such as a Traceback'
sets['non_isatss']['fields'] = {}
sets['non_isatss']['fields'][1] = {'key': 'last_valid_timestamp', 'label':'Last Event Time', 'formatter':'formatEventTime', 'prec':26, 'dtype':'s'}
sets['non_isatss']['fields'][2] = {'key': 'next_valid_timestamp', 'label':'Next Event Time', 'formatter':'formatEventTime', 'prec':26, 'dtype':'s'}
sets['non_isatss']['fields'][3] = {'key': 'site', 'label':'Site', 'prec':8, 'dtype':'s'}
sets['non_isatss']['fields'][4] = {'key': 'host', 'label':'Host', 'formatter':'formatHostShortName', 'prec':8, 'dtype':'s'}
sets['non_isatss']['fields'][5] = {'key': 'gid', 'label':'GID', 'prec':3, 'dtype':'d'}
sets['non_isatss']['fields'][6] = {'key': 'jid', 'label':'JID', 'prec':3, 'dtype':'d'}
sets['non_isatss']['fields'][7] = {'key': 'content', 'label':'Message Content', 'formatter':'formatNonIsatssContent', 'prec':3, 'dtype':'s'}

sets['cpu1avg'] = {}
sets['cpu1avg']['description'] = 'List of Average One Minute CPU Load every 5 minutes for all Servers in cluster'
sets['cpu1avg']['timebase']  = {'mode':'synthetic','format':'%Y%m%d.%H%M%S','width':20,'just':'left','interval':300}
sets['cpu1avg']['timerange'] = {'reference':'end','span':-3600}
sets['cpu1avg']['extractors'] = {}
sets['cpu1avg']['extractors']['mi6_cpu'] = {'module':'mi6_system_extractors', 'class':'ValBySelector'}
sets['cpu1avg']['fields'] = {}
sets['cpu1avg']['fields'][1]  = {'tm':'mi6_cpu','val':'la1_avg','selectors':{'host':{'method':'decode_host_shortname','args':{'shortname':'cobra'}}},  'label':'shelby','format':'5.2f','width':7,'just':'left'}
sets['cpu1avg']['fields'][2]  = {'tm':'mi6_cpu','val':'la1_avg','selectors':{'host':{'method':'decode_host_shortname','args':{'shortname':'ldm'}}},  'label':'dev1','format':'5.2f','width':7,'just':'left'}

sets['cpu1avgr'] = {}
sets['cpu1avgr']['description'] = 'List of Average One Minute CPU Load vs reported times for all CPRK Servers'
sets['cpu1avgr']['timebase']  = {'mode':'reported','format':'%Y%m%d.%H%M%S','width':20,'just':'left'}
sets['cpu1avgr']['timerange'] = {'reference':'end','span':-600}
sets['cpu1avgr']['extractors'] = {}
sets['cpu1avgr']['extractors']['mi6_cpu'] = {'module':'mi6_system_extractors', 'class':'ValBySelector'}
sets['cpu1avgr']['fields'] = {}
sets['cpu1avgr']['fields'][1]  = {'tm':'mi6_cpu','val':'la1_avg','selectors':{'host':{'method':'decode_host_shortname','args':{'shortname':'shelby'}}},  'label':'shelby','format':'5.2f','width':7,'just':'left'}
sets['cpu1avgr']['fields'][2]  = {'tm':'mi6_cpu','val':'la1_avg','selectors':{'host':{'method':'decode_host_shortname','args':{'shortname':'dev1'}}},  'label':'dev1','format':'5.2f','width':7,'just':'left'}

sets['freemem'] = {}
sets['freemem']['description'] = 'List of Minimum Free Memory every 5 minutes for all CPRK Servers'
sets['freemem']['timebase']  = {'mode':'synthetic','format':'%Y%m%d.%H%M%S','width':20,'just':'left','interval':300}
sets['freemem']['timerange'] = {'reference':'end','span':-3600*12}
sets['freemem']['extractors'] = {}
sets['freemem']['extractors']['mi6_mem'] = {'module':'mi6_system_extractors', 'class':'ValBySelector'}
sets['freemem']['fields'] = {}
sets['freemem']['fields'][1]  = {'tm':'mi6_mem','val':'free_min','selectors':{'host':{'method':'decode_host_shortname','args':{'shortname':'shelby'}}},  'label':'shelby','format':'5.2f','width':7,'just':'left'}
sets['freemem']['fields'][2]  = {'tm':'mi6_mem','val':'free_min','selectors':{'host':{'method':'decode_host_shortname','args':{'shortname':'dev1'}}},  'label':'dev1','format':'5.2f','width':7,'just':'left'}
