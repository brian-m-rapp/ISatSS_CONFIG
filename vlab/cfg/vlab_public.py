# configuration file for loading vlab GOES-R Meso Mission Manager application
import isatss_init
from   im_exceptions import *
from   vlab_local_config import repo

# imports
imports = []
imports.append({'module':'time',          'as':'time',          'src':'baseline'})
imports.append({'module':'datetime',      'as':'datetime',      'src':'baseline'})
ret = isatss_init.load_imports(__name__,imports)

vlab        = 'https://vlab.ncep.noaa.gov'
sslnoverify = False
appfolderid = 3081455
approles   = [ 10142, 10139 ] # role ID for the 'User' and 'Guest' entities
restoretime = time.strftime("%H:%MZ", time.gmtime(time.time() + datetime.timedelta(minutes=25).seconds))
maintmsg    = 'This application is currently offline for maintenance and should be available by '+restoretime+\
				'. If you need immediate support, please contact the SDM directly.'
content     = {}
content[1]  = {'file':'public.html', 'articleid':3081473,'version':1.0}

replacements = {}
replacements['globals.js'] = {}
replacements['globals.js']['vlabUrl']        = vlab
replacements['globals.js']['DbIndex']        = ''
replacements['globals.js']['companyId']      = 10132
replacements['globals.js']['groupId']        = 67059
replacements['globals.js']['forumReqCatId']  = 0
replacements['globals.js']['forumPlanCatId'] = 0
replacements['globals.js']['userList']       = 'The public view does not have a user list'
replacements['globals.js']['thisIsOps']      = 'true'

replacements['midas_public.js'] = {}
replacements['midas_public.js']['dataFileUrl']    = '/web/goes-r-end-user-mission-readiness-project/mds_data_window'
