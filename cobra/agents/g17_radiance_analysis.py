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
imports.append({'module':'sys',             'as':'sys',             'src':'baseline'})
imports.append({'module':'time',            'as':'time',            'src':'baseline'})
imports.append({'module':'datetime',        'as':'datetime',        'src':'baseline'})
imports.append({'module':'calendar',        'as':'calendar',        'src':'baseline'})
imports.append({'module':'im_agent99',      'as':'im_agent99',      'src':'isatss'})
imports.append({'module':'im_agent13',      'as':'im_agent13',      'src':'isatss'})
imports.append({'module':'im_exceptions',   'as':'ime',             'src':'isatss'})

import isatss_init
from turtledemo import fractalcurves
isatss_init.load_imports(__name__,imports)
isc = isatss_init.import_config()
#globals
fid = isatss_init.get_fid(__file__)

class RadianceAnalysis(im_agent99.Agent99):
	"""
	"""
	defs = {}
	defs['GOES_Radiance_Monitor'] = {}
	defs['GOES_Radiance_Monitor']['payload']  = {}
	defs['GOES_Radiance_Monitor']['payload']['site']       = {'type':'str',   'desc':'site that processed this message'}
	defs['GOES_Radiance_Monitor']['payload']['host_id']    = {'type':'str',   'desc':'host ID processing this message'}
	defs['GOES_Radiance_Monitor']['payload']['scene']      = {'type':'str',   'desc':'ABI scene',          'range':['FD', 'CONUS', 'M1', 'M2']}
	defs['GOES_Radiance_Monitor']['payload']['band']       = {'type':'int',   'desc':'ABI channel number'}
	defs['GOES_Radiance_Monitor']['payload']['scene_time'] = {'type':'int',   'desc':'unix scene start time'}
	defs['GOES_Radiance_Monitor']['payload']['frac']       = {'type':'int',   'desc':'# non-zero pixels/tile div by # pixels'}
	defs['GOES_Radiance_Monitor']['payload']['avg']        = {'type':'int',   'desc':'total value of pixels / # non-zero values'}

	def __init__(self, dossier, mi6_queue, logger, args=None):
		"""
		Calls the superclass __init__() and initializes the sector
		dictionary, instance args, and registere_messages to be
		processed.
		"""
		super().__init__(dossier, mi6_queue, logger)

		self.registered_messages = []
		self.registered_messages.append('1006.8')

		self.args      = args
		self.scenes    = {}
		if args != None and 'sat_id' in args:
			self.sat_id = args['sat_id']
		else:
			self.sat_id = 'G17'


	def update(self, msg):
		"""
		Called by an MI6 mission with a candidate filtered message.
		The only message processed is 1006.8 (im_grb_abii msg 8), which is
		produced when a tile is successfully completed.
		"""
		if msg['ident']['raw'] not in self.registered_messages:
			return

		if msg['ident']['module_id'] == 1006 and msg['ident']['msgid'] == 8:
			largs=msg['payload'].split()
			ldict={}
			for a in largs:
				asplit=a.split(':')
				ldict[asplit[0]]=asplit[1]

			s=ldict['s']
			if s not in self.scenes:
				self.scenes[s]= {}

			t=ldict['t']
			#if t not in self.scenes[s]:
			#	self.scenes[s][t] = {}
			scene_time = float(calendar.timegm(datetime.datetime.strptime(t, '%Y%m%d_%H%M%S').timetuple()))

			b = int(ldict['b'])
			if b not in self.scenes[s]:
				self.scenes[s][b] = {'nz':0,'nel':0,'avgv':0.0,'nt':0}

			if 't' in self.scenes[s][b] and self.scenes[s][b]['t'] != scene_time:
				if b >= 8:
					r = self.scenes[s][b]
					frac = 1.0*r['nz']/r['nel']
					avg = 1.0*r['avgv']/r['nt']
					#TODO: Output scene, band, time, frac, avg to dead drop if band == 10
					inrec = {}
					inrec['site']       = isc.site
					inrec['host_id']    = self.host_id
					inrec['sat_id']     = self.sat_id
					inrec['scene']      = s
					inrec['band']       = b
					inrec['scene_time'] = int(self.scenes[s][b]['t']*1000)
					inrec['frac']       = frac
					inrec['avg']        = avg
					self.makeDeadDrop('telemetry', 'GOES_Radiance_Monitor', inrec)
					self.logger.info('GOES-17 new scene {} scene_time {} band {}'.format(s, inrec['scene_time'], b))
					#logargs: 

				self.scenes[s][b] = {'nz':0,'nel':0,'avgv':0.0,'nt':0}
			else:
				self.scenes[s][b]['t'] = scene_time

			self.scenes[s][b]['nz'] += int(ldict['nz'])
			self.scenes[s][b]['nt'] += 1
			self.scenes[s][b]['nel'] += int(ldict['nel'])
			self.scenes[s][b]['avgv'] += 1.0*int(ldict['tv'])/int(ldict['nz'])


class RadianceAggregator(im_agent13.Agent13):
	defs = {}
	defs['GOES_Radiance_Monitor']  = {}

	def __init__(self, logger, publishQ, args=None):
		super().__init__(logger, publishQ, args)
		self.registered_messages['GOES_Scene_Change']  = {}


	def update(self, msg):
		if msg['msg'] not in self.registered_messages:
			return

		if msg['msg'] == 'GOES_Radiance_Monitor':
			content = {}
			content['type']    = 'telemetry'
			content['msg']     = 'GOES_Radiance_Values'
			content['payload'] = msg['payload']
			self.publish(content)

