#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
from math import isnan

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#poisum = 0;
#for person in enron_data:
#	poisum = poisum + enron_data[person]["poi"]
#print poisum

#print enron_data["PRENTICE JAMES"]['total_stock_value']
#print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
#print enron_data["SKILLING JEFFREY K"]["total_payments"]
#print enron_data["LAY KENNETH L"]["total_payments"]
#print enron_data["FASTOW ANDREW S"]["total_payments"]


salarycount = 0
emailaddresscount = 0
totalpaymentscount = 0
numpois = 0
total = 0
for person in enron_data:
	#print enron_data[person]["salary"]
	total = total + 1
	if enron_data[person]["poi"] == True:
		numpois = numpois + 1
	if enron_data[person]["salary"] !="NaN":
	 	salarycount = salarycount + 1
	if enron_data[person]["email_address"] != "NaN":
		emailaddresscount = emailaddresscount + 1		
	if enron_data[person]["total_payments"] == "NaN":
		if enron_data[person]["poi"] == True:
			totalpaymentscount = totalpaymentscount + 1		
print "salary count: ", salarycount
print "number of pois: ", numpois
print "email address count: ", emailaddresscount
print "total payments count: ", totalpaymentscount
print "total: ", total
print "percentage: ", float(float(totalpaymentscount)/float(total))
