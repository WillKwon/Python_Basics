'''
You need to have the file in the python working directory
'''

# Create a file object and you'll mess up with it
infile = open('read.txt','r')

lines = list(infile) # Read the entire file as list
print lines
infile.close() # Close file when done

# Once a file is "read off", it's gone
# So you need to open it again
infile = open('read.txt','r')

line1 = next(infile) # Reads until \n and cut
line2 = next(infile) # Reads from wherever finished 
print line1
print line2
lines = list(infile)
print lines
infile.close() # Close file when done

# Count lines in a file
infile = open('read.txt','r')

n_lines = 0
for line in infile:
    n_lines += 1
print n_lines
infile.close()


# Count characters in a file
infile = open('read.txt','r')

n_chars = 0
for line in infile:
    n_chars += len(line)
print n_chars
infile.close()





