
sender       = ('TOWR-S Updates', 'David.Bludis@noaa.gov')
contact_list = '/home/brapp/Downloads/dossier_contact_list.csv'
subject      = 'TOWR-S Meeting Friday, April 24 @ 1PM EDT'

# Contact list column layout
name_col     = 1    # Addressee name column
email_col    = 0    # Addressee e-mail column
elig_col     = 8    # eligible flag column - is addressee eligible to receive
send_col     = -1    # send flag column - should addressee be sent e-mail 
data_row     = 3

elements = {}

elements[1] = {}
elements[1]['type']    = 'body'
elements[1]['file']    = '/home/brapp/git/ISatSS_CONFIG/ninja/docs/mailer_body.html'

elements[2] = {}
elements[2]['type']    = 'imagelink'
elements[2]['article'] = 'https://vlab.ncep.noaa.gov/group/goes-r-end-user-mission-readiness-project/home'
#elements[2]['image']   = 'https://vlab.ncep.noaa.gov/documents/67059/9687021/Footer+Block.png/acca8475-dd5b-71ed-c149-3c9675f6546f'
elements[2]['image']   = 'https://vlab.ncep.noaa.gov/documents/67059/9687021/Footer+Block+Narrow.png/0453c7b5-3912-87ee-3469-0313b56d37ec'
elements[2]['alt']     = 'TOWR-S VLab community page'
elements[2]['ihash']   = True
elements[2]['lhash']   = False
elements[2]['col']     = 1
