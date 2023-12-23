from map import Map
from _3b import max_in_tree

word_count = Map()

with open('words.txt', 'r') as text:
    words = text.read().split()
    
    for word in words:
        word_count.set(words.count(word), word)

word_count.display()
print(f"\n\nMost frequent word: {max_in_tree(word_count.root)}")
