def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("List without duplicates:", remove_duplicates(nums))