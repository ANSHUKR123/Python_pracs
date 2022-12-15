
def isPalindrome(s):
    return s == s[::-1]


def replaceString(s):
    result = s
    vowels = "aeiou"
    for vowel in vowels:
        result = result.replace(vowel, "#")
    return result


while True:
    print("------String MENU-----")
    print("1. Length of string")
    print("2. Max of 3 strings")
    print("3. Replace vowels with '#'")
    print("4. Number of words in a string")
    print("5. Checking if string is a palindrome")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '6':
        print("Exiting program")
        break

    elif choice == '1':
        s = input("Enter your string: ")
        n = len(s)
        print(f"{s} has length {n}")

    elif choice == '2':
        s1 = input("Enter your string 1: ")
        s2 = input("Enter your string 2: ")
        s3 = input("Enter your string 3: ")
        max_str = max(s1, s2, s3)
        print(f"Max string is {max_str}")

    elif choice == '3':
        s = input("Enter your string to replace vowels in it : ")
        modified = replaceString(s)
        print(f"{s} is now {modified}")

    elif choice == '4':
        s = input("Enter the string: ")
        words = s.split()
        words_count = len(words)
        print(f"{s} has {words_count} words")

    elif choice == '5':
        s = input("Enter the string: ")
        if isPalindrome(s):
            print(f"{s} is a palindrome.")
        else:
            print(f"{s} is not a palindrome.")
    else:
        print("Make a valid choice")
