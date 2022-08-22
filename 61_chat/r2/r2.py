def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0 
    allen_photo_count=0
    viki_photo_count=0    
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2]=='圖片':
                allen_photo_count+=1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2]=='圖片':
                viki_photo_count+=1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('allen 說了'+str(allen_word_count)+'字,傳了'+str(allen_sticker_count)+'個貼圖')
    print('viki 說了'+str(viki_word_count)+'字,傳了'+str(viki_sticker_count)+'個貼圖')
    print('allen 圖片:'+str(allen_photo_count))
    print('viki 圖片:'+str(viki_photo_count))

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)

main()
