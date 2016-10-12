import random

# Spell Check and Auto-Complete
# Author: Sam Choi

class Markov():
	def __init__(self, data=None):
		# keys = words, values = dictionary of all possible next words and count
		self.word_history = {}
		# keys = words, values = most likely next word
		self.next_word_map = {}

	def train_word(self, word, next_word):
		word_dict = self.word_history.setdefault(word, {next_word : 0})
		word_dict.setdefault(next_word, 0)
		word_dict[next_word] += 1
		self.update()

	def train_set(self, words):
		# implement for data input in form of text file
		return 0

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
	model.retrieve_next(query)

test = Markov()
test.train_word("hello", "world")
test.train_word("hello", "friend")
test.train_word("hello", "world")
print(test.retrieve_next("hello"))

test.train_word("hello", "friend")
test.train_word("hello", "friend")
test.train_word("hello", "friend")
print(test.retrieve_next("hello"))


