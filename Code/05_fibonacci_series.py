def generate_fibonacci(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    num = int(input("Enter number of terms: "))
    print("Fibonacci series:", generate_fibonacci(num))
    