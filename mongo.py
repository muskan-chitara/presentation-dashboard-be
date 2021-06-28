import sel
from pymongo import MongoClient
#change the MongoClient connection string to your MongoDB database instance
client = MongoClient()
db=client.webdata1

data_dict = sel.df_bs.to_dict("records")
result=db.events.insert_one({"data":data_dict})