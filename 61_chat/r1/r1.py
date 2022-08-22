

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
        return lines


def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        # print(line)
        new.append(person+':'+line)

    # for tmpnew in new:
    #     print(tmpnew)
    return new


def write_file(filename, lines):
    with open('r1/'+filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('r1/input.txt')
    # print(lines)
    lines = convert(lines)
    write_file('Output.txt', lines)

main()
