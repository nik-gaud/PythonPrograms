def check_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def primes_in_range(start, end):
    result = []
    for num in range(start, end + 1):
        if check_prime(num):
            result.append(num)
    return result

if __name__ == "__main__":
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print("Prime numbers:", primes_in_range(start, end))
    