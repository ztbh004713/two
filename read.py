data = []
with open("money.txt" , "r") as f:
	for line in f:
		data.append(line.strip())
print(data)
print(len(data))