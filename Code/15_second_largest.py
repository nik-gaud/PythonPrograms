def second_largest(numbers):
    unique_sorted = sorted(set(numbers), reverse=True)
    return unique_sorted[1]

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Second largest:", second_largest(nums))