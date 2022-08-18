from operator import truediv
import random

# 開始數值
int_star = input('請輸入亂數起始值:')
int_star=int(int_star)

# 結束數值
int_end = input('請輸入亂數結束值:')
int_end=int(int_end)

# 亂數
int_rand = random.randint(int_star,int_end)

# 猜第幾次提示字串
str_msg=''

# 猜底幾次
count = 0
while True:
    
    count+=1
    num=input('請猜數字:')
    num=int(num)

    str_msg='這是你猜的第[',count,']次數'
    if num==int_rand:
        print('恭喜你猜對了!!!')
        break
    elif num > int_rand :
        print('你的數字太大了，可以小一點')
    elif num < int_rand :
        print('你的數字太小了，可以大一點')
    print(str_msg)
    print('')






