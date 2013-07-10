# -*- coding: utf8 -*-

MPNAME = 'my.mp'

import os,sys,time,re

OSM=open('Samara6.osm').read()

MP=open(MPNAME,'w')

yy,mm,dd,hh=time.localtime()[:4]
NOW='%.2i%.2i%.2i%.2i'%(yy%100,mm,dd,hh)

VER=re.findall(r'osm version="(.+?)"',OSM)[0]
CCC=re.findall(r'copyright="(.+?)"',OSM)[0]+' [http://osm.org]'

print >>MP,'''
[IMG ID]
ID=%s
Name=%s
Copyright=%s
Version=%s

Datum=W84
Elevation=m

LblCoding=9
CodePage=65001

Levels=1
Level0=24
;Level1=22
;Level2=20
;Level3=18
;Level4=16
;Level5=15

Preprocess=F
POIIndex=Y
[END]
'''%(NOW,NOW,CCC,VER)

for i in re.findall(r'<node id="(.+?)" lat="(.+?)" lon="(.+?)"',OSM):
    print >>MP,'''
; NodeID = %s
[POI]
Data0=(%s,%s)
Label=%s
[END]
    '''%(i[0],i[1],i[2],i[0])

MP.close()

print open(MPNAME).read()
