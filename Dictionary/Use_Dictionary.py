'''
Suppose we have a text of words and want to count which words appear how many times
'''

text = 'the cat sat on the mat'
words = text.split()
print words

record = {}
for word in words:
    if word in record:
        record[word] += 1
    else:
        record[word] = 1
        
print record
        
'''
Note that dictionaries are unordered, and you cannot predict how things will be Ordered
'''

# To print out record in a nicer way
items = list(record.items())
print items
print items.sort()

for (key, value) in items:
    print (key, value)