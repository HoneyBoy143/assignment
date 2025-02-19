def reverse_list(list):
    for i in range(len(list)//2):
        list[i], list[-i-1] = list[-i-1], list[i]
    return list
num=[]
n=int(input("Asign num of element in list: "))
for i in range(n):
    num_in_list=int(input("Asign the element in list: "))
    num.append(num_in_list)
print(num)
print(reverse_list(num))