import xml.etree.ElementTree as ET
fp = open("SearchForAZillow.xml","r")
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
