"""
This code is written by Paras Bhatia
"""

with open('input.txt', 'r') as file_handle:
	data = list(i.rstrip() for i in file_handle)



def binary(target):
	min_ = 0
	max_ = 99
	while True:
		if (min_+max_)//2 == target:
			return "found : ", (min_ + max_)//2
		elif (min_ + max_)//2<target:
			min_ = (min_ + max_)//2 + 1
			print(min_)
		elif (min_ + max_)//2>target:
			max_ = (min_ + max_)//2
			print(max_)

#print(binary(98))

"""
Part 1
"""

def seatID(data):
	seat_plan = {} 		#creating a dictionary with boardingpass as key and [row, seatnumber] in values
	for boarding_pass in data:
		#calculating row number
		min_ = 0
		max_ = 127
		rng  = (min_, max_)
		for i in boarding_pass[:7]:
			if i == 'F':
				max_ = (min_ + max_)//2
				rng = (min_, max_)
			elif i == 'B':
				min_ = (min_ + max_)//2 + 1
				rng = (min_, max_)
			
			#adding to dictionary
		seat_plan[boarding_pass] = [rng[0]]

		#calculating seat number 
		min_seat = 0
		max_seat = 7
		rng_seat = (min_seat, max_seat)
		for j in boarding_pass[7:]:
			if j == 'L':
				max_seat = (min_seat + max_seat)//2
				rng_seat = (min_seat, max_seat)
			elif j == 'R':
				min_seat = (min_seat + max_seat)//2 +1
				rng_seat = (min_seat, max_seat)
		seat_plan[boarding_pass].append(rng_seat[0])

	seat_ID_list = [i[0]*8 + i[1] for i in seat_plan.values()]

	return seat_ID_list

print("Highest seat ID on boarding pass list : ", max(seatID(data)))

"""
Part 2
"""

lst = sorted(seatID(data))
for i in range(len(lst)-1):
	if lst[i+1] - lst[i] > 1:
		print("My missing seat ID : ", lst[i]+1)
