# Points into GLM Grid configuration

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
job['name']     = 'ssmi_project'
job['cmd']      = 'mojo'
job['class']    = 'MOJO'
job['log']      = 'ssmi_project_log'
job['log_node'] = 1

job['data'] = {}
job['data']['output'] = {}
job['data']['output']['location']   = {'node':707}
job['data']['output']['aging']      = {'window':3600, 'mode':'creationtime'}
job['data']['output']['method']     = {'technique':'inplace'}
job['data']['output']['activeonly'] = True
job['data']['output']['schedule']   = {'interval':600}

job['data']['info']                = {}
job['data']['info']['location']    = {'node':708}
job['data']['info']['aging']       = {'window':3600, 'mode':'creationtime'}
job['data']['info']['method']      = {'technique':'inplace'}
job['data']['info']['activeonly']  = False
job['data']['info']['schedule']    = {'interval':600}
job['data']['info']['cfgorder']    = 1

job['data']['log']                 = {}
job['data']['log']['location']     = {'node':job['log_node']}
job['data']['log']['aging']        = {'window':2,'mode':'count'}
job['data']['log']['archive']      = {'window':7,'mode':'count'}
job['data']['log']['roots']        = [job['log']]
job['data']['log']['method']       = {'technique':'inplace'}
job['data']['log']['schedule']     = {'interval':3600}
job['data']['log']['activeonly']   = True

job['loglevel']             = 6

job['cntl_node']            = 705

job['input_type']           = {'type':'infofile','node':706,'delete_file':True, 'delete_info':True}

ncspec = {}
ncspec['destination'] = job['data']['output']
ncspec['namedef']     = []
ncspec['namedef'].append({'src':'filename.nc'})
#ncspec['namedef'].append({'src':'ncfs/02/globalmeta/satellite_id','translate':{'GOES-16':'G16'},'delimiter':'_proxyvis_'})
#ncspec['namedef'].append({'src':'tileno','fmt':'str','pad':{'len':2,'val':'0','just':'r'},'delimiter':'_'})
#ncspec['namedef'].append({'src':'stamp','delimiter':'.nc'})

ncspec['dimensions'] = {}

ncspec['globalmeta'] = {}

ncspec['variables']   = {}

ncspec['notifications'] = {'fields':{},'targets':{}}
ncspec['notifications']['targets']['orbits']  = {'node':job['data']['info']['location']['node'], 'enabled':True, 'prefix':'reproject_points', 'fields':['file','node']}

projdict = {}
projdict['southpolar'] = {'minlat':-100,'maxlat':-60,'projdef':{}}
projdict['southlamb']  = {'minlat':-60, 'maxlat':-30,'projdef':{}}

projdict['merc']       = {'minlat':-30, 'maxlat':30, 'projdef':{}}
projdict['merc']['ncspec'] = {}
projdict['merc']['ncspec']['globalmeta'] = {}
projdict['merc']['ncspec']['globalmeta']['grid_mapping_name'] = {'default': 'mercator'}
projdict['merc']['ncspec']['globalmeta']['standard_parallel'] = {}
projdict['merc']['ncspec']['globalmeta']['longitude_of_projection_origin'] = {}
projdict['merc']['ncspec']['globalmeta']['false_easting'] = {'default': 0}
projdict['merc']['ncspec']['globalmeta']['false_northing'] = {'default': 0}
projdict['merc']['ncspec']['globalmeta']['semi_major'] = {'default': 6371200}
projdict['merc']['ncspec']['globalmeta']['semi_minor'] = {'default': 6371200}

projdict['northlamb']  = {'minlat':30,  'maxlat':60, 'projdef':{}}
projdict['northpolar'] = {'minlat':60,  'maxlat':100,'projdef':{}}

job['modclass'] = {'module':'ssmi_project','class':'SSMI','args':{'ncspec':ncspec,'proj':projdict}}


