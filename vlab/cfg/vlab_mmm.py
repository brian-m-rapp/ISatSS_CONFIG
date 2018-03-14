# configuration file for loading vlab GOES-R Meso Mission Manager application
import isatss_init
from   im_exceptions import *
from   vlab_local_config import repo

# imports
imports = []
imports.append({'module':'time',          'as':'time',          'src':'baseline'})
imports.append({'module':'datetime',      'as':'datetime',      'src':'baseline'})
imports.append({'module':'userlist',      'as':'userlist',      'src':'isatss'})
ret = isatss_init.load_imports(__name__,imports)

vlab        = 'https://vlab.ncep.noaa.gov'
sslnoverify = False
appfolderid = 2290400
approles   = [ 10142 ] # role ID for the 'User' entity
restoretime = time.strftime("%H:%MZ", time.gmtime(time.time() + datetime.timedelta(minutes=25).seconds))
maintmsg    = 'This application is currently offline for maintenance and should be available by '+restoretime+\
				'. If you need immediate support, please contact the SDM directly.'

content     = {}
content[1]  = {'file':'index.html', 'articleid':2273646,'version':3.9}

replacements = {}
replacements['globals.js'] = {}
replacements['globals.js']['vlabUrl']        = vlab
replacements['globals.js']['DbIndex']        = 'napo_isatss_notifications'
replacements['globals.js']['companyId']      = 10132
replacements['globals.js']['groupId']        = 67059
replacements['globals.js']['forumReqCatId']  = 2302303                #1716877
replacements['globals.js']['forumPlanCatId'] = 2302316                #1716880
replacements['globals.js']['userList']       = userlist.userlist
replacements['globals.js']['thisIsOps']      = 'true'

replacements['midas.js'] = {}
replacements['midas.js']['showRequestPageButton'] = 'true'
replacements['midas.js']['requestsPage']          = '/group/goes-r-end-user-mission-readiness-project/requests'
