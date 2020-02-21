"""
Bryan Truong
2/21/2020
Completed for Siri Rotational Engineer Program Interview(s)
"""
import numpy as np
from nltk.corpus import words

english_words = words.words()

# If you want to remove stop words
english_words = [w for w in english_words if len(w) >= 3]


if __name__ == '__main__':
    print("Testing")
