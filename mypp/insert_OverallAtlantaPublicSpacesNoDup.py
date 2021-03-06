import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypp.settings")
from startpp.models import CityPublicSpaces
import xml.etree.ElementTree as ET
fp = open("V:\DVA\DVA Project\DVAProject\data\AtlantaPlacesData\AllIntegratedFiles\OverallAtlantaPublicSpacesNoDup.xml","r")
element = ET.parse(fp)

x = element.findall(".")
y = x[0].findall(".//result")
for i in y:
    
    name = i.find('name').text
    vicinity = i.find('vicinity').text
    location_lat = i.find("geometry/location/lat").text
    location_lng = i.find("geometry/location/lng").text
    icon = i.find('icon').text
    id = i.find('id').text
    place_id = i.find('place_id').text
    #price_level = i.find('price_level').text
    ca = CityPublicSpaces(name,vicinity,location_lat,location_lng,icon,id,place_id)
    #print icon
    ca.save()
    print '--------------------------------'