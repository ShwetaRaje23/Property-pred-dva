from django.contrib import admin
from models import *

# Register your models here.


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = [
    'zip_city_state',
    'zpid',
    'pageviewcount_currentmonth',
    'pageview_counttotal',
    'address_street',
    'address_zipcode',
    'address_latitude',
    'address_longitude',
    'links_homedetails',
    'links_photogallery',
    'links_homeinfo',
    'images_count',
    'images_image_url',
    'editedfacts_usecode',
    'editedfacts_bedrooms',
    'editedfacts_bathrooms',
    'editedfacts_finishedsqft',
    'editedfacts_heatingsystem',
    'editedfacts_coolingsystem',
    'editedfacts_appliances',
    'homedescription',
    'chart',
    'zestimate_amount',
    'zestimate_valuechange',
    'yearbuilt'
    ]


@admin.register(ZipCityState)
class ZipCityStateAdmin(admin.ModelAdmin):
    fields = [
    'address_zipcode',
    'address_city',
    'address_state'
    ]