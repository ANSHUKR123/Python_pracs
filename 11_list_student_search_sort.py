
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i

        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr


def linear_search(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1


def isSort(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def binary_search(arr, x):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def input_array(arr, n):
    for i in range(n):
        element = input(f"Enter {i+1}th student : ")
        arr.append(element)


n = int(input("Enter number of students : "))
assert n > 0, "n should be greater than zero"
students = []
input_array(students, n)

while True:
    print("---------MENU---------")
    print("1.Linear Search")
    print("2.Binary Search")
    print("3.Bubble Sort")
    print("4.Insertion Sort")
    print("5.Selection Sort")
    print("6.Exit")
    choice = int(input("Enter your choice : "))

    if choice == 6:
        print("Exiting program")
        break

    elif choice == 1:
        student = input("Enter student name to be searched : ")
        pos = linear_search(students, student)
        if pos == -1:
            print(f"{student} not found")
        else:
            print(f"{student} found at {pos}")
    elif choice == 2:

        if not isSort(students):
            print("Can't perform a binary search on unsorted array")
            continue

        student = input("Enter student name to be searched : ")
        pos = binary_search(students, student)
        if pos == -1:
            print(f"{student} not found")
        else:
            print(f"{student} found at {pos}")
    elif choice == 3:
        bubble_sort(students)
        print(f"Bubble Sorted : {students}")
    elif choice == 4:
        insertion_sort(students)
        print(f"Insertion Sorted : {students}")
    elif choice == 5:
        selection_sort(students)
        print(f"Selection Sorted : {students}")
    else:
        print("Make a valid choice")
