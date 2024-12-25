# Question 4: Count Word Frequency in a Sentence
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("this is a test this is only a test"))