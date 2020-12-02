""" 
This code is written by Paras Bhatia
"""

with open('input.txt', 'r') as file_handle:
	in_ = file_handle.readlines()
	data = list(map(int, in_))


"""
Part 1
"""
def twoEntries(list):
	for i in list:
		if (2020-i) in list:
			return (2020-i)*i


"""
Part 2
"""

def threeEntries(list):
	for i in range(0, len(list)-2):
		for j in range(i+1,len(list)-1):
			for k in range(j+1, len(list)):
				if list[i]+list[j]+list[k] == 2020:
					return list[i]*list[j]*list[k]

