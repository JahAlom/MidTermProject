"""Midterm Project to gather Dosa restaurant orders and generate customer and item JSON files."""
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
with open(args.filename, "r", encoding="utf-8") as file:
    orderlist = json.load(file)
#Printing messages to check if JSON succeeded and total number of orders there were
print("JSON successful")
print("Total orders = ", len(orderlist))

#Checking and reading order list and checking first order only
print("#1 Order: ", orderlist[0] if isinstance(orderlist, list) else list(orderlist.items())[:1])

#Function to create customer list of orders
def customerslist(orders):
    """Create a dictionary of customers and save it to a JSON file."""

    #Dictionary created with for loop to follow to go through order list
    customers = {}
    for order in orders:
        phone = order["phone"]
        name = order["name"]

        customers[phone] = name

    #Opening customers.json and writing data and use dump to write it in JSON format
    with open("customers.json", "w", encoding="utf-8") as file:
        json.dump(customers, file, indent = 4)

    #return customer info
    return customers

#Function to test Item list in orders
def itemslist(orders):    
    """Create a dictionary of item orders and save their prices and counts to a JSON file."""
        
    #Dictionary created to store items
    items = {}
    #For loop to go through each order 
    for order in orders:
        #Nested for loop to go through each item in the order and grab the data
        for item in order["items"]:
            itemname = item["name"]
            price = item["price"]

            #Checking if the item exists or not and if not, initializes it
            if itemname not in items:
                items[itemname] = {
                    "price": price,
                    "orders": 0
                }

            items[itemname]["orders"] += 1

    #Opening the json file and writes the item and dumps and writes the data in JSON format
    with open("items.json", "w", encoding="utf-8") as file:
        json.dump(items, file, indent = 4)

    #returns item info
    return items

#Calling the functions
customers = customerslist(orderlist)
items = itemslist(orderlist)

#Print totals for customers, items
print("\nTotal individual customers: ", len(customers))
print("\nTotal singular items: ", len(items))