def reverse_number(number):
    reversed_num = 0
    num = abs(number)
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    if number < 0:
        return -reversed_num
    return reversed_num

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Reversed number:", reverse_number(num))
    