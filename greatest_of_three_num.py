if __name__ == '__main__':
    x, y, z = [int(x) for x in input("Enter three values: ").split()]
    max = x if x > y else y
    max = y if y > z else z
    print(max)


