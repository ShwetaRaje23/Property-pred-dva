import csv
import numpy as np

def get_actual_weights():
    list_weights = []
    f = open('initial_w.csv', 'rt')
    reader = csv.reader(f)
    for row in reader:
        # print row
        list_weights = row

    list_weights = map(float, list_weights)

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
        new_weights = feature_ranks * calculate_pmf(initial_weights) + bias
    else:
        new_weights = feature_ranks * calculate_pmf(initial_weights)
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
    val = np.max(feature_ranks)
    initial_weights[idx] += val
    initial_weights[idx] /= 2.0

    pmf_updated = calculate_pmf(initial_weights)
    print "mass fx after reinforcement ", pmf_updated

    if np.sqrt(2) * np.linalg.norm(pmf_updated - pmf1) > 0.02:
        print "outlier detected, reverting back learning"
        initial_weights = backup

    return initial_weights


# def modify_system_weights():


if __name__ == '__main__':
    print update_search_parameters([1, 1, 1, 5])

    print update_with_reinforcement([1, 1, 1, 5])