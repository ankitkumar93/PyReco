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



#DATASET_FILE = 'dataset/yelp_dataset_challenge_academic_dataset'
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
REVIEWS_DATABASE = "sopyro"
TAGS_DATABASE = ""
REVIEWS_COLLECTION = "questions"

questions_collection = MongoClient(MONGO_CONNECTION_STRING)[REVIEWS_DATABASE][REVIEWS_COLLECTION]
print("connection done")
#questions_collection = MongoClient(MONGO_CONNECTION_STRING)[sopyro][questions]
question_cursor = questions_collection.find()
#print question_cursor
questionCount = question_cursor.count()
print(questionCount)
question_cursor.batch_size(50000)

# load nltk's English stopwords as variable called 'stopwords'
stopwords = nltk.corpus.stopwords.words('english')
stopFile = open("stopwords.txt", "r")
stopW = stopFile.read()
my_stopwords = stopW.split(", ")

# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

def main():

	synopses = []
	Id = []
	title = []
	tags = []
	for questions in question_cursor:
		synopses.append(questions["Body"])
		Id.append(questions["Id"])
		#title.append(questions["Title"])
		synopses.append(questions["Title"])
		tags.append(questions["Tags"])


	#use extend so it's a big flat list of vocab
	totalvocab_stemmed = []
	totalvocab_tokenized = []
	print("in main")
	for i in synopses:
		i = text_preprocess(i)
		allwords_stemmed = tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
		totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list

		allwords_tokenized = tokenize_only(i)
		totalvocab_tokenized.extend(allwords_tokenized)

	vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
	#ocab_frame = pd.DataFrame({'words': totalvocab_tokenized})
	print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
	print(vocab_frame.head())
	print()

	from sklearn.feature_extraction.text import TfidfVectorizer

	#define vectorizer parameters
	tfidf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=200000,
		min_df=0.2, stop_words='english',
		use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))
	
	tfidf_matrix = tfidf_vectorizer.fit_transform(synopses) #fit the vectorizer to synopses
	print(tfidf_matrix.shape)

	terms = tfidf_vectorizer.get_feature_names()

	from sklearn.metrics.pairwise import cosine_similarity
	dist = 1 - cosine_similarity(tfidf_matrix)
	print
	print
	
	from sklearn.cluster import KMeans
	num_clusters = 20
	km = KMeans(n_clusters=num_clusters)
	km.fit(tfidf_matrix)
	clusters = km.labels_.tolist()

	from sklearn.externals import joblib

	#uncomment the below to save your model 
	#since I've already run my model I am loading from the pickle
	joblib.dump(km,  'doc_cluster.pkl')
	km = joblib.load('doc_cluster.pkl')
	clusters = km.labels_.tolist()

	#posts = {'Title': title, "Id": Id, 'synopsis': synopses, 'cluster': clusters}
	posts = {"Id": Id, 'synopsis': synopses, 'cluster': clusters}
	#frame = pd.DataFrame(posts, index = [clusters] , columns = ['Title', 'Id', 'cluster'])
	frame = pd.DataFrame(posts, index = [clusters] , columns = ['Id', 'cluster'])
	print(frame['cluster'].value_counts()) #number of films per cluster (clusters from 0 to 4)

	
	
	print("Top terms per cluster:")
	print()
	#sort cluster centers by proximity to centroid
	order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

	for i in range(num_clusters):
		print("Cluster %d words:" % i, end='')
		
		for ind in order_centroids[i, :]: #replace 6 with n words per cluster
			print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')

		print() #add whitespace
		print() #add whitespace

		print("Cluster %d ids:" % i, end='')
		for id in frame.ix[i]['Id'].values.tolist():
			print(' %s,' % id, end='  ')

		print() #add whitespace
		print() #add whitespace
    
	print()
	print()


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