from collections import Counter
import sys
import time
import json
from supertrie import *

with open('american-english-insane', 'r') as f:
    english_words = f.read().splitlines()

replacement_map = {
    'Å': 'A',
    'á': 'a', 
    'â': 'a', 
    'ä': 'a', 
    'å': 'a', 
    'ç': 'c', 
    'è': 'e', 
    'é': 'e', 
    'ê': 'e', 
    'í': 'i', 
    'ñ': 'n', 
    'ó': 'o', 
    'ô': 'o', 
    'ö': 'o', 
    'û': 'u', 
    'ü': 'u' 
}

# Remove words with punctuation
upper_alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alphas = upper_alphas.lower()
alpha_characters = set(list(upper_alphas))
alpha_characters.update(set(list(lower_alphas)))
english_words_pruned = set()
for word in english_words:

    # Normalize to ASCII-like words.
    for char in replacement_map.keys():
        if char in word:
            replacement = replacement_map[char]
            word = word.replace(char, replacement)

    charset = set(list(word))
    if "'" in charset:
        continue
    if not charset - alpha_characters and len(word) > 2:
        english_words_pruned.add(word.lower())

sorted_word_list = sorted(english_words_pruned)

for word in sorted_word_list:
    print(word)
sys.exit(0)

class node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.length = len(data)
        self.is_valid_word = data in english_words_pruned
    def print_tree(self):
        if self.length == 0:
            print('root')
        elif self.is_valid_word:
            print(self.length * ' ' + self.data)
        for child in self.children:
            child.print_tree()
    def insert(self, data):
        if data.startswith(self.data):
            if len(data) == self.length + 1:
                #print(f'New child "{data}"', 'belongs here')
                self.children.append(node(data))
            elif len(data) > self.length + 1:
                #print(f'"{data}" is too long to go here')
                for child in self.children:
                    if data.startswith(child.data):
                        #print(f'"{data}" belongs under {child.data}')
                        child.insert(data)
                        return
                self.insert(data[:-1])
                self.insert(data)
    def count(self):
        count = 0
        if self.is_valid_word:
            count += 1
        for child in self.children:
            count += child.count()
        return count
    def count_words(self, word):
        count = 0
        if not word.startswith(self.data):
            print(word, 'does not start with', self.data)
            return count
        else:
            if word == self.data:
                print(word, 'matches', self.data)
                print('There are', self.count(), 'words under', word)
                return self.count()
            print(word, 'does start with', self.data)
            for child in self.children:
                if word.startswith(child.data):
                    return child.count_words(word)
        return count


    def search(self, word):
        if self.is_valid_word and word == self.data:
            return True
        elif word.startswith(self.data):
            # Word is one of my children
            for child in self.children:
                if child.search(word):
                    return True
        else:
            return False



root = node('')
for word in sorted_word_list:
    root.insert(word)
timer1 = time.time()
print(root.count_words('chu'))
timer2 = time.time()
print(timer2 - timer1)

tree = Trie()
for word in sorted_word_list:
    tree.insert(word)
timer1 = time.time()
print(tree.query('chu'))
timer2 = time.time()
print(timer2 - timer1)

