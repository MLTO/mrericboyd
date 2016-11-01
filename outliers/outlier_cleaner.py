#!/usr/bin/python

import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    # solution 1
    '''
    margin = 127
    ### your code goes here
    for i in range(len(ages)):
        # print (ages[i][0], predictions[i][0], net_worths[i][0])
        if net_worths[i][0] > margin:
            cleaned_data.append([ages[i][0], net_worths[i][0], (net_worths[i][0] - margin)])

    # solution 2
    '''
    margin = 80**2
    ### your code goes here
    for i in range(len(ages)):
        # print (ages[i][0], predictions[i][0], net_worths[i][0])
        error = (math.fabs(predictions[i][0] - net_worths[i][0]))**2
        if error < margin:
            cleaned_data.append([ages[i][0], net_worths[i][0], error])

    # similar to solution 1 but in one line
    # cleaned_data = [(ages[x][0], net_worths[x][0], (net_worths[x][0] - margin)) for x in range(len(net_worths)) if net_worths[x] > margin]

    print("len orig_data: ", len(ages))
    print("len cleaned_data: ", len(cleaned_data))
    return cleaned_data
    
