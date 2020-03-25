"""
    IDP Satellite Support Subsystem
    Copyright (C) 2016-2018 Joseph K. Zajic (joe.zajic@noaa.gov), Brian M. Rapp (brian.rapp@noaa.gov)

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
imports.append({'module':'numpy',         'as':'np',            'src':'numpy'})
imports.append({'module':'struct',        'as':'struct',        'src':'baseline'})
imports.append({'module':'math',          'as':'math',          'src':'baseline'})
imports.append({'module':'time',          'as':'time',          'src':'baseline'})
imports.append({'module':'im_ncfile',     'as':'im_ncfile',     'src':'isatss'})
imports.append({'module':'datetime',      'as':'datetime',      'src':'baseline'})
imports.append({'module':'calendar',      'as':'calendar',      'src':'baseline'})
imports.append({'module':'os',            'as':'os',            'src':'baseline'})
imports.append({'module':'pyresample',    'as':'pr',            'src':'baseline'})
import isatss_init
isatss_init.load_imports(__name__,imports)
isc = isatss_init.import_config()

# global variables
fid = isatss_init.get_fid(__file__)

def midpoint(lat1, lon1, lat2, lon2):
	dLon = math.radians(lon2 - lon1)
	lat1 = math.radians(lat1)
	lat2 = math.radians(lat2)
	lon1 = math.radians(lon1)

	Bx = math.cos(lat2) * math.cos(dLon)
	By = math.cos(lat2) * math.sin(dLon)
	lat3 = math.atan2(math.sin(lat1) + math.sin(lat2), math.sqrt((math.cos(lat1) + Bx) * (math.cos(lat1) + Bx) + By * By))
	lon3 = lon1 + math.atan2(By, math.cos(lat1) + Bx)
	lat3 = round(math.degrees(lat3), 6)
	lon3 = round(math.degrees(lon3), 6)

	if lon3 <= -180.0:
		lon3 += 360.0
	elif lon3 > 180.0:
		lon3 -= 360.0

	return(lat3, lon3)

def midLon(lon1, lon2):
	return midpoint(0.0, lon1, 0.0, lon2)[1]

class GeoRGE:
	"""
	"""
	def __init__(self, args,logger, info):
		"""
		Initialize self, arguments, logger and information.

		Arguments:
			dict infodict - must include a 'file' key containing fullpath name for input data set
			dict args     - must include an 'nspec' key containing a netcdf output definition dictionary
			obj  logger   - an instance of im_log.ISatSSLog
			obj  info     - an instance of im_info.ISatSSInfo

		Instance Variables created:
			dict infodict    - from infodict argument
			dict args        - from args argument
			bool writeflag   - True indicates that output file can be generated
			dict payload     - Notifications dictionary (empty initialization)
			obj  logger      - from logger argument
			obj  infomsg     - from info argument
			bool delete_file - True indicates that input file can be deleted.  Set by write method
			dict odata       - dictionary of output data items for use with im_ncfile.INCFile.populate 

		"""
		self.args      = args
		self.writeflag = True
		self.payload   = {}
		self.logger    = logger
		self.infomsg   = info
		self.delete_file = False
		self.data = {}
		self.vdims = {}

	def close(self):
		"""
		Closes the file.
		"""
		#self.nsf.close()


	def update(self, infodict):
		"""

		open file


		"""
		ncf= im_ncfile.INCFile(infodict['file'],mode='r')
		for v in ncf.variables:
			print(v)
			self.data[v] = ncf.get(v,flat=False)
			self.vdims[v] = ncf.ncf.variables[v].dimensions

		lats = self.data['Latitude_lores']
		lons = self.data['Longitude_lores']

		minlat = lats.min()
		maxlat = lats.max()
		ctrlat = (maxlat+minlat)/2
		minlon = lons.min()
		maxlon = lons.max()
		ctrlon = midLon(minlon, maxlon)

		print('Center Lat: {}'.format(ctrlat))
		print('Center Lon: {}'.format(ctrlon))
		projdef = None
		for p in self.args['proj']:
			proj = self.args['proj'][p]
			if ctrlat >= proj['minlat'] and ctrlat < proj['maxlat']:
				projdef = p
				break
		if projdef is None:
			self.logger.error('No applicable projection for center latitude={}'.format(ctrlat))
			return
		print('Projection Definition: {}'.format(projdef))

		projdict = {}
		projdict['a'] = 6371200
		projdict['b'] = 6371200
		ncspec   = {}
		ncspec['globalmeta'] = {}
		if projdef == 'southpolar':
			projdict['proj'] = 'stere'
			projdict['lon_0'] = ctrlon
		elif projdef == 'southlamb':
			projdict['proj'] = 'lcc'
			projdict['lon_0'] = ctrlon
			projdict['lat_0'] = ctrlat
			projdict['lat_1'] = ctrlat
			projdict['lat_2'] = ctrlat
		elif projdef == 'merc':
			projdict['proj'] = 'merc'
			projdict['lon_0'] = ctrlon
		elif projdef == 'northlamb':
			projdict['proj'] = 'lcc'
			projdict['lon_0'] = ctrlon
			projdict['lat_0'] = ctrlat
			projdict['lat_1'] = ctrlat
			projdict['lat_2'] = ctrlat
		elif projdef == 'northpolar':
			projdict['proj'] = 'stere'
			projdict['lon_0'] = ctrlon


		swath = pr.geometry.SwathDefinition(lons=lons,lats=lats)
		print('projdict: {}'.format(projdict))
		bb    = swath.compute_optimal_bb_area(proj_dict=projdict)
		print('Bounding Box: {}'.format(dir(bb)))
		print('Area Extent: {}'.format(bb.area_extent))
		area = pr.geometry.AreaDefinition(bb.area_id, projdef, projdict['proj'], projdict, 1024, 1024, bb.area_extent)
		print('Area: {}'.format(area))
		swath_con_37v = pr.image.ImageContainerNearest(self.data['Temp_37GHz_V'], swath, radius_of_influence=5000)
		print('swath_con_37v: {}'.format(swath_con_37v))
		area_con_37v = swath_con_37v.resample(area)
		print('area_con_37v: {}'.format(area_con_37v.image_data))

		return

		self.odata = {}

		self.odata['filename']  = os.path.splitext(os.path.basename(infodict['file']))[0] + '_ssmi.nc'

		oncf = im_ncfile.INCFile(prodinfo=self.args['ncspec'],mode='w',content=self.odata,info=self.infomsg)
		oncf.populate()
		oncf.write()

