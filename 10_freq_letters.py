

'''
    frequency_table = {}
        - key is a character a-z
        - value is int no. of times we see it
'''

frequency_table = {}
sentence = input("Enter sentence\n")

for char in sentence:

    if char not in frequency_table:
        frequency_table[char] = 1  # add first time to table
    else:
        frequency_table[char] += 1  # increment its occurence

for char in frequency_table:
    print(f"{char} occured {frequency_table[char]} times")
