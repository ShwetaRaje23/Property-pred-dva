from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import Context
from django.http import HttpResponse
from django.db import models
from startpp.models import Property
import numpy as np
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypp.settings")
from startpp.models import CityAmenities
from startpp.models import CitySchools
from startpp.models import CityEntertainment
from startpp.models import CityFood
from startpp.models import CityFoodPlaces
from startpp.models import CityHealth
from startpp.models import CityPlacesOfWorship
from startpp.models import CityPublicSpaces
from startpp.models import CityServicesData
from startpp.models import CityShopsData
from startpp.models import CityTransportationData
from startpp.models import CityMiscServicesData
from startpp.models import CityCrimeData
from startpp.models import CityPropertyData_temp
from startpp.models import CityPropertyData
from django.core import serializers
#import simplejson
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import Context
from django.http import HttpResponse
from django.db import models
from startpp.models import Property
#import simplejson
from django.core.serializers.json import DjangoJSONEncoder
import json
from reinforcement import update_search_parameters, update_with_reinforcement
from django.db.models import Q
# Create your views here.

def login(request):
    return render_to_response('login.html')

def hello_view(request):
    return render_to_response('helloworld.html', Context({'username':request.GET.get('name')}   ))

def showbubble(request):
    results = {}
    results['weight'] = update_search_weights
    results['data'] = obj
    return render_to_response('Bubble.html',Context({'results': results}))

def action_controller(request):
    return HttpResponse(content=request.GET.get('name'))

def inputdata_view(request):
    return render_to_response('maps2.html', Context({'username':request.GET.get('name')}   ))

def getdata_view(request):

    
    price_val = request.GET.get("getprice")
    bedrooms = request.GET.get("getbedroom")
    price_priority = request.GET.get("pricepri") #id = 1
    bedroom_priority = request.GET.get("bedroom_pri") #id = 2
    size_priority = str(2) #
    crime_priority = request.GET.get("crimepriority") #id = 3
    location_val = "55 MCDONOUGH BLVD SW"#request.GET.get("location")
   #  #priorities = [price_priority,bedroom_priority,crime_priority]
   #  #filter on pricepri and then on bedroom_pri or the other way round - only 2 possibilities
   #  query_set_crime = CityCrimeData.objects.filter(location = '55 MCDONOUGH BLVD SW')
   #  query_set_loc = CityPropertyData.objects.filter(location = 'LONG ISLAND DR NW')#
   #  final = query_set_loc
    feature_ranks = [price_priority, unicode(size_priority, "utf-8"), bedroom_priority, crime_priority]
    # attributes, update_search_weights = update_search_parameters(feature_ranks)
    attributes = [1,2,3,0]
    for i in range(0, 4):
      if(attributes[i] == 0):
          idx_price = i
      if(attributes[i] == 2):
          idx_bedroom = i
    

    if(idx_price < idx_bedroom):
        query_set_price = CityPropertyData.objects.filter(price_input__gt = float(price_val) * 0.8, price_input__lt = price_val)
        query_set_bed = query_set_price.filter(num_bedrooms=bedrooms)
        if(len(query_set_bed) == 0):
            final = query_set_price
    else:
        query_set_bed = CityPropertyData.objects.filter(num_bedrooms=bedrooms)
        query_set_price = query_set_bed.filter(price_input__gt = float(price_val) * 0.8, price_input__lt = price_val)
        if(len(query_set_price) == 0):
            final = query_set_bed
    #print '###################'
    #print serializers.serialize("json", final)
    #print '###################'
    #generate one final json based on the number of results
    final_crime = CityCrimeData.objects.filter(Q(location__contains = "BAKER RD NW")| Q(location__contains = "PEACHTREE") | Q(location__contains = "LENOX") | Q(location__contains = "HOWELL") | Q(location__contains = "BAKER") | Q(location__contains = "PIEDMONT"))[:20]
   #  final_dict = {}
   #  final_dict['prop_data'] = final
   #  final_dict['crime'] = final_crime
   #  obj = {
   # 'prop_data': serializers.serialize('json', final),
   # 'crime': serializers.serialize('json', query_set_crime)
   #  }
    #get random data from db
    
    # query_set_loc = CityPropertyData.objects.filter(location = 'LONG ISLAND DR NW')#
    final = CityPropertyData.objects.filter(pk__in= np.random.choice(5000, 20).tolist())
    
    #, location__contains = "LENOX", location__contains = "HOWELL", location__contains ="BAKER", location__contains="PIEDMONT")
    final_dict = {}
    final_dict['prop_data'] = serializers.serialize('json', final)
    final_dict['crime'] = serializers.serialize('json', final_crime)

    lati = []
    longi = []
    lname = []
    lprice = []
    for each in final.values():
      lati.append(float(each['location_lat']))
      longi.append(float(each['location_lng']))
      lname.append(each['location'])
      lprice.append(float(each["price_input"]))

    my_dict = {}
    my_dict['latitude'] = lati
    my_dict['longitude'] = longi
    my_dict['lname'] = lname
    my_dict['lprice'] = lprice


   #  obj = {
   # 'prop_data': serializers.serialize('json', final),
   # 'crime': serializers.serialize('json', final_crime)
   #  }
    
   #  #query_set_loc = CityPropertyData.objects.filter(location = '1194 WOODLAND AVE SE', )
    # obj_json = json.dumps(obj)
    # obj_json = json.dumps(final_dict)
    obj_json = json.dumps(my_dict)
    return render_to_response('maps2.html', Context({'results_json': obj_json}))
    # obj_json = json.dumps(my_dict)
    # return HttpResponse(final.values())

    #--------------------------correct-----------------------------------------
    # results = {}
    # results = Property.objects.filter(editedfacts_finishedsqft__gt=int(my_dict['Size of house Value']),yearbuilt__lt=2015-int(my_dict['Age of the house Value'])).values()
    # final_output = {}
    # for result in results:
    #     final_output[result['zpid']] = result
    # response = {'meta':{'status':'success'}, 'data':final_output}
    # print response
    # response = simplejson.dumps(response)
    # return render_to_response('Bubble.html', Context({'results_json': response}))
    #--------------------------------correct-------------
    # return HttpResponse(serializers.serialize("json", results), content_type='application/json')
    # return render_to_response('Bubble.html', Context({'results_json':results}   ))
    # return render_to_response('Bubble.html', serializers.serialize("json", results), content_type='application/json')
    # results_change = serializers.serialize("json",results)
    # return render(request, "Bubble.html", {'json_results':results_change})
    # return render_to_response('Bubble.html',{'json_results':results_change})
    # with open('results.json','w') as fp:
    #     json.dump(results_change, fp)
    #

def send_data_from_view(request):
    result_dict = {}

    result_dict["listing1"] = "Georgia Tech"
    result_dict["listing2"] = "Peachtree St."

    response = simplejson.dumps(result_dict)
    return render_to_response('maps2.html', Context({'results_json': response}))

def collect_feedback(request):
    return render_to_response('Feedback.html')

def feedback_data(request):
    my_list = []
    #Sequence is price, size, beds, safety
    my_list.append(request.GET.get("price"))
    my_list.append(request.GET.get("size"))
    my_list.append(request.GET.get("beds"))
    my_list.append(request.GET.get("safety"))



  # this will be used to search the parameters
    attributes, update_search_weights_normalized = update_search_parameters(my_list)

    update_with_reinforcement(my_list)
    return render_to_response('thanks.html')
