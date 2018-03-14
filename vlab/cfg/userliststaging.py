# MIDaS users and feature authorization

userlist = """ */
		G.userList = [
			{ uid: 49321,   uname: "Samuel Shea",          site: "AFC" },
			{ uid: 29573,   uname: "Bruce Entwistle",      site: "AWC" },
			{ uid: 2116452, uname: "Shari Mutchler",       site: "AWC" },
			{ uid: 162099,  uname: "Amanda Terborg",       site: "AWC" },
			{ uid: 16122,   uname: "Frank Alsheimer",      site: "CAE" },
			{ uid: 2303796, uname: "Joseph Clark",         site: "DTX" },
			{ uid: 700872,  uname: "Steve Considine",      site: "DTX" },
			{ uid: 1396720, uname: "Steven Freitag",       site: "DTX" },
			{ uid: 2397129, uname: "Dave Kook",            site: "DTX" },
			{ uid: 30181,   uname: "Greg Mann",            site: "DTX" },
			{ uid: 1415996, uname: "Michael Richter",      site: "DTX" },
			{ uid: 1648897, uname: "Bryan Tilley",         site: "DTX" },
			{ uid: 48571,   uname: "David Radell",         site: "ERHQ" },
			{ uid: 632648,  uname: "Ted Ryan",             site: "FWD" },
			{ uid: 166322,  uname: "Greg Story",           site: "FWR" },
			{ uid: 28993,   uname: "Michael Stavish",      site: "MFR" },
			{ uid: 622453,  uname: "John Boris",           site: "MPX" },
			{ uid: 68967,   uname: "Kevin Farina",         site: "MPX" },
			{ uid: 2455985, uname: "Charles Bell",         site: "MTR" },
			{ uid: 29364,   uname: "Warren Blier",         site: "MTR" },
			{ uid: 2497826, uname: "Richard Canepa",       site: "MTR" },
			{ uid: 124886,  uname: "Roger Gass",           site: "MTR" },
			{ uid: 397286,  uname: "Matthew Mehle",        site: "MTR" },
			{ uid: 2148270, uname: "Drew Peterson",        site: "MTR" },
			{ uid: 2461160, uname: "Wilfred Pi",           site: "MTR" },
			{ uid: 703395,  uname: "Scott Rowe",           site: "MTR" },
			{ uid: 2105943, uname: "Anna Schneider",       site: "MTR" },
			{ uid: 329623,  uname: "Suzanne Sims",         site: "MTR" },
			{ uid: 93428,   uname: "Kathryn Miretzky",     site: "NES" },
			{ uid: 47926,   uname: "Matthew Seybold",      site: "NES" },
			{ uid: 2303613, uname: "John Beven",           site: "NHC" },
			{ uid: 344316,  uname: "Monica Bozeman",       site: "NHC" },
			{ uid: 160509,  uname: "Mark DeMaria",         site: "NHC" },
			{ uid: 2421135, uname: "Christopher Mello",    site: "NHC" },
			{ uid: 2599138, uname: "Nelsie Ramos",         site: "NHC" },
			{ uid: 2304688, uname: "TPC Hurr",             site: "NHC" },
			{ uid: 2312268, uname: "TPC MAR",              site: "NHC" },
			{ uid: 1691120, uname: "Matthew Kramar",       site: "PBZ" },
			{ uid: 2380288, uname: "SABSupervisor",        site: "SAB" },
			{ uid: 2301114, uname: "SDM",                  site: "SDM", canPlan: true },
			{ uid: 2305708, uname: "Chris Broyles",        site: "SPC" },
			{ uid: 1400475, uname: "William Bunting",      site: "SPC" },
			{ uid: 564338,  uname: "Ariel Cohen",          site: "SPC" },
			{ uid: 2303268, uname: "Mark Darrow",          site: "SPC" },
			{ uid: 729869,  uname: "Andy Dean",            site: "SPC" },
			{ uid: 2315562, uname: "Roger Edwards",        site: "SPC" },
			{ uid: 2308841, uname: "Aaron Gleason",        site: "SPC" },
			{ uid: 2309336, uname: "Stephen Goss",         site: "SPC" },
			{ uid: 2303067, uname: "Jeremy Grams",         site: "SPC" },
			{ uid: 52461,   uname: "Gregory Grosshans",    site: "SPC" },
			{ uid: 124495,  uname: "Jared Guyer",          site: "SPC" },
			{ uid: 2313068, uname: "John Hart",            site: "SPC" },
			{ uid: 2305744, uname: "Ryan Jewell",          site: "SPC" },
			{ uid: 29684,   uname: "Israel Jirak",         site: "SPC" },
			{ uid: 2302974, uname: "Brynn Kerr",           site: "SPC" },
			{ uid: 364201,  uname: "Patrick Marsh",        site: "SPC" },
			{ uid: 2112519, uname: "Richard Mosier",       site: "SPC" },
			{ uid: 2309306, uname: "Jeffrey Peters",       site: "SPC" },
			{ uid: 2303217, uname: "Joey Picca",           site: "SPC" },
			{ uid: 2108771, uname: "Ashton Robinson",      site: "SPC" },
			{ uid: 601397,  uname: "Richard Thompson",     site: "SPC" },
			{ uid: 474890,  uname: "Steven J. Weiss",      site: "SPC" },
			{ uid: 439820,  uname: "SR-SRH Roc",           site: "SRHQ" },
			{ uid: 2306705, uname: "Kurt Vanspeybroeck",   site: "SRHQ" },
			{ uid: 524331,  uname: "Lee Byerle",           site: "OBS4" },
			{ uid: 54882,   uname: "Eric Guillot",         site: "OBS1" },
			{ uid: 2290224, uname: "Jose Harris",          site: "OBS5" },
			{ uid: 99563,   uname: "Brian Rapp",           site: "OBS2", canPlan: true },
			{ uid: 39359,   uname: "Joe Zajic",            site: "OBS3" } ];
		/* """
