#Code for Parsing XML and pushing data onto mongoDB
#Designed by Ankit Kumar for CSC 510 Project - NCSU - Spring 2016
#imports
import os
from pymongo import MongoClient
import xml.etree.ElementTree as XParser

#globals
#dump files
directory='./Dump/'
filename = "dump_0.xml"
#db
dbname = sopython
collname = dataset

#db init
client = MongoClient()
db = client[dbname]
coll = db[collname]

#db insert function
def inserttodb(attrib):
	doc = {}
	for key in attrib:
		doc[key] = attrib[key]
	result = coll.insert_one(doc)
	print "record insert with id: #" + str(result)


#xml processor
def processxml(file):
	for event, elem in XParser.iterparse(file):
		inserttodb(elem.attrib)

#main
filepath = os.path.join(directory, filename)
processxml(filepath)