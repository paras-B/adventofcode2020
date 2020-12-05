"""
This code is written by Paras Bhatia
"""

def parseFile(filename):
	with open(filename, 'r') as file_handle:
		in_ = file_handle.readlines()
		data = list(i.rstrip() for i in in_)
	return data


def countTrees(list):
	count = 0
	start = 0
	for i in range(1, len(list)):
		row = data[i]
		start = (start+3)%len(row)
		if row[start]=='#':
			count+=1
	return count

if __name__ == '__main__':
	data = parseFile('input.txt')
	print(countTrees(data))