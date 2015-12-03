import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypp.settings")
from startpp.models import CityCrimeData
from django.core import serializers

#filter is like a where clause in sql, the output is a QuerySet object
query_set = CityCrimeData.objects.filter(offense_id__in=[90360664,90370891])
print type(query_set)
print len(query_set)
print '$$$$$$$$$$'
print '$$$$$$$$$$'
for i in query_set:
    #print type(i)
    print (i.offense_id)
#print([query_set.offense_id for e in query_set])

data = serializers.serialize("json", query_set)
print 'data type', type(data)
print data