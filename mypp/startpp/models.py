import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../mypp.settings")
from django.db import models

# Create your models here.

from django.db import models

class ZipCityState(models.Model):
    #...
    def __str__(self):
        return self.address_zipcode
    address_zipcode =  models.CharField(max_length=5)
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=20)

class Property(models.Model):
    #...
    def __str__(self):
        return self.homedescription
    zip_city_state = models.ForeignKey(ZipCityState)
    zpid = models.CharField(max_length=10)
    pageviewcount_currentmonth = models.BigIntegerField(default=0)
    pageview_counttotal = models.BigIntegerField(default=0)
    address_street = models.CharField(max_length=100)
    address_zipcode = models.CharField(max_length=5)
    address_latitude = models.DecimalField(max_digits=10,decimal_places=5)
    address_longitude = models.DecimalField(max_digits=10,decimal_places=5)
    links_homedetails = models.CharField(max_length=100)
    links_photogallery = models.CharField(max_length=100)
    links_homeinfo = models.CharField(max_length=100)
    images_count = models.BigIntegerField(default=0)
    images_image_url = models.CharField(max_length=100)
    editedfacts_usecode = models.CharField(max_length=100)
    editedfacts_bedrooms = models.IntegerField(default=0)
    editedfacts_bathrooms = models.IntegerField(default=0)
    editedfacts_finishedsqft = models.DecimalField(max_digits=15,decimal_places=5)
    editedfacts_heatingsystem = models.CharField(max_length=100)
    editedfacts_coolingsystem = models.CharField(max_length=100)
    editedfacts_appliances = models.CharField(max_length=100)
    homedescription = models.CharField(max_length=100)
    chart = models.CharField(max_length=100)
    zestimate_amount = models.DecimalField(max_digits=15,decimal_places=5)
    zestimate_valuechange = models.DecimalField(max_digits=15,decimal_places=5)
    yearbuilt = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Properties'


class CityAmenities(models.Model):
    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id
    
class CitySchools(models.Model):
    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id

class CityEntertainment(models.Model):
    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id

class CityFood(models.Model):
    

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    #price_level = models.DecimalField(max_digits=5,decimal_places=4)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id

class CityFoodPlaces(models.Model):
    

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    #price_level = models.DecimalField(max_digits=5,decimal_places=4)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id

class CityHealth(models.Model):

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id
class CityPlacesOfWorship(models.Model):
    

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140, null=True)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id
        
class CityPublicSpaces(models.Model):
    

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140, null=True)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)

    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id

class CityServicesData(models.Model):
    

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id
        
class CityShopsData(models.Model):
    

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id
        
class CityTransportationData(models.Model):
    

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140, null=True)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id
        
class CityMiscServicesData(models.Model):
    

    name = models.CharField(max_length=140)
    vicinity = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    #rating = models.DecimalField(max_digits=5,decimal_places=4)
    icon = models.CharField(max_length=300)
    id = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256,primary_key=True)
    
    def __str__(self):
        return 'name: ',self.name, 'vicinity:', self.vicinity,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'icon:', self.icon, 'id:', self.id, 'place_id:', self.place_id
        
class CityCrimeData(models.Model):
    

    offense_id = models.BigIntegerField(primary_key=True)
    location = models.CharField(max_length=140)
    crime_type = models.CharField(max_length=140)
    neighborhood = models.CharField(max_length=140)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9)
    
    def __str__(self):
        return 'offense_id: ',self.offense_id, 'location:', self.location,'location_lat:', self.location_lat, 'location_lng:', self.location_lng, 'crime_type:', self.crime_type, 'neighborhood:', self.neighborhood

    
class CityPropertyData_temp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    num_bedrooms = models.BigIntegerField()
    location = models.CharField(max_length=140)
    price_input = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    
class CityPropertyData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    num_bedrooms = models.BigIntegerField()
    location = models.CharField(max_length=140)
    price_input = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    location_lat = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    location_lng = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    
class InitialWeights(models.Model):
    id = models.BigIntegerField(primary_key=True)
    price = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    area = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    bedrooms = models.DecimalField(max_digits=100,decimal_places=9, null=True)
    crime = models.DecimalField(max_digits=100,decimal_places=9, null=True)





