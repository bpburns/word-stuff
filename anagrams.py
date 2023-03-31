from collections import Counter
import sys
import time

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
    if not charset - alpha_characters:
        english_words_pruned.add(word.lower())
    else:
        print(f'Skipping {word}')

letter_counter = Counter()
for word in english_words_pruned:
    letter_counter.update(list(word))

for letter, count in sorted(letter_counter.items()):
    print(letter, count)

for word in sorted(english_words_pruned):
    print(word)

english_words = ['hello', 'oh']

def return_anagrams(input_letters):
    anagrams = set()
    
    input_letters_counter = Counter(input_letters)
    
    for dictionary_word in english_words:
    
        # If the dictionary word contains letters that are not in the
        # input letters, then the dictionary word cannot be an anagram
        # of the input letters.
        
        if not set(dictionary_word) - set(input_letters):
            check_word = set()
            for letter, count in Counter(dictionary_word).items():
                if count <= input_letters_counter[letter]:
                    check_word.add(letter)
            if check_word == set(dictionary_word):
                anagrams.add(dictionary_word)
    anagrams -= {''}
    return(anagrams)
