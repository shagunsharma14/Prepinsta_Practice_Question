if __name__ == '__main__':
    num = input()
    rev_num = ""
    for _ in num:
        r = int(num)%10
        rev_num += str(r)
        num = int(num)/10
    print(rev_num)

    