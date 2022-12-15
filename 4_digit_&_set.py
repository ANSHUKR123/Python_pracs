
def get_digits(n):
    assert n >= 10, "Number should be >= 10"
    # return set(str(n))

    digits = set()
    str_num = str(n)
    for digit in str_num:
        digits.add(int(digit))
    return digits


n = int(input("Enter a number : "))
assert n > 0, "Number should be positive atleast"
print(f"Digits : {get_digits(n)}")
