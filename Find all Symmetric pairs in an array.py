if __name__ == '__main__':
    ls = []
    while True:
        x, y = input().split()
        if x.lower()==' q' or y.lower()=='q':
            break
        ls.append((x,y))
        set_is = set()
        for (x,y) in ls:
            set_is.add((x,y))
            if (y,x) in set_is:
                print(f'({x,y})')