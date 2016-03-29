#Desgined by Ankit Kumar
#Used to Create simhashes of questions in a new collection

#imports
from simhash import Simhash
from pymongo import MongoClient
import sys

#globals
db_addr = "mongodb://localhost:27017/"
collection_name = "qhash"
tag_collection_name = "sol1"
db_name = "pyreco"
width = 32

#db connection
client = MongoClient(db_addr)
db = client[db_name]
collection = db[collection_name]
tag_collection = db[tag_collection_name]

#function to import all question tags
def importtags():
	data = tag_collection.find()
	return data

#function to calculate hash of the supplied data
def calchash(data):
	hashdata = Simhash(data,width)
	return hashdata.value

#function to insert into collection
def insert(hashdata, id):
	row = {"Id" : id, "Hash" : hashdata}
	row_id = collection.insert_one(row)
	print row_id

#main code
tagdata = importtags()
for row in tagdata:
	id = row["id"]
	tags = row["tags"]
	hashinput = tags.split(" ")
	hashval = calchash(hashinput)
	insert(hashval, id)
