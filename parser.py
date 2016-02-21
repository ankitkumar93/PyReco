#Code for Breaking down XML into smaller chunks and filtering on Python Tag
#Designed by Ankit Kumar for CSC 510 Project - NCSU - Spring 2016
import os
import xml.etree.ElementTree as XParser
counter = 0
file_number = 0
filename = "dump_"
directory = './Dump/'
extension = ".xml"
file_limit = 100000
root = XParser.Element("posts")
def processElem(attrib):
	global counter
	global file_limit
	if(counter < file_limit):
		row = XParser.SubElement(root, "row")
		for key in attrib:
			row.set(key, attrib[key])
	counter += 1
	if(counter == file_limit):
		global file_number
		tree = XParser.ElementTree(root)
		path = os.path.join(directory,filename+str(file_number)+extension)
		tree.write(path)
		counter = 0
		print "file: #" + str(file_number) + " done!"
		file_number += 1


for event, elem in XParser.iterparse('../Data/Posts.xml'):
	tags = elem.attrib.get('Tags')
	if tags != None:
		if '<python>' in tags:
			processElem(elem.attrib)
	elem.clear()