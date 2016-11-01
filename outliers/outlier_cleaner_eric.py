#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    error = [0 for i in ages]

    ### your code goes here

    #ages2 = []
    #print ages
    #for i in ages:
    #    #print ("ages i 0 0 ", ages[i][0][0])
    #    ages2.append(ages[i][0][0])
    #print ("ages2", ages2)

    # now, let's loop over the data and find the error for each
    for i in ages:
        error[i] = (predictions[i]-net_worths[i])**2 
        print("error for ", i, ": ", error[i])

    # now, figure out which data point is the biggest outlier, and remove it
    newages = []
    new_nw = []
    new_error = []
    for i in ages:
        newages.append(ages[i])
        new_nw.append(net_worths[i])
        new_error.append(error[i])

    bigerror = 0
    errorindex = 0
    for i in newages:
        if (newerror[i] > bigerror):
            bigerror = error[i]
            errorindex = i
    # now, generate a NEW ages list without that point
    newages = []
    new_nw = []
    for i in ages:
        if (i != errorindex):
            newages.append(ages[i])
            new_nw.append(net_worths[i])
    print(newages)
    print(new_nw)


    print ("biggest error is ", bigerror, "at point", errorindex)
    
    return cleaned_data

