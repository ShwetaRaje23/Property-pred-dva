# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:12:54 2015

@author: Laura
"""

#from pyzillow.pyzillow import ZillowWrapper
import xml.etree.ElementTree as ET
import urllib2


API_key = 'X1-ZWz1a2hjdxu77v_305s0'
zpid = '2105024542'
url = 'http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=' + API_key + '&zpid=' + zpid

document = urllib2.urlopen (url).read()
tree = ET.fromstring(document)

curMth = tree.find('response/pageViewCount/currentMonth').text
tot = tree.find('response/pageViewCount/total').text

street = tree.find('response/address/street').text
zipc = tree.find('response/address/zipcode').text
city = tree.find('response/address/city').text
state = tree.find('response/address/state').text
lat = tree.find('response/address/latitude').text
lon = tree.find('response/address/longitude').text

hD = tree.find('response/links/homeDetails').text
pG = tree.find('response/links/photoGallery').text
hI = tree.find('response/links/homeInfo').text

imgCt = tree.find('response/images/count').text
imgUrl = tree.find('response/images/image/url').text

uC = tree.find('response/editedFacts/useCode').text
bedrooms = tree.find('response/editedFacts/bedrooms').text
bath = tree.find('response/editedFacts/bathrooms').text
finArea = tree.find('response/editedFacts/finishedSqFt').text
heating = tree.find('response/editedFacts/heatingSystem').text
cooling = tree.find('response/editedFacts/coolingSystem').text
app = tree.find('response/editedFacts/appliances').text

homeDesc = 
'''
d = {'zpid':zpid, 
     'pageViewCount':{'currentMonth':curMth, 
                      'total':tot}, 
     'address':{'street':street, 
                'zipcode':zipc,
                'city':city,
                'state':state,
                'latitude':lat,
                'longitude':lon},
     'links':{'homeDetails':hD,
              'photoGallery':pG,
              'homeInfo':hI},
     'images':{'count':imgCt,
               'image':{'url':}}}
'''
'''
tree = ET.fromstring(document)
file_handle = open("../data/UpdatedPropertyDetails.xml","wb")
xml = "UpdatedPropertyDetails:updatedPropertyDetails"
print document

print type(document)
#xml = document.strip()
value = ET.fromstring(document).find('response/editedFacts/bedrooms')
if len(value):
    print 'Found value:', value.text

tree = ET.parse(url)
node = tree.find('request')

node.writexml(file_handle)
file_handle.write(xml)
xml.writexml(file_handle)
root = tree.getroot()
print node

tree.write(file_handle)
file_handle.close()
''' 


 