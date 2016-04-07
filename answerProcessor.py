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
filebase = "dump_" 
extension =".xml"
filenumber = 0
filecount = 52

#db
dbname = 'pyreco'
collname = 'answers'
collnameq = 'questions'

#db init
client = MongoClient()
db = client[dbname]
coll = db[collname]
collq = db[collnameq]

#keywords filter
keylist = ['LastEditDate', 'LastEditorUserId', 'LastActivityDate', 'OwnerUserId', 'CreationDate']
anskey = 'AnswerCount'
bodykey = 'Body'
accanskey = 'AcceptedAnswerId'
idkey = 'Id'

#answer id list
answerids = []

#filter the body to make it only text
def filtertext(text):
	soup = BeautifulSoup(text, "html.parser")
	parsed_text = soup.getText()
	return parsed_text

#db insert function for answers
def inserttodb(attrib):
	doc = {}
	if idkey in attrib and attrib[idkey] in answerids
		answerids.remove(attrib[idkey])
		for key in attrib:
			if key not in keylist:
				if key == bodykey:
					doc[key] = filtertext(attrib[key])
				else:
					doc[key] = attrib[key]
		result = colla.insert_one(doc)


#xml processor for answers
def processxml(file):
	for event, elem in XParser.iterparse(file):
		inserttodb(elem.attrib)

#answer id fetcher
def fetchanswerids():
	global answerids
	qdata = collq.find()

	for row in qdata:
		answerids.append(row[accanskey])

#main
def main():
	global questionids
	#fetch answer ids
	answerids = fetchanswerids()

	#insert answers into db
	filenumber = 0
	while filenumber < filecount:
		filename = filebase + str(filenumber) + extension
		filepath = os.path.join(directory, filename)
		processxml(filepath)
		print "file number: #" + str(filenumber) + " done!"
		filenumber += 1
	print "db answers insertion done!"