# 1. Reverse the digits of an integer
def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = int(str(n)[::-1])
    return sign * reversed_n

# 2. Recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 3. Function that returns the character that appears most frequently
from collections import Counter

def most_frequent_character(s):
    counter = Counter(s)
    most_common_char, _ = counter.most_common(1)[0]
    return most_common_char

# 4. Function to determine whether a given string is a pangram
import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

# 5. Function to check if the list contains two consecutive threes
def has_consecutive_threes(lst):
    for i in range(len(lst) - 1):
        if lst[i] == 3 and lst[i + 1] == 3:
            return True
    return False

# 6. Function to reverse the order of words in a sentence like Master Yoda
def yoda_speak(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

