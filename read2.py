data = []                           
count = 0                           
with open("reviews.txt" , "r") as f:  
	for line in f:                    
		data.append(line)
		count += 1                  
		if count % 1000 == 0:       
			print(len(data))            
print("档案读取完毕，总共有" , len(data) , "笔资料。")                                                              
#影片教学：如何撰写留言平均长度
sum_len = 0                #要计算平均前一样先设置一个变数记录
for d in data:             #使用for回圈读取data清单并设立一个变数记录
	sum_len += len(d)      #在回圈中每执行一次，就将len（d）的长度累加在sum_len内
print(sum_len)             
print(sum_len / len(data))   #如果运算模式，已有了回圈记录下每一笔索引的长度后，在除上data清单的总数即可算出留言的平均数。
print("计算结果，留言的平均长度为：" , sum_len / len(data))
#影片教学：如何撰写清单的筛选
#重点撰写程式的困难点在于如何把问题逻辑使用正确语法写出来
c = []               #撰写一个空清单变数，用以装入筛选出来的资料
for e in data:       #使用for回圈将data清单的资料依序取出存放在变数e
	if len(e) < 100: #使用if判断式，判断取出的资料len（e）留言长度是否小于100 
		c.append(e)  #撰写清单新增函式.append()，将符合条件长度小于100的留言新增进 c清单中
print(len(c))        #在回圈架构外撰写 print(len(c))列印出已新增到c清单中，留言数小于100的总数
print("一共有" , len(c), "笔留言长度小于100。")
print(c[0])          #列印出c清单中 索引值0 的资料
print(c[1])
#另一种筛选的使用，使用字串作为筛选条件
j = []
for a in data:
	if "oh" in a:      #if后面承接的是 是非题（True，False），如果oh有在变数d内
		j.append(a)    #新增进j清单中
print("一共有" , len(j) ,"笔留言提到oh。")
print(j[0])

#影片教学 list comprehension（清单快写法）
j = [a for a in data if "oh" in a]    #进阶的写法，在python中较为不易被初学者学习，不太易懂


