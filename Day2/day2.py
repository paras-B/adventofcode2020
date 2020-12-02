"""
This code is written by Paras Bhatia
"""

import re

with open('input.txt', 'r') as file_handle:
	in_ = file_handle.readlines()
	data = list(i.rstrip() for i in in_)

"""
Part 1
"""
pattern1 = re.compile(r'(\d+)(-)(\d+)')
pattern2 = re.compile(r'[a-z]')

def validPasswordCount(list):
	total_count = 0
	for i in range(len(data)):
		r = data[i].split(':')
		min_ = int(pattern1.search(r[0]).group(1))
		max_ = int(pattern1.search(r[0]).group(3))
		alpha = pattern2.search(r[0]).group(0)
		alpha_count = r[1].count(alpha)
		if min_<=alpha_count<=max_:
			total_count+=1
	return total_count		

"""
Part 2
"""

def tobogganPolicy(list):
	total_count = 0
	for i in range(len(data)):
		r = data[i].split(':')
		pos_1 = int(pattern1.search(r[0]).group(1))
		pos_2 = int(pattern1.search(r[0]).group(3))
		alpha = pattern2.search(r[0]).group(0)
		rule1 = [r[1][pos_1]==alpha,
				r[1][pos_2]!=alpha]
		rule2 = [r[1][pos_1]!=alpha,
				r[1][pos_2]==alpha]
		if all(rule1) or all(rule2):
			total_count+=1
	return total_count

print(tobogganPolicy(data))
