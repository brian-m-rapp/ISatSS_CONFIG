# configuration file for loading vlab GOES-R Meso Mission Manager application
# imports
import isatss_init
from   im_exceptions import *
from   vlab_local_config import repo

imports = []
imports.append({'module':'time',          'as':'time',          'src':'baseline'})
imports.append({'module':'datetime',      'as':'datetime',      'src':'baseline'})
imports.append({'module':'userlistdev',   'as':'userlist',      'src':'isatss'})
ret = isatss_init.load_imports(__name__,imports)

vlab        = 'https://vlab-dev.ncep.noaa.gov'
sslnoverify = True
appfolderid = 2297109
approles   = [ 10142 ] # role ID for the 'User' entity
restoretime = time.strftime("%H:%MZ", time.gmtime(time.time() + datetime.timedelta(minutes=5).seconds))
maintmsg    = 'This application is currently offline for maintenance and should be available by '+restoretime+\
				'. If you need immediate support, please contact the SDM directly.'

content     = {}
content[1]  = {'file':'requests.html', 'articleid':1852160,'version':1.1}

replacements = {}
replacements['globals.js'] = {}
replacements['globals.js']['vlabUrl']        = vlab
replacements['globals.js']['DbIndex']        = 'napo_isatss_notifications'
replacements['globals.js']['companyId']      = 10132
replacements['globals.js']['groupId']        = 67059
replacements['globals.js']['forumReqCatId']  = 1716877
replacements['globals.js']['forumPlanCatId'] = 1716880
replacements['globals.js']['userList']       = userlist.userlist
replacements['globals.js']['thisIsOps']      = 'false'

replacements['requests.js'] = {}

