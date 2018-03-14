# isatss goes-r 2km abi l1b to fixed grid tiles

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
job['name']  = 'george_goesr_test_tiles_scmirecttiles'
job['cmd']   = 'george'
job['class'] = 'GeoRGE'
job['log']   = 'george_goesr_test_tiles_scmirecttiles_log'

job['notifications'] = {}
job['notifications']['ncm'] = {'node':8,'enabled':True,'fields':['file','node'],'prefix':'abi_fixed_tiles'}
job['notifications']['mon'] = {'node':16,'enabled':False,'fields':['file'],'prefix':'abi_fixed_tiles'}

job['data']  = {}
job['data']['products'] = {}
job['data']['products']['location']   = {'node':15, 'path':'goesr/reprojected'}
job['data']['products']['aging']      = {'window':7200, 'mode':'nested','fmt':'%Y%m%d%H%M%S.nc','extract':{'method':'tail','nchars':17}}
job['data']['products']['method']     = {'technique':'inplace'}
job['data']['infoncm']                = {}
job['data']['infoncm']['location']    = {'node':8}
job['data']['infoncm']['filter']      = {'type':'starts','test':job['notifications']['ncm']['prefix']}
job['data']['infoncm']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['infoncm']['method']      = {'technique':'inplace'}
job['data']['infoncm']['activeonly']  = True
job['data']['infoncm']['schedule']    = {'interval':600}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':1,'path':'log'}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['pause_empty'] = 5
job['qlimit']      = 100	# number of queued items to process in single run of the process method
job['maxopen']     = 500	# maximum number of input files to hold open at any one time
job['cache_life']  = 1200
job['cache_check'] = 120

job['input_type']  = {'type':'infofile','node':12,'delete_file':False, 'delete_info':True}

job['cntl_node']     = 13


job['hash_definition'] = []
job['hash_definition'].append({'parm':'reftime','meta':{'src':'globalmeta/start_date_time','fmt':'float','method':'string_to_unixtime','in_tfmt':'%Y%j%H%M%S'},'info':'reftime', 'part':'dynamic'})
job['hash_definition'].append({'parm':'scene',  'meta':{'src':'globalmeta/source_scene','fmt':'str','translate':{'Full Disk':'FD','CONUS':'CO','Mesoscale-1':'M1','Mesoscale-2':'M2'}},    'info':'scene',   'part':'product'})
job['hash_definition'].append({'parm':'mode',   'meta':{'src':'globalmeta/abi_mode','fmt':'str'},                                       'info':'mode',    'part':'product'})
job['hash_definition'].append({'parm':'band',   'meta':{'src':'globalmeta/channel_id','fmt':'int'},                                     'info':'band',    'part':'product'})
job['hash_definition'].append({'parm':'x0',     'meta':{'src':'globalmeta/tile_column_offset','fmt':'int'},                             'info':'x0',      'part':'tile'})
job['hash_definition'].append({'parm':'y0',     'meta':{'src':'globalmeta/tile_row_offset','fmt':'int'},                                'info':'y0',      'part':'tile'})
job['hash_definition'].append({'parm':'xlen',   'meta':{'src':'globalmeta/product_tile_width','fmt':'int'},                             'info':'xlen',    'part':'tile'})
job['hash_definition'].append({'parm':'ylen',   'meta':{'src':'globalmeta/product_tile_height','fmt':'int'},                            'info':'ylen',    'part':'tile'})

job['grid_definition'] = []
job['grid_definition'].append({'parm':'type',   'meta':{'default':'ABIFixedGrid'},                                              'info':'type'})
job['grid_definition'].append({'parm':'ncname', 'meta':{'default':'fixedgrid_projection'},                                      'info':'ncname'})
job['grid_definition'].append({'parm':'xlen',   'meta':{'src':'globalmeta/product_columns','fmt':'int'},                        'info':'xlen'})
job['grid_definition'].append({'parm':'ylen',   'meta':{'src':'globalmeta/product_rows','fmt':'int'},                           'info':'ylen'})
ang_stack        = [{'src':'variables/x/attr/scale_factor','fmt':'float'}]
ang_stack.append({'src':'variables/x/attr/units','translate':{'microradian':1.0e-6}})
ang_stack.append('*')
job['grid_definition'].append({'parm':'ang',    'meta':{'method':'calc','stack':ang_stack,'fmt':'float'},                       'info':'ang',     'part':'parms'})
az_off_stack     = [{'src':'variables/x/attr/add_offset','fmt':'float'}]
az_off_stack.append({'src':'variables/x/attr/scale_factor','fmt':'float'})
az_off_stack.append({'src':'globalmeta/tile_column_offset','fmt':'float'})
az_off_stack.append('*')
az_off_stack.append('-')
az_off_stack.append({'src':'variables/x/attr/units','translate':{'microradian':1.0e-6}})
az_off_stack.append('*')
job['grid_definition'].append({'parm':'az_off', 'meta':{'method':'calc','stack':az_off_stack,'fmt':'float'},                                     'info':'az_off',  'part':'parms'})
el_off_stack     = [{'src':'variables/y/attr/add_offset','fmt':'float'}]
el_off_stack.append({'src':'variables/y/attr/scale_factor','fmt':'float'})
el_off_stack.append({'src':'globalmeta/tile_row_offset','fmt':'float'})
el_off_stack.append('*')
el_off_stack.append('-')
el_off_stack.append({'src':'variables/y/attr/units','translate':{'microradian':1.0e-6}})
el_off_stack.append('*')
job['grid_definition'].append({'parm':'el_off', 'meta':{'method':'calc','stack':el_off_stack,'fmt':'float'},                     'info':'el_off',  'part':'parms'})
job['grid_definition'].append({'parm':'lon0',   'meta':{'src':'globalmeta/satellite_longitude','fmt':'float'},                  'info':'lon0',    'part':'parms'})

job['grids']              = {}
job['grids'][1]           = {'type':'Rectilinear','xlen':4500,'ylen':4500, 'ncname':'rectilinear_projection'}		#2km FD rectilinear
job['grids'][1]['parms']  = {'j0':2250,'lat0':0.0,'i0':2250,'lon0':-89.5,'dlat':0.0312,'dlon':0.0312}
job['grids'][2]           = {'type':'Rectilinear','xlen':9000,'ylen':9000, 'ncname':'rectilinear_projection'}		#1km FD rectilinear
job['grids'][2]['parms']  = {'j0':4500,'lat0':0.0,'i0':4500,'lon0':-89.5,'dlat':0.0156,'dlon':0.0156}
job['grids'][3]           = {'type':'Rectilinear','xlen':18000,'ylen':18000, 'ncname':'rectilinear_projection'}		#hkm FD rectilinear
job['grids'][3]['parms']  = {'j0':9000,'lat0':0.0,'i0':9000,'lon0':-89.5,'dlat':0.0078,'dlon':0.0078}
job['grids'][4]           = {'type':'Rectilinear','xlen':3000,'ylen':2000, 'ncname':'rectilinear_projection'}		#2km CO rectilinear
job['grids'][4]['parms']  = {'j0':1000,'lat0':29.28,'i0':1500,'lon0':-91.39,'dlat':0.022,'dlon':0.022}
job['grids'][5]           = {'type':'Rectilinear','xlen':6000,'ylen':4000, 'ncname':'rectilinear_projection'}		#1km CO rectilinear
job['grids'][5]['parms']  = {'j0':2000,'lat0':29.28,'i0':3000,'lon0':-91.39,'dlat':0.011,'dlon':0.011}
job['grids'][6]           = {'type':'Rectilinear','xlen':12000,'ylen':8000, 'ncname':'rectilinear_projection'}		#0.5km CO rectilinear
job['grids'][6]['parms']  = {'j0':4000,'lat0':29.28,'i0':6000,'lon0':-91.39,'dlat':0.0055,'dlon':0.0055}

job['gridtrans'] = {}
job['gridtrans'][1] = {'type':'Rectilinear'}

job['tilespecs'] = {}
job['tilespecs'][1] = {'x_tiles':1,'y_tiles':1}


job['tilesets']        = {}
# 2km fd rectilinear
job['tilesets'][1]     = {'gridid':1,'tiles':{},'type':'output'}
job['tilesets'][1]['tiles'][1]  = {'x0':0,   'y0':0,   'xlen':1500,'ylen':1500}
job['tilesets'][1]['tiles'][2]  = {'x0':1500,'y0':0,   'xlen':1500,'ylen':1500}
job['tilesets'][1]['tiles'][3]  = {'x0':3000,'y0':0,   'xlen':1500,'ylen':1500}
job['tilesets'][1]['tiles'][4]  = {'x0':0,   'y0':1500,'xlen':1500,'ylen':1500}
job['tilesets'][1]['tiles'][5]  = {'x0':1500,'y0':1500,'xlen':1500,'ylen':1500}
job['tilesets'][1]['tiles'][6]  = {'x0':3000,'y0':1500,'xlen':1500,'ylen':1500}
job['tilesets'][1]['tiles'][7]  = {'x0':0,   'y0':3000,'xlen':1500,'ylen':1500}
job['tilesets'][1]['tiles'][8]  = {'x0':1500,'y0':3000,'xlen':1500,'ylen':1500}
job['tilesets'][1]['tiles'][9]  = {'x0':3000,'y0':3000,'xlen':1500,'ylen':1500}
# 1km fd rectilinear from 1km 
job['tilesets'][2]     = {'gridid':2,'tiles':{},'type':'output'}
job['tilesets'][2]['tiles'][1]  = {'x0':0,   'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][2]  = {'x0':1000,'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][3]  = {'x0':2000,'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][4]  = {'x0':3000,'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][5]  = {'x0':4000,'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][6]  = {'x0':5000,'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][7]  = {'x0':6000,'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][8]  = {'x0':7000,'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][9]  = {'x0':8000,'y0':0,   'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][10] = {'x0':0,   'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][11] = {'x0':1000,'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][12] = {'x0':2000,'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][13] = {'x0':3000,'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][14] = {'x0':4000,'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][15] = {'x0':5000,'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][16] = {'x0':6000,'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][17] = {'x0':7000,'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][18] = {'x0':8000,'y0':1000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][19] = {'x0':0,   'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][20] = {'x0':1000,'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][21] = {'x0':2000,'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][22] = {'x0':3000,'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][23] = {'x0':4000,'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][24] = {'x0':5000,'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][25] = {'x0':6000,'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][26] = {'x0':7000,'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][27] = {'x0':8000,'y0':2000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][28] = {'x0':0,   'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][29] = {'x0':1000,'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][30] = {'x0':2000,'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][31] = {'x0':3000,'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][32] = {'x0':4000,'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][33] = {'x0':5000,'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][34] = {'x0':6000,'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][35] = {'x0':7000,'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][36] = {'x0':8000,'y0':3000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][37] = {'x0':0,   'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][38] = {'x0':1000,'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][39] = {'x0':2000,'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][40] = {'x0':3000,'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][41] = {'x0':4000,'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][42] = {'x0':5000,'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][43] = {'x0':6000,'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][44] = {'x0':7000,'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][45] = {'x0':8000,'y0':4000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][46] = {'x0':0,   'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][47] = {'x0':1000,'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][48] = {'x0':2000,'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][49] = {'x0':3000,'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][50] = {'x0':4000,'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][51] = {'x0':5000,'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][52] = {'x0':6000,'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][53] = {'x0':7000,'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][54] = {'x0':8000,'y0':5000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][55] = {'x0':0,   'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][56] = {'x0':1000,'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][57] = {'x0':2000,'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][58] = {'x0':3000,'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][59] = {'x0':4000,'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][60] = {'x0':5000,'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][61] = {'x0':6000,'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][62] = {'x0':7000,'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][63] = {'x0':8000,'y0':6000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][64] = {'x0':0,   'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][65] = {'x0':1000,'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][66] = {'x0':2000,'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][67] = {'x0':3000,'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][68] = {'x0':4000,'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][69] = {'x0':5000,'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][70] = {'x0':6000,'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][71] = {'x0':7000,'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][72] = {'x0':8000,'y0':7000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][73] = {'x0':0,   'y0':8000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][74] = {'x0':1000,'y0':8000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][75] = {'x0':2000,'y0':8000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][76] = {'x0':3000,'y0':8000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][77] = {'x0':4000,'y0':8000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][78] = {'x0':5000,'y0':8000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][79] = {'x0':6000,'y0':8000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][80] = {'x0':7000,'y0':8000,'xlen':1000,'ylen':1000}
job['tilesets'][2]['tiles'][81] = {'x0':8000,'y0':8000,'xlen':1000,'ylen':1000}
# hkm fd rectilinear from hkm 
job['tilesets'][3]     = {'gridid':3,'tiles':{},'type':'output'}
job['tilesets'][3]['tiles'][1]  = {'x0':0,    'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][2]  = {'x0':2000, 'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][3]  = {'x0':4000, 'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][4]  = {'x0':6000, 'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][5]  = {'x0':8000, 'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][6]  = {'x0':10000,'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][7]  = {'x0':12000,'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][8]  = {'x0':14000,'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][9]  = {'x0':16000,'y0':0,   'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][10] = {'x0':0,    'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][11] = {'x0':2000, 'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][12] = {'x0':4000, 'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][13] = {'x0':6000, 'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][14] = {'x0':8000, 'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][15] = {'x0':10000,'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][16] = {'x0':12000,'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][17] = {'x0':14000,'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][18] = {'x0':16000,'y0':2000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][19] = {'x0':0,    'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][20] = {'x0':2000, 'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][21] = {'x0':4000, 'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][22] = {'x0':6000, 'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][23] = {'x0':8000, 'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][24] = {'x0':10000,'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][25] = {'x0':12000,'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][26] = {'x0':14000,'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][27] = {'x0':16000,'y0':4000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][28] = {'x0':0,    'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][29] = {'x0':2000, 'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][30] = {'x0':4000, 'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][31] = {'x0':6000, 'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][32] = {'x0':8000, 'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][33] = {'x0':10000,'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][34] = {'x0':12000,'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][35] = {'x0':14000,'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][36] = {'x0':16000,'y0':6000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][37] = {'x0':0,    'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][38] = {'x0':2000, 'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][39] = {'x0':4000, 'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][40] = {'x0':6000, 'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][41] = {'x0':8000, 'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][42] = {'x0':10000,'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][43] = {'x0':12000,'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][44] = {'x0':14000,'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][45] = {'x0':16000,'y0':8000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][46] = {'x0':0,    'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][47] = {'x0':2000, 'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][48] = {'x0':4000, 'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][49] = {'x0':6000, 'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][50] = {'x0':8000, 'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][51] = {'x0':10000,'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][52] = {'x0':12000,'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][53] = {'x0':14000,'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][54] = {'x0':16000,'y0':10000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][55] = {'x0':0,    'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][56] = {'x0':2000, 'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][57] = {'x0':4000, 'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][58] = {'x0':6000, 'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][59] = {'x0':8000, 'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][60] = {'x0':10000,'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][61] = {'x0':12000,'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][62] = {'x0':14000,'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][63] = {'x0':16000,'y0':12000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][64] = {'x0':0,    'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][65] = {'x0':2000, 'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][66] = {'x0':4000, 'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][67] = {'x0':6000, 'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][68] = {'x0':8000, 'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][69] = {'x0':10000,'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][70] = {'x0':12000,'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][71] = {'x0':14000,'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][72] = {'x0':16000,'y0':14000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][73] = {'x0':0,    'y0':16000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][74] = {'x0':2000, 'y0':16000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][75] = {'x0':4000, 'y0':16000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][76] = {'x0':6000, 'y0':16000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][77] = {'x0':8000, 'y0':16000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][78] = {'x0':10000,'y0':16000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][79] = {'x0':12000,'y0':16000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][80] = {'x0':14000,'y0':16000,'xlen':2000,'ylen':2000}
job['tilesets'][3]['tiles'][81] = {'x0':16000,'y0':16000,'xlen':2000,'ylen':2000}

# 2km conus rectilinear from 2km 
job['tilesets'][4]     = {'gridid':4,'tiles':{},'type':'output'}
job['tilesets'][4]['tiles'][1]  = {'x0':0,   'y0':0,    'xlen':1500,'ylen':1000}
job['tilesets'][4]['tiles'][2]  = {'x0':1500,'y0':0,    'xlen':1500,'ylen':1000}
job['tilesets'][4]['tiles'][3]  = {'x0':0,   'y0':1000, 'xlen':1500,'ylen':1000}
job['tilesets'][4]['tiles'][4]  = {'x0':1500,'y0':1000, 'xlen':1500,'ylen':1000}
# 1km conus rectilinear from 1km 
job['tilesets'][5]     = {'gridid':5,'tiles':{},'type':'output'}
job['tilesets'][5]['tiles'][1]  = {'x0':0,   'y0':0,   'xlen':1500,'ylen':2000}
job['tilesets'][5]['tiles'][2]  = {'x0':1500,'y0':0,   'xlen':1500,'ylen':2000}
job['tilesets'][5]['tiles'][3]  = {'x0':3000,'y0':0,   'xlen':1500,'ylen':2000}
job['tilesets'][5]['tiles'][4]  = {'x0':4500,'y0':0,   'xlen':1500,'ylen':2000}
job['tilesets'][5]['tiles'][5]  = {'x0':0,   'y0':2000,'xlen':1500,'ylen':2000}
job['tilesets'][5]['tiles'][6]  = {'x0':1500,'y0':2000,'xlen':1500,'ylen':2000}
job['tilesets'][5]['tiles'][7]  = {'x0':3000,'y0':2000,'xlen':1500,'ylen':2000}
job['tilesets'][5]['tiles'][8]  = {'x0':4500,'y0':2000,'xlen':1500,'ylen':2000}
# 0.5km conus rectilinear from 0.5km 
job['tilesets'][6]     = {'gridid':6,'tiles':{},'type':'output'}
job['tilesets'][6]['tiles'][1]  = {'x0':0,   'y0':0,   'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][2]  = {'x0':3000,'y0':0,   'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][3]  = {'x0':6000,'y0':0,   'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][4]  = {'x0':9000,'y0':0,   'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][5]  = {'x0':0,   'y0':2000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][6]  = {'x0':3000,'y0':2000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][7]  = {'x0':6000,'y0':2000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][8]  = {'x0':9000,'y0':2000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][9]  = {'x0':0,   'y0':4000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][10] = {'x0':3000,'y0':4000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][11] = {'x0':6000,'y0':4000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][12] = {'x0':9000,'y0':4000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][13] = {'x0':0,   'y0':6000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][14] = {'x0':3000,'y0':6000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][15] = {'x0':6000,'y0':6000,'xlen':3000,'ylen':2000}
job['tilesets'][6]['tiles'][16] = {'x0':9000,'y0':6000,'xlen':3000,'ylen':2000}

job['defaults'] = {}
job['defaults']['inputs'] = {}
job['defaults']['inputs']['gridtype'] = 'static'
job['defaults']['inputs']['tilemode'] = 'static'
job['defaults']['inputs']['layers'] = {}
job['defaults']['inputs']['layers']['scmi'] = {'var':'Sectorized_CMI', 'desc':'Scaled Integer Reflectance/BT'}

job['inputs'] = {}
job['inputs']['FD_3_1']  = {}
job['inputs']['FD_3_2']  = {}
job['inputs']['FD_3_3']  = {}
job['inputs']['FD_3_4']  = {}
job['inputs']['FD_3_5']  = {}
job['inputs']['FD_3_6']  = {}
job['inputs']['FD_3_7']  = {}
job['inputs']['FD_3_8']  = {}
job['inputs']['FD_3_9']  = {}
job['inputs']['FD_3_10'] = {}
job['inputs']['FD_3_11'] = {}
job['inputs']['FD_3_12'] = {}
job['inputs']['FD_3_13'] = {}
job['inputs']['FD_3_14'] = {}
job['inputs']['FD_3_15'] = {}
job['inputs']['FD_3_16'] = {}
job['inputs']['FD_4_1']  = {}
job['inputs']['FD_4_2']  = {}
job['inputs']['FD_4_3']  = {}
job['inputs']['FD_4_4']  = {}
job['inputs']['FD_4_5']  = {}
job['inputs']['FD_4_6']  = {}
job['inputs']['FD_4_7']  = {}
job['inputs']['FD_4_8']  = {}
job['inputs']['FD_4_9']  = {}
job['inputs']['FD_4_10'] = {}
job['inputs']['FD_4_11'] = {}
job['inputs']['FD_4_12'] = {}
job['inputs']['FD_4_13'] = {}
job['inputs']['FD_4_14'] = {}
job['inputs']['FD_4_15'] = {}
job['inputs']['FD_4_16'] = {}
job['inputs']['CO_3_1']  = {}
job['inputs']['CO_3_2']  = {}
job['inputs']['CO_3_3']  = {}
job['inputs']['CO_3_4']  = {}
job['inputs']['CO_3_5']  = {}
job['inputs']['CO_3_6']  = {}
job['inputs']['CO_3_7']  = {}
job['inputs']['CO_3_8']  = {}
job['inputs']['CO_3_9']  = {}
job['inputs']['CO_3_10'] = {}
job['inputs']['CO_3_11'] = {}
job['inputs']['CO_3_12'] = {}
job['inputs']['CO_3_13'] = {}
job['inputs']['CO_3_14'] = {}
job['inputs']['CO_3_15'] = {}
job['inputs']['CO_3_16'] = {}

job['defaults']['outputs'] = {}
job['defaults']['outputs']['grid']    = 1
job['defaults']['outputs']['gridtype'] = 'provided'
job['defaults']['outputs']['tilemode'] = 'provided'
job['defaults']['outputs']['tileset'] = 1
job['defaults']['outputs']['notify'] = ['ncm']
job['defaults']['outputs']['enabled'] = True
job['defaults']['outputs']['pathdef'] = []
job['defaults']['outputs']['pathdef'].append({'src':'globalmeta/start_date_time','method':'tstring_reformat','in_tfmt':'%Y%j%H%M%S','tfmt':'%Y%m%d','delimiter':'/'})
job['defaults']['outputs']['pathdef'].append({'src':'globalmeta/start_date_time','method':'tstring_reformat','in_tfmt':'%Y%j%H%M%S','tfmt':'%H','delimiter':'/'})
job['defaults']['outputs']['pathdef'].append({'src':'globalmeta/channel_id','fmt':'str','pad':2,'padval':'0','delimiter':''})
job['defaults']['outputs']['namedef'] = []
job['defaults']['outputs']['namedef'].append({'ident':'product','pad':2,'padval':'a','delimiter':'_'})
job['defaults']['outputs']['namedef'].append({'src':'globalmeta/channel_id','fmt':'str','pad':2,'padval':'0','delimiter':'_'})
job['defaults']['outputs']['namedef'].append({'ident':'tileid','pad':2,'padval':'0','delimiter':'_'})
job['defaults']['outputs']['namedef'].append({'src':'globalmeta/start_date_time','method':'tstring_reformat','in_tfmt':'%Y%j%H%M%S','tfmt':'%Y%m%d%H%M%S','delimiter':'.nc'})
job['defaults']['outputs']['shortnamedef'] = []
job['defaults']['outputs']['shortnamedef'].append({'src':'variables/fixedgrid_projection/attr/longitude_of_projection_origin','fmt':'float','translate':{-75.0:'E',-89.5:'T'},'delimiter':''})
job['defaults']['outputs']['shortnamedef'].append({'src':'globalmeta/source_scene','fmt':'str','translate':{'Full Disk':'FD','CONUS':'CONUS','Mesoscale-1':'M1','Mesoscale-2':'M2'},'delimiter':'-'})
job['defaults']['outputs']['shortnamedef'].append({'src':'globalmeta/source_spatial_resolution','fmt':'float','translate':{2.0:'020',1.0:'010',0.5:'005'},'delimiter':'-B'})
job['defaults']['outputs']['shortnamedef'].append({'src':'globalmeta/bit_depth','fmt':'str','pad':2,'padval':'0','delimiter':'-M'})
job['defaults']['outputs']['shortnamedef'].append({'src':'globalmeta/abi_mode','fmt':'str','delimiter':'-C','default':'4'})
job['defaults']['outputs']['shortnamedef'].append({'src':'globalmeta/channel_id','fmt':'str','pad':2,'padval':'0','delimiter':''})

job['defaults']['outputs']['dimensions'] = {}
job['defaults']['outputs']['dimensions']['x'] = {'default':1024,'src':'tile/xlen'}
job['defaults']['outputs']['dimensions']['y'] = {'default':1024,'src':'tile/ylen'}

job['defaults']['outputs']['globalmeta'] = {}
job['defaults']['outputs']['globalmeta']['title']                      = {'default':'Sectorized Cloud and Moisture Full Disk Imagery'}
job['defaults']['outputs']['globalmeta']['ICD_version']                = {'default':'SE-08_7034704_GS_AWIPS_Ext_ICD_RevB.3'}
job['defaults']['outputs']['globalmeta']['Conventions']                = {'default':'CF-1.6'}
job['defaults']['outputs']['globalmeta']['production_location']        = {'default':'WCDAS',	'src':'globalmeta/production_location'}
job['defaults']['outputs']['globalmeta']['product_name']               = {'default':'junk','special':'create_name','nametype':'shortnamedef'}
job['defaults']['outputs']['globalmeta']['channel_id']                 = {'default':1,			'src':'globalmeta/channel_id'}
job['defaults']['outputs']['globalmeta']['central_wavelength']         = {'default':0.47,		'src':'globalmeta/central_wavelength'}
job['defaults']['outputs']['globalmeta']['satellite_id']               = {'default':'GOES-17',	'src':'globalmeta/satellite_id'}
job['defaults']['outputs']['globalmeta']['abi_mode']                   = {'default':4,			'src':'globalmeta/abi_mode'}
job['defaults']['outputs']['globalmeta']['source_scene']               = {'default':'Full Disk','src':'globalmeta/source_scene'}
job['defaults']['outputs']['globalmeta']['product_center_latitude']    = {'default':0.0,		'src':'prod/ctrlat'}
job['defaults']['outputs']['globalmeta']['product_center_longitude']   = {'default':-89.5,		'src':'prod/ctrlon'}
job['defaults']['outputs']['globalmeta']['periodicity']                = {'default':5,			'src':'globalmeta/periodicity'}
job['defaults']['outputs']['globalmeta']['projection']                 = {'default':'fixedgrid_projection','src':'grid/ncname'}
job['defaults']['outputs']['globalmeta']['bit_depth']                  = {'default':10,         'src':'globalmeta/bit_depth'}
job['defaults']['outputs']['globalmeta']['source_spatial_resolution']  = {'default':2.0,        'src':'globalmeta/source_spatial_resolution'}
job['defaults']['outputs']['globalmeta']['request_spatial_resolution'] = {'default':2.0,        'src':'globalmeta/request_spatial_resolution'}  #TODO: jkz
job['defaults']['outputs']['globalmeta']['start_date_time']            = {'default':'1970001000000','src':'globalmeta/start_date_time'}
job['defaults']['outputs']['globalmeta']['number_product_tiles']       = {'default':15,         'src':'prod/ntiles'}
job['defaults']['outputs']['globalmeta']['tile_center_latitude']       = {'default':45.504,		'src':'tile/ctrlat'}
job['defaults']['outputs']['globalmeta']['tile_center_longitude']      = {'default':-121.489,	'src':'tile/ctrlon'}
job['defaults']['outputs']['globalmeta']['product_tile_width']         = {'default':1024,       'src':'tile/xlen'}
job['defaults']['outputs']['globalmeta']['product_tile_height']        = {'default':1024,       'src':'tile/ylen'}
job['defaults']['outputs']['globalmeta']['product_rows']               = {'default':3072,       'src':'prod/ylen'}
job['defaults']['outputs']['globalmeta']['product_columns']            = {'default':5120,       'src':'prod/xlen'}
job['defaults']['outputs']['globalmeta']['pixel_x_size']               = {'default':2.0,        'src':'globalmeta/source_spatial_resolution'}
job['defaults']['outputs']['globalmeta']['pixel_y_size']               = {'default':2.0,        'src':'globalmeta/source_spatial_resolution'} #TODO: jkz
job['defaults']['outputs']['globalmeta']['tile_row_offset']            = {'default':0,          'src':'tile/j0'}
job['defaults']['outputs']['globalmeta']['tile_column_offset']         = {'default':0,          'src':'tile/i0'}
job['defaults']['outputs']['globalmeta']['satellite_latitude']         = {'default':0.0,		'src':'globalmeta/satellite_latitude'}
job['defaults']['outputs']['globalmeta']['satellite_longitude']        = {'default':-137.0,     'src':'globalmeta/satellite_longitude'}
job['defaults']['outputs']['globalmeta']['satellite_altitude']         = {'default':35786023,   'src':'globalmeta/satellite_altitude'}
job['defaults']['outputs']['globalmeta']['output_product_name']        = {'default':'Full Disk','src':'globalmeta/source_scene'}

job['defaults']['outputs']['variables']  = {}
job['defaults']['outputs']['variables']['x']  = {}
job['defaults']['outputs']['variables']['x']['fmt']                    = {'default':'i2'}
job['defaults']['outputs']['variables']['x']['shape']                  = {'default':['x']}
job['defaults']['outputs']['variables']['x']['start']                  = {'default':0}
job['defaults']['outputs']['variables']['x']['delta']                  = {'default':1}
job['defaults']['outputs']['variables']['x']['attrs'] = {}
job['defaults']['outputs']['variables']['x']['attrs']['standard_name'] = {'default':'projection_x_coordinate'}
job['defaults']['outputs']['variables']['x']['attrs']['units']         = {'default':'microradian',	'src':'tile/grid_units'}
job['defaults']['outputs']['variables']['x']['attrs']['add_offset']    = {'default':0.0,			'src':'tile/grid_x_offset'}
job['defaults']['outputs']['variables']['x']['attrs']['scale_factor']  = {'default':56.0,			'src':'tile/grid_x_scale','fmt':'float'}

job['defaults']['outputs']['variables']['y']  = {}
job['defaults']['outputs']['variables']['y']['fmt']                    = {'default':'i2'}
job['defaults']['outputs']['variables']['y']['shape']                  = {'default':['y']}
job['defaults']['outputs']['variables']['y']['start']                  = {'default':0}
job['defaults']['outputs']['variables']['y']['delta']                  = {'default':1}
job['defaults']['outputs']['variables']['y']['attrs'] = {}
job['defaults']['outputs']['variables']['y']['attrs']['standard_name'] = {'default':'projection_y_coordinate'}
job['defaults']['outputs']['variables']['y']['attrs']['units']         = {'default':'microradian',	'src':'tile/grid_units'}
job['defaults']['outputs']['variables']['y']['attrs']['add_offset']    = {'default':0.0,			'src':'tile/grid_y_offset'}
job['defaults']['outputs']['variables']['y']['attrs']['scale_factor']  = {'default':-56.0,			'src':'tile/grid_y_scale','fmt':'float'}

job['defaults']['outputs']['variables']['Sectorized_CMI'] = {}
job['defaults']['outputs']['variables']['Sectorized_CMI']['fmt']                    = {'default':'u2'}
job['defaults']['outputs']['variables']['Sectorized_CMI']['shape']                  = {'default':['y','x']}
job['defaults']['outputs']['variables']['Sectorized_CMI']['fill']                   = {'default':-1}
job['defaults']['outputs']['variables']['Sectorized_CMI']['zlib']                   = {'default':True}
job['defaults']['outputs']['variables']['Sectorized_CMI']['complevel']              = {'default':1}
job['defaults']['outputs']['variables']['Sectorized_CMI']['shuffle']                = {'default':True}
job['defaults']['outputs']['variables']['Sectorized_CMI']['data']                   = {'default':[],'layer':'scmi'}
job['defaults']['outputs']['variables']['Sectorized_CMI']['attrs'] = {}
job['defaults']['outputs']['variables']['Sectorized_CMI']['attrs']['standard_name'] = {'default':'brightness_temperature','src':'variables/Sectorized_CMI/attr/standard_name'}
job['defaults']['outputs']['variables']['Sectorized_CMI']['attrs']['units']         = {'default':'kelvin','src':'variables/Sectorized_CMI/attr/units'}
job['defaults']['outputs']['variables']['Sectorized_CMI']['attrs']['grid_mapping']  = {'default':'fixedgrid_projection','src':'grid/ncname'}
job['defaults']['outputs']['variables']['Sectorized_CMI']['attrs']['add_offset']    = {'default':0,		  'src':'variables/Sectorized_CMI/attr/add_offset'}
job['defaults']['outputs']['variables']['Sectorized_CMI']['attrs']['scale_factor']  = {'default':1,       'src':'variables/Sectorized_CMI/attr/scale_factor'}
job['defaults']['outputs']['variables']['Sectorized_CMI']['attrs']['valid_min']     = {'default':0}
job['defaults']['outputs']['variables']['Sectorized_CMI']['attrs']['valid_max']     = {'default':2**14-1, 'src':'variables/Sectorized_CMI/attr/valid_max'}

job['defaults']['outputs']['variables']['rectilinear_projection'] = {}
job['defaults']['outputs']['variables']['rectilinear_projection']['fmt']                                     = {'default':'i'}
job['defaults']['outputs']['variables']['rectilinear_projection']['shape']                                   = {'default':[]}
job['defaults']['outputs']['variables']['rectilinear_projection']['attrs'] = {}
job['defaults']['outputs']['variables']['rectilinear_projection']['attrs']['grid_mapping_name']              = {'default':'rectilinear'}
job['defaults']['outputs']['variables']['rectilinear_projection']['attrs']['latitude_of_projection_origin']  = {'default':0.0,           'src':'grid/parms/lat0','fmt':'float'}
job['defaults']['outputs']['variables']['rectilinear_projection']['attrs']['longitude_of_projection_origin'] = {'default':-75.0,		 'src':'grid/parms/lon0','fmt':'float'}
job['defaults']['outputs']['variables']['rectilinear_projection']['attrs']['semi_major']                     = {'default':6378137,       'src':'variables/fixedgrid_projection/attr/semi_major', 'fmt':'float'}
job['defaults']['outputs']['variables']['rectilinear_projection']['attrs']['semi_minor']                     = {'default':6356752.31414, 'src':'variables/fixedgrid_projection/attr/semi_minor', 'fmt':'float'}
job['defaults']['outputs']['variables']['rectilinear_projection']['attrs']['origin_column']       			 = {'default':1000,			 'src':'grid/parms/i0', 'fmt':'int'}
job['defaults']['outputs']['variables']['rectilinear_projection']['attrs']['origin_line']       			 = {'default':1000,			 'src':'grid/parms/j0', 'fmt':'int'}


# full disk
job['outputs'] = {}
job['outputs']['1'] = {}
job['outputs']['1']['input']  = 'FD_3_1'
job['outputs']['1']['grid']    = 2
job['outputs']['1']['tileset'] = 2
job['outputs']['2'] = {}
job['outputs']['2']['input']  = 'FD_3_2'
job['outputs']['2']['grid']    = 3
job['outputs']['2']['tileset'] = 3
job['outputs']['3'] = {}
job['outputs']['3']['input']  = 'FD_3_3'
job['outputs']['3']['grid']    = 2
job['outputs']['3']['tileset'] = 2
job['outputs']['4'] = {}
job['outputs']['4']['input']  = 'FD_3_4'
job['outputs']['5'] = {}
job['outputs']['5']['input']  = 'FD_3_5'
job['outputs']['5']['grid']    = 2
job['outputs']['5']['tileset'] = 2
job['outputs']['6'] = {}
job['outputs']['6']['input']  = 'FD_3_6'
job['outputs']['7'] = {}
job['outputs']['7']['input']  = 'FD_3_7'
job['outputs']['8'] = {}
job['outputs']['8']['input']  = 'FD_3_8'
job['outputs']['9'] = {}
job['outputs']['9']['input']  = 'FD_3_9'
job['outputs']['10'] = {}
job['outputs']['10']['input'] = 'FD_3_10'
job['outputs']['11'] = {}
job['outputs']['11']['input'] = 'FD_3_11'
job['outputs']['12'] = {}
job['outputs']['12']['input'] = 'FD_3_12'
job['outputs']['13'] = {}
job['outputs']['13']['input'] = 'FD_3_13'
job['outputs']['14'] = {}
job['outputs']['14']['input'] = 'FD_3_14'
job['outputs']['15'] = {}
job['outputs']['15']['input'] = 'FD_3_15'
job['outputs']['16'] = {}
job['outputs']['16']['input'] = 'FD_3_16'
# conus
job['outputs']['17'] = {}
job['outputs']['17']['input']  = 'CO_3_1'
job['outputs']['17']['grid']    = 5
job['outputs']['17']['tileset'] = 5
job['outputs']['18'] = {}
job['outputs']['18']['input']  = 'CO_3_2'
job['outputs']['18']['grid']    = 6
job['outputs']['18']['tileset'] = 6
job['outputs']['19'] = {}
job['outputs']['19']['input']  = 'CO_3_3'
job['outputs']['19']['grid']    = 5
job['outputs']['19']['tileset'] = 5
job['outputs']['20'] = {}
job['outputs']['20']['input']  = 'CO_3_4'
job['outputs']['20']['grid']    = 4
job['outputs']['20']['tileset'] = 4
job['outputs']['21'] = {}
job['outputs']['21']['input']  = 'CO_3_5'
job['outputs']['21']['grid']    = 5
job['outputs']['21']['tileset'] = 5
job['outputs']['22'] = {}
job['outputs']['22']['input']  = 'CO_3_6'
job['outputs']['22']['grid']    = 4
job['outputs']['22']['tileset'] = 4
job['outputs']['23'] = {}
job['outputs']['23']['input']  = 'CO_3_7'
job['outputs']['23']['grid']    = 4
job['outputs']['23']['tileset'] = 4
job['outputs']['24'] = {}
job['outputs']['24']['input']  = 'CO_3_8'
job['outputs']['24']['grid']    = 4
job['outputs']['24']['tileset'] = 4
job['outputs']['25'] = {}
job['outputs']['25']['input']  = 'CO_3_9'
job['outputs']['25']['grid']    = 4
job['outputs']['25']['tileset'] = 4
job['outputs']['26'] = {}
job['outputs']['26']['input'] = 'CO_3_10'
job['outputs']['26']['grid']    = 4
job['outputs']['26']['tileset'] = 4
job['outputs']['27'] = {}
job['outputs']['27']['input'] = 'CO_3_11'
job['outputs']['27']['grid']    = 4
job['outputs']['27']['tileset'] = 4
job['outputs']['28'] = {}
job['outputs']['28']['input'] = 'CO_3_12'
job['outputs']['28']['grid']    = 4
job['outputs']['28']['tileset'] = 4
job['outputs']['29'] = {}
job['outputs']['29']['input'] = 'CO_3_13'
job['outputs']['29']['grid']    = 4
job['outputs']['29']['tileset'] = 4
job['outputs']['30'] = {}
job['outputs']['30']['input'] = 'CO_3_14'
job['outputs']['30']['grid']    = 4
job['outputs']['30']['tileset'] = 4
job['outputs']['31'] = {}
job['outputs']['31']['input'] = 'CO_3_15'
job['outputs']['31']['grid']    = 4
job['outputs']['31']['tileset'] = 4
job['outputs']['32'] = {}
job['outputs']['32']['input'] = 'CO_3_16'
job['outputs']['32']['grid']    = 4
job['outputs']['32']['tileset'] = 4

job['outputs'][33] = {}
job['outputs'][33]['input']    = 'M1_1'
job['outputs'][33]['grid']     = 1
job['outputs'][33]['gridtype'] = 'translate'
job['outputs'][33]['tilemode'] = 'spec'
job['outputs'][33]['tilespec'] = 1
job['outputs'][33]['tileset']  = 0
job['outputs'][34] = {}
job['outputs'][34]['input']    = 'M1_2'
job['outputs'][34]['grid']     = 1
job['outputs'][34]['gridtype'] = 'translate'
job['outputs'][34]['tilemode'] = 'spec'
job['outputs'][34]['tilespec'] = 1
job['outputs'][34]['tileset']  = 0
job['outputs'][35] = {}
job['outputs'][35]['input']  = 'M1_3'
job['outputs'][35]['grid']     = 1
job['outputs'][35]['gridtype'] = 'translate'
job['outputs'][35]['tilemode'] = 'spec'
job['outputs'][35]['tilespec'] = 1
job['outputs'][35]['tileset'] = 0
job['outputs'][36] = {}
job['outputs'][36]['input']  = 'M1_4'
job['outputs'][36]['grid']     = 1
job['outputs'][36]['gridtype'] = 'translate'
job['outputs'][36]['tilemode'] = 'spec'
job['outputs'][36]['tilespec'] = 1
job['outputs'][36]['tileset']  = 0
job['outputs'][37] = {}
job['outputs'][37]['input']  = 'M1_5'
job['outputs'][37]['grid']     = 1
job['outputs'][37]['gridtype'] = 'translate'
job['outputs'][37]['tilemode'] = 'spec'
job['outputs'][37]['tilespec'] = 1
job['outputs'][37]['tileset'] = 0
job['outputs'][38] = {}
job['outputs'][38]['input']  = 'M1_6'
job['outputs'][38]['grid']     = 1
job['outputs'][38]['gridtype'] = 'translate'
job['outputs'][38]['tilemode'] = 'spec'
job['outputs'][38]['tilespec'] = 1
job['outputs'][38]['tileset'] = 0
job['outputs'][39] = {}
job['outputs'][39]['input']  = 'M1_7'
job['outputs'][39]['grid']     = 1
job['outputs'][39]['gridtype'] = 'translate'
job['outputs'][39]['tilemode'] = 'spec'
job['outputs'][39]['tilespec'] = 1
job['outputs'][39]['tileset'] = 0
job['outputs'][40] = {}
job['outputs'][40]['input']  = 'M1_8'
job['outputs'][40]['grid']     = 1
job['outputs'][40]['gridtype'] = 'translate'
job['outputs'][40]['tilemode'] = 'spec'
job['outputs'][40]['tilespec'] = 1
job['outputs'][40]['tileset'] = 0
job['outputs'][41] = {}
job['outputs'][41]['input']  = 'M1_9'
job['outputs'][41]['grid']     = 1
job['outputs'][41]['gridtype'] = 'translate'
job['outputs'][41]['tilemode'] = 'spec'
job['outputs'][41]['tilespec'] = 1
job['outputs'][41]['tileset'] = 0
job['outputs'][42] = {}
job['outputs'][42]['input']  = 'M1_10'
job['outputs'][42]['grid']     = 1
job['outputs'][42]['gridtype'] = 'translate'
job['outputs'][42]['tilemode'] = 'spec'
job['outputs'][42]['tilespec'] = 1
job['outputs'][42]['tileset'] = 0
job['outputs'][43] = {}
job['outputs'][43]['input']  = 'M1_11'
job['outputs'][43]['grid']     = 1
job['outputs'][43]['gridtype'] = 'translate'
job['outputs'][43]['tilemode'] = 'spec'
job['outputs'][43]['tilespec'] = 1
job['outputs'][43]['tileset'] = 0
job['outputs'][44] = {}
job['outputs'][44]['input']  = 'M1_12'
job['outputs'][44]['grid']     = 1
job['outputs'][44]['gridtype'] = 'translate'
job['outputs'][44]['tilemode'] = 'spec'
job['outputs'][44]['tilespec'] = 1
job['outputs'][44]['tileset'] = 0
job['outputs'][45] = {}
job['outputs'][45]['input']  = 'M1_13'
job['outputs'][45]['grid']     = 1
job['outputs'][45]['gridtype'] = 'translate'
job['outputs'][45]['tilemode'] = 'spec'
job['outputs'][45]['tilespec'] = 1
job['outputs'][45]['tileset'] = 0
job['outputs'][46] = {}
job['outputs'][46]['input'] = 'M1_14'
job['outputs'][46]['grid']     = 1
job['outputs'][46]['gridtype'] = 'translate'
job['outputs'][46]['tilemode'] = 'spec'
job['outputs'][46]['tilespec'] = 1
job['outputs'][46]['tileset'] = 0
job['outputs'][47] = {}
job['outputs'][47]['input'] = 'M1_15'
job['outputs'][47]['grid']     = 1
job['outputs'][47]['gridtype'] = 'translate'
job['outputs'][47]['tilemode'] = 'spec'
job['outputs'][47]['tilespec'] = 1
job['outputs'][47]['tileset'] = 0
job['outputs'][48] = {}
job['outputs'][48]['input'] = 'M1_16'
job['outputs'][48]['grid']     = 1
job['outputs'][48]['gridtype'] = 'translate'
job['outputs'][48]['tilemode'] = 'spec'
job['outputs'][48]['tilespec'] = 1
job['outputs'][48]['tileset'] = 0


job['outputs'][49] = {}
job['outputs'][49]['input']   = 'M2_1'
job['outputs'][49]['grid']     = 1
job['outputs'][49]['gridtype'] = 'translate'
job['outputs'][49]['tilemode'] = 'spec'
job['outputs'][49]['tilespec'] = 1
job['outputs'][49]['tileset'] = 0
job['outputs'][50] = {}
job['outputs'][50]['input']  = 'M2_2'
job['outputs'][50]['grid']     = 1
job['outputs'][50]['gridtype'] = 'translate'
job['outputs'][50]['tilemode'] = 'spec'
job['outputs'][50]['tilespec'] = 1
job['outputs'][50]['tileset'] = 0
job['outputs'][51] = {}
job['outputs'][51]['input']  = 'M2_3'
job['outputs'][51]['grid']     = 1
job['outputs'][51]['gridtype'] = 'translate'
job['outputs'][51]['tilemode'] = 'spec'
job['outputs'][51]['tilespec'] = 1
job['outputs'][51]['tileset'] = 0
job['outputs'][52] = {}
job['outputs'][52]['input']  = 'M2_4'
job['outputs'][52]['grid']     = 1
job['outputs'][52]['gridtype'] = 'translate'
job['outputs'][52]['tilemode'] = 'spec'
job['outputs'][52]['tilespec'] = 1
job['outputs'][52]['tileset'] = 0
job['outputs'][53] = {}
job['outputs'][53]['input']  = 'M2_5'
job['outputs'][53]['grid']     = 1
job['outputs'][53]['gridtype'] = 'translate'
job['outputs'][53]['tilemode'] = 'spec'
job['outputs'][53]['tilespec'] = 1
job['outputs'][53]['tileset'] = 0
job['outputs'][54] = {}
job['outputs'][54]['input']  = 'M2_6'
job['outputs'][54]['grid']     = 1
job['outputs'][54]['gridtype'] = 'translate'
job['outputs'][54]['tilemode'] = 'spec'
job['outputs'][54]['tilespec'] = 1
job['outputs'][54]['tileset'] = 0
job['outputs'][55] = {}
job['outputs'][55]['input']  = 'M2_7'
job['outputs'][55]['grid']     = 1
job['outputs'][55]['gridtype'] = 'translate'
job['outputs'][55]['tilemode'] = 'spec'
job['outputs'][55]['tilespec'] = 1
job['outputs'][55]['tileset'] = 0
job['outputs'][56] = {}
job['outputs'][56]['input']  = 'M2_8'
job['outputs'][56]['grid']     = 1
job['outputs'][56]['gridtype'] = 'translate'
job['outputs'][56]['tilemode'] = 'spec'
job['outputs'][56]['tilespec'] = 1
job['outputs'][56]['tileset'] = 0
job['outputs'][57] = {}
job['outputs'][57]['input']  = 'M2_9'
job['outputs'][57]['grid']     = 1
job['outputs'][57]['gridtype'] = 'translate'
job['outputs'][57]['tilemode'] = 'spec'
job['outputs'][57]['tilespec'] = 1
job['outputs'][57]['tileset'] = 0
job['outputs'][58] = {}
job['outputs'][58]['input']  = 'M2_10'
job['outputs'][58]['grid']     = 1
job['outputs'][58]['gridtype'] = 'translate'
job['outputs'][58]['tilemode'] = 'spec'
job['outputs'][58]['tilespec'] = 1
job['outputs'][58]['tileset'] = 0
job['outputs'][59] = {}
job['outputs'][59]['input']  = 'M2_11'
job['outputs'][59]['grid']     = 1
job['outputs'][59]['gridtype'] = 'translate'
job['outputs'][59]['tilemode'] = 'spec'
job['outputs'][59]['tilespec'] = 1
job['outputs'][59]['tileset'] = 0
job['outputs'][60] = {}
job['outputs'][60]['input']  = 'M2_12'
job['outputs'][60]['grid']     = 1
job['outputs'][60]['gridtype'] = 'translate'
job['outputs'][60]['tilemode'] = 'spec'
job['outputs'][60]['tilespec'] = 1
job['outputs'][60]['tileset'] = 0
job['outputs'][61] = {}
job['outputs'][61]['input']  = 'M2_13'
job['outputs'][61]['grid']     = 1
job['outputs'][61]['gridtype'] = 'translate'
job['outputs'][61]['tilemode'] = 'spec'
job['outputs'][61]['tilespec'] = 1
job['outputs'][61]['tileset'] = 0
job['outputs'][62] = {}
job['outputs'][62]['input'] = 'M2_14'
job['outputs'][62]['grid']     = 1
job['outputs'][62]['gridtype'] = 'translate'
job['outputs'][62]['tilemode'] = 'spec'
job['outputs'][62]['tilespec'] = 1
job['outputs'][62]['tileset'] = 0
job['outputs'][63] = {}
job['outputs'][63]['input'] = 'M2_15'
job['outputs'][63]['grid']     = 1
job['outputs'][63]['gridtype'] = 'translate'
job['outputs'][63]['tilemode'] = 'spec'
job['outputs'][63]['tilespec'] = 1
job['outputs'][63]['tileset'] = 0
job['outputs'][64] = {}
job['outputs'][64]['input'] = 'M2_16'
job['outputs'][64]['grid']     = 1
job['outputs'][64]['gridtype'] = 'translate'
job['outputs'][64]['tilemode'] = 'spec'
job['outputs'][64]['tilespec'] = 1
job['outputs'][64]['tileset'] = 0

job['outputs']['65'] = {}
job['outputs']['65']['input']  = 'FD_4_1'
job['outputs']['65']['grid']    = 2
job['outputs']['65']['tileset'] = 2
job['outputs']['66'] = {}
job['outputs']['66']['input']  = 'FD_4_2'
job['outputs']['66']['grid']    = 3
job['outputs']['66']['tileset'] = 3
job['outputs']['67'] = {}
job['outputs']['67']['input']  = 'FD_4_3'
job['outputs']['67']['grid']    = 2
job['outputs']['67']['tileset'] = 2
job['outputs']['68'] = {}
job['outputs']['68']['input']  = 'FD_4_4'
job['outputs']['69'] = {}
job['outputs']['69']['input']  = 'FD_4_5'
job['outputs']['69']['grid']    = 2
job['outputs']['69']['tileset'] = 2
job['outputs']['70'] = {}
job['outputs']['70']['input']  = 'FD_4_6'
job['outputs']['71'] = {}
job['outputs']['71']['input']  = 'FD_4_7'
job['outputs']['72'] = {}
job['outputs']['72']['input']  = 'FD_4_8'
job['outputs']['73'] = {}
job['outputs']['73']['input']  = 'FD_4_9'
job['outputs']['74'] = {}
job['outputs']['74']['input'] = 'FD_4_10'
job['outputs']['75'] = {}
job['outputs']['75']['input'] = 'FD_4_11'
job['outputs']['76'] = {}
job['outputs']['76']['input'] = 'FD_4_12'
job['outputs']['77'] = {}
job['outputs']['77']['input'] = 'FD_4_13'
job['outputs']['78'] = {}
job['outputs']['78']['input'] = 'FD_4_14'
job['outputs']['79'] = {}
job['outputs']['79']['input'] = 'FD_4_15'
job['outputs']['80'] = {}
job['outputs']['80']['input'] = 'FD_4_16'
# mode 4 conus from fd
job['outputs']['81'] = {}
job['outputs']['81']['input']  = 'FD_4_1'
job['outputs']['81']['grid']    = 5
job['outputs']['81']['tileset'] = 5
job['outputs']['81']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['82'] = {}
job['outputs']['82']['input']  = 'FD_4_2'
job['outputs']['82']['grid']    = 6
job['outputs']['82']['tileset'] = 6
job['outputs']['82']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['83'] = {}
job['outputs']['83']['input']  = 'FD_4_3'
job['outputs']['83']['grid']    = 5
job['outputs']['83']['tileset'] = 5
job['outputs']['83']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['84'] = {}
job['outputs']['84']['input']  = 'FD_4_4'
job['outputs']['84']['grid']    = 4
job['outputs']['84']['tileset'] = 4
job['outputs']['84']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['85'] = {}
job['outputs']['85']['input']  = 'FD_4_5'
job['outputs']['85']['grid']    = 5
job['outputs']['85']['tileset'] = 5
job['outputs']['85']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['86'] = {}
job['outputs']['86']['input']  = 'FD_4_6'
job['outputs']['86']['grid']    = 4
job['outputs']['86']['tileset'] = 4
job['outputs']['86']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['87'] = {}
job['outputs']['87']['input']  = 'FD_4_7'
job['outputs']['87']['grid']    = 4
job['outputs']['87']['tileset'] = 4
job['outputs']['87']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['88'] = {}
job['outputs']['88']['input']  = 'FD_4_8'
job['outputs']['88']['grid']    = 4
job['outputs']['88']['tileset'] = 4
job['outputs']['88']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['89'] = {}
job['outputs']['89']['input']  = 'FD_4_9'
job['outputs']['89']['grid']    = 4
job['outputs']['89']['tileset'] = 4
job['outputs']['89']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['90'] = {}
job['outputs']['90']['input'] = 'FD_4_10'
job['outputs']['90']['grid']    = 4
job['outputs']['90']['tileset'] = 4
job['outputs']['90']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['91'] = {}
job['outputs']['91']['input'] = 'FD_4_11'
job['outputs']['91']['grid']    = 4
job['outputs']['91']['tileset'] = 4
job['outputs']['91']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['92'] = {}
job['outputs']['92']['input'] = 'FD_4_12'
job['outputs']['92']['grid']    = 4
job['outputs']['92']['tileset'] = 4
job['outputs']['92']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['93'] = {}
job['outputs']['93']['input'] = 'FD_4_13'
job['outputs']['93']['grid']    = 4
job['outputs']['93']['tileset'] = 4
job['outputs']['93']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['94'] = {}
job['outputs']['94']['input'] = 'FD_4_14'
job['outputs']['94']['grid']    = 4
job['outputs']['94']['tileset'] = 4
job['outputs']['94']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['95'] = {}
job['outputs']['95']['input'] = 'FD_4_15'
job['outputs']['95']['grid']    = 4
job['outputs']['95']['tileset'] = 4
job['outputs']['95']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]
job['outputs']['96'] = {}
job['outputs']['96']['input'] = 'FD_4_16'
job['outputs']['96']['grid']    = 4
job['outputs']['96']['tileset'] = 4
job['outputs']['96']['replace'] = [{'item':'globalmeta','replace':{'output_product_name':{'default':'CONUS'}}}]

