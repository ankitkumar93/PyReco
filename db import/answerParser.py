#Code for Breaking down XML into smaller chunks and filtering on Answers
#Designed by Ankit Kumar for CSC 510 Project - NCSU - Spring 2016
import os
import xml.etree.ElementTree as XParser
from bs4 import BeautifulSoup
from pymongo import MongoClient

#globals
counter = 0
print_bound = 10
switch_bound = 4000
write_bound = 5000

#db
dbname = 'pyreco'
collname = 'questions'
collnamea = 'answers'

#db init
client = MongoClient()
db = client[dbname]
coll = db[collname]
colla = db[collnamea]

#keys
accanskey = 'AcceptedAnswerId'
idkey = 'Id'
postypekey = 'PostTypeId'
keylist = ['LastEditDate', 'LastEditorUserId', 'LastActivityDate', 'OwnerUserId', 'CreationDate']
bodykey = 'Body'

#answer ids
answerids = []

#filter the body to make it only text
def filtertext(text):
	soup = BeautifulSoup(text, "html.parser")
	parsed_text = soup.getText()
	return parsed_text

#db insert function for answers
def inserttodb(attrib):
	doc = {}
	if idkey in attrib:
		for key in attrib:
			if key not in keylist:
				if key == bodykey:
					doc[key] = filtertext(attrib[key])
				else:
					doc[key] = attrib[key]
		result = colla.insert_one(doc)

#process element
def processElem(attrib):
	#insert to db
	inserttodb(attrib)
	
	#print processing
	global counter
	global print_bound

	counter += 1
	if counter % print_bound == 0:
		print "#" + str(counter) + " records processed"
	
	#dynamic print bound
	if counter == switch_bound:
		print_bound = 1

#answer id fetcher
def fetchanswerids():
	outputids = []
	qdata = coll.find()

	for row in qdata:
		outputids.append(row[accanskey])

	return outputids


#parse
def main():
	#fetch answer ids
	global answerids
	answerids = fetchanswerids()

	print "answer ids done!"

	#parse xml
	for event, elem in XParser.iterparse('../Resources/Posts/Posts.xml'):
		posttype = elem.attrib.get(postypekey)
		currid = elem.attrib.get(idkey)
		if posttype != None:
			if posttype == '2' and currid in answerids:
				processElem(elem.attrib)
				answerids.remove(currid)
		elem.clear()
		if counter == write_bound:
			break

	print "all done!"

if __name__ == '__main__':
	main()
