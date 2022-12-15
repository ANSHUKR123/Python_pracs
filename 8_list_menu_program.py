
def isNums(arr):
    for element in arr:
        is_int = isinstance(element, int)
        is_float = isinstance(element, float)
        if not (is_int or is_float):
            return False
    return True


def isStrings(arr):
    for element in arr:
        if not isinstance(element, str):
            return False
    return True


def countOdds(arr):
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count


def find(arr, x):
    if x not in arr:
        return -1
    return arr.index(x)


def deleteElement(arr, x):
    if x not in arr:
        print(f"Can't remove {x} from list as it doesn't exist")
        return
    arr.remove(x)
    print(f"Removed {x} from list : {arr}")


def common_members(arr1, arr2):
    common_elements = []
    for element in arr1:
        if element in arr2 and element not in common_elements:
            common_elements.append(element)
    return common_elements


def input_list(arr, n):
    for i in range(n):
        element = eval(input(f"Enter {i+1}th element : "))
        arr.append(element)


my_list_1 = []
n = int(input("Enter number of elements : "))
assert n > 0, "n should be positive"
input_list(my_list_1, n)


if isNums(my_list_1):
    print("It is a numeric list")
    print(f"Odd values : {countOdds(my_list_1)}")

if isStrings(my_list_1):
    print("It is a string list")
    print(f"Largest string : {max(my_list_1)}")


print(f"Reversed list : {my_list_1[::-1]}")

x = eval(input("Enter element to be searched : "))
pos = find(my_list_1, x)

if pos == -1:
    print(f"{x} not found in list")
else:
    print(f"{x} found in list at {pos}")

if isNums(my_list_1) or isStrings(my_list_1):
    my_list_1.sort(reverse=True)
    print(f"List sorted in descending order : {my_list_1}")
else:
    print("Can't sort mixed list")

print("Finding common members")
l1 = []
n1 = int(input("Enter number of elements of list 1 : "))
input_list(l1, n1)

l2 = []
n2 = int(input("Enter number of elements of list 2 : "))
input_list(l2, n2)

commons = common_members(l1, l2)
print(f"Common members : {commons}")
