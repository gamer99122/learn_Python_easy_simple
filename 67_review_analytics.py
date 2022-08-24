import time
import progressbar

# 從44延伸

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
        # if count % 10000 == 0:
        #     print(len(data))
print('檔案讀取完了，總共有[', len(data), ']筆資料')

print(data[0])

# 文字計數
start_time = time.time()
wc = {}
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 100000:
        print(word, wc[word])
end_time = time.time()
print('花了', end_time-start_time, '秒')


while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過喔!')
