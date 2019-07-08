from pymongo import MongoClient
import pandas as pd
import pprint

# establish a connection to MongoDB with PyMongo you use the MongoClient class:
client = MongoClient('mongodb://localhost:27017/')
db = client.companies

req = db.companies.find({"category_code":"web"})
print(list(req))


'''
for i,company in enumerate(companies):
    pprint.pprint(company)
    if i == 5:
        break
        '''
# nobody likes to have companies with more than 10 years
req = db.companies.find({founded_year:{$gte: 2009}})
print(list(req))