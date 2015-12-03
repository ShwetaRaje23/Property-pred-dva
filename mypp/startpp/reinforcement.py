import csv
import numpy as np
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import Context
from django.http import HttpResponse
from django.db import models
from startpp.models import Property
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
from startpp.models import InitialWeights
from django.core import serializers
import simplejson
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

def get_actual_weights():
    list_weights = []
    #f = open('initial_w.csv', 'rt')
    init_weights = InitialWeights.objects.all()
    #query_set_crime = InitialWeights.objects.filter(location = location_val)
    #reader = csv.reader(f)
    for row in init_weights:
        # print row
        list_weights = [row.price, row.area, row.bedrooms, row.crime]
    list_weights = [float(x) for x in list_weights]
    #list_weights = map(float, list_weights)

    # print list_weights
    return list_weights

'''
vector - a 1d numpy row vector
'''
def calculate_pmf(vector):
    sum = np.sum(vector)
    pmf = vector/sum
    assert np.all(pmf) <= 1, "probability cannot be greater than 1"
    return pmf

'''
 pmf - is the 1d numpy array for probability mass/density function
'''
def calculate_cdf(pmf):
    return np.cumsum(pmf)

# returns ranked attribute indexes and the normalized weights

def update_search_parameters(feature_ranks, explore=False, epsilon=[1/4.]*4):
    initial_weights = get_actual_weights()
    initial_weights = np.array(initial_weights)
    # please do not mind me trying to do some epsilon-greedy stuff here with epsilon = 0
    bias = np.zeros(4)
    if explore:
        bias = np.random.multinomial(4, epsilon, size=1) + 1
        #bias = calculate_pmf(bias)

    feature_ranks = np.array(feature_ranks)
    if explore:
        new_weights = np.multiply(np.array(feature_ranks, np.float), np.array(calculate_pmf(initial_weights), np.float)) + bias
    else:
        new_weights = np.multiply(np.array(feature_ranks, np.float), np.array(calculate_pmf(initial_weights), np.float))
    update_search_weights_normalized = calculate_pmf(new_weights)

    attributes = np.argsort(update_search_weights_normalized)
    attributes = attributes[::-1]
    return attributes, update_search_weights_normalized
    #print update_search_weights_normalized

def update_with_reinforcement(feature_ranks):
    initial_weights = get_actual_weights()
    from copy import deepcopy
    backup = deepcopy(initial_weights)
    pmf1 = calculate_pmf(np.array(initial_weights))
    print "mass fx 1 ", pmf1
    feature_ranks = np.array(feature_ranks)
    idx = np.argmax(feature_ranks)
    val = np.max(np.array(feature_ranks, np.float))
    initial_weights[idx] += val
    initial_weights[idx] /= 2.0

    pmf_updated = calculate_pmf(initial_weights)
    print "mass fx after reinforcement ", pmf_updated

    if np.sqrt(2) * np.linalg.norm(pmf_updated - pmf1) > 0.02:
        print "outlier detected, reverting back learning"
        initial_weights = backup
    price = initial_weights[0]
    area = initial_weights[1]
    bedrooms = initial_weights[2]
    crime = initial_weights[3]
    InitialWeights.objects.all().delete()
    ca = InitialWeights(1, price, area, bedrooms, crime)
    ca.save()
    #return initial_weights


# def modify_system_weights():


if __name__ == '__main__':
    print update_search_parameters([1, 1, 1, 5])

    print update_with_reinforcement([1, 1, 1, 5])