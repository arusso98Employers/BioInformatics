def main(input):
	count = 0
	i_val = 0
	c_list = []
	i_list = []
	r_list = []
	g_list = list(input)

	for i in g_list:
		if i == "C":
			count -=1
		elif i == "G":
			count +=1
		c_list.append(count)

	min = c_list[0]
	for i in c_list:
		if i < min:
			min = i
	for i in c_list:
		if i == min:
			r_list.append(i_val)
		i_val += 1

	r_list[:] = [x + 1 for x in r_list]
	print ' '.join(map(str, r_list))







f = open("input1.txt", "r")
input_str = f.read()
main(input_str)