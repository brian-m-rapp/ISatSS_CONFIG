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
job['name']  = 'ncm_goesr_scmirecttiles_area'
job['cmd']   = 'ncm'
job['class'] = 'NCM'
job['log']   = 'ncm_goesr_scmirecttiles_area_log'

job['data']  = {}
job['data']['products'] = {}
job['data']['products']['location']   = {'node':14,'type':'datapath','path':'area/goes16'}
job['data']['products']['aging']      = {'window':86400, 'mode':'nested','fmt':'%Y%m%d_%H%M','extract':{'method':'head','nchars':13}}
job['data']['products']['method']     = {'technique':'stage','path':'isatss_incinerator'}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':12,'type':'datapath','path':'log'}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True

job['pause_empty'] = 5
job['qlimit']      = 10000
job['maxopen']     = 500 

#job['input_type']   = {'type':'dropzone','dropzone':'/home/jzajic/isatss_data/dropzone','delete_file':False}
job['input_type']  = {'type':'infofile','node':8,'delete_file':True, 'delete_info':True}

job['cntl_node']     = 9
job['notifications'] = {'finish':{'node':6,'enabled':False},'ldm':{'node':6,'enabled':True,'fields':['file','node']}}
job['links']         = {'link1':{'enabled':False}}
job['dots']          = True

job['hash_definition'] = []
job['hash_definition'].append({'parm':'scene',  'meta':{'src':'globalmeta/output_product_name','fmt':'str','translate':{'Full Disk':'FD','CONUS':'CO','Mesoscale-1':'M1', 'Mesoscale-2':'M2'}},    'info':'scene',   'part':'product'})
job['hash_definition'].append({'parm':'band',   'meta':{'src':'globalmeta/channel_id','fmt':'int'},                                     'info':'band',    'part':'product'})
job['hash_definition'].append({'parm':'x0',     'meta':{'src':'globalmeta/tile_column_offset','fmt':'int'},                             'info':'x0',      'part':'tile'})
job['hash_definition'].append({'parm':'y0',     'meta':{'src':'globalmeta/tile_row_offset','fmt':'int'},                                'info':'y0',      'part':'tile'})
job['hash_definition'].append({'parm':'xlen',   'meta':{'src':'globalmeta/product_tile_width','fmt':'int'},                             'info':'xlen',    'part':'tile'})
job['hash_definition'].append({'parm':'ylen',   'meta':{'src':'globalmeta/product_tile_height','fmt':'int'},                            'info':'ylen',    'part':'tile'})
job['hash_definition'].append({'parm':'reftime','meta':{'src':'globalmeta/start_date_time','fmt':'float','method':'string_to_unixtime','in_tfmt':'%Y%j%H%M%S'},'info':'reftime', 'part':'dynamic'})

job['defaults'] = {}
job['defaults']['inputs'] = {}
job['defaults']['inputs']['layers'] = {}
job['defaults']['inputs']['layers']['scmi'] = {'var':'Sectorized_CMI', 'desc':'Scaled Integer Reflectance/BT'}

job['inputs'] = {}
job['inputs']['FD_1']  = {}
job['inputs']['FD_2']  = {}
job['inputs']['FD_3']  = {}
job['inputs']['FD_4']  = {}
job['inputs']['FD_5']  = {}
job['inputs']['FD_6']  = {}
job['inputs']['FD_7']  = {}
job['inputs']['FD_8']  = {}
job['inputs']['FD_9']  = {}
job['inputs']['FD_10'] = {}
job['inputs']['FD_11'] = {}
job['inputs']['FD_12'] = {}
job['inputs']['FD_13'] = {}
job['inputs']['FD_14'] = {}
job['inputs']['FD_15'] = {}
job['inputs']['FD_16'] = {}
job['inputs']['CO_1']  = {}
job['inputs']['CO_2']  = {}
job['inputs']['CO_3']  = {}
job['inputs']['CO_4']  = {}
job['inputs']['CO_5']  = {}
job['inputs']['CO_6']  = {}
job['inputs']['CO_7']  = {}
job['inputs']['CO_8']  = {}
job['inputs']['CO_9']  = {}
job['inputs']['CO_10'] = {}
job['inputs']['CO_11'] = {}
job['inputs']['CO_12'] = {}
job['inputs']['CO_13'] = {}
job['inputs']['CO_14'] = {}
job['inputs']['CO_15'] = {}
job['inputs']['CO_16'] = {}
job['inputs']['M1_1']  = {}
job['inputs']['M1_2']  = {}
job['inputs']['M1_3']  = {}
job['inputs']['M1_4']  = {}
job['inputs']['M1_5']  = {}
job['inputs']['M1_6']  = {}
job['inputs']['M1_7']  = {}
job['inputs']['M1_8']  = {}
job['inputs']['M1_9']  = {}
job['inputs']['M1_10'] = {}
job['inputs']['M1_11'] = {}
job['inputs']['M1_12'] = {}
job['inputs']['M1_13'] = {}
job['inputs']['M1_14'] = {}
job['inputs']['M1_15'] = {}
job['inputs']['M1_16'] = {}
job['inputs']['M2_1']  = {}
job['inputs']['M2_2']  = {}
job['inputs']['M2_3']  = {}
job['inputs']['M2_4']  = {}
job['inputs']['M2_5']  = {}
job['inputs']['M2_6']  = {}
job['inputs']['M2_7']  = {}
job['inputs']['M2_8']  = {}
job['inputs']['M2_9']  = {}
job['inputs']['M2_10'] = {}
job['inputs']['M2_11'] = {}
job['inputs']['M2_12'] = {}
job['inputs']['M2_13'] = {}
job['inputs']['M2_14'] = {}
job['inputs']['M2_15'] = {}
job['inputs']['M2_16'] = {}

job['defaults']['outputs'] = {}
job['defaults']['outputs']['pathdef'] = []
job['defaults']['outputs']['pathdef'].append({'src':'globalmeta/output_product_name','fmt':'str','translate':{'Full Disk':'fulldisk','CONUS':'conus','Mesoscale-1':'meso1','Mesoscale-2':'meso2'},'delimiter':'/'})
chtrans = {'1':'b01_visr','2':'b02_visb','3':'b03_nir_veg','4':'b04_nir_cir','5':'b05_nir_snoice','6':'b06_nir_cldphys'}
chtrans.update({'7':'b07_nir_sw','8':'b08_wv_hi','9':'b09_wv_mid','10':'b10_wv_lo','11':'b11_ir_cldphase','12':'b12_ir_ozone','13':'b13_ir_clean','14':'b14_ir','15':'b15_ir_dirty','16':'b16_ir_c02'})
chtrans2 = {'1':'vis_blue','2':'vis_red','3':'nir_veggie','4':'nir_cirrus','5':'nir_snoice','6':'nir_cldphys'}
chtrans2.update({'7':'swir','8':'wv_high','9':'wv_mid','10':'wv_lo','11':'ir_cldphase','12':'ir_ozone','13':'ir_clean','14':'ir','15':'ir_dirty','16':'ir_c02'})
job['defaults']['outputs']['pathdef'].append({'src':'globalmeta/channel_id','fmt':'str','translate':chtrans,'delimiter':''})
job['defaults']['outputs']['namedef'] = []
job['defaults']['outputs']['namedef'].append({'src':'globalmeta/start_date_time','method':'tstring_reformat','in_tfmt':'%Y%j%H%M%S','tfmt':'%Y%m%d_%H%M','delimiter':'.'})
job['defaults']['outputs']['namedef'].append({'src':'globalmeta/central_wavelength','fmt':'str','method':'char_replace','oldchar':'.','newchar':'p','delimiter':'_'})
job['defaults']['outputs']['namedef'].append({'src':'globalmeta/channel_id','fmt':'str','translate':chtrans2,'delimiter':'_'})
job['defaults']['outputs']['namedef'].append({'src':'globalmeta/output_product_name',      'fmt':'str','translate':{'Full Disk':'FD','CONUS':'CON','Mesoscale-1':'M1','Mesoscale-2':'M2'},'delimiter':''})
job['defaults']['outputs']['priddef'] = []
job['defaults']['outputs']['priddef'].append({'default':'16','delimiter':''})
job['defaults']['outputs']['priddef'].append({'src':'globalmeta/output_product_name',      'fmt':'str','translate':{'Full Disk':'FDRECT1','CONUS':'CORECT1','Mesoscale-1':'M1RECT1','Mesoscale-2':'M2RECT1'},'delimiter':''})
job['defaults']['outputs']['priddef'].append({'src':'globalmeta/channel_id','fmt':'str','pad':2,'padval':'0','delimiter':''})
job['defaults']['outputs']['priddef'].append({'src':'globalmeta/start_date_time','method':'tstring_reformat','in_tfmt':'%Y%j%H%M%S','tfmt':'%Y%m%d%H%M','delimiter':''})
job['defaults']['outputs']['meta'] = {}
job['defaults']['outputs']['meta']['areanumber']  = {'default':1}
job['defaults']['outputs']['meta']['band']        = {'default':4,     'src':'globalmeta/channel_id','fmt':'int'}
job['defaults']['outputs']['meta']['bpe']         = {'default':1}
job['defaults']['outputs']['meta']['caltype']     = {'default':'BRIT'}
job['defaults']['outputs']['meta']['projection']  = {'default':{},    'special':'get_projection'}
job['defaults']['outputs']['meta']['comment']     = {'default':''}
job['defaults']['outputs']['meta']['createstamp'] = {'default':0,     'special':'now'}
job['defaults']['outputs']['meta']['sensor']      = {'default':186}
job['defaults']['outputs']['meta']['sourcetype']  = {'default':'VISR'}
job['defaults']['outputs']['meta']['startstamp']  = {'default':0,     'src':'globalmeta/start_date_time','fmt':'float','method':'string_to_unixtime','in_tfmt':'%Y%j%H%M%S'}
job['defaults']['outputs']['meta']['xlen']        = {'default':1024,  'src':'globalmeta/product_columns','fmt':'int'}
job['defaults']['outputs']['meta']['ylen']        = {'default':1024,  'src':'globalmeta/product_rows','fmt':'int'}
job['defaults']['outputs']['ntiles']              = {'default':36,    'src':'globalmeta/number_product_tiles','fmt':'int'}
job['defaults']['outputs']['data']                = {'default':[],    'method':'fcalc','stack':['scmi','1','lookup']}
job['defaults']['outputs']['luts']                = {'1':{'type':'area_bt',  'parms':{'dtype':'u1'}}}
job['defaults']['outputs']['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['defaults']['outputs']['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['defaults']['outputs']['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['defaults']['outputs']['notify'] = ['finish','ldm']
job['defaults']['outputs']['link'] = ['link1']

job['outputs'] = {}
job['outputs'][1] = {}
job['outputs'][1]['input']  = 'FD_4'
job['outputs'][1]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][1]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][1]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][1]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][2] = {}
job['outputs'][2]['input']  = 'FD_6'
job['outputs'][2]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][2]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][2]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][2]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][3] = {}
job['outputs'][3]['input']  = 'FD_7'
job['outputs'][4] = {}
job['outputs'][4]['input']  = 'FD_8'
job['outputs'][5] = {}
job['outputs'][5]['input']  = 'FD_9'
job['outputs'][6] = {}
job['outputs'][6]['input']  = 'FD_10'
job['outputs'][7] = {}
job['outputs'][7]['input']  = 'FD_11'
job['outputs'][8] = {}
job['outputs'][8]['input']  = 'FD_12'
job['outputs'][9] = {}
job['outputs'][9]['input']  = 'FD_13'
job['outputs'][10] = {}
job['outputs'][10]['input'] = 'FD_14'
job['outputs'][11] = {}
job['outputs'][11]['input'] = 'FD_15'
job['outputs'][12] = {}
job['outputs'][12]['input'] = 'FD_16'
job['outputs'][13] = {}
job['outputs'][13]['input']  = 'FD_1'
job['outputs'][13]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][13]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][13]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][13]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][14] = {}
job['outputs'][14]['input']  = 'FD_2'
job['outputs'][14]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][14]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][14]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][14]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][15] = {}
job['outputs'][15]['input']  = 'FD_3'
job['outputs'][15]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][15]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][15]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][15]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][16] = {}
job['outputs'][16]['input']  = 'FD_5'
job['outputs'][16]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][16]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][16]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][16]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}

job['outputs'][17] = {}
job['outputs'][17]['input']  = 'CO_4'
job['outputs'][17]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][17]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][17]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][17]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][18] = {}
job['outputs'][18]['input']  = 'CO_6'
job['outputs'][18]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][18]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][18]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][18]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][19] = {}
job['outputs'][19]['input']  = 'CO_7'
job['outputs'][20] = {}
job['outputs'][20]['input']  = 'CO_8'
job['outputs'][21] = {}
job['outputs'][21]['input']  = 'CO_9'
job['outputs'][22] = {}
job['outputs'][22]['input']  = 'CO_10'
job['outputs'][23] = {}
job['outputs'][23]['input']  = 'CO_11'
job['outputs'][24] = {}
job['outputs'][24]['input']  = 'CO_12'
job['outputs'][25] = {}
job['outputs'][25]['input']  = 'CO_13'
job['outputs'][26] = {}
job['outputs'][26]['input'] = 'CO_14'
job['outputs'][27] = {}
job['outputs'][27]['input'] = 'CO_15'
job['outputs'][28] = {}
job['outputs'][28]['input'] = 'CO_16'
job['outputs'][29] = {}
job['outputs'][29]['input']  = 'CO_1'
job['outputs'][29]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][29]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][29]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][29]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][30] = {}
job['outputs'][30]['input']  = 'CO_2'
job['outputs'][30]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][30]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][30]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][30]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][31] = {}
job['outputs'][31]['input']  = 'CO_3'
job['outputs'][31]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][31]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][31]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][31]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][32] = {}
job['outputs'][32]['input']  = 'CO_5'
job['outputs'][32]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][32]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][32]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][32]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][33] = {}
job['outputs'][33]['input']  = 'M1_4'
job['outputs'][33]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][33]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][33]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][33]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][34] = {}
job['outputs'][34]['input']  = 'M1_6'
job['outputs'][34]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][34]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][34]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][34]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][35] = {}
job['outputs'][35]['input']  = 'M1_7'
job['outputs'][36] = {}
job['outputs'][36]['input']  = 'M1_8'
job['outputs'][37] = {}
job['outputs'][37]['input']  = 'M1_9'
job['outputs'][38] = {}
job['outputs'][38]['input']  = 'M1_10'
job['outputs'][39] = {}
job['outputs'][39]['input']  = 'M1_11'
job['outputs'][40] = {}
job['outputs'][40]['input']  = 'M1_12'
job['outputs'][41] = {}
job['outputs'][41]['input']  = 'M1_13'
job['outputs'][42] = {}
job['outputs'][42]['input'] = 'M1_14'
job['outputs'][43] = {}
job['outputs'][43]['input'] = 'M1_15'
job['outputs'][44] = {}
job['outputs'][44]['input'] = 'M1_16'
job['outputs'][45] = {}
job['outputs'][45]['input']  = 'M1_1'
job['outputs'][45]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][45]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][45]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][45]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][46] = {}
job['outputs'][46]['input']  = 'M1_2'
job['outputs'][46]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][46]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][46]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][46]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][47] = {}
job['outputs'][47]['input']  = 'M1_3'
job['outputs'][47]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][47]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][47]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][47]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][48] = {}
job['outputs'][48]['input']  = 'M1_5'
job['outputs'][48]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][48]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][48]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][48]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][49] = {}
job['outputs'][49]['input']  = 'M2_4'
job['outputs'][49]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][49]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][49]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][49]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][50] = {}
job['outputs'][50]['input']  = 'M2_6'
job['outputs'][50]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][50]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][50]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][50]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][51] = {}
job['outputs'][51]['input']  = 'M2_7'
job['outputs'][52] = {}
job['outputs'][52]['input']  = 'M2_8'
job['outputs'][53] = {}
job['outputs'][53]['input']  = 'M2_9'
job['outputs'][54] = {}
job['outputs'][54]['input']  = 'M2_10'
job['outputs'][55] = {}
job['outputs'][55]['input']  = 'M2_11'
job['outputs'][56] = {}
job['outputs'][56]['input']  = 'M2_12'
job['outputs'][57] = {}
job['outputs'][57]['input']  = 'M2_13'
job['outputs'][58] = {}
job['outputs'][58]['input'] = 'M2_14'
job['outputs'][59] = {}
job['outputs'][59]['input'] = 'M2_15'
job['outputs'][60] = {}
job['outputs'][60]['input'] = 'M2_16'
job['outputs'][61] = {}
job['outputs'][61]['input']  = 'M2_1'
job['outputs'][61]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][61]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][61]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][61]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][62] = {}
job['outputs'][62]['input']  = 'M2_2'
job['outputs'][62]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][62]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][62]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][62]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][63] = {}
job['outputs'][63]['input']  = 'M2_3'
job['outputs'][63]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][63]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][63]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][63]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}
job['outputs'][64] = {}
job['outputs'][64]['input']  = 'M2_5'
job['outputs'][64]['luts']   = {'1':{'type':'area_refl','parms':{'dtype':'u1'}}}
job['outputs'][64]['luts']['1']['parms']['inscale']  = {'src':'variables/Sectorized_CMI/attr/scale_factor','fmt':'float'}
job['outputs'][64]['luts']['1']['parms']['inoffset'] = {'src':'variables/Sectorized_CMI/attr/add_offset','fmt':'float'}
job['outputs'][64]['luts']['1']['parms']['inbits']   = {'src':'globalmeta/bit_depth','fmt':'int'}

