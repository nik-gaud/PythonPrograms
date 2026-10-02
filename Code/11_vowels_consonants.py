def count_vowels_consonants(text):
    vowels = 0
    consonants = 0
    for char in text.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    return vowels, consonants

if __name__ == "__main__":
    text = input("Enter a string: ")
    v, c = count_vowels_consonants(text)
    print("Vowels:", v)
    print("Consonants:", c)
    