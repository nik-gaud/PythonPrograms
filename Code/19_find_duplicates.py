def find_duplicates(numbers):
    seen = []
    duplicates = []
    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.append(num)
    return duplicates

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Duplicate elements:", find_duplicates(nums))