from pymongo import MongoClient
import pandas as pd
import pprint
import json
import pandas as pd
import requests


def conectMongo ():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.companies
    not_dead = db.companies.find({"$and": [ {"offices":{"$not":{"$size":0}}}, {"deadpooled_year":None } ] })
    df_entry = pd.DataFrame(not_dead)
    df = df_entry.copy()
    return df
df1=conectMongo ()
#print(df1)


#1 CURRENCY ----
def separateColumns(df):
    df['currency'] = df['total_money_raised'].str[0]
    df['total_money_raised'] = df['total_money_raised'].str[1:]
    return df
df1_s = separateColumns(df1)
#print(df1_s)

def ChangeNonNumeric(row):
    row = str(row)
    try:
        if "B" in row:
            row = row.replace("B", "")
            row = float(row)*1000000000
        elif "M" in row:
            row = row.replace("M", "")
            row = float(row)*1000000
        elif "k" in row:
            row = row.replace("k", "")
            row = float(row)*1000
    except: row=None
    return row
def Apply_ChangeNonNumeric(df):
    df['total_money_raised'] = df['total_money_raised'].apply(ChangeNonNumeric)
    return df
df_1_c= Apply_ChangeNonNumeric(df1_s)
#print(df_1_c)

def change_string(row):
    row = str(row)
    return row
def merge_currency_columns(df):
    df['currency'] = df['currency'].apply(change_string)
    df['total_money_raised'] = df['total_money_raised'].apply(change_string)
    df['currency'] = df['total_money_raised'] + df['currency']
    return df
df_1_m = merge_currency_columns(df_1_c)
print(df_1_m)


# si meto esto dentro de la función me da problemas. Why?
url = 'https://api.exchangerate-api.com/v4/latest/USD'
res = requests.get(url)
data = res.json()
    # EXCHANGE RATE API
def exchangeRate (row):
    print(res)
    row = str(row)
    try:
        if "$" in row:
            row = row.replace("$","")
            row = float(row)*data['rates']['USD']
        if "€" in row:
            row = row.replace("€","")
            row = float(row)*data['rates']['EUR']
        if "£" in row:
            row = row.replace("£","")
            row = float(row)*data['rates']['GBP']
        else:
            row = row.replace("$","")
            row = float(row)*data['rates']['USD']     
    except:
        row = row
    return row
def Apply_exchangeRate(df):
    df['currency'] = df['currency'].apply(exchangeRate)
    return df
df1_d = Apply_exchangeRate(df_1_m)
print(df1_d)