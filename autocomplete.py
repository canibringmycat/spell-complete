import random
import nltk
from nltk.corpus import webtext
# Spell Check and Auto-Complete application
# Author: Sam Choi
# Auto-Complete:
# - Uses a stochastic model to predict the most likely next word
# - Implements a Markov Decision Process based on the last word used


class Markov():
	def __init__(self, data=None):
		# keys = words, values = dictionary of all possible next words and count
		self.word_history = {}
		# add data structure that keeps track of normalized probabilities

		# keys = words, values = most likely next word
		self.next_word_map = {}

	def train_word(self, word, next_word):
		word = word.lower()
		next_word = next_word.lower()
		word_dict = self.word_history.setdefault(word, {next_word : 0})
		word_dict.setdefault(next_word, 0)
		word_dict[next_word] += 1
		self.update()

	def train_set(self, words, domain=0):
		# implement for data input in form of text file
		# possible forms of words... .txt, string (sentence), etc
		if domain == 0:
			domain = len(words)-1
		for i in range(domain):
			self.train_word(words[i], words[i+1])

	def update(self):
		for word in self.word_history:
			most_probable = 0
			best_next = "..."
			for key, value in self.word_history[word].items():
				if value > most_probable:
					best_next = key
					most_probable = value
			self.next_word_map[word] = best_next

	def retrieve_next(self, word):
		return self.next_word_map.setdefault(word, "...")

	def probability(self, word, next_word):
		word = word.lower()
		next_word = next_word.lower()
		total = sum([val for val in self.word_history[word].values()])
		return 1.0*self.word_history[word][next_word]/total


# returns the next most probable word given a most recent word
def auto_complete(model, query):
	return model.retrieve_next(query)



# test = Markov()
# test.train_word("hello", "world")
# test.train_word("hello", "world")
# test.train_word("hello", "friend")
# test.train_word("goodbye", "friend")
# test.train_word("hello", "Sam")
# test.train_word("hello", "Sam")
# test.train_word("hello", "friend")
# print(auto_complete(test, "hello"))
# print(test.word_history)
# print(test.next_word_map)



# test.train_set("hello friend my name is Sam Choi hello friend hello friend".split(" "))
# print(auto_complete(test, "hello"))
# new_york = webtext.words('overheard.txt')

pirates = webtext.words('pirates.txt')
# comment everytime you use an NLTK function, explaining

# beautiful soup -> NYT, WSJ, etc

# GOAL: get v1.0 of python notebook
# make the slide/image of transition matrix vs. dictionary



file_test = Markov()
file_test.train_set(pirates, 2000)
print(file_test.word_history['jack'])
print(file_test.retrieve_next('jack'))
print(file_test.probability('jack', 'sparrow'))



# Next: spell checker with edit distance
# Look for best edit distance algorithm



# Alternate Ideas
# Matrix mapping prev and next values
# create transition matrix ... single run of preprocessing
# feature vector = current input
# two choices:
# 1. look for last word's values in P
# 2. 

# scrape text from blog/etc


# make a python notebook
# start by defining class/subroutines with explanation for each function
# after defining, allow for the class to input query and see probabilities
# show that you can store results
# look into NLTK API for bigrams
# lookup "pickle" for preprocessing in a python notebook





