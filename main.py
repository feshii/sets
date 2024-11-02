s1 = {1, 45, 2, 55, 3, 64, 4, 12}
s2 = {2, 23, 4.5, 7, 67, 30, 99, 12}
print(s1.intersection(s2))  # {2, 12}
print(s1.union(s2))  # {1, 2, 3, 4, 4.5, 7, 12, 45, 55, 64, 67, 99, 23, 30}
print(s1.difference(s2))  # {64, 1, 3, 45, 55}
print(s2.difference(s1))  # {99, 67, 4.5, 7, 23, 30}
print(s1.symmetric_difference(s2))  # {64, 1, 3, 45, 55, 4.5, 7, 67, 99, 23, 30}