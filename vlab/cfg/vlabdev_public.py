# configuration file for loading vlab GOES-R Meso Mission Manager application

from   vlab_local_config import repo

vlab        = 'https://vlab-dev.ncep.noaa.gov'
sslnoverify = True
appfolderid = 2599914
approles   = [ 10142, 10139 ] # role ID for the 'User' entity

content     = {}
content[1]  = {'file': 'public.html', 'articleid': 2599920,'version': 1.0}

replacements = {}
replacements['globals.js'] = {}
replacements['globals.js']['companyId']      = 10132
replacements['globals.js']['groupId']        = 67059
replacements['globals.js']['userList']       = 'The public view does not have a user list'
replacements['globals.js']['DbIndex']        = ''
replacements['globals.js']['forumReqCatId']  = 0
replacements['globals.js']['forumPlanCatId'] = 0
replacements['globals.js']['vlabUrl']        = 'https://vlab-dev.ncep.noaa.gov'
replacements['globals.js']['thisIsOps']      = 'false'

replacements['midas_public.js'] = {}
replacements['midas_public.js']['dataFileUrl']    = '/web/goes-r-end-user-mission-readiness-project/mds_data_window'

