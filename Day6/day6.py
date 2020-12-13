"""
This code is written by Paras Bhatia
"""

import re

with open('input.txt', 'r') as file_handle:
	data = file_handle.read()[:]


"""
Part 1 & 2
"""

def yesCounts(in_):
	formatted_data = in_.split('\n\n')
	count_anyone = 0
	count_everyone = 0
	for i in formatted_data:
		questions = ""
		group = re.split(r'[\n]', i)
		questions += ''.join(group)
		count_anyone += len(set(questions))
		
		#calculating count for everyone answered the question
		
		count_everyone += len(set.intersection(*map(set, group)))
	return count_anyone, count_everyone

print(yesCounts(data))