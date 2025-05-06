import pymongo
import pandas as pd


path = "/home/codespace/.cache/kagglehub/datasets/devdope/200k-spotify-songs-light-dataset/versions/1"

df = pd.read_csv(path + "/light_spotify_dataset.csv", header=0)


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Convert DataFrame to dictionary and insert into MongoDB
collection.insert_many(df.to_dict('records'))

