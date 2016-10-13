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


# returns the next most probable word given a most recent word
def auto_complete(model, query):
	return model.retrieve_next(query)



# test = Markov()
# test.train_word("hello", "world")
# test.train_word("hello", "world")
# test.train_word("hello", "friend")
# test.train_word("hello", "friend")
# print(auto_complete(test, "hello"))

# test.train_set("hello friend my name is Sam Choi hello friend hello friend".split(" "))
# print(auto_complete(test, "hello"))

new_york = webtext.words('overheard.txt')
pirates = webtext.words('pirates.txt')

file_test = Markov()
file_test.train_set(pirates, 3000)
print(file_test.word_history['what'])
print(file_test.retrieve_next('what'))



