# Methode1
# list1 = [10, 21, 45, 66, 78]
# list2 = [10, 22, 46, 66, 78, 90]

# diff = []
# for elem in list1:
#     if elem not in list2:
#         diff.append(elem)

# for elem in list2:
#     if elem not in list1:
#         diff.append(elem)
        
# diff.sort()

# print(diff)


# Methode2
# list1 = [10, 21, 45, 66, 78]
# list2 = [10, 22, 46, 66, 78, 90]

# diff= set(list1).symmetric_difference(set(list2))
# diff= list(diff)
# diff.sort()

# print(diff)

#Methode3
list1 = [10, 21, 45, 66, 78]
list2 = [10, 22, 46, 66, 78, 90]

diff1 = set(list1) - set(list2)
diff2 = set(list2) - set(list1)
diff= list(diff1) + list(diff2)
diff.sort()




# Kann man sets von einander extrahieren aber nicht summieren?


print(diff)