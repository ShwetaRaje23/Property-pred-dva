__author__ = 'Shweta'

'''
parameters: Take the weights form the initial Online survey we have
result: dictionary of weights for each aspect

'''

aspects = ['Size of the house',	'Proximity to public transport',	'Price of the house',	'Number of bedrooms',	'School in the neighborhood', 	'Hospital in the neighbourhood',	'Pet friendly',	'Yard available',	'Bars around	Crime rate in the locality',	'Places of worship around',	'Closeness to workplace',	'Closeness to super market',	'Age of the house']
weights = [4.081081081, 3.864864865, 4.621621622, 3.837837838,	2.594594595, 3.324324324, 3.027027027, 3.27027027, 2.459459459,	4.567567568, 2.135135135 , 4.135135135, 4.216216216, 3.621621622]


def get_weights():

	results_dict = {}
	i = -1
	for each in aspects:
		i += 1
		results_dict[each] = weights[i]
	
	return results_dict


results_dict = {}
results_dict = get_weights()
print results_dict
