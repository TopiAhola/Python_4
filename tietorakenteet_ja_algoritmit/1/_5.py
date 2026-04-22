"""
Count vowels
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

For example, if s = 'hello', your program should print:

Number of vowels: 2

"""

s = input()

vowels = 'aeiouäöAEIOUÄÖ'
vowel_count :int = 0
for character in s:
    if character in vowels:
        vowel_count += 1

print(f'Number of vowels: {vowel_count}')