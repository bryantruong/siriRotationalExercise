"""
Bryan Truong
2/21/2020
Completed for Siri Rotational Engineer Program Interview(s)
"""
import numpy as np
from nltk.corpus import words
from collections import defaultdict

englishWords = words.words()
# All possible words that are 3 characters or greater
englishWords = [w for w in englishWords if len(w) >= 3]


class Trie(object):
    # Each "node" is a dictionary, with the key being the letter and the value being the neighboring children
    def __init__(self):
        self.children = defaultdict(Trie)  # Use default dict so that if the child doesn't exist, it is created
        self.complete = False  # Use a complete flag to save time on search

    def addWord(self, word):
        if not word:  # Base case (empty string case)
            self.complete = True
        else:
            # Recursively call addWord with the substring after the first letter
            self.children[word[0]].addWord(word[1:])

    def checkWord(self, word, prefixCheck = False):
        if not word:  # Base case (empty string case)
            return prefixCheck or self.complete  # If it was part of a valid word, self.complete will be True
        else:
            if word[0] in self.children:  # only do the check if the next letter is a child
                return self.chilrden[word[0]].checkWord(word[1:], prefixCheck)
            else:  # if the next letter is a child, the word isn't valid
                return False

    # Sanity check to see if trie is working correctly
    def showTrie(self, indent=0):
        for child in self.children:
            print(str(child), self.children[child].complete)
            # Print that child's children
            self.children[child].showTrie(indent=indent+1)







# Use a trie (prefix tree) to represent possible words
# def build_dictionary_trie(wordBank, node):
#     for word in wordBank:
#         if word[0] not in node:


if __name__ == '__main__':
    root = Trie()
    dictionary = ["and", "an", "ant", "cat"]
    for word in dictionary:
        root.addWord(word)
    root.showTrie()