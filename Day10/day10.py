

with open('input.txt', 'r') as file_handle:
	data = list(int(j[0]) for j in [i.rstrip().split(' ') for i in file_handle])

data = sorted(data)

def partOne(data):
	ones_difference = []
	threes_difference = []
	outlet = 0
	built_in_device_rating = max(data) + 3
	while True:
		if len(ones_difference) + len(threes_difference)*3 == built_in_device_rating:
			return len(ones_difference)*len(threes_difference)
		else:
			for i in range(len(data)-1):
				if (data[i]-outlet)==1:
					ones_difference.append(data[i])
				if (data[i+1]-data[i])==3:
					threes_difference.append(data[i+1])
				elif ((data[i+1]-data[i])==1):
					ones_difference.append(data[i+1])
			threes_difference.append(built_in_device_rating)
	return len(ones_difference)*len(threes_difference)

print(partOne(data))

"""
Part 2
"""
paths = [1]
def numberofPaths(n):
	s = 0
	for i in range(n-1,-1,-1):
		print(i)
		if(data[n]-data[i]<=3):
			s+=paths[i]
		else: break
	return s

data = sorted(data)
data.append(data[-1]+3)
data = [0] + data
for i in range(1,len(data)):
	paths.append(numberofPaths(i))
	print("x: ", i, "data", data[i]," ", numberofPaths(i))

print(paths)
print(paths[-1])