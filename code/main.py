# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:26:55 2015

@author: Animesh, Laura, Minal, Shweta and Vasavi
"""

import get_ids
import get_data

d = {}     
url = "../data/SearchForAtlantaZillow.xml"
API_key = 'X1-ZWz1a2hjdxu77v_305s0'
    

id_list = get_ids.getIds(url)
d = get_data.getData(id_list, API_key,d)
print d