# -*- coding: utf-8 -*-

"""
Created on Sun Oct 11 15:12:54 2015

@author: Laura and Minal
"""

#from pyzillow.pyzillow import ZillowWrapper
import xml.etree.ElementTree as ET
import urllib2
import get_ids

def getData(idList, API_key,d):
    for zpid in idList:
        updatedPropData(API_key, zpid, d)
        getZestimate(API_key, zpid,d)
        chartData(API_key, zpid, d)
    path = '../data/DeepSearchResults.xml'
    zpid, year = get_ids.getYear(path)
    for i in range(len(zpid)):
        d[zpid[i]]['yearBuilt'] = year[i]
    return d
    

def updatedPropData(API_key, zpid, d):
    #zpid = '2105024542'
    urlGUPD = 'http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=' + API_key + '&zpid=' + str(zpid)
    
    
    documentGUPD = urllib2.urlopen (urlGUPD).read()
    treeGUPD = ET.fromstring(documentGUPD)
    
    try:
        curMth = treeGUPD.find('response/pageViewCount/currentMonth').text
    except:
        curMth = 0
    try:
        tot = treeGUPD.find('response/pageViewCount/total').text
    except:
        tot = 0
    try:
        street = treeGUPD.find('response/address/street').text
    except:
        street = ''
    try:        
        zipc = treeGUPD.find('response/address/zipcode').text
    except:
        zipc = 0
    try:
        city = treeGUPD.find('response/address/city').text
    except:
        city = ''
    try:
        state = treeGUPD.find('response/address/state').text
    except:
        state = ''
    try:
        lat = treeGUPD.find('response/address/latitude').text
    except:
        lat = ''
    try:        
        lon = treeGUPD.find('response/address/longitude').text
    except:
        lon = ''
    try:
        hD = treeGUPD.find('response/links/homeDetails').text
    except:
        hD = ''
    try:        
        pG = treeGUPD.find('response/links/photoGallery').text
    except:
        pG = ''
    try:        
        hI = treeGUPD.find('response/links/homeInfo').text
    except:
        hI = ''
    try:
        imgCt = treeGUPD.find('response/images/count').text
    except:
        imgCt = 0
    try:        
        imgUrl = treeGUPD.find('response/images/image/url').text
    except:
        imgUrl = ''
    try:    
        uC = treeGUPD.find('response/editedFacts/useCode').text
    except:
        uC = ''
    try:        
        bedrooms = treeGUPD.find('response/editedFacts/bedrooms').text
    except:
        bedrooms = 0
    try:        
        bath = treeGUPD.find('response/editedFacts/bathrooms').text
    except:
        bath = 0
    try:        
        finArea = treeGUPD.find('response/editedFacts/finishedSqFt').text
    except:
        finArea = 0
    try:
        heating = treeGUPD.find('response/editedFacts/heatingSystem').text
    except:
        heating = ''
    try:
        cooling = treeGUPD.find('response/editedFacts/coolingSystem').text
    except:
        cooling = ''
    try:    
        app = treeGUPD.find('response/editedFacts/appliances').text
    except:
        app = ''
    try:
        homeDesc = treeGUPD.find('response/homeDescription').text
    except:
        homeDesc = ''
    
    d[zpid] = { 
     'pageViewCount':{'currentMonth':curMth, 
                      'total':tot}, 
     'address':{'streeGUPDt':street, 
                'zipcode':zipc,
                'city':city,
                'state':state,
                'latitude':lat,
                'longitude':lon},
     'links':{'homeDetails':hD,
              'photoGallery':pG,
              'homeInfo':hI},
     'images':{'count':imgCt,
               'image':{'url':imgUrl}},
     'editedFacts':{'useCode':uC,
                    'bedrooms':bedrooms,
                    'bathrooms':bath,
                    'finishedSqFt':finArea,
                    'heatingSystem':heating,
                    'coolingSystem':cooling,
                    'appliances':app},
     'homeDescription':homeDesc,
     'chart':0,
     'zestimate':{'amount':0,
                  'valueChange':0},
     'yearBuilt':0}

def getZestimate(API_key, zpid,d):
    urlGZ = 'http://www.zillow.com/webservice/GetZestimate.htm?zws-id=' + API_key + '&zpid=' + str(zpid)

    documentGZ = urllib2.urlopen(urlGZ).read()
    treeGZ = ET.fromstring(documentGZ)
    
    try:
        price = treeGZ.find('response/zestimate/amount').text
    except:
        price = 0
    try:
        thirtydaychange = treeGZ.find('response/zestimate/valueChange').text
    except:
        thirtydaychange = 0
        
    d[zpid]['zestimate']['amount']=price
    d[zpid]['zestimate']['valueChange']=thirtydaychange

def chartData(API_key, zpid, d):
    urlGC = 'http://www.zillow.com/webservice/GetChart.htm?zws-id=' + API_key + '&unit-type=dollar&zpid=' + str(zpid) + '&width=300&height=150&chartDuration=5years'
    documentGC = urllib2.urlopen (urlGC).read()
    treeGC = ET.fromstring(documentGC)  
    try:
        chImg = treeGC.find('response/url').text
    except:
        chImg = ''
    d[zpid]['chart'] = chImg





 