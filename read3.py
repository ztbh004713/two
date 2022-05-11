data = []
con = 0
with open("reviews.txt" , "r") as f:
	for line in f:
		data.append(line)
		con += 1
		if con % 10000 == 0:
			print(len(data))
print("档案读取完毕，总共有" , len(data) , "笔资料。")
hg = 0
for a in data:
	hg += len(a)
print(hg / len(data))

new = []
for d in data:
	if len(d) < 500:
		new.append(d)
print(len(new))
print("筛选后一共有" , len(new) , "笔资料字节低于500。")

print(new[10])

so = ["我好帅" for c in data if "cool" in c]
print(so)
print(len(so))

ds = [len(xx) < 1000 for xx in data]
print(ds)
print(len(ds))