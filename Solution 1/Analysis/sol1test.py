from __future__ import print_function
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from pymongo import MongoClient
import sys



#DATASET_FILE = 'dataset/yelp_dataset_challenge_academic_dataset'
# db.keywords.find({$text: {$search: "\"NULL database\""}})
# db.keywords.find({$text: {$search: "varchar oracle"}})
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
POSTS_DATABASE = "sol1db"
POSTS_COLLECTION = "posts"
KEYWORDS_COLLECTION = "keywords"

questions_collection = MongoClient(MONGO_CONNECTION_STRING)[POSTS_DATABASE][POSTS_COLLECTION]
keywords_collection = MongoClient(MONGO_CONNECTION_STRING)[POSTS_DATABASE][KEYWORDS_COLLECTION]
question_cursor = questions_collection.find()
keywords_cursor = keywords_collection.find()
question_cursor.batch_size(50000)


def main():
	text = 'how to connect mongo database locally using python'
	ids = find_text(text)
	print("question id is ")
	print(ids)

def find_text(text):
	ids = []
	cursor = keywords_collection.find()
	for doc in cursor:
		ids.append(doc["id"])
	return ids

			
	
if __name__ == "__main__":
    main()