#Jahurul Alom
#IS_601

import json
import argparse

#Using an argument Parser as described in the assignment
parse = argparse.ArgumentParser()

#Filename is retrieved
parse.add_argument("filename")

#The argument is read as asked in the project req
args = parse.parse_args()

#The JSON file is opened and read
with open(args.filename, "r") as file:
    orderlist = json.load(file)

#Printing messages to check if JSON succeeded and 
#total number of orders there were
print("JSON successful")
print("Total orders = ", len(orderlist))

#Checking and reading order list and checking first order only
#print("#1: ", orderlist[0] if isinstance(orderlist, list) else list(orderlist.items())[:1])

#Function to create customer list of orders
def customerslist(orders):

    #Dictionary created with for loop to follow to go through order list
    customers = {}
    for order in orderlist:
        phone = order["phone"]
        name = order["name"]

        customers[phone] = name

    #Opening customers.json and writing data and use dump to write it in JSON format
    with open("customers.json", "w") as file:
        json.dump(customers, file, indent = 4)

    #return customer info
    return customers
    