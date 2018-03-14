# isatss job definition for garbage collector


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
job['name']  = 'grb_notifier'
job['cmd']   = 'notifier'
job['class'] = 'Notifier'
job['log']   = 'grb_notifier_log'

job['data'] = {}
job['data']['log']                    = {}
job['data']['log']['location']        = {'node':1,'path':'log'}
job['data']['log']['aging']           = {'window':2,'mode':'count'}
job['data']['log']['archive']         = {'window':7,'mode':'count'}
job['data']['log']['roots']           = [job['log']]
job['data']['log']['method']          = {'technique':'inplace'}
job['data']['log']['schedule']        = {'interval':3600}
job['data']['log']['activeonly']      = True


job['input_type']  = {'type':'infofile','node':16,'delete_file':True, 'delete_info':True}
job['pause_empty'] = 60.0
job['qlimit']      = 10

"""
job['vlabs'] = {}
#job['vlabs']['dev'] = {}
#job['vlabs']['dev']['urlbase']     = 'https://vlab-dev.ncep.noaa.gov'
#job['vlabs']['dev']['sslnoverify'] = True
job['vlabs']['ops'] = {}
job['vlabs']['ops']['urlbase']     = 'https://vlab.ncep.noaa.gov'
job['vlabs']['ops']['sslnoverify'] = False

job['indices']     = {}
job['indices']['napo_isatss_notifications'] = {'stamped_item':{'defn':{'properties':{'stamp':{'type':'float'}}},'keys':['stamp']}}
job['indices']['napo_isatss_staging']       = {'stamped_item':{'defn':{'properties':{'stamp':{'type':'float'}}},'keys':['stamp']}}
#napo_isatss_staging
"""
