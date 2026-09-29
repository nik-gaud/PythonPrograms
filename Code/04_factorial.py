def calculate_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial is:", calculate_factorial(num))
    
