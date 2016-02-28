***********************************
Creating MongoDB with shared json:
***********************************

1. Get the json file with data
2. Run:
	mongoimport --db <db_name> --collection <collection_name> --file <json_file_name>
	example: mongoimport --db test --collection restaurants --drop --file primer-dataset.json
	//collection is similar to Table in relational db
3. Accessing:
	Inside Mongo Console:
	a. use <db_name>
	b. db.<collection_name>
	c. db.collection.find({})

***********************************
working with MongoDB in python:
***********************************
1. install the package:
	sudo pip install pymongo
2. import in code:
	from pymongo import MongoClient
3. Create a connection:
	client = MongoClient("mongodb://mongodb0.example.net:27019")
4. 
Note: The mongoimport connects to a mongod instance running on localhost on port number 27017.