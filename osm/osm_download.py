API_PROD = 'http://api.openstreetmap.org/api'
API_DEV  = 'http://api06.dev.openstreetmap.org/api'
API = API_DEV

import os,sys,time
os.system('wget -O %s.xml %s/%s'%('capabilities',API,'capabilities'))
print '.'

