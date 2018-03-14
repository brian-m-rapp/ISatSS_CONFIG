# configuration file for loading vlab GOES-R Meso Mission Manager application

import isatss_init
from   im_exceptions import *
from   vlab_local_config import repo

# imports
imports = []
imports.append({'module':'time',          'as':'time',          'src':'baseline'})
imports.append({'module':'datetime',      'as':'datetime',      'src':'baseline'})
imports.append({'module':'userlistdev',   'as':'userlist',      'src':'isatss'})
ret = isatss_init.load_imports(__name__,imports)

vlab        = 'https://vlab-dev.ncep.noaa.gov'
sslnoverify = True
appfolderid = 2704913
approles    = []
repo        = '/raftr/GOMES/Blackout'
#repo        = '/raftr/ops_gomes/GOMES/vlab-dev'

restoretime = time.strftime("%H:%MZ", time.gmtime(time.time() + datetime.timedelta(minutes=5).seconds))
maintmsg    = 'This application is currently offline for maintenance and should be available by '+restoretime+\
                '. If you need immediate support, please contact the SDM directly.'

content     = {}
content[1]  = {'file':'index.html', 'articleid':2704922,'version':1.0}

replacements = {}
replacements['globals.js'] = {}
replacements['globals.js']['companyId']      = 10132
replacements['globals.js']['groupId']        = 67059
replacements['globals.js']['forumReqCatId']  = 0
replacements['globals.js']['forumPlanCatId'] = 0
replacements['globals.js']['vlabUrl']        = vlab

replacements['blackout.js'] = {}

