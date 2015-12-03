import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypp.settings")
from startpp.models import InitialWeights
import xml.etree.ElementTree as ET

price = 4.621621622
area = 4.081081081
bedrooms = 3.837837838
crime = 4.567567568
#InitialWeights.objects.all().delete()
ca = InitialWeights(1, price, area, bedrooms, crime)
ca.save()