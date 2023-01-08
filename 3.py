#!/usr/bin/env python

def rotate(ls, x):
	return ls[x:] + ls[:x]

n = int(input('Enter the number of elements in the list '))
print('Enter the elements ')
ls = []
for i in range(n):
	ls.append(int(input()))

key = int(input('Enter the key to rotate the array by '))
print(rotate(ls, key))
