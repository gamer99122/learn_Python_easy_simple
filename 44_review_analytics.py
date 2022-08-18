from datetime import date


data=[]
count=0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count+=1
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取完了，總共有[',len(data),']筆資料')

int_leng=0
for d in data:
    int_leng += len(d)

print('平均留言長度 :',int_leng/len(data))






# 檔案連結:https://yottau-download.s3-ap-northeast-1.amazonaws.com/41f50f630cd4186a4ea7723d2c9e50a3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIKVP4DX3YDXF73WA%2F20220818%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Date=20220818T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-content-disposition=attachment%3B%20filename%3D%223-8%20%E4%B8%8B%E8%BC%89%E8%B3%87%E6%96%99%E6%AA%94.pdf%22&X-Amz-Signature=3ddee5a3f2ac8f3a7836ac28caf5494488869ec3c9d4b8fc910027169a9391d0