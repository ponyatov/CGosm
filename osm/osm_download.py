API_PROD = 'http://api.openstreetmap.org/api'
API_DEV  = 'http://api06.dev.openstreetmap.org/api'
API = API_DEV

import os,sys,time
C='wget -O %s.xml %s/%s'%('capabilities',API,'capabilities') ; print C,;print os.system(C)
print '.'

