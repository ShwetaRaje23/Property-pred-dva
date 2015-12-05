import os
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypp.settings")
from startpp.models import CityPropertyData
import xml.etree.ElementTree as ET
data_file_path = "/Users/Shweta/Documents/GatechSem3/DVA/Project/DVAProject/data/AtlantaPropertyListing_Sci_DatasetFINAL.csv"

handle = open(data_file_path, 'r')
contents = handle.read()
handle.close()
rows = contents.split('\n')
rows.pop(0)
#print 'rows', type(rows)
#print len(rows)
#print 'ghgkjdhHHld'
out = [  [i for i in r.split(',')] for r in rows if r ]
#print 'out len', len(out)
#print out[0]
#print len(out[0])
#print '###############'
for row in out:
    id = float(row[0])#long
    if(row[2] == ''):
        row[2] = 0
    num_bedrooms = float(row[2])#long
    location = row[1]#str
    if(row[3] == ''):
        row[3] = 897263
    price = float(row[3])#long
    #print row[71].strip()
    print '222'
    print row[4].strip()
    print '222'
    print '##'
    print row[5].strip()
    print '##'
    lat = float(row[4])#float
    lon = float(row[5])#float
    
    ca = CityPropertyData(id, num_bedrooms, location, price, lat, lon)
    #print icon
    ca.save()
    #print type(row)
