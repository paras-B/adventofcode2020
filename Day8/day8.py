
with open('input.txt', 'r') as file_handle:
	instruction_set =  list([j[0], int(j[1])] for j in [i.rstrip().split(' ') for i in file_handle])



"""
Part 1
"""

 

def accumulatorValue(data):
	history = []
	idx = 0
	accumulator = False
	terminated = False
	while True:
		if idx>=len(instruction_set):
			terminated = True
			return accumulator , terminated

		instruct, arg = instruction_set[idx]
		
		if idx in history:
			return accumulator, terminated
		history.append(idx)

		if instruct == 'nop':
			idx+=1
		elif instruct == 'acc':
			accumulator += arg
			idx+=1
		elif instruct == 'jmp':
			idx += arg


"""
Part 2
"""

def changeInstruction(instruct):
	return 'jmp' if instruct=='nop' else 'nop'


def fixBootCode(data):
	global accumulator
	for idx, turn in enumerate(data):
		if turn[0]=='nop' or turn[0]=='jmp':
			prev = turn[0]
			instruction_set[idx][0]=changeInstruction(turn[0])
			accumulator, terminated =  accumulatorValue(instruction_set)
			if terminated:
				return accumulator
			instruction_set[idx][0]=prev

print(accumulatorValue(instruction_set)[0])

print(fixBootCode(instruction_set))