# Question 1: Sum Numbers in a List
def sum_numbers(numbers):
    return sum(numbers)

print(sum_numbers([1, 2, 3, 4, 5]))


# Question 2: Print Even Numbers Between 1 and 20
for num in range(1, 21):
    if num % 2 == 0:
        print(num)


# Question 3: Find the Largest Number in a List
def find_largest(numbers):
    return max(numbers)

print(find_largest([3, 5, 7, 2, 8]))


# Question 4: Count Word Frequency in a Sentence
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("this is a test this is only a test"))