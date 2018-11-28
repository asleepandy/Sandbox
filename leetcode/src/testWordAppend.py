"""
練習題目 by 小琳
"""

import sys

def getBlankArray(count, number):
	array = []
	for i in range(0, number):
		if i == 0:
			array.append(count/number + count%number)
		else:
			array.append(count/number)
	return array

def aligned(string, maxWidth):
	string_array = string.split()
	sting_count = 0
	result_string = ""
	blank_array = []
	blank_count = 0
	# get only string count
	for s in string_array:
		sting_count += len(s)

	blank_count = (maxWidth - sting_count)
	# add blank to string
	if len(string_array) == 1:
		result_string = string_array[0] + " " * blank_count
	else:
		blank_array = getBlankArray(blank_count, len(string_array) - 1)
		for i in range(len(string_array)):
			if i < len(blank_array):
				result_string = result_string + string_array[i] + " " * blank_array[i]
			else:
				result_string = result_string + string_array[i]
	return result_string # end word_array_print 

def word_array_print(array):
	result_string = "[\n"
	for a in array:
		result_string = result_string + "\"" + a + "\"\n"
	result_string = result_string + "]\n"
	return result_string # end word_array_print 

def word_append(words, maxWidth):
	s = ""
	p = []
	for w in words:
		if (len(s) + len(w) + 1) > maxWidth:
			p.append(aligned(s, maxWidth))
			s = w
		else:
			if len(s) > 0:
				s = s + " " + w
			else:
				s = w
	p.append(aligned(s, maxWidth))
	return word_array_print(p) # end word_append

def main():
	source_file_name = sys.argv[1] if len(sys.argv) > 1 else "loremIpsum.txt"
	maxWidth =  int(float(sys.argv[2]))  if len(sys.argv) > 2 else 16
	
	source_file = open(source_file_name)
	target_file = open("targetFile.txt", "w")
	
	array = source_file.read().split()
	result = word_append(array, maxWidth)

	print result
	target_file.write(result)

	source_file.close()
	target_file.close()
	pass

main()

