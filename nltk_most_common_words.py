#@ Autor: Lorenzo Olivier
#@ date: 02-22-2018

import requests
import nltk


# code of a Http rest Api for searching live articles from web
API_KEY = "" #<YOUR API KEY>

# set query and date from newsapi.org to get natural languages sample
query = "Apple"
date = "2018-02-25" 


def get_url(query, date):
	""""Find natural language strings in https://newsapi.org that 
		quote a certain word from a certain date"""

	if API_KEY == "": 
		raise Exception ("get_url: unable to find a apiKey, please insert your apiKey")
	if query == "" or date == "":
		raise Exception ("get_url: wrong input")
	return "https://newsapi.org/v2/everything?q=%s&from=%s&sortBy=popularity&apiKey=%s" % (query, date, API_KEY)


def get_data(query, date):
	'''Take data from the selected url for a certain keyword
	   starting from a certain date and converting it to json format '''
	# call the http address   
	url = get_url(query, date)
	# acquisition of the url
	response = requests.get(url)
	if response.status_code != 200:
		raise Exception("get_data: unable to retrive data")
	data = response.json()
	if data["status"] != "ok":
		raise Exception("get_data: json error")
	return data

def getWord(token):
	''' Select only the words that are matched to name tags '''
	if token[1] in ['NNP', 'NNS', 'NN']:
		return True 
	else:
		return False
def extractWord(word):
	'''Extract the name from the dataset'''
	return word[0]
	

try:
	data = get_data(query, date)
	print ("Got %d Results" % data["totalResults"])
	print "Calculating graph. Please wait..."

	words = []
	for article in data["articles"]:
		text = article["description"]
		#find in the python sourse code's words and convert it in Token
		tokens = nltk.word_tokenize(text)
		#create for every token a dataset with ('word', 'part of speech TAG')
		tagged = nltk.pos_tag(tokens)
		filteredTokens = filter(getWord, tagged)
		words += map(extractWord, filteredTokens)

	# produce a frequency distribuction of the words
	freq = nltk.FreqDist(words)
	# produce a graph of the frequency
	freq.plot(20, cumulative=False)
	# there is an unexpected invalid syntax error if I try
	# to print the data, it seems to like an encoding error.
except Exception as e: 
	print ("Error: %s" % e) 
	

