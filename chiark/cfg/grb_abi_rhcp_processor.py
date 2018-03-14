# isatss job definition for grb abi scmi tile generation


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
job['name']  = 'grb_abi_rhcp_processor'
job['cmd']   = 'grber'
job['class'] = 'GRBProc'
job['log']   = 'grb_abi_rhcp_processor_log'

job['inpath']      = '/scratch/isatss_data/incoming/grb_rhcp/abi'
job['notifications'] = {}
job['notifications']['ldm']  =  {'node':6,'enabled':True,'fields':['file','prodid','wmo'],'prefix':'abi_rhcp_ldm'}
job['notifications']['area'] =  {'node':12,'enabled':True,'fields':['file'],'prefix':'abi_rhcp_area'}
job['notifications']['marea'] = {'node':10,'enabled':True,'fields':['file'],'prefix':'abi_rhcp_marea'}
job['notifications']['mon']   = {'node':16,'enabled':True,'fields':['file','node','band','size','scene','sat','mode','ctime','ptime','clat','clon','tileno','tiletot','fault'],'prefix':'abi_lhcp_mon','jobinfo':True}

job['read_node']   = 3
job['satcfg']	   = 'goesr_config'
job['qlimit']      = 1000

#TODO: create a data characterization object
job['data'] = {}
job['data']['products']               = {}
job['data']['products']['location']   = {'node':14, 'type':'datapath', 'path':'abi'}
job['data']['products']['aging']      = {'window':86400, 'mode':'elapsedname', 'fmt':'%Y%m%d%H'}
job['data']['products']['method']     = {'technique':'stage', 'path':'incinerator'}
job['data']['products']['activeonly'] = True															# check pidfile
job['data']['products']['schedule']   = {'interval':600}
job['data']['infoldm']                = {}
job['data']['infoldm']['location']    = {'node':6,'type':'infopath'}
job['data']['infoldm']['filter']      = {'type':'starts','test':job['notifications']['ldm']['prefix']}
job['data']['infoldm']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['infoldm']['method']      = {'technique':'inplace'}
job['data']['infoldm']['activeonly']  = True
job['data']['infoldm']['schedule']    = {'interval':600}
job['data']['infoarea']                = {}
job['data']['infoarea']['location']    = {'node':12,'type':'infopath'}
job['data']['infoarea']['filter']      = {'type':'starts','test':job['notifications']['area']['prefix']}
job['data']['infoarea']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['infoarea']['method']      = {'technique':'inplace'}
job['data']['infoarea']['activeonly']  = True
job['data']['infoarea']['schedule']    = {'interval':600}
job['data']['infomarea']               = {}
job['data']['infomarea']['location']   = {'node':10,'type':'infopath'}
job['data']['infomarea']['filter']     = {'type':'starts','test':job['notifications']['marea']['prefix']}
job['data']['infomarea']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['infomarea']['method']     = {'technique':'inplace'}
job['data']['infomarea']['activeonly'] = True
job['data']['infomarea']['schedule']   = {'interval':600}
job['data']['infomon']                 = {}
job['data']['infomon']['location']     = {'node':16,'type':'infopath'}
job['data']['infomon']['filter']       = {'type':'starts','test':job['notifications']['mon']['prefix']}
job['data']['infomon']['aging']        = {'window':3600, 'mode':'creationtime'}
job['data']['infomon']['method']       = {'technique':'inplace'}
job['data']['infomon']['activeonly']   = True
job['data']['infomon']['schedule']     = {'interval':600}
job['data']['log']                     = {}
job['data']['log']['location']	       = {'node':1,'type':'datapath', 'path':'log'}
job['data']['log']['aging']            = {'window':2,'mode':'count'}
job['data']['log']['archive']          = {'window':7,'mode':'count'}
job['data']['log']['roots']            = [job['log']]
job['data']['log']['method']           = {'technique':'inplace'}
job['data']['log']['schedule']         = {'interval':3600}
job['data']['log']['activeonly']       = True

job['defaults'] = {}
job['defaults']['products'] = {}
job['defaults']['products']['bands']               = [4,6,7,8,9,10,11,12,13,14,15,16]
job['defaults']['products']['center']              = {'lat':0.0,'lon':0.0}
job['defaults']['products']['class']               = 'image'
job['defaults']['products']['ins']                 = 'abi'
job['defaults']['products']['module']			   = 'im_grb_abii'
job['defaults']['products']['notify']			   = ['area','ldm']
job['defaults']['products']['outroot']             = job['data']['products']['location']
job['defaults']['products']['prodtype']			   = 'ABII'
job['defaults']['products']['production_location'] = 'NAPO'
job['defaults']['products']['satellite']           = 'Test'
job['defaults']['products']['scene']               = 'FD'
job['defaults']['products']['shape']               = {'y':506,'x':904}
job['defaults']['products']['spec']                = 'abi_scmi_tile'
job['defaults']['products']['tiles']               = 62
job['defaults']['products']['wmo_enabled']         = True

job['products'] = {}
# 2km full disk
job['products'][0]  = {'tile':0, 'blocks':[4,5],            'map':{'y':0,'x':904},   'shape':{'y':404,'x':904}}
job['products'][1]  = {'tile':1, 'blocks':[0,1,6,7],        'map':{'y':0,'x':1808},  'shape':{'y':404,'x':904}}
job['products'][2]  = {'tile':2, 'blocks':[2,3,8,9],        'map':{'y':0,'x':2712},  'shape':{'y':404,'x':904}}
job['products'][3]  = {'tile':3, 'blocks':[10,11],          'map':{'y':0,'x':3616},  'shape':{'y':404,'x':904}}
job['products'][4]  = {'tile':4, 'blocks':[20],             'map':{'y':404,'x':0}}
job['products'][5]  = {'tile':5, 'blocks':[12,13,21,22],    'map':{'y':404,'x':904}}
job['products'][6]  = {'tile':6, 'blocks':[14,15,23,24],    'map':{'y':404,'x':1808}}
job['products'][7]  = {'tile':7, 'blocks':[16,17,25,26],    'map':{'y':404,'x':2712}}
job['products'][8]  = {'tile':8, 'blocks':[18,19,27,28],    'map':{'y':404,'x':3616}}
job['products'][9]  = {'tile':9, 'blocks':[29],             'map':{'y':404,'x':4520}}
job['products'][10] = {'tile':10,'blocks':[30,40,41],       'map':{'y':910,'x':0}}
job['products'][11] = {'tile':11,'blocks':[31,32,42,43],    'map':{'y':910,'x':904}}
job['products'][12] = {'tile':12,'blocks':[33,34,44,45],    'map':{'y':910,'x':1808}}
job['products'][13] = {'tile':13,'blocks':[35,36,46,47],    'map':{'y':910,'x':2712}}
job['products'][14] = {'tile':14,'blocks':[37,38,48,49],    'map':{'y':910,'x':3616}}
job['products'][15] = {'tile':15,'blocks':[39,50,51],       'map':{'y':910,'x':4520}}
job['products'][16] = {'tile':16,'blocks':[52,53,64,65],    'map':{'y':1416,'x':0}}
job['products'][17] = {'tile':17,'blocks':[54,55,66,67],    'map':{'y':1416,'x':904}}
job['products'][18] = {'tile':18,'blocks':[56,57,68,69],    'map':{'y':1416,'x':1808}}
job['products'][19] = {'tile':19,'blocks':[58,59,70,71],    'map':{'y':1416,'x':2712}}
job['products'][20] = {'tile':20,'blocks':[60,61,72,73],    'map':{'y':1416,'x':3616}}
job['products'][21] = {'tile':21,'blocks':[62,63,74,75],    'map':{'y':1416,'x':4520}}
job['products'][22] = {'tile':22,'blocks':[76,77,88,89],    'map':{'y':1922,'x':0}}
job['products'][23] = {'tile':23,'blocks':[78,79,90,91],    'map':{'y':1922,'x':904}}
job['products'][24] = {'tile':24,'blocks':[80,81,92,93],    'map':{'y':1922,'x':1808}}
job['products'][25] = {'tile':25,'blocks':[82,83,94,95],    'map':{'y':1922,'x':2712}}
job['products'][26] = {'tile':26,'blocks':[84,85,96,97],    'map':{'y':1922,'x':3616}}
job['products'][27] = {'tile':27,'blocks':[86,87,98,99],    'map':{'y':1922,'x':4520}}
job['products'][28] = {'tile':28,'blocks':[100,101,112,113],'map':{'y':2428,'x':0},   'shape':{'y':505,'x':904}}
job['products'][29] = {'tile':29,'blocks':[102,103,114,115],'map':{'y':2428,'x':904}, 'shape':{'y':505,'x':904}}
job['products'][30] = {'tile':30,'blocks':[104,105,116,117],'map':{'y':2428,'x':1808},'shape':{'y':505,'x':904}}
job['products'][31] = {'tile':31,'blocks':[106,107,118,119],'map':{'y':2428,'x':2712},'shape':{'y':505,'x':904}}
job['products'][32] = {'tile':32,'blocks':[108,109,120,121],'map':{'y':2428,'x':3616},'shape':{'y':505,'x':904}}
job['products'][33] = {'tile':33,'blocks':[110,111,122,123],'map':{'y':2428,'x':4520},'shape':{'y':505,'x':904}}
job['products'][34] = {'tile':34,'blocks':[124,125,136,137],'map':{'y':2933,'x':0}}
job['products'][35] = {'tile':35,'blocks':[126,127,138,139],'map':{'y':2933,'x':904}}
job['products'][36] = {'tile':36,'blocks':[128,129,140,141],'map':{'y':2933,'x':1808}}
job['products'][37] = {'tile':37,'blocks':[130,131,142,143],'map':{'y':2933,'x':2712}}
job['products'][38] = {'tile':38,'blocks':[132,133,144,145],'map':{'y':2933,'x':3616}}
job['products'][39] = {'tile':39,'blocks':[134,135,146,147],'map':{'y':2933,'x':4520}}
job['products'][40] = {'tile':40,'blocks':[148,149,160,161],'map':{'y':3439,'x':0}}
job['products'][41] = {'tile':41,'blocks':[150,151,162,163],'map':{'y':3439,'x':904}}
job['products'][42] = {'tile':42,'blocks':[152,153,164,165],'map':{'y':3439,'x':1808}}
job['products'][43] = {'tile':43,'blocks':[154,155,166,167],'map':{'y':3439,'x':2712}}
job['products'][44] = {'tile':44,'blocks':[156,157,168,169],'map':{'y':3439,'x':3616}}
job['products'][45] = {'tile':45,'blocks':[158,159,170,171],'map':{'y':3439,'x':4520}}
job['products'][46] = {'tile':46,'blocks':[172,173,184,185],'map':{'y':3945,'x':0}}
job['products'][47] = {'tile':47,'blocks':[174,175,186,187],'map':{'y':3945,'x':904}}
job['products'][48] = {'tile':48,'blocks':[176,177,188,189],'map':{'y':3945,'x':1808}}
job['products'][49] = {'tile':49,'blocks':[178,179,190,191],'map':{'y':3945,'x':2712}}
job['products'][50] = {'tile':50,'blocks':[180,181,192,193],'map':{'y':3945,'x':3616}}
job['products'][51] = {'tile':51,'blocks':[182,183,194,195],'map':{'y':3945,'x':4520}}
job['products'][52] = {'tile':52,'blocks':[196,206],        'map':{'y':4451,'x':0}}
job['products'][53] = {'tile':53,'blocks':[197,198,207,208],'map':{'y':4451,'x':904}}
job['products'][54] = {'tile':54,'blocks':[199,200,209,210],'map':{'y':4451,'x':1808}}
job['products'][55] = {'tile':55,'blocks':[201,202,211,212],'map':{'y':4451,'x':2712}}
job['products'][56] = {'tile':56,'blocks':[203,204,213,214],'map':{'y':4451,'x':3616}}
job['products'][57] = {'tile':57,'blocks':[205,215],        'map':{'y':4451,'x':4520}}
job['products'][58] = {'tile':58,'blocks':[216,217,224],    'map':{'y':4957,'x':904}, 'shape':{'y':467,'x':904}}
job['products'][59] = {'tile':59,'blocks':[218,219,225,226],'map':{'y':4957,'x':1808},'shape':{'y':467,'x':904}}
job['products'][60] = {'tile':60,'blocks':[220,221,227,228],'map':{'y':4957,'x':2712},'shape':{'y':467,'x':904}}
job['products'][61] = {'tile':61,'blocks':[222,223,229],    'map':{'y':4957,'x':3616},'shape':{'y':467,'x':904}}

# 1 km full disk
job['products'][62]  = {'tile':0, 'bands':[1,3,5],'blocks':[4,5],            'map':{'y':0,  'x':1808}, 'shape':{'y':808,'x':1808}}
job['products'][63]  = {'tile':1, 'bands':[1,3,5],'blocks':[0,1,6,7],        'map':{'y':0,  'x':3616}, 'shape':{'y':808,'x':1808}}
job['products'][64]  = {'tile':2, 'bands':[1,3,5],'blocks':[2,3,8,9],        'map':{'y':0,  'x':5424}, 'shape':{'y':808,'x':1808}}
job['products'][65]  = {'tile':3, 'bands':[1,3,5],'blocks':[10,11],          'map':{'y':0,  'x':7232}, 'shape':{'y':808,'x':1808}}
job['products'][66]  = {'tile':4, 'bands':[1,3,5],'blocks':[20],             'map':{'y':808, 'x':0},   'shape':{'y':1012,'x':1808}}
job['products'][67]  = {'tile':5, 'bands':[1,3,5],'blocks':[12,13,21,22],    'map':{'y':808, 'x':1808},'shape':{'y':1012,'x':1808}}
job['products'][68]  = {'tile':6, 'bands':[1,3,5],'blocks':[14,15,23,24],    'map':{'y':808, 'x':3616},'shape':{'y':1012,'x':1808}}
job['products'][69]  = {'tile':7, 'bands':[1,3,5],'blocks':[16,17,25,26],    'map':{'y':808, 'x':5424},'shape':{'y':1012,'x':1808}}
job['products'][70]  = {'tile':8, 'bands':[1,3,5],'blocks':[18,19,27,28],    'map':{'y':808, 'x':7232},'shape':{'y':1012,'x':1808}}
job['products'][71]  = {'tile':9, 'bands':[1,3,5],'blocks':[29],             'map':{'y':808, 'x':9040},'shape':{'y':1012,'x':1808}}
job['products'][72]  = {'tile':10,'bands':[1,3,5],'blocks':[30,40,41],       'map':{'y':1820,'x':0},   'shape':{'y':1012,'x':1808}}
job['products'][73]  = {'tile':11,'bands':[1,3,5],'blocks':[31,32,42,43],    'map':{'y':1820,'x':1808},'shape':{'y':1012,'x':1808}}
job['products'][74]  = {'tile':12,'bands':[1,3,5],'blocks':[33,34,44,45],    'map':{'y':1820,'x':3616},'shape':{'y':1012,'x':1808}}
job['products'][75]  = {'tile':13,'bands':[1,3,5],'blocks':[35,36,46,47],    'map':{'y':1820,'x':5424},'shape':{'y':1012,'x':1808}}
job['products'][76]  = {'tile':14,'bands':[1,3,5],'blocks':[37,38,48,49],    'map':{'y':1820,'x':7232},'shape':{'y':1012,'x':1808}}
job['products'][77]  = {'tile':15,'bands':[1,3,5],'blocks':[39,50,51],       'map':{'y':1820,'x':9040},'shape':{'y':1012,'x':1808}}
job['products'][78]  = {'tile':16,'bands':[1,3,5],'blocks':[52,53,64,65],    'map':{'y':2832,'x':0},   'shape':{'y':1012,'x':1808}}
job['products'][79]  = {'tile':17,'bands':[1,3,5],'blocks':[54,55,66,67],    'map':{'y':2832,'x':1808},'shape':{'y':1012,'x':1808}}
job['products'][80]  = {'tile':18,'bands':[1,3,5],'blocks':[56,57,68,69],    'map':{'y':2832,'x':3616},'shape':{'y':1012,'x':1808}}
job['products'][81]  = {'tile':19,'bands':[1,3,5],'blocks':[58,59,70,71],    'map':{'y':2832,'x':5424},'shape':{'y':1012,'x':1808}}
job['products'][82]  = {'tile':20,'bands':[1,3,5],'blocks':[60,61,72,73],    'map':{'y':2832,'x':7232},'shape':{'y':1012,'x':1808}}
job['products'][83]  = {'tile':21,'bands':[1,3,5],'blocks':[62,63,74,75],    'map':{'y':2832,'x':9040},'shape':{'y':1012,'x':1808}}
job['products'][84]  = {'tile':22,'bands':[1,3,5],'blocks':[76,77,88,89],    'map':{'y':3844,'x':0},   'shape':{'y':1012,'x':1808}}
job['products'][85]  = {'tile':23,'bands':[1,3,5],'blocks':[78,79,90,91],    'map':{'y':3844,'x':1808},'shape':{'y':1012,'x':1808}}
job['products'][86]  = {'tile':24,'bands':[1,3,5],'blocks':[80,81,92,93],    'map':{'y':3844,'x':3616},'shape':{'y':1012,'x':1808}}
job['products'][87]  = {'tile':25,'bands':[1,3,5],'blocks':[82,83,94,95],    'map':{'y':3844,'x':5424},'shape':{'y':1012,'x':1808}}
job['products'][88]  = {'tile':26,'bands':[1,3,5],'blocks':[84,85,96,97],    'map':{'y':3844,'x':7232},'shape':{'y':1012,'x':1808}}
job['products'][89]  = {'tile':27,'bands':[1,3,5],'blocks':[86,87,98,99],    'map':{'y':3844,'x':9040},'shape':{'y':1012,'x':1808}}
job['products'][90]  = {'tile':28,'bands':[1,3,5],'blocks':[100,101,112,113],'map':{'y':4856,'x':0},   'shape':{'y':1010,'x':1808}}
job['products'][91]  = {'tile':29,'bands':[1,3,5],'blocks':[102,103,114,115],'map':{'y':4856,'x':1808},'shape':{'y':1010,'x':1808}}
job['products'][92]  = {'tile':30,'bands':[1,3,5],'blocks':[104,105,116,117],'map':{'y':4856,'x':3616},'shape':{'y':1010,'x':1808}}
job['products'][93]  = {'tile':31,'bands':[1,3,5],'blocks':[106,107,118,119],'map':{'y':4856,'x':5424},'shape':{'y':1010,'x':1808}}
job['products'][94]  = {'tile':32,'bands':[1,3,5],'blocks':[108,109,120,121],'map':{'y':4856,'x':7232},'shape':{'y':1010,'x':1808}}
job['products'][95]  = {'tile':33,'bands':[1,3,5],'blocks':[110,111,122,123],'map':{'y':4856,'x':9040},'shape':{'y':1010,'x':1808}}
job['products'][96]  = {'tile':34,'bands':[1,3,5],'blocks':[124,125,136,137],'map':{'y':5866,'x':0},   'shape':{'y':1012,'x':1808}}
job['products'][97]  = {'tile':35,'bands':[1,3,5],'blocks':[126,127,138,139],'map':{'y':5866,'x':1808},'shape':{'y':1012,'x':1808}}
job['products'][98]  = {'tile':36,'bands':[1,3,5],'blocks':[128,129,140,141],'map':{'y':5866,'x':3616},'shape':{'y':1012,'x':1808}}
job['products'][99]  = {'tile':37,'bands':[1,3,5],'blocks':[130,131,142,143],'map':{'y':5866,'x':5424},'shape':{'y':1012,'x':1808}}
job['products'][100] = {'tile':38,'bands':[1,3,5],'blocks':[132,133,144,145],'map':{'y':5866,'x':7232},'shape':{'y':1012,'x':1808}}
job['products'][101] = {'tile':39,'bands':[1,3,5],'blocks':[134,135,146,147],'map':{'y':5866,'x':9040},'shape':{'y':1012,'x':1808}}
job['products'][102] = {'tile':40,'bands':[1,3,5],'blocks':[148,149,160,161],'map':{'y':6878,'x':0},   'shape':{'y':1012,'x':1808}}
job['products'][103] = {'tile':41,'bands':[1,3,5],'blocks':[150,151,162,163],'map':{'y':6878,'x':1808},'shape':{'y':1012,'x':1808}}
job['products'][104] = {'tile':42,'bands':[1,3,5],'blocks':[152,153,164,165],'map':{'y':6878,'x':3616},'shape':{'y':1012,'x':1808}}
job['products'][105] = {'tile':43,'bands':[1,3,5],'blocks':[154,155,166,167],'map':{'y':6878,'x':5424},'shape':{'y':1012,'x':1808}}
job['products'][106] = {'tile':44,'bands':[1,3,5],'blocks':[156,157,168,169],'map':{'y':6878,'x':7232},'shape':{'y':1012,'x':1808}}
job['products'][107] = {'tile':45,'bands':[1,3,5],'blocks':[158,159,170,171],'map':{'y':6878,'x':9040},'shape':{'y':1012,'x':1808}}
job['products'][108] = {'tile':46,'bands':[1,3,5],'blocks':[172,173,184,185],'map':{'y':7890,'x':0},   'shape':{'y':1012,'x':1808}}
job['products'][109] = {'tile':47,'bands':[1,3,5],'blocks':[174,175,186,187],'map':{'y':7890,'x':1808},'shape':{'y':1012,'x':1808}}
job['products'][110] = {'tile':48,'bands':[1,3,5],'blocks':[176,177,188,189],'map':{'y':7890,'x':3616},'shape':{'y':1012,'x':1808}}
job['products'][111] = {'tile':49,'bands':[1,3,5],'blocks':[178,179,190,191],'map':{'y':7890,'x':5424},'shape':{'y':1012,'x':1808}}
job['products'][112] = {'tile':50,'bands':[1,3,5],'blocks':[180,181,192,193],'map':{'y':7890,'x':7232},'shape':{'y':1012,'x':1808}}
job['products'][113] = {'tile':51,'bands':[1,3,5],'blocks':[182,183,194,195],'map':{'y':7890,'x':9040},'shape':{'y':1012,'x':1808}}
job['products'][114] = {'tile':52,'bands':[1,3,5],'blocks':[196,206],        'map':{'y':8902,'x':0},   'shape':{'y':1012,'x':1808}}
job['products'][115] = {'tile':53,'bands':[1,3,5],'blocks':[197,198,207,208],'map':{'y':8902,'x':1808},'shape':{'y':1012,'x':1808}}
job['products'][116] = {'tile':54,'bands':[1,3,5],'blocks':[199,200,209,210],'map':{'y':8902,'x':3616},'shape':{'y':1012,'x':1808}}
job['products'][117] = {'tile':55,'bands':[1,3,5],'blocks':[201,202,211,212],'map':{'y':8902,'x':5424},'shape':{'y':1012,'x':1808}}
job['products'][118] = {'tile':56,'bands':[1,3,5],'blocks':[203,204,213,214],'map':{'y':8902,'x':7232},'shape':{'y':1012,'x':1808}}
job['products'][119] = {'tile':57,'bands':[1,3,5],'blocks':[205,215],        'map':{'y':8902,'x':9040},'shape':{'y':1012,'x':1808}}
job['products'][120] = {'tile':58,'bands':[1,3,5],'blocks':[216,217,224],    'map':{'y':9914,'x':1808},'shape':{'y':934, 'x':1808}}
job['products'][121] = {'tile':59,'bands':[1,3,5],'blocks':[218,219,225,226],'map':{'y':9914,'x':3616},'shape':{'y':934, 'x':1808}}
job['products'][122] = {'tile':60,'bands':[1,3,5],'blocks':[220,221,227,228],'map':{'y':9914,'x':5424},'shape':{'y':934, 'x':1808}}
job['products'][123] = {'tile':61,'bands':[1,3,5],'blocks':[222,223,229],    'map':{'y':9914,'x':7232},'shape':{'y':934, 'x':1808}}

# 0.5km full disk
job['products'][124] = {'tile':0, 'bands':[2],'blocks':[4,5],            'map':{'y':0,   'x':3616},  'shape':{'y':1616,'x':3616}}
job['products'][125] = {'tile':1, 'bands':[2],'blocks':[0,1,6,7],        'map':{'y':0,   'x':7232},  'shape':{'y':1616,'x':3616}}
job['products'][126] = {'tile':2, 'bands':[2],'blocks':[2,3,8,9],        'map':{'y':0,   'x':10848}, 'shape':{'y':1616,'x':3616}}
job['products'][127] = {'tile':3, 'bands':[2],'blocks':[10,11],          'map':{'y':0,   'x':14464}, 'shape':{'y':1616,'x':3616}}
job['products'][128] = {'tile':4, 'bands':[2],'blocks':[20],             'map':{'y':1616,'x':0},     'shape':{'y':2024,'x':3616}}
job['products'][129] = {'tile':5, 'bands':[2],'blocks':[12,13,21,22],    'map':{'y':1616,'x':3616},  'shape':{'y':2024,'x':3616}}
job['products'][130] = {'tile':6, 'bands':[2],'blocks':[14,15,23,24],    'map':{'y':1616,'x':7232},  'shape':{'y':2024,'x':3616}}
job['products'][131] = {'tile':7, 'bands':[2],'blocks':[16,17,25,26],    'map':{'y':1616,'x':10848}, 'shape':{'y':2024,'x':3616}}
job['products'][132] = {'tile':8, 'bands':[2],'blocks':[18,19,27,28],    'map':{'y':1616,'x':14464}, 'shape':{'y':2024,'x':3616}}
job['products'][133] = {'tile':9, 'bands':[2],'blocks':[29],             'map':{'y':1616,'x':18080}, 'shape':{'y':2024,'x':3616}}
job['products'][134] = {'tile':10,'bands':[2],'blocks':[30,40,41],       'map':{'y':3640,'x':0},     'shape':{'y':2024,'x':3616}}
job['products'][135] = {'tile':11,'bands':[2],'blocks':[31,32,42,43],    'map':{'y':3640,'x':3616},  'shape':{'y':2024,'x':3616}}
job['products'][136] = {'tile':12,'bands':[2],'blocks':[33,34,44,45],    'map':{'y':3640,'x':7232},  'shape':{'y':2024,'x':3616}}
job['products'][137] = {'tile':13,'bands':[2],'blocks':[35,36,46,47],    'map':{'y':3640,'x':10848}, 'shape':{'y':2024,'x':3616}}
job['products'][138] = {'tile':14,'bands':[2],'blocks':[37,38,48,49],    'map':{'y':3640,'x':14464}, 'shape':{'y':2024,'x':3616}}
job['products'][139] = {'tile':15,'bands':[2],'blocks':[39,50,51],       'map':{'y':3640,'x':18080}, 'shape':{'y':2024,'x':3616}}
job['products'][140] = {'tile':16,'bands':[2],'blocks':[52,53,64,65],    'map':{'y':5664,'x':0},     'shape':{'y':2024,'x':3616}}
job['products'][141] = {'tile':17,'bands':[2],'blocks':[54,55,66,67],    'map':{'y':5664,'x':3616},  'shape':{'y':2024,'x':3616}}
job['products'][142] = {'tile':18,'bands':[2],'blocks':[56,57,68,69],    'map':{'y':5664,'x':7232},  'shape':{'y':2024,'x':3616}}
job['products'][143] = {'tile':19,'bands':[2],'blocks':[58,59,70,71],    'map':{'y':5664,'x':10848}, 'shape':{'y':2024,'x':3616}}
job['products'][144] = {'tile':20,'bands':[2],'blocks':[60,61,72,73],    'map':{'y':5664,'x':14464}, 'shape':{'y':2024,'x':3616}}
job['products'][145] = {'tile':21,'bands':[2],'blocks':[62,63,74,75],    'map':{'y':5664,'x':18080}, 'shape':{'y':2024,'x':3616}}
job['products'][146] = {'tile':22,'bands':[2],'blocks':[76,77,88,89],    'map':{'y':7688,'x':0},     'shape':{'y':2024,'x':3616}}
job['products'][147] = {'tile':23,'bands':[2],'blocks':[78,79,90,91],    'map':{'y':7688,'x':3616},  'shape':{'y':2024,'x':3616}}
job['products'][148] = {'tile':24,'bands':[2],'blocks':[80,81,92,93],    'map':{'y':7688,'x':7232},  'shape':{'y':2024,'x':3616}}
job['products'][149] = {'tile':25,'bands':[2],'blocks':[82,83,94,95],    'map':{'y':7688,'x':10848}, 'shape':{'y':2024,'x':3616}}
job['products'][150] = {'tile':26,'bands':[2],'blocks':[84,85,96,97],    'map':{'y':7688,'x':14464}, 'shape':{'y':2024,'x':3616}}
job['products'][151] = {'tile':27,'bands':[2],'blocks':[86,87,98,99],    'map':{'y':7688,'x':18080}, 'shape':{'y':2024,'x':3616}}
job['products'][152] = {'tile':28,'bands':[2],'blocks':[100,101,112,113],'map':{'y':9712,'x':0},     'shape':{'y':2020,'x':3616}}
job['products'][153] = {'tile':29,'bands':[2],'blocks':[102,103,114,115],'map':{'y':9712,'x':3616},  'shape':{'y':2020,'x':3616}}
job['products'][154] = {'tile':30,'bands':[2],'blocks':[104,105,116,117],'map':{'y':9712,'x':7232},  'shape':{'y':2020,'x':3616}}
job['products'][155] = {'tile':31,'bands':[2],'blocks':[106,107,118,119],'map':{'y':9712,'x':10848}, 'shape':{'y':2020,'x':3616}}
job['products'][156] = {'tile':32,'bands':[2],'blocks':[108,109,120,121],'map':{'y':9712,'x':14464}, 'shape':{'y':2020,'x':3616}}
job['products'][157] = {'tile':33,'bands':[2],'blocks':[110,111,122,123],'map':{'y':9712,'x':18080}, 'shape':{'y':2020,'x':3616}}
job['products'][158] = {'tile':34,'bands':[2],'blocks':[124,125,136,137],'map':{'y':11732,'x':0},    'shape':{'y':2024,'x':3616}}
job['products'][159] = {'tile':35,'bands':[2],'blocks':[126,127,138,139],'map':{'y':11732,'x':3616}, 'shape':{'y':2024,'x':3616}}
job['products'][160] = {'tile':36,'bands':[2],'blocks':[128,129,140,141],'map':{'y':11732,'x':7232}, 'shape':{'y':2024,'x':3616}}
job['products'][161] = {'tile':37,'bands':[2],'blocks':[130,131,142,143],'map':{'y':11732,'x':10848},'shape':{'y':2024,'x':3616}}
job['products'][162] = {'tile':38,'bands':[2],'blocks':[132,133,144,145],'map':{'y':11732,'x':14464},'shape':{'y':2024,'x':3616}}
job['products'][163] = {'tile':39,'bands':[2],'blocks':[134,135,146,147],'map':{'y':11732,'x':18080},'shape':{'y':2024,'x':3616}}
job['products'][164] = {'tile':40,'bands':[2],'blocks':[148,149,160,161],'map':{'y':13756,'x':0},    'shape':{'y':2024,'x':3616}}
job['products'][165] = {'tile':41,'bands':[2],'blocks':[150,151,162,163],'map':{'y':13756,'x':3616}, 'shape':{'y':2024,'x':3616}}
job['products'][166] = {'tile':42,'bands':[2],'blocks':[152,153,164,165],'map':{'y':13756,'x':7232}, 'shape':{'y':2024,'x':3616}}
job['products'][167] = {'tile':43,'bands':[2],'blocks':[154,155,166,167],'map':{'y':13756,'x':10848},'shape':{'y':2024,'x':3616}}
job['products'][168] = {'tile':44,'bands':[2],'blocks':[156,157,168,169],'map':{'y':13756,'x':14464},'shape':{'y':2024,'x':3616}}
job['products'][169] = {'tile':45,'bands':[2],'blocks':[158,159,170,171],'map':{'y':13756,'x':18080},'shape':{'y':2024,'x':3616}}
job['products'][170] = {'tile':46,'bands':[2],'blocks':[172,173,184,185],'map':{'y':15780,'x':0},    'shape':{'y':2024,'x':3616}}
job['products'][171] = {'tile':47,'bands':[2],'blocks':[174,175,186,187],'map':{'y':15780,'x':3616}, 'shape':{'y':2024,'x':3616}}
job['products'][172] = {'tile':48,'bands':[2],'blocks':[176,177,188,189],'map':{'y':15780,'x':7232}, 'shape':{'y':2024,'x':3616}}
job['products'][173] = {'tile':49,'bands':[2],'blocks':[178,179,190,191],'map':{'y':15780,'x':10848},'shape':{'y':2024,'x':3616}}
job['products'][174] = {'tile':50,'bands':[2],'blocks':[180,181,192,193],'map':{'y':15780,'x':14464},'shape':{'y':2024,'x':3616}}
job['products'][175] = {'tile':51,'bands':[2],'blocks':[182,183,194,195],'map':{'y':15780,'x':18080},'shape':{'y':2024,'x':3616}}
job['products'][176] = {'tile':52,'bands':[2],'blocks':[196,206],        'map':{'y':17804,'x':0},    'shape':{'y':2024,'x':3616}}
job['products'][177] = {'tile':53,'bands':[2],'blocks':[197,198,207,208],'map':{'y':17804,'x':3616}, 'shape':{'y':2024,'x':3616}}
job['products'][178] = {'tile':54,'bands':[2],'blocks':[199,200,209,210],'map':{'y':17804,'x':7232}, 'shape':{'y':2024,'x':3616}}
job['products'][179] = {'tile':55,'bands':[2],'blocks':[201,202,211,212],'map':{'y':17804,'x':10848},'shape':{'y':2024,'x':3616}}
job['products'][180] = {'tile':56,'bands':[2],'blocks':[203,204,213,214],'map':{'y':17804,'x':14464},'shape':{'y':2024,'x':3616}}
job['products'][181] = {'tile':57,'bands':[2],'blocks':[205,215],        'map':{'y':17804,'x':18080},'shape':{'y':2024,'x':3616}}
job['products'][182] = {'tile':58,'bands':[2],'blocks':[216,217,224],    'map':{'y':19828,'x':3616}, 'shape':{'y':1868,'x':3616}}
job['products'][183] = {'tile':59,'bands':[2],'blocks':[218,219,225,226],'map':{'y':19828,'x':7232}, 'shape':{'y':1868,'x':3616}}
job['products'][184] = {'tile':60,'bands':[2],'blocks':[220,221,227,228],'map':{'y':19828,'x':10848},'shape':{'y':1868,'x':3616}}
job['products'][185] = {'tile':61,'bands':[2],'blocks':[222,223,229],    'map':{'y':19828,'x':14464},'shape':{'y':1868,'x':3616}}

# 2km CONUS
job['products'][186] = {'scene':'CO','tile':0,'blocks':[0,1,6,7],    'map':{'y':0,   'x':0},   'shape':{'y':465, 'x':833},'tiles':9}
job['products'][187] = {'scene':'CO','tile':1,'blocks':[2,3,8,9],    'map':{'y':0,   'x':833}, 'shape':{'y':465, 'x':833},'tiles':9}
job['products'][188] = {'scene':'CO','tile':2,'blocks':[4,5,10,11],  'map':{'y':0,   'x':1666},'shape':{'y':465, 'x':834},'tiles':9}
job['products'][189] = {'scene':'CO','tile':3,'blocks':[12,13,18,19],'map':{'y':465, 'x':0},   'shape':{'y':506, 'x':833},'tiles':9}
job['products'][190] = {'scene':'CO','tile':4,'blocks':[14,15,20,21],'map':{'y':465, 'x':833}, 'shape':{'y':506, 'x':833},'tiles':9}
job['products'][191] = {'scene':'CO','tile':5,'blocks':[16,17,22,23],'map':{'y':465, 'x':1666},'shape':{'y':506, 'x':834},'tiles':9}
job['products'][192] = {'scene':'CO','tile':6,'blocks':[24,25,30,31],'map':{'y':971, 'x':0},   'shape':{'y':529, 'x':833},'tiles':9}
job['products'][193] = {'scene':'CO','tile':7,'blocks':[26,27,32,33],'map':{'y':971, 'x':833}, 'shape':{'y':529, 'x':833},'tiles':9}
job['products'][194] = {'scene':'CO','tile':8,'blocks':[28,29,34,35],'map':{'y':971, 'x':1666},'shape':{'y':529, 'x':834},'tiles':9}

# 1km CONUS
job['products'][195] = {'scene':'CO','tile':0,'blocks':[0,1,6,7],    'map':{'y':0,   'x':0},   'shape':{'y':930, 'x':1666}, 'bands':[1,3,5],'tiles':9}
job['products'][196] = {'scene':'CO','tile':1,'blocks':[2,3,8,9],    'map':{'y':0,   'x':1666},'shape':{'y':930, 'x':1666}, 'bands':[1,3,5],'tiles':9}
job['products'][197] = {'scene':'CO','tile':2,'blocks':[4,5,10,11],  'map':{'y':0,   'x':3332},'shape':{'y':930, 'x':1668}, 'bands':[1,3,5],'tiles':9}
job['products'][198] = {'scene':'CO','tile':3,'blocks':[12,13,18,19],'map':{'y':930, 'x':0},   'shape':{'y':1012,'x':1666}, 'bands':[1,3,5],'tiles':9}
job['products'][199] = {'scene':'CO','tile':4,'blocks':[14,15,20,21],'map':{'y':930, 'x':1666},'shape':{'y':1012,'x':1666}, 'bands':[1,3,5],'tiles':9}
job['products'][200] = {'scene':'CO','tile':5,'blocks':[16,17,22,23],'map':{'y':930, 'x':3332},'shape':{'y':1012,'x':1668}, 'bands':[1,3,5],'tiles':9}
job['products'][201] = {'scene':'CO','tile':6,'blocks':[24,25,30,31],'map':{'y':1942,'x':0},   'shape':{'y':1058,'x':1666}, 'bands':[1,3,5],'tiles':9}
job['products'][202] = {'scene':'CO','tile':7,'blocks':[26,27,32,33],'map':{'y':1942,'x':1666},'shape':{'y':1058,'x':1666}, 'bands':[1,3,5],'tiles':9}
job['products'][203] = {'scene':'CO','tile':8,'blocks':[28,29,34,35],'map':{'y':1942,'x':3332},'shape':{'y':1058,'x':1668}, 'bands':[1,3,5],'tiles':9}

# 0.5km CONUS
job['products'][204] = {'scene':'CO','tile':0,'blocks':[0,1,6,7],    'map':{'y':0,   'x':0},   'shape':{'y':1860,'x':3332}, 'bands':[2],'tiles':9}
job['products'][205] = {'scene':'CO','tile':1,'blocks':[2,3,8,9],    'map':{'y':0,   'x':3332},'shape':{'y':1860,'x':3332}, 'bands':[2],'tiles':9}
job['products'][206] = {'scene':'CO','tile':2,'blocks':[4,5,10,11],  'map':{'y':0,   'x':6664},'shape':{'y':1860,'x':3336}, 'bands':[2],'tiles':9}
job['products'][207] = {'scene':'CO','tile':3,'blocks':[12,13,18,19],'map':{'y':1860,'x':0},   'shape':{'y':2024,'x':3332}, 'bands':[2],'tiles':9}
job['products'][208] = {'scene':'CO','tile':4,'blocks':[14,15,20,21],'map':{'y':1860,'x':3332},'shape':{'y':2024,'x':3332}, 'bands':[2],'tiles':9}
job['products'][209] = {'scene':'CO','tile':5,'blocks':[16,17,22,23],'map':{'y':1860,'x':6664},'shape':{'y':2024,'x':3336}, 'bands':[2],'tiles':9}
job['products'][210] = {'scene':'CO','tile':6,'blocks':[24,25,30,31],'map':{'y':3884,'x':0},   'shape':{'y':2116,'x':3332}, 'bands':[2],'tiles':9}
job['products'][211] = {'scene':'CO','tile':7,'blocks':[26,27,32,33],'map':{'y':3884,'x':3332},'shape':{'y':2116,'x':3332}, 'bands':[2],'tiles':9}
job['products'][212] = {'scene':'CO','tile':8,'blocks':[28,29,34,35],'map':{'y':3884,'x':6664},'shape':{'y':2116,'x':3336}, 'bands':[2],'tiles':9}

# 2km Mesos
job['products'][213] = {'scene':'M1','tile':0,'blocks':[0,1,2,3],    'map':{'y':0,   'x':0},   'shape':{'y':500, 'x':500},'tiles':1}
job['products'][213]['notify'] = ['marea','ldm','mon']
job['products'][214] = {'scene':'M2','tile':0,'blocks':[0,1,2,3],    'map':{'y':0,   'x':0},   'shape':{'y':500, 'x':500},'tiles':1}
job['products'][214]['notify'] = ['marea','ldm','mon']
# 1km Mesos
job['products'][215] = {'scene':'M1','tile':0,'blocks':[0,1,2,3],    'map':{'y':0,   'x':0},   'shape':{'y':1000,'x':1000}, 'bands':[1,3,5],'tiles':1}
job['products'][215]['notify'] = ['marea','ldm','mon']
job['products'][216] = {'scene':'M2','tile':0,'blocks':[0,1,2,3],    'map':{'y':0,   'x':0},   'shape':{'y':1000,'x':1000}, 'bands':[1,3,5],'tiles':1}
job['products'][216]['notify'] = ['marea','ldm','mon']
# 0.5km Mesos
job['products'][217] = {'scene':'M1','tile':0,'blocks':[0,1,2,3],    'map':{'y':0,   'x':0},   'shape':{'y':2000,'x':2000}, 'bands':[2],'tiles':1}
job['products'][217]['notify'] = ['marea','ldm','mon']
job['products'][218] = {'scene':'M2','tile':0,'blocks':[0,1,2,3],    'map':{'y':0,   'x':0},   'shape':{'y':2000,'x':2000}, 'bands':[2],'tiles':1}
job['products'][218]['notify'] = ['marea','ldm','mon']


