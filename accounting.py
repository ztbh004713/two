products = []
while True:
  name = input("請輸入商品名稱: ")
  if name == "exit":
    break
  price = input("請輸入商品價格: ")
  p =[]
  p.append(name)
  p.append(price)
  products.append(p)
print(products)