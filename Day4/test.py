x = ['eyr:1988', 'iyr:2015', 'ecl:gry', 'hgt:153in', 'pid:173cm', 'hcl:0c6261', 'byr:1966']
d = {}
for i in x:
	d[i.split(':')[0]] = i.split(':')[1]
print(d)