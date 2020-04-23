sender       = ('TOWR-S Updates', 'David.Bludis@noaa.gov')
contact_list = '/home/brapp/Downloads/contact_list.csv'
subject      = 'GOES-17 ABI Loop Heat Pipe Upcoming Event'

# Contact list column layout
name_col     = 1    # Addressee name column
email_col    = 0    # Addressee e-mail column
elig_col     = 7    # eligible flag column - is addressee eligible to receive
send_col     = 9    # send flag column - should addressee be sent e-mail 
data_row     = 2

elements = {}
elements[1] = {}
elements[1]['type']    = 'imagelink'
elements[1]['article'] = 'https://vlab.ncep.noaa.gov/group/goes-r-end-user-mission-readiness-project/email-announcements/?p_r_p_article_id=9580980#heading1'
elements[1]['image']   = 'https://vlab.ncep.noaa.gov/documents/67059/9687010/Title+Block.png/ca8b5dfa-e508-e091-5b93-fc90d289a3c3'
elements[1]['alt']     = 'GOES-17 Cooling System Impacts Update'
elements[1]['ihash']   = True
elements[1]['lhash']   = False
elements[1]['col']     = 1

elements[2] = {}
elements[2]['type']    = 'imagelink'
elements[2]['article'] = 'https://forms.gle/AmZGVG2UA51aaQkf7'
elements[2]['image']   = 'https://vlab.ncep.noaa.gov/documents/67059/9687021/Sign+Me+Up+Block.png/f6feb11e-a274-71d7-373c-cafbf9b22301'
elements[2]['alt']     = 'Sign up for TOWR-S email list'
elements[2]['ihash']   = False
elements[2]['lhash']   = False
elements[2]['col']     = 1

elements[3] = {}
elements[3]['type']    = 'imagelink'
elements[3]['article'] = 'https://vlab.ncep.noaa.gov/group/goes-r-end-user-mission-readiness-project/home'
elements[3]['image']   = 'https://vlab.ncep.noaa.gov/documents/67059/9687021/Footer+Block.png/acca8475-dd5b-71ed-c149-3c9675f6546f'
elements[3]['alt']     = 'TOWR-S VLab community page'
elements[3]['ihash']   = False
elements[3]['lhash']   = False
elements[3]['col']     = 1

elements[4] = {}
elements[4]['type']    = 'body'
elements[4]['file']    = '/home/brapp/devl/body.html'

elements[5] = {}
elements[5]['type']       = 'gtracker'
elements[5]['tracker_id'] = 'UA-48112603-7'
elements[5]['doc_path']   = '/path to link'
elements[5]['doc_title']  = 'Test Newsletter'
