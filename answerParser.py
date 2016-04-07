#Code for Breaking down XML into smaller chunks and filtering on Answers
#Designed by Ankit Kumar for CSC 510 Project - NCSU - Spring 2016
import os
import xml.etree.ElementTree as XParser
counter = 0
file_number = 0
filename = "dump_"
directory = './AnswerDump/'
extension = ".xml"
file_limit = 100000
file_limit = 10000
print_bound = 1000
root = XParser.Element("posts")
def processElem(attrib):
	global counter
	global file_limit
	global print_bound
	global root
	if(counter < file_limit):
		row = XParser.SubElement(root, "row")
		for key in attrib:
			row.set(key, attrib[key])
	counter += 1
	if counter % print_bound == 0:
		print "#" + str(counter) + " records processed"
	if(counter == file_limit):
		global file_number
		tree = XParser.ElementTree(root)
		path = os.path.join(directory,filename+str(file_number)+extension)
		tree.write(path)
		counter = 0
		print "file: #" + str(file_number) + " done!"
		file_number += 1
		root.clear()


for event, elem in XParser.iterparse('../Resources/Posts/Posts.xml'):
	posttype = elem.attrib.get('PostTypeId')
	if posttype != None:
		if posttype == '2':
			processElem(elem.attrib)
	elem.clear()

#at the end appent the remaining data to a file
tree = XParser.ElementTree(root)
path = os.path.join(directory,filename+str(file_number)+extension)
tree.write(path)
print "file: #" + str(file_number) + " done!"
print "last file has records : #" + str(counter)
	elem.clear()
