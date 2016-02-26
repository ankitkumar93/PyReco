#Code for Parsing XML and pushing data onto mongoDB
#Designed by Ankit Kumar for CSC 510 Project - NCSU - Spring 2016
#imports
import os
from pymongo import MongoClient
import xml.etree.ElementTree as XParser

#globals
#dump files
directory='./Dump/'
filebase = "dump_" 
extension =".xml"
filenumber = 0
filecount = 52

#db
dbname = 'pyreco'
collname = 'questions'

#db init
client = MongoClient()
db = client[dbname]
coll = db[collname]

#keywords filter
keylist = ['LastEditDate', 'LastEditorUserId', 'LastActivityDate', 'OwnerUserId', 'CreationDate']
anskey = 'AnswerCount'

#db insert function
def inserttodb(attrib):
	doc = {}
	if anskey in attrib and int(attrib[anskey]) > 0:
		for key in attrib:
			if key not in keylist:
				doc[key] = attrib[key]
		result = coll.insert_one(doc)


#xml processor
def processxml(file):
	for event, elem in XParser.iterparse(file):
		inserttodb(elem.attrib)

#main
while filenumber < filecount:
	filename = filebase + str(filenumber) + extension
	filepath = os.path.join(directory, filename)
	processxml(filepath)
	print "file number: #" + str(filenumber) + " done!"
	filenumber += 1
print "db insertion done!"