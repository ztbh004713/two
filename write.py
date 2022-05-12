#字串可以做运算（+ , *) 无法（- ，/）
products = []                             
while True:                              
    name = input("請輸入商品名稱: ")        
    if name == "exit":                     
        break                               
    price = input("請輸入商品價格: ") 
    price = int(price)                        #再输入价格的时候，可将其型态转换为整数
    sugar = input("请输入商品糖分: ")
    capacity = input("请输入商品容量: ")       
    products.append([name , price , sugar , capacity])                       
print(products) 

for p in products:
    print(p[0] , "的价格是：" , p[1] , "元 ," , "糖分：" , "," , p[2] , "商品的容量为：" , p[3] , "。")


with open("write.csv" , "w") as f:    #撰写制式公式开启档案，"r" 读取档案、"w" 写入档案、 as 当做 f 变数名称
	for p in products:                   #for 回圈 将products[]清单中的资讯 一笔一笔取出 变数为 p
		f.write(p[0] + "," + p[1] + "," + str(p[2]) + "," + p[3] + "\n")    
#如已价格转换为整数时，则需记得将该栏位p[2] 撰写为：str(p[2])，其原因为 字串仅能跟字串做 +的运算，中间掺杂int()则无法运行。                       
#write 开启的档案进行写入的动作
#p[0] 为字串，将f.write()中的字串进行+的运算  \n 换行功能
#with open("write.csv"   csv档:Comma-Separated Values,也稱為字元分隔值,檔案以純文字形式儲存表格資料（數字和文字）。
