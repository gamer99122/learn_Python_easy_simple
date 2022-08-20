from genericpath import isfile
import os

products49 = []

is_csv_file = False

# 判斷檔案是否存在
if os.path.isfile('products.csv'):
    print('檔案存在')
    is_csv_file = True
else:
    print('檔案不存在')


# 如果檔案有存在就讀檔案，如果沒有products.csv，直接讀檔會發生錯誤
if is_csv_file == True :
    # # 讀檔案
    with open('products.csv', 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products49.append([name, price])
    print(products49)

while True:
    name = input('請輸入你的產品名稱:')
    if name == 'q':
        break
    price = input('請輸入你的價錢:')
    products49.append([name, price])
print(products49)

for p in products49:
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in products49:
        f.write(p[0]+','+str(p[1])+'\n')

# 備註:
# while loop
# input
# list
# for loop
# print
