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