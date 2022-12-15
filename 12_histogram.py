from matplotlib import pyplot as plt


def make_histogram(nums):
    plt.hist(nums)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.xlim(min(nums)-1, max(nums)+1)
    plt.title("Histogram")
    plt.show()


num_str = input("Enter space separated numbers to plot histogram\n")
data = num_str.split()
data = [int(i) for i in data]
make_histogram(data)
