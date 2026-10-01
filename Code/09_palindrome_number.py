def is_palindrome_number(number):
    original = number
    reversed_num = 0
    num = abs(number)
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return abs(original) == reversed_num

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_palindrome_number(num):
        print("Palindrome")
    else:
        print("Not Palindrome")