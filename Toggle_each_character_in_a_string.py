if __name__ == '__main__':
    st = input()
    new_st = ''
    for i in st:
        if i.islower():
            new_st += i.upper()
        elif i.isupper():
            new_st += i.lower()
    print(new_st)