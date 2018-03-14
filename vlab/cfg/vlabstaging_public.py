# configuration file for loading vlab GOES-R Meso Mission Manager application
import isatss_init
from   im_exceptions import *

# imports
imports = []
imports.append({'module':'time',            'as':'time',          'src':'baseline'})
imports.append({'module':'datetime',        'as':'datetime',      'src':'baseline'})
ret = isatss_init.load_imports(__name__,imports)

vlab        = 'https://vlab.ncep.noaa.gov'
sslnoverify = False
appfolderid = 2323723
approles   = [ 10142 ] # role ID for the 'User' entity
restoretime = time.strftime("%H:%MZ", time.gmtime(time.time() + datetime.timedelta(minutes=20).seconds))
maintmsg    = 'This application is currently offline for maintenance and should be available by '+restoretime+\
				'. If you need immediate support, please contact the SDM directly.'

repo        = '/raftr/ops_gomes/GOMES/MIDaS'

content     = {}
content[1]  = {'file': 'index.html', 'articleid': 2323655,'version': 1.0}

replacements = {}
replacements['globals.js'] = {}
replacements['globals.js']['vlabUrl']        = 'https://vlab.ncep.noaa.gov'
replacements['globals.js']['DbIndex']        = ''
replacements['globals.js']['companyId']      = 10132
replacements['globals.js']['groupId']        = 67059
replacements['globals.js']['forumReqCatId']  = 0					# Not used for public view
replacements['globals.js']['forumPlanCatId'] = 0					# Not used for public view

replacements['globals.js']['userList']       = 'The public view does not have a user list'
replacements['globals.js']['thisIsOps']      = 'false'

replacements['midas_public.js'] = {}
replacements['midas_public.js']['dataFileUrl']    = '/documents/midas_query_results.json'

