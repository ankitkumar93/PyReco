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
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
POSTS_DATABASE = "sol1db"
POSTS_COLLECTION = "posts"
KEYWORDS_COLLECTION = "keywords"

questions_collection = MongoClient(MONGO_CONNECTION_STRING)[POSTS_DATABASE][POSTS_COLLECTION]
keywords_collection = MongoClient(MONGO_CONNECTION_STRING)[POSTS_DATABASE][KEYWORDS_COLLECTION]
question_cursor = questions_collection.find()
questionCount = question_cursor.count()
question_cursor.batch_size(50000)

# load nltk's English stopwords as variable called 'stopwords'
stopwords = nltk.corpus.stopwords.words('english')
stopFile = open("/home/harshdeep/Documents/SE/stopwords.txt", "r")
stopW = stopFile.read()
my_stopwords = stopW.split(", ")
updatedstopwords = my_stopwords + stopwords + ['python']
print(len(updatedstopwords))

# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
done = 0
start = time.time()

def main():
	for question in question_cursor:
		Create_BagOfWords(question)

			
	
def Create_BagOfWords(question):
	text = question["Body"] + question["Title"] + question["Tags"]
	text = re.sub(r'python|Python|[^A-Za-z0-9. ]+',' ',text)
	tokens = nltk.word_tokenize(text)
	tokens = set(tokens)
	tagged = nltk.pos_tag(tokens)
	tagged = [word for (word,tag) in tagged if tag not in ["PRP","RB","JJ", "JJS"] and word.lower() not in updatedstopwords]
	text = ' '.join([word for word in tagged])
	question["Body"] = text;
	insert_BagofWords(question)
	done += 1
	if done % 100 == 0:
		end = time.time()
		os.system('cls')
		print 'Done ' + str(done) + ' out of ' + str(reviewsCount) + ' in ' + str((end - start))


def insert_BagofWords(question):
	keywords_collection.insert_one({
        "id": question["Id"],
        "tags": question["Body"]        
    })

if __name__ == "__main__":
    main()