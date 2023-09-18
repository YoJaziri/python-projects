
from collections import Counter

liste = []
with open ('apache_logs.txt', 'r') as file:
    for x in file:
        liste.append(x.strip())
        

print(liste[0])

first_line = liste[0]


liste_2 = first_line.split()
print(liste_2)

first_line_status_code = liste_2[8]

print(first_line_status_code)


status_codes = []

for line in liste:
    liste_3 = line.split()
    code = liste_3[8]
    status_codes.append(code)
    
    
# print

status_200 = 0

for code in status_codes:
    if int(code) == 200:
        status_200 = status_200 +1
    
print(f'status_200 = {status_200}')

status_400 = 0

for code in status_codes:
    if int(code) == 400:
        status_400 = status_400 +1
    
print(f'status_400 = {status_400}')

print(len(status_codes))

status_counter = Counter(status_codes)

print(status_counter)



lines_with_404 = []

for line in liste:
    liste_4 = line.split()
    if int(liste_4[8]) == 404:
        lines_with_404.append(line)

print(lines_with_404[0])

print(lines_with_404[0].split())


        
names_resource_list = []

for line in lines_with_404:
    liste_5 = line.split()
    path = liste_5[6]
    names_resource_list.append(path)
    
print(names_resource_list[0])


print (Counter(names_resource_list).most_common(3))