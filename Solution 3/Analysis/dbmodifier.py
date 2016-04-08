#code for importing n documents into db
#designed by Ankit Kumar

#imports
from pymongo import MongoClient

#globals
mongo_url = "mongodb://localhost:27017/"
db_name = "pyreco"
dump_collection_name = "dump_questions"
questions_collection_name = "questions"

#parameter = count to be imported
questions_count = 5000

#init db
connection = MongoClient(mongo_url)
db = connection[db_name]
dump_collection = db[dump_collection_name]
questions_collection = db[questions_collection_name]

#cursors
dump_cursor = dump_collection.find()

#main
def main():
	index = 0
	for dump_row in dump_cursor:
		insertintodb(dump_row)
		index += 1
		print "inserted row: " + str(index)
		if index == questions_count:
			break

#insert into db
def insertintodb(row):
	questions_collection.insert_one(row)

#execute main
if __name__ == "__main__":
    main()
