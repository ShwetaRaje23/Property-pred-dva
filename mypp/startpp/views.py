from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import Context
from django.http import HttpResponse
import json
# Create your views here.


def hello_view(request):
    return render_to_response('helloworld.html', Context({'username':request.GET.get('name')}   ))

def action_controller(request):
    return HttpResponse(content=request.GET.get('name'))

def inputdata_view(request):
    return render_to_response('inputdata.html', Context({'username':request.GET.get('name')}   ))

def getdata_view(request):
    my_dict = {}
    my_dict['Size of house'] = request.GET.get('size_of_house')
    my_dict['Proximity To Public Transport'] = request.GET.get('proximity_to_public_transport')
    my_dict['Price of the house'] = request.GET.get('proximity_to_public_transport')
    my_dict['Number of bedrooms'] = request.GET.get('number_of_bedrooms')
    my_dict['School in the neighborhood'] = request.GET.get('school_in_the_neighborhood')
    my_dict['Hospital in the neighborhood'] = request.GET.get('hospital_in_the_neighborhood')
    my_dict['Pet friendly'] = request.GET.get('pet_friendly')
    my_dict['Yard available'] = request.GET.get('yard_available')
    my_dict['Bars around'] = request.GET.get('bars_around')
    my_dict['Crime rate in the locality'] = request.GET.get('crime_rate_in_the_locality')
    my_dict['Places of worship around'] = request.GET.get('places_of_worship_nearby')
    my_dict['Closeness to workplace'] = request.GET.get('closeness_to_workplace')
    my_dict['Closeness to super market'] = request.GET.get('closeness_to_super_market')
    my_dict['Age of the house'] = request.GET.get('age_of_the_house')
    return HttpResponse(json.dumps(my_dict))
