"""
I took help to solve this problem from discussion forums. I was not able to solve it. So, tried understanding other people's code.
"""




data = {}
with open('input.txt', 'r') as file:
	for line in file.readlines():
		words = line.split()
		key = words[0] + ' ' + words[1]
		data[key] = {}
		for i, word in enumerate(words):
			if words[i].isnumeric():
				subKey = words[i + 1] + ' ' + words[i + 2]
				data[key][subKey] = int(word)


def containsTargetBag(targetName, insideBags):
	for child in insideBags:
		if child == targetName:
			return True
		if containsTargetBag(targetName, data[child]):
			return True
	return False


def countInsideBags(insideBags):
	if insideBags == {}:
		return 0
	total = 0
	for insideBagName in insideBags:
		total += ((countInsideBags(data[insideBagName]) + 1) * insideBags[insideBagName])
	return total


answer = []
targetName = 'shiny gold'
for bag in data:
	if containsTargetBag(targetName, data[bag]):
		answer.append(bag)


print(len(answer))
print(countInsideBags(data['shiny gold']))