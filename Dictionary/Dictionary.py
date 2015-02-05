# {'key' : 'value'}

# This is how you create a dictionary
mydict = {'cat':'gato', 'dog':'perro'}

print mydict
print type(mydict)

# If you input a key then give you the associated value
print mydict['cat']
print mydict['dog']

# You can add elements
mydict['mouse'] = 'raton'
print mydict

# You can also delete an element
del mydict['dog']
print mydict

# Shows (key, value) pairs
print mydict.items()
for (english, spanish) in mydict.items():
    print (spanish, english)
    
# You get key value pairs
print list(mydict.items())

# You only get keys
print list(mydict)

# You can test if a key is present (not for the value)
print 'cat' in mydict










