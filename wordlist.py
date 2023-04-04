from collections import Counter
import time
import json
from supertrie import Trie

WORD_FILE = 'american-english-insane'
print(f'Reading word file {WORD_FILE}')
with open(WORD_FILE, 'r') as f:
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
print('Normalizing word list.')
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

print('Sorting word list.')
sorted_word_list = sorted(english_words_pruned)

WORD_LIST = sorted_word_list

print('Building word trie.')
WORD_TRIE = Trie()
for word in WORD_LIST:
    WORD_TRIE.insert(word)

print('Building word set')
WORD_SET = set()
for word in WORD_LIST:
    WORD_SET.add(word)
