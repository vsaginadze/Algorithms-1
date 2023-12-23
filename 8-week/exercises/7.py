from map import Map

word_count = Map()

with open('words.txt', 'r') as text:
    words = text.read().split()
    
    for word in words:
        word_count.set(words.count(word), word)

word_count.display()

t = word_count.root
while t:
    if t.right:
        t = t.right
    else:
        print(f'Most occured word is -> "{t.value}" with {t.key} occurences')
        break
