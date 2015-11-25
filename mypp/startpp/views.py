from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import Context
from django.http import HttpResponse
from django.db import models
from startpp.models import Property
import json
from django.core import serializers


# Create your views here.


def hello_view(request):
    return render_to_response('helloworld.html', Context({'username':request.GET.get('name')}   ))

def action_controller(request):
    return HttpResponse(content=request.GET.get('name'))

def inputdata_view(request):
    return render_to_response('inputdata.html', Context({'username':request.GET.get('name')}   ))

def getdata_view(request):
    my_dict = {}
    my_dict['Size of house Value'] = request.GET.get('size_of_house_value')
    my_dict['Proximity To Public Transport Value'] = request.GET.get('proximity_to_public_transport_value')
    my_dict['Price of the house Value'] = request.GET.get('price_of_the_house_value')
    my_dict['Number of bedrooms Value'] = request.GET.get('number_of_bedrooms_value')
    my_dict['School in the neighborhood Value'] = request.GET.get('school_in_the_neighborhood_value')
    my_dict['Hospital in the neighborhood Value'] = request.GET.get('hospital_in_the_neighborhood_value')
    my_dict['Pet friendly Value'] = request.GET.get('pet_friendly_value')
    my_dict['Yard available Value'] = request.GET.get('yard_available_value')
    my_dict['Bars around Value'] = request.GET.get('bars_around_value')
    my_dict['Crime rate in the locality Value'] = request.GET.get('crime_rate_in_the_locality_value')
    my_dict['Places of worship around Value'] = request.GET.get('places_of_worship_nearby_value')
    my_dict['Closeness to workplace Value'] = request.GET.get('closeness_to_workplace_value')
    my_dict['Closeness to super market Value'] = request.GET.get('closeness_to_super_market_value')
    my_dict['Age of the house Value'] = request.GET.get('age_of_the_house_value')
    my_dict['Size of house Priority'] = request.GET.get('size_of_house')
    my_dict['Proximity To Public Transport Priority'] = request.GET.get('proximity_to_public_transport')
    my_dict['Price of the house Priority'] = request.GET.get('proximity_to_public_transport')
    my_dict['Number of bedrooms Priority'] = request.GET.get('number_of_bedrooms')
    my_dict['School in the neighborhood Priority'] = request.GET.get('school_in_the_neighborhood')
    my_dict['Hospital in the neighborhood Priority'] = request.GET.get('hospital_in_the_neighborhood')
    my_dict['Pet friendly Priority'] = request.GET.get('pet_friendly')
    my_dict['Yard available Priority'] = request.GET.get('yard_available')
    my_dict['Bars around Priority'] = request.GET.get('bars_around')
    my_dict['Crime rate in the locality Priority'] = request.GET.get('crime_rate_in_the_locality')
    my_dict['Places of worship around Priority'] = request.GET.get('places_of_worship_nearby')
    my_dict['Closeness to workplace Priority'] = request.GET.get('closeness_to_workplace')
    my_dict['Closeness to super market Priority'] = request.GET.get('closeness_to_super_market')
    my_dict['Age of the house Priority'] = request.GET.get('age_of_the_house')
    # for key in my_dict:
    #     my_dict[key] = float(my_dict[key])

    results = {}

    results = Property.objects.filter(editedfacts_finishedsqft__gt=int(my_dict['Size of house Value']),yearbuilt__lt=2015-int(my_dict['Age of the house Value']))

    return HttpResponse(serializers.serialize("json", results), content_type='application/json')
