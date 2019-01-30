job = {}
job['name']      = 'isatss_ldm_manager'
job['cmd']       = 'ldmer'
job['class']     = 'LDMer'
job['log']       = 'isatss_ldm_manager_log'
job['log_node']  = 1
job['loglevel']  = 5
job['cntl_node'] = 7

job['input_type']       = {'type':'infofile','node':41, 'delete_info':True, 'delete_file':True}
job['files_per_cycle']  = 50
job['watcher_timeout']  = 1000

job['data'] = {}
job['data']['log'] = {}
job['data']['log']['location']   = {'node':job['log_node']}
job['data']['log']['aging']      = {'window':2, 'mode':'count'}
job['data']['log']['archive']    = {'window':7, 'mode':'count'}
job['data']['log']['roots']      = [job['log']]
job['data']['log']['method']     = {'technique':'inplace'}
job['data']['log']['schedule']   = {'interval':3600}
job['data']['log']['activeonly'] = True

job['data']['ldm_data'] = {}
job['data']['ldm_data']['location']   = {'node':12}
job['data']['ldm_data']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['ldm_data']['method']     = {'technique':'inplace'}
job['data']['ldm_data']['activeonly'] = False
job['data']['ldm_data']['schedule']   = {'interval':300}
job['data']['ldm_data']['cfgorder']   = 0

job['ldm_monitor']    = {'active':True, 'interval':60, 'restart':True, 'shutdown_on_exit':True, 'restart_on_startup':True}
job['ldm_lib']        = '/usr/local/ldm/lib'
job['ldmadmin']       = '/usr/local/ldm/bin/ldmadmin'
job['pqcat']          = '/usr/local/ldm/bin/pqact'
job['pqcheck']        = '/usr/local/ldm/bin/pqcheck'
job['ldmd_cfg_file']  = '/usr/local/ldm/etc/ldmd.conf'
job['pqact_cfg_file'] = '/usr/local/ldm/etc/pqact.conf'
job['queue_file']     = '/usr/local/ldm/var/queues/ldm.pq'

job['ldmd_config'] = {}
job['ldmd_config']['allow'] = []
#job['ldmd_config']['allow'].append({'feedset':'ANY', 'hostname':'aib2.napo.nws.noaa.gov', 'OK':'', 'not':'', 'desc':['']})
#job['ldmd_config']['allow'].append({'feedset':'ANY', 'hostname':'lotus.napo.nws.noaa.gov', 'OK':'', 'not':'', 'desc':['']})
#job['ldmd_config']['allow'].append({'feedset':'ANY', 'hostname':'aib.napo.nws.noaa.gov', 'OK':'^GCOM.*', 'not':'', 'desc':['']})

job['ldmd_config']['requests'] = []
#job['ldmd_config']['requests'].append({'feedset':'ANY','pattern':'^ascat_.*','host':'nwave.napo.nws.noaa.gov','desc':['ASCAT Winds from NHC']})
#job['ldmd_config']['requests'].append({'feedset':'ANY','pattern':'^NPR.*','host':'nwave.napo.nws.noaa.gov','desc':['DMSP SSMI from NHC']})


job['pqact_config']     = []
#job['pqact_config'].append({'feedtype':'EXP','pattern':'(^ascat.*)','action':'FILE','options':'-overwrite -log -close','filename':{'datapath':'ldm_data','spec':'\\1_(seq)'},'desc':['ASCAT Winds']})
#job['pqact_config'].append({'feedtype':'EXP','pattern':'(^NPR.*.NS)','action':'FILE','options':'-overwrite -log -close','filename':{'datapath':'ldm_data','spec':'\\1'},'desc':['DMSP SSMI']})

#amsr2, atms, jason2/3
job['pqact_config'].append({'feedtype':'EXP','pattern':'^(isatss_AMSR2-MBT.*)','action':'FILE','options':'-overwrite -log -close','filename':{'datapath':'ldm_data','spec':'\\1'},'desc':['AMSR2']})
job['pqact_config'].append({'feedtype':'EXP','pattern':'^(isatss_NPR-MIRS.*)', 'action':'FILE','options':'-overwrite -log -close','filename':{'datapath':'ldm_data','spec':'\\1'},'desc':['ATMS']})
job['pqact_config'].append({'feedtype':'EXP','pattern':'^(jason_.*)',          'action':'FILE','options':'-overwrite -log -close','filename':{'datapath':'ldm_data','spec':'\\1'},'desc':['Jason 2/3']})
