import itertools

def count_letters(word):
    return len(word) - word.count(' ')

characters=raw_input("Enter the word:- ")
length = count_letters(characters)
count=0

combos = itertools.permutations(characters,length)
f = file("word_file.txt",'r').read()
for x in combos:	
	curr = ''.join(x)
	for w in f.split():
		if(curr[0]==w[0]):
			if(count_letters(w)==length):
				if(w==curr):
					count=count+1
					print str(count)+". "+curr
					break
		else:
			continue
