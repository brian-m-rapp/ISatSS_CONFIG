# configuration file for loading vlab GOES-R Meso Mission Manager application

from   vlab_local_config import repo

vlab        = 'https://vlab.ncep.noaa.gov'
sslnoverify = False
appfolderid = 2323723

content     = {}
content[1]  = {'file':'index.html', 'articleid':2323655,'version':1.0}

replacements = {}
replacements['goes-meso-request.js'] = {}
replacements['goes-meso-request.js']['companyId']      = 10132
replacements['goes-meso-request.js']['groupId']        = 67059
replacements['goes-meso-request.js']['forumReqCatId']  = 141138 #2302303		#1716877
replacements['goes-meso-request.js']['forumPlanCatId'] = 141138 #2302316		#1716880

ulst = """ [{ uid: "49321",   uname: "Samuel Shea",          site: "AFC"  },
            { uid: "16122",   uname: "Frank Alsheimer",      site: "CAE"  },
            { uid: "29364",   uname: "Warren Blier",         site: "MTR"  },
            { uid: "1691120", uname: "Matthew Kramar",       site: "PBZ"  },
            { uid: "344316",  uname: "Monica Bozeman",       site: "NHC"  },
            { uid: "160509",  uname: "Mark DeMaria",         site: "NHC"  },
            { uid: "2303613", uname: "John Beven",           site: "NHC"  },
            { uid: "2304688", uname: "TPC Hurr",             site: "NHC"  },
            { uid: "29573",   uname: "Bruce Entwistle",      site: "AWC"  },
            { uid: "68967",   uname: "Kevin Farina",         site: "MPX"  },
            { uid: "622453",  uname: "John Boris",           site: "MPX"  },
            { uid: "52461",   uname: "Gregory Grosshans",    site: "SPC"  },
            { uid: "54882",   uname: "Eric Guillot",         site: "OBS1" },
            { uid: "29684",   uname: "Israel Jirak",         site: "SPC"  },
            { uid: "1691120", uname: "Matthew Kramar",       site: "PBZ"  },
            { uid: "30181",   uname: "Greg Mann",            site: "DTX"  },
            { uid: "1648897", uname: "Bryan Tilley",         site: "DTX"  },
            { uid: "93428",   uname: "Kathryn Miretzky",     site: "NES"  },
            { uid: "2116452", uname: "Shari Mutchler",       site: "AWC"  },
            { uid: "48571",   uname: "David Radell",         site: "ERHQ" },
            { uid: "2306705", uname: "Kurt Vanspeybroeck",   site: "SRHQ" },
            { uid: "439820",  uname: "SR-SRH Roc",           site: "SRHQ" },
            { uid: "99563",   uname: "Brian Rapp",           site: "OBS2" },
            { uid: "632648",  uname: "Ted Ryan",             site: "FWD"  },
            { uid: "47926",   uname: "Matthew Seybold",      site: "NES"  },
            { uid: "28993",   uname: "Michael Stavish",      site: "MFR"  },
            { uid: "166322",  uname: "Greg Story",           site: "FWR"  },
            { uid: "2301114", uname: "SDM",                  site: "SDM"  },
            { uid: "162099",  uname: "Amanda Terborg",       site: "AWC"  },
            { uid: "2302974", uname: "Brynn Kerr",           site: "SPC"  },
            { uid: "2303067", uname: "Jeremy Grams",         site: "SPC"  },
            { uid: "1400475", uname: "William Bunting",      site: "SPC"  },
            { uid: "2303268", uname: "Mark Darrow",          site: "SPC"  },
            { uid: "564338",  uname: "Ariel Cohen",          site: "SPC"  },
            { uid: "2303217", uname: "Joey Picca",           site: "SPC"  },
            { uid: "601397",  uname: "Richard Thompson",     site: "SPC"  },
            { uid: "729869",  uname: "Andy Dean",            site: "SPC"  },
            { uid: "124495",  uname: "Jared Guyer",          site: "SPC"  },
            { uid: "2305708", uname: "Chris Broyles",        site: "SPC"  },
            { uid: "2108771", uname: "Ashton Robinson",      site: "SPC"  },
            { uid: "2305744", uname: "Ryan Jewell",          site: "SPC"  },
            { uid: "364201",  uname: "Patrick Marsh",        site: "SPC"  },
            { uid: "2308841", uname: "Aaron Gleason",        site: "SPC"  },
            { uid: "2309306", uname: "Jeffrey Peters",       site: "SPC"  },
            { uid: "2309336", uname: "Stephen Goss",         site: "SPC"  },
            { uid: "2313068", uname: "John Hart",            site: "SPC"  },
            { uid: "2112519", uname: "Richard Mosier",       site: "SPC"  },
            { uid: "2315562", uname: "Roger Edwards",        site: "SPC"  },
            { uid: "39359",   uname: "Joe Zajic",            site: "OBS3" },
            { uid: "51327",   uname: "Mike Johnson",         site: "OBS4" }]"""

replacements['goes-meso-request.js']['userList'] = ulst

