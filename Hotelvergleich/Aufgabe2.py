list1 = [10, 21, 45, 66, 78]
list2 = [10, 22, 46, 66, 78, 90]

common_values = set(list1).intersection(list2)
common_values = list(common_values)
common_values.sort()

print(common_values)