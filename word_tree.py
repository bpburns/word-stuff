from collections import Counter
import sys
import time
import json
from supertrie import *
from wordlist import WORD_LIST

newtree = Trie()
newtree.insert('doo')
newtree.insert('doodoo')
newtree.insert('doop')
newtree.insert('d')
newtree.insert('doo')
print(newtree.query(''))
print('chu' in WORD_LIST)
sys.exit(0)

print('Building the trie tree.')
tree = Trie()
for word in WORD_LIST:
    tree.insert(word)
timer1 = time.time()
for word in tree.query('chu'):
    print(word)
    time.sleep(1)
print(len(tree.query('chu')))
timer2 = time.time()
print(timer2 - timer1)

timer1 = time.time()
counter = 0
for word in WORD_LIST:
    if word.startswith('chu'):
        counter += 1
print(counter)
timer2 = time.time()
print(timer2 - timer1)
