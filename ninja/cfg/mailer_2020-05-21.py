contact_list  = {}
contact_list['file']        = '/home/brapp/Downloads/test_contact_list.csv'
contact_list['header_rows'] = 2
contact_list['name_col']    = 1    # Addressee name column
contact_list['email_col']   = 0    # Addressee e-mail column
contact_list['elig_col']    = 7    # eligible flag column - is addressee eligible to receive
contact_list['send_col']    = -1   # send flag column - should addressee be sent e-mail 

smtp_server = {}
smtp_server['host']       = 'localhost'
smtp_server['port']       = 25
smtp_server['auth_id']    = None
smtp_server['sender']     = ('TOWR-S Updates', 'David.Bludis@noaa.gov')
smtp_server['batch_size'] = 1

subject       = 'Test #1 - Next Session of the Satellite Book Club Seminar Series is Thursday 5/21!'

elements = []

topimage = {}
topimage['type']      = 'imagelink'
topimage['article']   = 'https://vlab.ncep.noaa.gov/group/goes-r-end-user-mission-readiness-project/email-announcements/?p_r_p_article_id=10177234'
topimage['anchor']    = 'heading1'
topimage['image']     = 'https://vlab.ncep.noaa.gov/documents/67059/10099454/SBC_Session_2_Initial_Email_Header_Block.png/4f2ed5b9-c0e8-b935-9100-d72cd7310fde?t=1589820886466'
topimage['imageargs'] = {'campaign_id':'20200518'}
topimage['alt']       = 'SBC Seminar Series - May 21, 2020 @ 12:00 PM EDT'
topimage['max-width'] = '100%'
topimage['width']     = 800
topimage['imagehash'] = True
topimage['linkhash']  = True
topimage['col']       = 1
elements.append(topimage)

htmlbody = {}
htmlbody['type']    = 'htmlbody'
htmlbody['file']    = '/home/brapp/git/ISatSS_CONFIG/ninja/docs/mailer_body_2020-05-18.html'
elements.append(htmlbody)

textbody = {}
textbody['type']    = 'textbody'
textbody['file']    = '/home/brapp/git/ISatSS_CONFIG/ninja/docs/mailer_body_2020-05-18.txt'
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

