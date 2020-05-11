
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
smtp_server['batch_size'] = 100

subject       = 'Test #5 - Access to GOES-R Mesoscale Domain Sector Request Tool Restored'

elements = []

htmlbody = {}
htmlbody['type']    = 'htmlbody'
htmlbody['file']    = '/home/brapp/git/ISatSS_CONFIG/ninja/docs/mailer_body_2020-05-08.html'
elements.append(htmlbody)

textbody = {}
textbody['type']    = 'textbody'
textbody['file']    = '/home/brapp/git/ISatSS_CONFIG/ninja/docs/mailer_body_2020-05-08.txt'
elements.append(textbody)

imagelink = {}
imagelink['type']    = 'imagelink'
imagelink['article'] = 'https://vlab.ncep.noaa.gov/group/goes-r-end-user-mission-readiness-project/home'
#imagelink['image']   = 'https://vlab.ncep.noaa.gov/documents/67059/9687021/Footer+Block.png/acca8475-dd5b-71ed-c149-3c9675f6546f'
imagelink['image']   = 'https://vlab.ncep.noaa.gov/documents/67059/9687021/Footer+Block+Narrow.png/0453c7b5-3912-87ee-3469-0313b56d37ec'
imagelink['alt']     = 'TOWR-S VLab community page'
imagelink['ihash']   = True
imagelink['lhash']   = False
imagelink['col']     = 1
elements.append(imagelink)
