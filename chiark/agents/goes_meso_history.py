# agent99 and agent 13 modules for IDP Big Brother Monitoring

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

# imports
imports = []
imports.append({'module':'calendar',        'as':'calendar',        'src':'baseline'})
imports.append({'module':'sys',             'as':'sys',             'src':'baseline'})
imports.append({'module':'time',            'as':'time',            'src':'baseline'})
imports.append({'module':'im_agent13',      'as':'im_agent13',      'src':'isatss'})
imports.append({'module':'im_agent99',      'as':'im_agent99',      'src':'isatss'})
imports.append({'module':'im_exceptions',   'as':'ime',             'src':'isatss'})
import isatss_init
isatss_init.load_imports(__name__,imports)
isc = isatss_init.import_config()
#globals
fid=9998

class GoesMesoHistory(im_agent13.Agent13):
	defs = {}
	defs['GOES_Meso_History'] = {}

	def __init__(self, logger, publishQ, args=None):
		super().__init__(logger, publishQ, args)
		self.registered_messages['GOES_Status_Input'] = {}

		self.init_time = time.time()

		self.exclude = {}
		if args != None and 'excluded_jobs' in args:
			self.exclude = args['excluded_jobs']

		self.job_thresholds = {}
		if  args != None and 'job_thresholds' in args:
			self.job_thresholds = args['job_thresholds']
		else:
			self.job_thresholds = {'latency_yellow':300,'latency_red':600,'restart_yellow':10,'restart_red':20}


		self.bbstatus = {}
		self.bbstatus['jobs'] = {}
		for gid in isc.groups:
			if gid == 0:
				continue
			for jid in isc.groups[gid]['jobs']:
				if gid in self.exclude and jid in self.exclude[gid]:
					continue
				if gid not in self.bbstatus['jobs']:
					self.bbstatus['jobs'][gid] = {}
				self.bbstatus['jobs'][gid][jid] = {'last':0, 'state':'green','pid':-1,'restarts':0,'accumulated_restarts':0}

		# LHCP and RHCP inputs
		self.bbstatus['inputs'] = {'bands':{}}
		if args != None and 'input_thresholds' in args and 'last_received_yellow' in args['input_thresholds']:
			self.bbstatus['inputs']['lhcp_last_rcvd_yellow'] = args['input_thresholds']['last_received_yellow']
			self.bbstatus['inputs']['rhcp_last_rcvd_yellow'] = args['input_thresholds']['last_received_yellow']
		else:
			self.bbstatus['inputs']['lhcp_last_rcvd_yellow'] = 400
			self.bbstatus['inputs']['rhcp_last_rcvd_yellow'] = 400
		if args != None and 'input_thresholds' in args and 'last_received_red' in args['input_thresholds']:
			self.bbstatus['inputs']['lhcp_last_rcvd_red'] = args['input_thresholds']['last_received_red']
			self.bbstatus['inputs']['rhcp_last_rcvd_red'] = args['input_thresholds']['last_received_red']
		else:
			self.bbstatus['inputs']['lhcp_last_rcvd_red'] = 800
			self.bbstatus['inputs']['rhcp_last_rcvd_red'] = 800

		for b in goesr_abi_config.band:
			self.bbstatus['inputs']['bands'][b] = {'pol':goesr_abi_config.band[b]['pol'],'last':0}

		# Imagery Output Tiles and Area files
		self.bbstatus['outputs'] = {'bands':{}}
		if args != None and 'output_thresholds' in args and 'last_sent_yellow' in args['output_thresholds']:
			self.bbstatus['outputs']['last_sent_yellow'] = args['output_thresholds']['last_sent_yellow']
		else:
			self.bbstatus['outputs']['last_sent_yellow'] = 400
		if args != None and 'output_thresholds' in args and 'last_sent_red' in args['output_thresholds']:
			self.bbstatus['outputs']['last_sent_red'] = args['output_thresholds']['last_sent_red']
		else:
			self.bbstatus['outputs']['last_sent_red'] = 800
		for b in goesr_abi_config.band:
			self.bbstatus['outputs']['bands'][b] = {'area':{'last':0},'tile':{'last':0}}

		# Missing Products
		self.bbstatus['missing'] = {'scancycles':{}}
		if args != None and 'missing_thresholds' in args and 'window_start' in args['missing_thresholds']:
			self.bbstatus['missing']['window_start'] = args['missing_thresholds']['window_start']
		else:
			self.bbstatus['missing']['window_start'] = 1200
		if args != None and 'missing_thresholds' in args and 'window_length' in args['missing_thresholds']:
			self.bbstatus['missing']['window_length'] = args['missing_thresholds']['window_length']
		else:
			self.bbstatus['missing']['window_length'] = 3600
		if args != None and 'missing_thresholds' in args and 'in_count_yellow' in args['missing_thresholds']:
			self.bbstatus['missing']['in_count_yellow'] = args['missing_thresholds']['in_count_yellow']
		else:
			self.bbstatus['missing']['in_count_yellow'] = 1
		if args != None and 'missing_thresholds' in args and 'in_count_red' in args['missing_thresholds']:
			self.bbstatus['missing']['in_count_red'] = args['missing_thresholds']['in_count_red']
		else:
			self.bbstatus['missing']['in_count_red'] = 5
		if args != None and 'missing_thresholds' in args and 'tile_count_yellow' in args['missing_thresholds']:
			self.bbstatus['missing']['tile_count_yellow'] = args['missing_thresholds']['tile_count_yellow']
		else:
			self.bbstatus['missing']['tile_count_yellow'] = 1
		if args != None and 'missing_thresholds' in args and 'tile_count_red' in args['missing_thresholds']:
			self.bbstatus['missing']['tile_count_red'] = args['missing_thresholds']['tile_count_red']
		else:
			self.bbstatus['missing']['tile_count_red'] = 5
		if args != None and 'missing_thresholds' in args and 'area_count_yellow' in args['missing_thresholds']:
			self.bbstatus['missing']['area_count_yellow'] = args['missing_thresholds']['area_count_yellow']
		else:
			self.bbstatus['missing']['area_count_yellow'] = 1
		if args != None and 'missing_thresholds' in args and 'area_count_red' in args['missing_thresholds']:
			self.bbstatus['missing']['area_count_red'] = args['missing_thresholds']['area_count_red']
		else:
			self.bbstatus['missing']['area_count_red'] = 5



	def update(self,msg):
		if msg['msg'] not in self.registered_messages:
			return

		if msg['msg'] == 'im_daemon-heartbeat':
			p = msg['payload']
			self.logger.info('heartbeat received {}/{}'.format(p['gid'],p['jid']))
			if p['gid'] not in self.bbstatus['jobs'] or p['jid'] not in self.bbstatus['jobs'][p['gid']]:
				return

			g = p['gid']
			j = p['jid']
			if g in self.bbstatus['jobs'] and j in self.bbstatus['jobs'][g]:
				if self.bbstatus['jobs'][g][j]['pid'] == -1:
					self.bbstatus['jobs'][g][j]['pid'] = p['active_pid']
				if self.bbstatus['jobs'][g][j]['last'] == 0:
					self.bbstatus['jobs'][g][j]['last'] = p['stamp']/1000
					return
				dt = p['stamp']/1000 - self.bbstatus['jobs'][g][j]['last']
				self.bbstatus['jobs'][g][j]['last'] = p['stamp']/1000
				if dt > self.job_thresholds['latency_red']:
					self.bbstatus['jobs'][g][j]['state'] = 'red'
				elif dt > self.job_thresholds['latency_yellow']:
					self.bbstatus['jobs'][g][j]['state'] = 'yellow'

				if p['active_pid'] != self.bbstatus['jobs'][g][j]['pid']:
					self.bbstatus['jobs'][g][j]['pid'] = p['active_pid']
					self.bbstatus['jobs'][g][j]['restarts'] += 1
					self.bbstatus['jobs'][g][j]['accumulated_restarts'] += 1
				bv = self.bbstatus['jobs'][g][j]
				bvstamp = time.strftime('%Y%m%d%H%M%S',time.gmtime(bv['last']))
				self.logger.info('Heartbeat:  {}/{} {} {} {} {} {}'.format(g,j,bvstamp,bv['state'],bv['pid'],bv['restarts'],bv['accumulated_restarts']))
			return

		elif msg['msg'] == 'ABI_L1b_Input':
			p = msg['payload']
			self.logger.info('abi_l1b_input {} {} {}'.format(p['abiscene'],p['abichan'],p['obstart']),fid=fid,lid=2)
			self.bbstatus['inputs']['bands'][p['abichan']]['last'] = p['rcvstamp']

			# scancycle
			obstime    = time.strptime(p['obstart'],'%Y%m%d%H%M%S')
			obsmin     = obstime.tm_min
			ssmin      = 15*int(obsmin/15)
			cyclestr   = time.strftime('%Y%m%d%H',obstime)+str(ssmin).rjust(2,'0')

			if cyclestr not in self.bbstatus['missing']['scancycles']:
				self.bbstatus['missing']['scancycles'][cyclestr] = {'modes':[],'inputs':[],'areas':[],'tiles':[]}
			scancycle = self.bbstatus['missing']['scancycles'][cyclestr]
			if p['abimode'] not in scancycle['modes']:
				scancycle['modes'].append(p['abimode'])
			scancycle['inputs'].append(p['abiscene']+'_'+str(p['abichan'])+'_'+str(p['obstart']))

		elif msg['msg'] == 'ABI_Output':
			p = msg['payload']
			if 'tileno' not in p:
				p['tileno'] = ''
			self.logger.info('abi_output {} {} {} {} {} {}'.format(p['obstart'],p['abimode'],p['abiscene'],p['abichan'],p['ftype'],p['tileno']),fid=fid,lid=3)
			self.bbstatus['outputs']['bands'][p['abichan']][p['ftype']]['last'] = p['posttime']

			# scancycle
			obstime    = time.strptime(p['obstart'],'%Y%m%d%H%M%S')
			obsmin     = obstime.tm_min
			ssmin      = 15*int(obsmin/15)
			cyclestr   = time.strftime('%Y%m%d%H',obstime)+str(ssmin).rjust(2,'0')

			if cyclestr not in self.bbstatus['missing']['scancycles']:
				self.bbstatus['missing']['scancycles'][cyclestr] = {'modes':[],'inputs':[],'areas':[],'tiles':[]}
			scancycle = self.bbstatus['missing']['scancycles'][cyclestr]
			if p['abimode'] not in scancycle['modes']:
				scancycle['modes'].append(p['abimode'])
			if p['ftype'] == 'tile':
				scancycle['tiles'].append(p['abiscene']+'_'+str(p['abichan'])+'_'+str(p['obstart']+'_'+str(p['tileno'])))
			else:
				scancycle['areas'].append(p['abiscene']+'_'+str(p['abichan'])+'_'+str(p['obstart']))

		elif msg['msg'] == 'bbmon-report-alert':
			self.logger.info('bbmon processing report alert',fid=fid,lid=4)
			content = {}
			content['type']    = 'telemetry'
			content['msg']     = 'BB_Monitor'
			content['stamp']   = 1000*time.time()
			payload = {}

			# job status
			payload['app_status']     = 'green'
			payload['red_jobs']       = ''
			payload['yellow_jobs']    = ''
			payload['restarted_jobs'] = ''
			payload['restart_alert']  = ''
			now = time.time()
			for gid in self.bbstatus['jobs']:
				for jid in self.bbstatus['jobs'][gid]:
					dt = now - self.bbstatus['jobs'][gid][jid]['last']
					if dt > self.job_thresholds['latency_red'] or self.bbstatus['jobs'][gid][jid]['state'] == 'red':
						payload['app_status'] = 'red'
						if len(payload['red_jobs']) > 0:
							payload['red_jobs'] += ','
						payload['red_jobs'] += str(gid)+'/'+str(jid)
					elif dt > self.job_thresholds['latency_yellow'] or self.bbstatus['jobs'][gid][jid]['state'] == 'yellow':
						if payload['app_status'] != 'red':
							payload['app_status'] = 'yellow'
						if len(payload['yellow_jobs']) > 0:
							payload['yellow_jobs'] += ','
						payload['yellow_jobs'] += str(gid)+'/'+str(jid)

					if self.bbstatus['jobs'][gid][jid]['restarts'] > 0:
						if payload['app_status'] != 'red':
							payload['app_status'] = 'yellow'
						if len(payload['restarted_jobs']) > 0:
							payload['restarted_jobs'] += ','
						payload['restarted_jobs'] += str(gid)+'/'+str(jid)

					if self.bbstatus['jobs'][gid][jid]['accumulated_restarts'] > self.job_thresholds['restart_red']:
						payload['app_status'] = 'red'
						if len(payload['restart_alert']) > 0:
							payload['restart_alert'] += ','
						payload['restart_alert'] += str(gid)+'/'+str(jid)
					elif self.bbstatus['jobs'][gid][jid]['accumulated_restarts'] > self.job_thresholds['restart_yellow']:
						if payload['app_status'] != 'red':
							payload['app_status'] = 'yellow'
						if len(payload['restart_alert']) > 0:
							payload['restart_alert'] += ','
						payload['restart_alert'] += str(gid)+'/'+str(jid)


					self.bbstatus['jobs'][gid][jid]['state']   = 'green'
					self.bbstatus['jobs'][gid][jid]['restarts'] = 0

			# input status
			payload['lhcp_input']  = 'green'
			payload['rhcp_input']  = 'green'
			for b in self.bbstatus['inputs']['bands']:
				dt = now - self.bbstatus['inputs']['bands'][b]['last']
				if self.bbstatus['inputs']['bands'][b]['pol'] == 'RHCP':
					if payload['rhcp_input'] != 'red' and dt > self.bbstatus['inputs']['rhcp_last_rcvd_yellow']:
						payload['rhcp_input'] = 'yellow'
					if dt > self.bbstatus['inputs']['rhcp_last_rcvd_red']:
						payload['rhcp_input'] = 'red'
				elif self.bbstatus['inputs']['bands'][b]['pol'] == 'LHCP':
					if payload['lhcp_input'] != 'red' and dt > self.bbstatus['inputs']['lhcp_last_rcvd_yellow']:
						payload['lhcp_input'] = 'yellow'
					if dt > self.bbstatus['inputs']['lhcp_last_rcvd_red']:
						payload['lhcp_input'] = 'red'

			# output status
			payload['area_output']  = 'green'
			payload['tile_output']  = 'green'
			for b in self.bbstatus['outputs']['bands']:
				#area
				dt = now - self.bbstatus['outputs']['bands'][b]['area']['last']
				if payload['area_output'] != 'red' and dt > self.bbstatus['outputs']['last_sent_yellow']:
					payload['area_output'] = 'yellow'
				if dt > self.bbstatus['outputs']['last_sent_red']:
					payload['area_output'] = 'red'
				#tiles
				dt = now - self.bbstatus['outputs']['bands'][b]['tile']['last']
				if payload['tile_output'] != 'red' and dt > self.bbstatus['outputs']['last_sent_yellow']:
					payload['tile_output'] = 'yellow'
				if dt > self.bbstatus['outputs']['last_sent_red']:
					payload['tile_output'] = 'red'

			# missing products
			payload['missing_input'] = 'green'
			payload['missing_areas'] = 'green'
			payload['missing_tiles'] = 'green'
			scancycles = self.bbstatus['missing']['scancycles']
			late    = now - self.bbstatus['missing']['window_start']
			early   = late - self.bbstatus['missing']['window_length']
			dellist = []
			for c in scancycles:
				scancycle = scancycles[c]
				m = scancycle['modes']
				if '3' in m and '4' in m:
					mstr = 'B'
				elif '3' in m:
					mstr = '3'
				else:
					mstr = '4'

				if '3' in m:
					incount   = 544
					areacount = 544
					tilecount = 1904
				elif '4' in m:
					incount   = 48
					areacount = 48
					tilecount = 2976

				cstamp = calendar.timegm(time.strptime(c,'%Y%m%d%H%M'))
				nocheck = False
				if cstamp < early:
					dellist.append(c)
					checked = 'aged_off'
				if cstamp > late:
					nocheck = True
					checked = 'premature'
				if cstamp < self.init_time:
					nocheck = True
					checked = 'startup'

				if mstr == 'B':
					nocheck = True

				if not nocheck:
					checked = 'checked'
					missing_inputs = incount   - len(scancycle['inputs'])
					if missing_inputs > self.bbstatus['missing']['in_count_yellow']:
						payload['missing_input'] = 'yellow'
					if missing_inputs > self.bbstatus['missing']['in_count_red']:
						payload['missing_input'] = 'red'

					missing_areas  = areacount - len(scancycle['areas'])
					if missing_areas > self.bbstatus['missing']['area_count_yellow']:
						payload['missing_areas'] = 'yellow'
					if missing_areas > self.bbstatus['missing']['area_count_red']:
						payload['missing_areas'] = 'red'

					missing_tiles  = tilecount - len(scancycle['tiles'])
					if missing_tiles > self.bbstatus['missing']['tile_count_yellow']:
						payload['missing_tiles'] = 'yellow'
					if missing_tiles > self.bbstatus['missing']['tile_count_red']:
						payload['missing_tiles'] = 'red'

				self.logger.info('Scancycle {}:  {} {} {} {} {}'.format(c,mstr,len(scancycle['inputs']),len(scancycle['areas']),len(scancycle['tiles']),checked))

			for d in dellist:
				del self.bbstatus['missing']['scancycles'][d]

			content['payload'] = payload
			self.publish(content)
			self.logger.info('Published a BB_Monitor record',fid=fid,lid=5)


class GoesStatusInput(im_agent99.Agent99):
	defs = {}
	defs['GOES_Status_Input'] = {}

	def __init__(self, dossier, mi6_queue, logger, args=None):
		super().__init__(dossier, mi6_queue, logger)

		self.registered_messages = []
		self.registered_messages.append('4.56')

		self.args      = args
		self.sectors   = {}


	def update(self, msg):
		if msg['ident']['raw'] not in self.registered_messages:
			return

		if msg['ident']['module_id'] == 4 and msg['ident']['msgid'] == 56:
            # parse for scene, start time, size, creation time, ABI Mode, Band
			msgsplit   = msg['payload'].split()
			tile_time  = float(msgsplit[2].split('_')[0])
			tile_name  = msgsplit[3].split('/')[-1]
			split_name = tile_name.split('_')
			sat_id     = split_name[0]
			sat_mode   = int(split_name[1])
			scene      = split_name[2]
			center_lat = float(msgsplit[5].split('=')[1])
			center_lon = float(msgsplit[6].split('=')[1])

			if sat_id not in self.sectors:
				self.sectors[sat_id] = {}

			if scene not in self.sectors[sat_id]:
				self.sectors[sat_id][scene] = {}

			if 'obs_time' not in self.sectors[sat_id][scene] or self.sectors[sat_id][scene]['obs_time'] != tile_time:
				# Dealing with a new instance of a given scene (or the first scene of this type)
				self.sectors[sat_id][scene]['obs_time'] = tile_time

				inrec = {}
				inrec['rcvstamp'] = msg['timestamp']
				inrec['sat_id']   = sat_id
				inrec['mode']     = sat_mode
				inrec['scene']    = scene
				inrec['obs_time'] = tile_time
				inrec['clat']     = center_lat
				inrec['clon']     = center_lon

				self.makeDeadDrop('telemetry', 'GOES_Status_Input', inrec)
				self.logger.info('GOES new scene {} mode {} obs_time {} center {}/{}'.format(scene, sat_mode, tile_time, center_lat, center_lon))
