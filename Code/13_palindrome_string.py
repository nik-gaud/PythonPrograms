def is_palindrome_string(text):
    cleaned = text.lower()
    reversed_text = ""
    for char in cleaned:
        reversed_text = char + reversed_text
    return cleaned == reversed_text

if __name__ == "__main__":
    text = input("Enter a string: ")
    if is_palindrome_string(text):
        print("Palindrome")
    else:
        print("Not Palindrome")
        