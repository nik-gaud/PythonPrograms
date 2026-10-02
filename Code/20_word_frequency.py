def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Word frequency:", word_frequency(sentence))