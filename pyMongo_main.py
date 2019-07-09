from pymongo import MongoClient
import pandas as pd
import pprint
import json


# establish a connection to MongoDB with PyMongo you use the MongoClient class:
client = MongoClient('mongodb://localhost:27017/')
db = client.companies




'''     
# nobody likes to have companies with more than 10 years
req = db.companies.find({'founded_year':{'$gte': '2009'}})
print(list(req))'''