product = []

while True:
    name = input('請輸入你的產品名稱:')

    if name == 'q':
        break
    price = input('請輸入你的價錢:')
    
    # 第一種寫法
    # detail =[]
    # detail.append(name)
    # detail.append(price)
    # product.append(detail)

    # 第二種寫法
    # detail=[name,price]
    # product.append(detail)

    # 第三種寫法
    product.append([name,price])

# print(product)

for p in product:
    # print(p)
    print('商品名稱:',p[0],'價格:',p[1])