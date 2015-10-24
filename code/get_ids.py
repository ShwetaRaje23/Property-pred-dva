import xml.etree.ElementTree as ET

def getIds(path):
    fp = open(path,"r")
    element = ET.parse(fp)
    #print type(element);
    #below statement finds all the elements with name 'zpid' in the xml path 'response/results/result/zpid' from file provided; note that the path starts from one level below the root 'SearchResults'.
    e = element.findall('response/results/result/zpid') 
    ids = []
    for i in e:
        ids.append(int(i.text));
    
    final_list = list(set(ids)) #final list containing the de-duplicated list of int ids
    #print type(final_list[0])
    #print len(ids) #length of ids list with duplicates
    #print len(final_list)  #length of ids after removing
    return final_list
    
def getYear(path, d):
    fp = open(path,"r")
    element = ET.parse(fp)
    for e in element.iter(tag="result"):
        zpid = element.find('zpid')
        year = element.find('yearBuilt')
        if year:
            d[zpid]["yearBuilt"] = year

    '''
    ids = []
    years = []
    for i in zpid:
        ids.append(int(i.text))
    for i in year:
        years.append(int(i.text))
    
    final_list_ids = list(set(ids)) #final list containing the de-duplicated list of int ids
    final_list_years = list(set(years))
    '''
    return d
    
