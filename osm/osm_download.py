API = 'http://api.openstreetmap.org/api/0.6'
# API  = 'http://api06.dev.openstreetmap.org/api/0.6'

# AUTH = '--http-user=Pupkinz --http-password=jhOQfKvh'
AUTH = ''

# bounds minlat='53.2439672' minlon='50.186491' maxlat='53.2488207' maxlon='50.1942801'
BOX_6 = 'bbox=50.186491,53.2439672,50.1942801,53.2488207'

REL_SAMARA = '287507'
REL_NSK = '1263373'
REL_TOL = '1345135'

FILES=open('files','w')

import os,sys,time,re

def WGET(call,targ=''):
    if targ:
        T=targ+'.osm'
        print >>FILES,T
    else:
        T=call
    C='wget %s -O %s %s/%s'%(AUTH,T,API,call)
    print C
    return os.system(C)

# get api status & capabs
WGET('capabilities')
# get permissions
WGET('permissions')
# check api online
print re.findall(r'<status database="online" api="online" gpx="online"/>',open('capabilities').read())[0]

# download map 6 proseka
WGET('map?%s'%BOX_6,'Samara6')

for REL in [REL_SAMARA,REL_NSK,REL_TOL]: 
    # download Samara draft map
    WGET('relation/%s/full'%REL,REL)
    # download subareas
    for SUBREL in re.findall(r'<member type="relation" ref="(\d+)" role="subarea"/>',open('%s.osm'%REL).read()):
        WGET('relation/%s/full'%SUBREL,SUBREL)

FILES.close()

print '.'

