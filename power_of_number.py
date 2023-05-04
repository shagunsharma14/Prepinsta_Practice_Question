def power_is(num, power):
    if power < 1:
        return 1
    return num * power_is(num, power-1)

if __name__ == '__main__':
    num, power = input().split()
    print(power_is(int(num), int(power)))