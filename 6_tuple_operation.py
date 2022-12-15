

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)


# Print another tuple whose values are even numbers in the given tuple
l1 = list(t1)
l2 = [x for x in t1 if x % 2 == 0]
t3 = tuple(l2)
print(f"Even tuple : {t3}")


# Concatenate a tuple t2=(11,13,15) with t1
t2 = (11, 13, 15)
l1 = list(t1)
l2 = list(t2)
l1.extend(l2)
t1 = tuple(l1)
print(f"New t1 : {t1}")
