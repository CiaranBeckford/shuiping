from dragonmapper import hanzi

def chinese_str(input):
	new_str = list()
	for i in input:
		if hanzi.has_chinese(i) == True:
			new_str.append(i)
	output = ''.join(new_str)
	return output
