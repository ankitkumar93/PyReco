import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
import string
#strip any proper nouns (NNP) or plural proper nouns (NNPS) from a text
from nltk.tag import pos_tag
stopwords = nltk.corpus.stopwords.words('english')

####
from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel
from itertools import izip

def main():
    #parse_xml()
    test()


def parse_xml():
	from xml.dom import minidom
	xmldoc = minidom.parse('test.xml')
	itemlist = xmldoc.getElementsByTagName('row')
	text = GenerateBOW(itemlist[0].attributes['Body'].value)
	#text = strip_text_POS(text)
	text = text_processing2(text)
	

def strip_text_POS(str):
	tagged = pos_tag(str.split()) #use NLTK's part of speech tagger
	print tagged
	non_propernouns = [word for word,pos in tagged if pos != 'NNP' and pos != 'NNPS']
	#print non_propernouns

def text_processing(str):
	from gensim import corpora, models, similarities 

	#remove proper names
	#preprocess = [strip_proppers(doc) for doc in str]

	#tokenize
	tokenized_text = [tokenize_and_stem(text) for text in str]

	#remove stop words
	texts = [[word for word in text if word not in stopwords] for text in tokenized_text]

def text_processing2(str):
	from gensim import corpora, models, similarities
	texts = str.split()

	#create a Gensim dictionary from the texts
	dictionary = corpora.Dictionary([texts])

	#remove extremes (similar to the min/max df step used when creating the tf-idf matrix)
	#dictionary.filter_extremes(no_below=1, no_above=0.8)

	#convert the dictionary to a bag of words corpus for reference
	#corpus = [dictionary.doc2bow(text) for text in texts]
	
	corpus = dictionary.doc2bow(texts)
	#print corpus


	lda = models.LdaModel(corpus, num_topics=2, id2word=dictionary)
	lda.show_topics()
	# topics_matrix = lda.show_topics(formatted=False, num_words=20)
	# print topics_matrix
	# topics_matrix = np.array(topics_matrix)
	# topic_words = topics_matrix[:,:,1]
	# for i in topic_words:
	# 	print([str(word) for word in i])
	# 	print()
	print "done"


def GenerateBOW(str):
	stopwords = set(nltk.corpus.stopwords.words('english')) 
	sentence = ""
	#print stopwords

	for word in str.split():
		if word.lower() not in stopwords:
			#print word
			sentence=sentence + " " +  word.lower()
	return sentence


def test():
	documents = ["Human machine survey machine machine  machine interface for lab abc computer applications", "A survey of user opinion of computer system response time", "Graph minors A survey"]
	do(documents)

def do(documents):
	#remove common words and tokenize
	stoplist = set('for a of the and to in'.split())
	texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

	#remove words that appear only once
	# all_tokens = sum(texts, [])
	# tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
	# texts = [[word for word in text if word not in tokens_once] for text in texts]

	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]

	# I can print out the topics for LSA
	# lsi = models.LdaModel(corpus, id2word=dictionary, num_topics=5)
	# corpus_lsi = lsi[corpus]

	# for l,t in izip(corpus_lsi,corpus):
	# 	print l,"#",t
	# 	print
	# for top in lsi.print_topics(2):
	# 	print top

	# I can print out the documents and which is the most probable topics for each doc.
	lda = ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=1)
	print lda.show_topics()

	topics_matrix = lda.show_topics(formatted=False, num_words=2)
	print topics_matrix
	print np.array(topics_matrix)
	#topics_matrix = np.array(topics_matrix)
	#topic_words = topics_matrix[:,:,1]
	# for i in topic_words:
	# 	print([str(word) for word in i])
	# 	print()

	# for l,t in izip(corpus_lda,corpus):
 #  		print l,"#",t
	# print

	# # But I am unable to print out the topics, how should i do it?
	# for top in lda.print_topics(10):
 #  		print top

if __name__=="__main__":
    main()