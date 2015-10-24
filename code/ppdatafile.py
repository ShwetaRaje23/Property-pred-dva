# -*- coding: utf-8 -*-
#Minal
"""
Created on Sun Oct 11 15:12:54 2015

@author: Laura
"""

#from pyzillow.pyzillow import ZillowWrapper
import xml.etree.ElementTree as ET
import urllib2

API_key = 'X1-ZWz1a2hjdxu77v_305s0'
zpid = '2105024542'
urlGZ = 'http://www.zillow.com/webservice/GetZestimate.htm?zws-id=' + API_key + '&zpid=' + zpid

documentGZ = urllib2.urlopen(urlGZ).read()
treeGZ = ET.fromstring(documentGZ)

price = treeGZ.find('response/zestimate/amount').text
thirtydaychange = treeGZ.find('response/zestimate/valueChange').text
print price, thirtydaychange

'''
homeDescGZ =

dGZ = {'zpid':zpid,
     'zestimate':{'amount':price,
                      'valueChange':thirtydaychange}
     }
'''



 