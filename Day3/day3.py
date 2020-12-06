"""
This code is written by Paras Bhatia
"""

def parseFile(filename):
	with open(filename, 'r') as file_handle:
		in_ = file_handle.readlines()
		data = list(i.rstrip() for i in in_)
	return data

"""
Part 1
"""

def countTrees(list, dc, dr):
	score = 0
	r=0
	c=0
	while r+1<len(list):
		c+=dc
		r+=dr
		print(c, r)
		if list[r][c%len(list[r])]=='#':
			score+=1
	return score

""" 
Part 2
"""
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

if __name__ == '__main__':
	data = parseFile('input.txt')
	print(countTrees(data, 3,1))

	ans = 1
	for (dc,dr) in slopes:
		ans*=countTrees(data, dc, dr)
	print(ans)