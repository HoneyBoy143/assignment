def descending_list(numlist):
    for i in range(len(numlist)-1):
        for j in range(i+1, len(numlist)):
            if numlist[i] < numlist[j]:
                numlist[i], numlist[j] = numlist[j], numlist[i]
    return numlist

a = []
num = int(input("Assign number of elements in list: "))
for i in range(num):
    num_in_list = int(input("Assign the element in list: "))
    a.append(num_in_list)

print(descending_list(a))