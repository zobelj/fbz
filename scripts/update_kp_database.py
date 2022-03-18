import pymongo
import re

def connect_to_mongo():
    client = pymongo.MongoClient("mongodb+srv://joe:boilerup@cluster0.si4pj.mongodb.net/database?retryWrites=true&w=majority")
    db = client["database"]
    collection = db["bracket_school"]
    settings_collection = db["bracket_calculate_setting"]
    return collection, settings_collection

import requests
import pandas as pd
import numpy as np

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def get_kp():
    url = "http://kenpom.com"
    r = requests.get(url, headers=header)
    df = pd.read_html(r.text)[0]

    df.columns = df.columns.droplevel([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    df["Rk"] = df["Rk"].replace('', np.nan)
    df.dropna(subset=["Rk"], inplace=True)
    df.drop(df[df["Rk"] == 'Rk'].index, inplace=True)
    df = df.iloc[:, :10]
    df.columns = ['Rk', 'Team', 'Conf', 'W-L', 'AdjEM', 'AdjO', 'badAdjO', 'AdjD', 'badAdjD', 'AdjT']
    df.drop(['badAdjO', 'badAdjD'], axis=1, inplace=True)

    return df

def format_team(row):
    team = re.sub('[0-9]', '', row['Team'])
    return {'name': team, 'rank': int(row['Rk']), 'conference': row['Conf'], 'wins': int(row['W-L'].split('-')[0]), 'losses': int(row['W-L'].split('-')[1]), 'adjEM': float(row['AdjEM']), 'adjO': float(row['AdjO']), 'adjD': float(row['AdjD']), 'adjT': float(row['AdjT'])}

def update():
    collection, settings_collection = connect_to_mongo()

    mongo_db = []
    df = get_kp()
    for row in df.iterrows():
        mongo_db.append(format_team(row[1]))    

    # get average adjT from df and average points
    df['AdjT'] = df['AdjT'].astype(float)
    df['AdjO'] = df['AdjO'].astype(float)
    avg_adjT = df['AdjT'].mean()
    avg_adjO = df['AdjO'].mean()

    # get the first entry in the settings collection
    settings_collection.find_one_and_update({}, {'$set': {'avg_adjT': avg_adjT, 'avg_adjO': avg_adjO}})

    # replace existing data with mongo_db
    collection.drop()
    collection.insert_many(mongo_db)
