array = [1,2,3,4,1,23]

dublicate = []

for i in array:
    if i not in dublicate:
        dublicate.append(i)
        
print(dublicate)