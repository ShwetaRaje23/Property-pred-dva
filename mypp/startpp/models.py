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
        return self.homdescription
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







