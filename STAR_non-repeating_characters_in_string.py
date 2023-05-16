
if __name__ == '__main__':
    st = input()
    for i in st:
        count = 0
        for j in st:
            if i==j:
                count += 1
            if count > 1:
                break
        if count == 1:
            print(i, end = ' ')