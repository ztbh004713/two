#products = []                             制定一个空清单
#while True:                               while True 让回圈可以重复执行 
#  name = input("請輸入商品名稱: ")         设定一个变数，并使用input 给予使用者填写
#  if name == "exit":                      并撰写一个条件来终止程式继续执行
#    break                                 终止回圈
#  price = input("請輸入商品價格: ")        在while回圈内，可撰写多个条件
#  p =[]                                   建置一个空清单，可将回圈内的多个条件写入清单中
#  p.append(name)                          .append(name) 将使用者填写的条件装入 while回圈中建立的清单中
#  p.append(price)                         .append(price) 将使用者填写的条件装入 while回圈中建立的清单中
#  products.append(p)                      再将p清单放入最早设置的products清单中 
#print(products)                           最后印出清单 （products[]清单中 会印出p「」清单中的name，price的资讯
#----------------------------------------------------------------------------------------------------------
#上方程式码再最后要写入p[]清单中时，可以进阶写法
#name = input("請輸入商品名稱: ")
#price = input("請輸入商品價格: ") 
#p =[]                            原先建立一个清单用来装入 使用者填入的资讯                                
#p.append(name)                   再将使用者填入的资讯新增进入p[]清单       
#p.append(price)                  
#影片教学进阶写法，可以减少写的行数把这三行程式撰写为一行
#p = [name , price]  

#  p = [name , price]                                   
#  products.append(p)                       
#print(products) 

#最进阶的写法
#products.append([name , price])

products = []                             
while True:                              
    name = input("請輸入商品名稱: ")        
    if name == "exit":                     
        break                               
    price = input("請輸入商品價格: ") 
    sugar = input("请输入商品糖分: ")
    capacity = input("请输入商品容量： ")       
    products.append([name , price , sugar , capacity])                       
print(products) 

for p in products:
    print(p[0] , "的价格是：" , p[1] , "元 ," , "糖分：" , p[2] , "商品的容量为：" , p[3] , "。")
#撰写for回圈 将products[]清单的资讯 列印出来。