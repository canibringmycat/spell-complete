import random

# Spell Check and Auto-Complete
# Author: Sam Choi

class Markov():
	def __init__(self):
		# keys = words, values = dictionary of all possible next words and count
		self.word_history = {}
		# keys = words, values = most likely next word
		self.next_word_map = {}

	def train_word(self, word, next_word):
		word_dict = self.word_history.setdefault(word, {next_word : 0})
		word_dict.setdefault(next_word, 0)
		word_dict[next_word] += 1

	def train_set(self, words):
		# implement for data input in form of text file
		return 0

	def retrieve_next(self, word):
		return self.next_word_map.setdefault(word, "...")


# returns the next most probable word given a most recent word
def auto_complete(model, query):
	model.retrieve_next(query)




