# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:20:59 2015

@author: Laura
"""
import csv
my_dict = {"test": 1, "testing": 2}

def createCSV():
    f = open('mycsvfile.csv','wb')
    w = csv.DictWriter(f,my_dict.keys())
    w.writeheader()
    w.writerow(my_dict.values())
    f.close()