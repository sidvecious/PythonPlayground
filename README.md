# Python Playground
-----------------------------

## tl;dr
This project is divided into 2 parts. 
The first part consists in a program able to request a page from Wikipedia, and search a target link in the html.
The second part consist in a program able to process through Natural Language news feeds, gathered using and api services. The target of processing is a graph outlining the most common words in the feeds.

Both parts where written in python 2.7

------------------------------
## wikipedia_link_automatic_search

based on Udacity tutorial: "Introduction to Python Programming"
https://classroom.udacity.com/courses/ud1110

------------------------------
## nltk_most_common_words

based on NLTK 3.2.5 documentation and newsapi.org
* https://www.nltk.org/
* https://newsapi.org/

The Project uses a Natural language Toolkit to find texts with references to a given word starting from a given date.
To do this, use the text found through newsapi.org and use a personal API key free of charge available to developers. since the key is personal, it is necessary to have one to run the program successfully.
if contacted I will give you the access key.
Since the program is able to recognize the 'tokens' of a sentence, I keept only the following tokens:
- NNP: 
- NNS: 
- NN: name
This choise was made to have 'clean' words to build the graph (no 'as', '...', 'i', 'a', ...)
The statistics is visible through a graph.


## requirement:
- ntlk
- requests
- Beautiful Soup





 






