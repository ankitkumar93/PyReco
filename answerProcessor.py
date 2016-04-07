#Code for Parsing XML and pushing data onto mongoDB
#Designed by Ankit Kumar for CSC 510 Project - NCSU - Spring 2016
#imports
import os
from pymongo import MongoClient
import xml.etree.ElementTree as XParser
from bs4 import BeautifulSoup
import time

#globals
#dump files
directory='./AnswerDump/'
filebase = "answerdump" 
extension =".xml"

#db
dbname = 'pyreco'
collname = 'answers'

#db init
client = MongoClient()
db = client[dbname]
coll = db[collname]

#keywords filter
keylist = ['LastEditDate', 'LastEditorUserId', 'LastActivityDate', 'OwnerUserId', 'CreationDate']
bodykey = 'Body'
idkey = 'Id'

#filter the body to make it only text
def filtertext(text):
	soup = BeautifulSoup(text, "html.parser")
	parsed_text = soup.getText()
	return parsed_text

#db insert function for answers
def inserttodb(attrib):
	doc = {}
	if idkey in attrib
		for key in attrib:
			if key not in keylist:
				if key == bodykey:
					doc[key] = filtertext(attrib[key])
				else:
					doc[key] = attrib[key]
		result = coll.insert_one(doc)


#xml processor for answers
def processxml(file):
	for event, elem in XParser.iterparse(file):
		inserttodb(elem.attrib)


#main
def main():
	#insert answers into db
	filename = filebase + extension
	filepath = os.path.join(directory, filename)
	processxml(filepath)

	print "db answers insertion done!"