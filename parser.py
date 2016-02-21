import os
import xml.etree.ElementTree as XParser
counter = 0
file_number = 0
filename = "dump_"
directory = './Dump/'
extension = ".xml"
file_limit = 1000
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
		file_number += 1
		print "current file" + str(file_number)


for event, elem in XParser.iterparse('../Data/Posts.xml'):
	tags = elem.attrib.get('Tags')
	if tags != None:
		if '<python>' in tags:
			processElem(elem.attrib)
	elem.clear()