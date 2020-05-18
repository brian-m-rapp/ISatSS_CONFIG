contact_list  = {}
contact_list['file']        = '/home/brapp/Downloads/test_contact_list.csv'
contact_list['header_rows'] = 2
contact_list['name_col']    = 1    # Addressee name column
contact_list['email_col']   = 0    # Addressee e-mail column
contact_list['elig_col']    = 7    # eligible flag column - is addressee eligible to receive
contact_list['send_col']    = -1   # send flag column - should addressee be sent e-mail 

smtp_server = {}
smtp_server['host']       = 'smtp.gmail.com'
smtp_server['port']       = 587
smtp_server['auth_id']    = 1
smtp_server['sender']     = ('TOWR-S Updates', 'David.Bludis@noaa.gov')
smtp_server['batch_size'] = 1

subject       = 'Test #1 - Satellite Book Club Seminar Series Session 1 Follow-Up'

elements = []

htmlbody = {}
htmlbody['type']    = 'htmlbody'
htmlbody['file']    = '/home/brapp/git/ISatSS_CONFIG/ninja/docs/survey_body_2020-05-14.html'
elements.append(htmlbody)

textbody = {}
textbody['type']    = 'textbody'
textbody['file']    = '/home/brapp/git/ISatSS_CONFIG/ninja/docs/survey_body_2020-05-14.txt'
elements.append(textbody)

bottomimage = {}
bottomimage['type']      = 'imagelink'
bottomimage['article']   = 'https://vlab.ncep.noaa.gov/group/goes-r-end-user-mission-readiness-project/home'
bottomimage['image']     = 'https://vlab.ncep.noaa.gov/documents/67059/9687021/Footer+Block+Narrow.png/0453c7b5-3912-87ee-3469-0313b56d37ec?t=1587679572449'
bottomimage['alt']       = 'TOWR-S Team'
bottomimage['max-width'] = '100%'
bottomimage['imagehash'] = False
bottomimage['linkhash']  = False
bottomimage['col']       = 1
elements.append(bottomimage)
