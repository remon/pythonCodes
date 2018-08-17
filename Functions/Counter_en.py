from collections import Counter

#@DimaAlmasri


#print top 3 counter

words = [
  'Dima', 'Mohammad', 'Randa', 'Dima', 'Randa', 'Sara', 'Saed', 'Dima',
  'Randa', 'eyes', 'marwa', 'Dima', 'ayman', 'Suha', 'Dima', 'Dana', 'Randa',
  'Dima', "Sara", 'Randa', 'Dima', 'Sara', 'Dima', 'Sara', 'Dima',
  'Saed', 'Saed', "Rasha", 'Dima'
]
word_counts = Counter(words)

print(word_counts.most_common(3))
print "____________________"
