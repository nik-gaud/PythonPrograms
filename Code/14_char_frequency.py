def char_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1
    return freq

if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Character frequency:", char_frequency(text))
    