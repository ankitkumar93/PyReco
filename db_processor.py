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
directory='./Dump/'
filebase = "dump_" 
extension =".xml"
filenumber = 0
filecount = 1

#db
dbname = 'pyreco'
collnameq = 'questions'
collnamea = 'answers'

#db init
client = MongoClient()
db = client[dbname]
collq = db[collnameq]
colla = db[collnamea]

#keywords filter
keylist = ['LastEditDate', 'LastEditorUserId', 'LastActivityDate', 'OwnerUserId', 'CreationDate']
anskey = 'AnswerCount'
bodykey = 'Body'

#answer vallist
answervals = []

#filter the body to make it only text
def filtertext(text):
	soup = BeautifulSoup(text, "html.parser")
	parsed_text = soup.getText()
	return parsed_text

#db insert function for questions
def inserttodbq(attrib):
	doc = {}
	if anskey in attrib and int(attrib[anskey]) > 0:
		answervals.append(attrib[anskey])
		for key in attrib:
			if key not in keylist:
				if key == bodykey:
					doc[key] = filtertext(attrib[key])
				else:
					doc[key] = attrib[key]
		result = collq.insert_one(doc)

#db insert function for answers
def inserttodba(attrib):
	doc = {}
	if anskey in attrib and int(attrib[anskey]) in answervals:
		for key in attrib:
			if key not in keylist:
				if key == bodykey:
					doc[key] = filtertext(attrib[key])
				else:
					doc[key] = attrib[key]
		result = colla.insert_one(doc)


#xml processor for questions
def processxmlq(file):
	for event, elem in XParser.iterparse(file):
		inserttodbq(elem.attrib)

#xml processor for answers
def processxmla(file):
	for event, elem in XParser.iterparse(file):
		inserttodba(elem.attrib)

#main
#insert questions into db
while filenumber < filecount:
	filename = filebase + str(filenumber) + extension
	filepath = os.path.join(directory, filename)
	processxmlq(filepath)
	print "file number: #" + str(filenumber) + " done!"
	filenumber += 1
print "db questions insertion done!"

#insert answers into db
filenumber = 0
while filenumber < filecount:
	filename = filebase + str(filenumber) + extension
	filepath = os.path.join(directory, filename)
	processxmla(filepath)
	print "file number: #" + str(filenumber) + " done!"
	filenumber += 1
print "db answers insertion done!"