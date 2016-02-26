import sys
import nltk

def main():
    parse_xml()

def parse_xml():
	from xml.dom import minidom
	xmldoc = minidom.parse('test.xml')
	itemlist = xmldoc.getElementsByTagName('row')
	#print(len(itemlist))
	#print(itemlist[0].attributes['Body'].value)
	GenerateBOW(itemlist[0].attributes['Body'].value)
	

def GenerateBOW(str):
	stopwords = set(nltk.corpus.stopwords.words('english')) 
	sentence = ""
	#print stopwords

	for word in str.split():
		if word.lower() not in stopwords:
			#print word
			sentence=sentence + " " +  word.lower()
	#print sentence
	FilterSentence(sentence)

def FilterSentence(sentence):
	tokens = nltk.word_tokenize(sentence)
	ls = {'.' , ',' , '<', '>' , '/p' , 'p', '?' }
	newtokens = []
	for token in tokens:
		if token not in ls:
			newtokens.append(token)
	tagged = nltk.pos_tag(newtokens)
	print tagged
	print len(tagged)

if __name__=="__main__":
    main()