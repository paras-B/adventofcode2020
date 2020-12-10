"""
This code is written by Paras Bhatia
"""

import re
import collections


with open('input.txt', 'r') as file_handle:
	data = file_handle.read()[:]


codes_8 = ['byr', 'iyr', 'eyr',
		'hgt', 'hcl', 'ecl',
		'pid', 'cid']

codes_7 = ['byr', 'iyr', 'eyr',
		'hgt', 'hcl', 'ecl',
		'pid']

""" 
Part 1
"""
def validPassportsCount(input):
	pattern = re.compile(r'byr|iyr|eyr|hgt|hcl|ecl|pid|cid')
	passports = input.split('\n\n')
	total_passport = 0
	for passport in passports:
		batch = re.split(r'[\n]',passport)
		passport_as_a_string = "".join(batch)
		if sorted(list(pattern.findall(passport_as_a_string))) == sorted(codes_8) or \
			sorted(list(pattern.findall(passport_as_a_string))) == sorted(codes_7):
			total_passport+=1
	return total_passport

print(validPassportsCount(data))

"""
Part 2
"""

def validPassportsStrictCount(input):
	pattern = re.compile(r'byr|iyr|eyr|hgt|hcl|ecl|pid|cid')
	passports = input.split('\n\n')
	valid_passports = []
	total_strict_passport = 0
	for passport in passports:
		batch = re.split(r'[\n]',passport)
		passport_as_a_string = "".join(batch)
		if sorted(list(pattern.findall(passport_as_a_string))) == sorted(codes_8) or \
			sorted(list(pattern.findall(passport_as_a_string))) == sorted(codes_7):
			valid_passports.append(batch)

	for i in valid_passports:
		x = list((" ".join(i)).split())
		d={}
		for j in x:
			d[j.split(':')[0]] = j.split(':')[1]
		if 1920<=int(d['byr'])<=2002 and 2010<=int(d['iyr'])<=2020 and 2020<=int(d['eyr'])<=2030 and \
		re.match(r'^#[0-9a-f]{6}$',d['hcl']) and (d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and \
		re.match(r'^[0-9]{9}$',d['pid']) and re.match(r'\d+..',d['hgt'])  and (d['hgt'].endswith('cm') and 150<=int(d['hgt'][:-2])<=193 \
		or d['hgt'].endswith('in') and 59<=int(d['hgt'][:-2])<=76):
			total_strict_passport+=1
	return total_strict_passport
		


print(validPassportsStrictCount(data))






