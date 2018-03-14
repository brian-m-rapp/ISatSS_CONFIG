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
imports.append({'module':'calendar',      'as':'calendar',      'src':'baseline'})
imports.append({'module':'sys',           'as':'sys',           'src':'baseline'})
imports.append({'module':'time',          'as':'time',          'src':'baseline'})
imports.append({'module':'im_agent13',    'as':'im_agent13',    'src':'isatss'})
imports.append({'module':'im_agent99',    'as':'im_agent99',    'src':'isatss'})
imports.append({'module':'im_exceptions', 'as':'ime',           'src':'isatss'})
import isatss_init
isatss_init.load_imports(__name__,imports)
isc = isatss_init.import_config()
#globals
#fid = isatss_init.get_fid(__file__)
fid=9999

logger_items = {}
logger_items[1]  = {'class':'BBMon','method':'update','level':'info'}
logger_items[2]  = {'class':'BBMon','method':'update','level':'info'}
logger_items[3]  = {'class':'BBMon','method':'update','level':'info'}
logger_items[4]  = {'class':'BBMon','method':'update','level':'info'}
logger_items[5]  = {'class':'BBMon','method':'update','level':'info'}
logger_items[6]  = {'class':'ABIL1BInput','method':'update','level':'info'}
logger_items[7]  = {'class':'BBMon','method':'update','level':'warning'}

class BBMon(im_agent13.Agent13):
	defs = {}
	defs['BB_Monitor'] = {}

	def __init__(self, logger, publishQ, args=None):
		super().__init__(logger, publishQ, args)
		self.registered_messages['im_daemon-heartbeat'] = {}
		self.registered_messages['bbmon-report-alert']  = {'interval':300}
		self.registered_messages['ABI_L1b_Input']       = {}
		self.registered_messages['ABI_Output']          = {}

		self.exclude = {}
		if args != None and 'excluded_jobs' in args:
			self.exclude = args['excluded_jobs']

		self.abi_thresholds = {'3':{},'4':{},'both':{}}
		self.abi_thresholds['3']['inputs']    = {'green':544, 'yellow':500}
		self.abi_thresholds['3']['tiles']     = {'green':1904,'yellow':1800}
		self.abi_thresholds['3']['areas']     = {'green':544, 'yellow':500}
		self.abi_thresholds['4']['inputs']    = {'green':48,  'yellow':40}
		self.abi_thresholds['4']['tiles']     = {'green':2976,'yellow':2800}
		self.abi_thresholds['4']['areas']     = {'green':96,  'yellow':80}
		self.abi_thresholds['both']['inputs'] = {'green':48,  'yellow':40}
		self.abi_thresholds['both']['tiles']  = {'green':1904,'yellow':1800}
		self.abi_thresholds['both']['areas']  = {'green':96,  'yellow':80}
		if args != None and 'abi_thresholds' in args:
			for m in args['abi_thresholds']:
				for e in args['abi_thresholds'][m]:
					for s in args['abi_thresholds'][m][e]:
						self.abi_thresholds[m][e][s] = args['abi_thresholds'][m][e][s]


		self.jobtotal = 0
		self.bbstatus_blank = {'jobs':{},'abi':{}}
		self.bbstatus_blank['abi'][0]  = {'inputs':0,'modes':[],'tiles':0,'areas':0}
		self.bbstatus_blank['abi'][1]  = {'inputs':0,'modes':[],'tiles':0,'areas':0}
		self.bbstatus_blank['abi'][2]  = {'inputs':0,'modes':[],'tiles':0,'areas':0}
		self.bbstatus_blank['abi'][15] = {'inputs':0,'modes':[],'tiles':0,'areas':0}
		for gid in isc.groups:
			if gid == 0:
				continue
			self.bbstatus_blank['jobs'][gid] = {}
			for jid in isc.groups[gid]['jobs']:
				if gid in self.exclude and jid in self.exclude[gid]:
					continue
				self.bbstatus_blank['jobs'][gid][jid] = {'active_pid':None,'last_heard':None,'checked_in':0,'restart':False}
				self.jobtotal += 1
		self.bbstatus = self.bbstatus_blank.copy()



	def update(self,msg):
		if msg['msg'] not in self.registered_messages:
			return

		if msg['msg'] == 'im_daemon-heartbeat':
			p = msg['payload']
			if p['gid'] not in self.bbstatus['jobs'] or p['jid'] not in self.bbstatus['jobs'][p['gid']]:
				return

			tstring = time.strftime('%Y%m%d%H%M%S',time.gmtime(p['stamp']/1000.0))
			self.logger.info('processing heartbeat for {}/{} {}'.format(p['gid'],p['jid'],tstring),fid=fid,lid=1)
			j = self.bbstatus['jobs'][p['gid']][p['jid']]

			if j['active_pid'] == None:
				self.bbstatus['jobs'][p['gid']][p['jid']]['active_pid'] = p['active_pid']

			elif j['active_pid'] != p['active_pid']:
				# application was restarted
				self.bbstatus['jobs'][p['gid']][p['jid']]['active_pid'] = p['active_pid']
				self.bbstatus['jobs'][p['gid']][p['jid']]['restart']    = True

			self.bbstatus['jobs'][p['gid']][p['jid']]['last_heard']     = p['stamp']
			self.bbstatus['jobs'][p['gid']][p['jid']]['checked_in']     += 1

		elif msg['msg'] == 'ABI_L1b_Input':
			p = msg['payload']
			self.logger.info('bbmon abi l1b input {} {} {}'.format(p['abiscene'],p['abichan'],p['obstart']),fid=fid,lid=2)
			if p['abimode'] not in self.bbstatus['abi'][0]['modes']:
					self.bbstatus['abi'][0]['modes'].append(p['abimode'])
			self.bbstatus['abi'][0]['inputs'] += 1

		elif msg['msg'] == 'ABI_Output':
			p = msg['payload']
			self.logger.info('abi output {}'.format(p['obstart']),fid=fid,lid=3)
			if p['abimode'] not in self.bbstatus['abi'][0]['modes']:
					self.bbstatus['abi'][0]['modes'].append(p['abimode'])
			if p['ftype']   == 'tile':
				self.bbstatus['abi'][0]['tiles'] += 1
			elif p['ftype'] == 'area':
				self.bbstatus['abi'][0]['areas'] += 1


		elif msg['msg'] == 'bbmon-report-alert':
			self.logger.info('bbmon processing report alert',fid=fid,lid=4)
			content = {}
			content['type']    = 'telemetry'
			content['msg']     = 'BB_Monitor'
			content['stamp']   = 1000*time.time()
			payload = {'jobtotal':self.jobtotal,'checkins':0,'restarts':0,'app_status':'green'}
			for gid in self.bbstatus['jobs']:
				for jid in self.bbstatus['jobs'][gid]:
					j = self.bbstatus['jobs'][gid][jid]
					payload['checkins'] += j['checked_in']
					if j['restart']:
						payload['restarts'] += 1
					if j['checked_in'] < 4:
						payload['app_status'] = 'red'
						self.logger.warning('Red Job:  {}/{}'.format(gid,jid),fid=fid,lid=7)

			self.bbstatus['abi'][15]  = {'inputs':0,'modes':[],'tiles':0,'areas':0}
			for m in [0,1,2]:
				b = self.bbstatus['abi'][m]
				self.bbstatus['abi'][15]['inputs'] += b['inputs']
				self.bbstatus['abi'][15]['tiles']  += b['tiles']
				self.bbstatus['abi'][15]['areas']   += b['areas']
				for am in b['modes']:
					if am not in self.bbstatus['abi'][15]['modes']:
						self.bbstatus['abi'][15]['modes'].append(am)

			abistatus = self.bbstatus['abi'][15]
			if '3' in abistatus['modes'] and '4' in abistatus['modes']:
				m = 'both'
			elif '3' in abistatus['modes']:
				m = '3'
			elif '4' in abistatus['modes']:
				m = '4'
			for e in self.abi_thresholds[m]:
				if abistatus[e] >= self.abi_thresholds[m][e]['green']:
					self.bbstatus['abi'][e+'_status'] = 'green'
				elif abistatus[e] >= self.abi_thresholds[m][e]['yellow']:
					self.bbstatus['abi'][e+'_status'] = 'yellow'
				else:
					self.bbstatus['abi'][e+'_status'] = 'red'

			payload['abi'] = self.bbstatus['abi'].copy()

			content['payload'] = payload
			self.publish(content)
			self.logger.info('Published a BB_Monitor record',fid=fid,lid=5)

			self.bbstatus['abi'][2]  = self.bbstatus['abi'][1].copy()
			self.bbstatus['abi'][1]  = self.bbstatus['abi'][0].copy()
			self.bbstatus['abi'][0]  = {'inputs':0,'modes':[],'tiles':0,'areas':0}
			for gid in self.bbstatus['jobs']:
				for jid in self.bbstatus['jobs'][gid]:
					self.bbstatus['jobs'][gid][jid]['checked_in'] = 0
					self.bbstatus['jobs'][gid][jid]['restart']    = False

class ABIL1BInput(im_agent99.Agent99):
	defs = {}
	defs['ABI_L1b_Input'] = {}

	def __init__(self, dossier, mi6_queue, logger, args=None):
		super().__init__(dossier, mi6_queue, logger)

		self.registered_messages = []
		self.registered_messages.append('1004.5')
		self.args = args


	def update(self, msg):
		if msg['ident']['raw'] not in self.registered_messages:
			return

		if msg['ident']['module_id'] == 1004 and msg['ident']['msgid'] == 5:
			inrec = {}
            # parse for scene, start time, size, creation time, ABI Mode, Band
			msgsplit       = msg['payload'].split()
			node           = int(msgsplit[5])
			if node not in self.args['receipt_nodes']:
				return

			inrec['fsize']          = int(msgsplit[7])
			fname                   = msgsplit[2]
			fnamesplit              = fname.split('_')
			inrec['sat']            = fnamesplit[2]
			sname                   = fnamesplit[1]
			snamesplit              = sname.split('-')
			mcsplit                 = snamesplit[3].split('C')
			inrec['abichan']        = int(mcsplit[1])
			inrec['abimode']        = mcsplit[0].replace('M','')
			inrec['abiscene']       = snamesplit[2].replace('Rad','')
			obstart_jdate           = fnamesplit[3].replace('s','')[:-1]
			obstart_tuple           = time.strptime(obstart_jdate,'%Y%j%H%M%S')
			inrec['obstart']        = time.strftime('%Y%m%d%H%M%S',obstart_tuple)
			inrec['obstart_stamp']  = calendar.timegm(obstart_tuple)
			creation_jdate          = fnamesplit[5].replace('c','')[:-3]
			creation_tuple          = time.strptime(creation_jdate,'%Y%j%H%M%S')
			inrec['creation']       = time.strftime('%Y%m%d%H%M%S',creation_tuple)
			inrec['creation_stamp'] = calendar.timegm(creation_tuple)
			inrec['rcvstamp']       = msg['timestamp']

			self.makeDeadDrop('telemetry', 'ABI_L1b_Input', inrec)
			self.logger.info('bbmon abi l1b input {} {} {}'.format(inrec['abiscene'],inrec['abichan'],inrec['obstart']),fid=fid,lid=6)

class ABIOutput(im_agent99.Agent99):
	defs = {}
	defs['ABI_Output'] = {}
	scene_decode = {'M1':'M1','M2':'M2','FD':'F','CONUS':'C','CO':'C'}

	def __init__(self, dossier, mi6_queue, logger, args=None):
		super().__init__(dossier, mi6_queue, logger)

		self.registered_messages = []
		self.registered_messages.append('13.5')

		self.args = args

	def update(self, msg):
		if msg['ident']['raw'] not in self.registered_messages:
			return

		if msg['ident']['module_id'] == 13 and msg['ident']['msgid'] == 5:
			# parse for scene, start time, size, creation time, ABI Mode, Band
			outrec = {}

			msgsplit = msg['payload'].split()
			if '.nc' in msgsplit[1]:
				outrec['fsize']    = int(msgsplit[8])
				nsplit             = msgsplit[1].split('_')
				outrec['sat']      = nsplit[0]
				outrec['abimode']  = nsplit[1]
				outrec['abiscene'] = ABIOutput.scene_decode[nsplit[2]]
				outrec['abichan']  = int(nsplit[3])
				outrec['obstart']  = nsplit[5].replace('.nc','')
				outrec['tileno']   = nsplit[4]
				outrec['posttime'] = msg['timestamp']
				outrec['ftype']    = 'tile'

			else:
				outrec['fsize']    = int(msgsplit[5])
				prodid             = msgsplit[2]
				fname              = msgsplit[1]
				fnamesplit         = fname.split('.')[1].split('_')
				outrec['sat']      = fnamesplit[0]
				outrec['abimode']  = fnamesplit[1]
				outrec['abiscene'] = ABIOutput.scene_decode[prodid[2:4]]
				outrec['abichan']  = int(prodid[9:11])
				outrec['obstart']  = fname.split('.')[0]
				outrec['posttime'] = msg['timestamp']
				outrec['ftype']    = 'area'

			self.makeDeadDrop('telemetry', 'ABI_Output', outrec)

