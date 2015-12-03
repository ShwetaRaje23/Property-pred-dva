import os
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypp.settings")
from startpp.models import CityCrimeData
import xml.etree.ElementTree as ET
data_file_path = "V:\DVA\DVA Project\DVAProject\data\Atlanta_crimedata.csv"

handle = open(data_file_path, 'r')
contents = handle.read()
handle.close()
rows = contents.split('\r')
rows.pop(0)
print 'rows', type(rows)
print len(rows)
print 'ghgkjdhHHld'
out = [  [i for i in r.split(',')] for r in rows if r ]
print 'out len', len(out)
print out[0]
print len(out[0])
print '###############'
for row in out:
    offense_id = float(row[1])#long
    #offense_id = long(row[1])#long
    location = row[10]#str
    crime_type = row[18]#str
    neighborhood = row[19]#str
    location_lat = float(row[21])#float
    location_lng = float(row[22])#float
    
    ca = CityCrimeData(offense_id,location,crime_type,neighborhood,location_lat,location_lng)
    #print icon
    ca.save()
    #print type(row)
