if __name__ == '__main__':
    num = input()
    sum = 0
    for _ in range(len(num)):
        r = int(num) % 10
        sum += r
        num = int(num) / 10
    print(sum)
