#!/usr/bin/env python

def converter(s):
	ls = []
	for word in s.split():
		w = word[1:] + word[0] + 'ay'
		ls.append(w)
	print('Piglatin : ', ' '.join(ls))

	new_l = []
	for token in ls:
		w = token[-3] + token[:-3]
		new_l.append(w)
	print('Back : ', ' '.join(new_l))

converter(input('Enter a string '))
