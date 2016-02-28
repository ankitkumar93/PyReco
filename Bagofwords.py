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

questions_collection = MongoClient(MONGO_CONNECTION_STRING)[POSTS_DATABASE][POSTS_COLLECTION]
question_cursor = questions_collection.find()
questionCount = question_cursor.count()
question_cursor.batch_size(50000)

# load nltk's English stopwords as variable called 'stopwords'
stopwords = nltk.corpus.stopwords.words('english')
stopFile = open("stopwords.txt", "r")
stopW = stopFile.read()
my_stopwords = stopW.split(", ")
updatedstopwords = my_stopwords + stopwords


# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

def main():
	questions = []
	Id = []
	title = []
	tags = []
	for question in question_cursor:
		questions.append(question["Body"])
		Id.append(question["Id"])
		title.append(question["Title"])
		tags.append(question["Tags"])

	print(questions[2])
	sys.exit(1)
	


def text_preprocess(words):
	res = ""
	words = words.split()
	for word in words:
		if word.lower() not in my_stopwords:
			res = res + " " + word
	return res


def tokenize_and_stem(text):
	# first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
	tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
	filtered_tokens = []
	# filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
	for token in tokens:
		if re.search('[a-zA-Z]', token):
			filtered_tokens.append(token)
	stems = [stemmer.stem(t) for t in filtered_tokens]
	return stems

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

if __name__ == "__main__":
    main()