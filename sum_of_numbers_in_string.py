if __name__ == '__main__':
    st = input()
    st_sum = 0
    for i in st:
        if 48<=ord(i)<=57:
            st_sum += int(i)
    print(st_sum)