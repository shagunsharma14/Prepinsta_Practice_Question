def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

low, high = map(int, input("Enter the range (low and high): ").split())
prime_numbers = [num for num in range(low, high + 1) if is_prime(num)]

print("Prime numbers in the given range:", prime_numbers)
