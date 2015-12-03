from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import Context
from django.http import HttpResponse
from django.db import models
from startpp.models import Property
import simplejson
from django.core.serializers.json import DjangoJSONEncoder
import json
from reinforcement import update_search_parameters

# Create your views here.


def hello_view(request):
    return render_to_response('helloworld.html', Context({'username':request.GET.get('name')}   ))

def showbubble(request):
    return render_to_response('Bubble.html')

def action_controller(request):
    return HttpResponse(content=request.GET.get('name'))

def inputdata_view(request):
    return render_to_response('maps2.html', Context({'username':request.GET.get('name')}   ))

def getdata_view(request):
    my_dict = {}
    # my_dict['Size of house Value'] = request.GET.get('size_of_house_value')
    # my_dict['Proximity To Public Transport Value'] = request.GET.get('proximity_to_public_transport_value')
    # my_dict['Price of the house Value'] = request.GET.get('price_of_the_house_value')
    # my_dict['Number of bedrooms Value'] = request.GET.get('number_of_bedrooms_value')
    # my_dict['School in the neighborhood Value'] = request.GET.get('school_in_the_neighborhood_value')
    # my_dict['Hospital in the neighborhood Value'] = request.GET.get('hospital_in_the_neighborhood_value')
    # my_dict['Pet friendly Value'] = request.GET.get('pet_friendly_value')
    # my_dict['Yard available Value'] = request.GET.get('yard_available_value')
    # my_dict['Bars around Value'] = request.GET.get('bars_around_value')
    # my_dict['Crime rate in the locality Value'] = request.GET.get('crime_rate_in_the_locality_value')
    # my_dict['Places of worship around Value'] = request.GET.get('places_of_worship_nearby_value')
    # my_dict['Closeness to workplace Value'] = request.GET.get('closeness_to_workplace_value')
    # my_dict['Closeness to super market Value'] = request.GET.get('closeness_to_super_market_value')
    # my_dict['Age of the house Value'] = request.GET.get('age_of_the_house_value')
    # my_dict['Size of house Priority'] = request.GET.get('size_of_house')
    # my_dict['Proximity To Public Transport Priority'] = request.GET.get('proximity_to_public_transport')
    # my_dict['Price of the house Priority'] = request.GET.get('proximity_to_public_transport')
    # my_dict['Number of bedrooms Priority'] = request.GET.get('number_of_bedrooms')
    # my_dict['School in the neighborhood Priority'] = request.GET.get('school_in_the_neighborhood')
    # my_dict['Hospital in the neighborhood Priority'] = request.GET.get('hospital_in_the_neighborhood')
    # my_dict['Pet friendly Priority'] = request.GET.get('pet_friendly')
    # my_dict['Yard available Priority'] = request.GET.get('yard_available')
    # my_dict['Bars around Priority'] = request.GET.get('bars_around')
    # my_dict['Crime rate in the locality Priority'] = request.GET.get('crime_rate_in_the_locality')
    # my_dict['Places of worship around Priority'] = request.GET.get('places_of_worship_nearby')
    # my_dict['Closeness to workplace Priority'] = request.GET.get('closeness_to_workplace')
    # my_dict['Closeness to super market Priority'] = request.GET.get('closeness_to_super_market')
    # my_dict['Age of the house Priority'] = request.GET.get('age_of_the_house')
    # for key in my_dict:
    #     my_dict[key] = float(my_dict[key])

    my_dict["price"] = request.GET.get("getprice")
    my_dict["bedrooms"] = request.GET.get("getbedroom")
    my_dict["price_priority"] = request.GET.get("pricepri")
    my_dict["bedroom_priority"] = request.GET.get("bedroom_pri")
    my_dict["crime_priority"] = request.GET.get("crimepriority")

    return HttpResponse(json.dumps(my_dict))

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
