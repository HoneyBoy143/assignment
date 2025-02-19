def max1(numlist):
  max=numlist[0]
  for i in numlist:
    if i>max:
      max=i
  return max
a=[]
num=int(input("Asign num of element in list: "))
for i in range (num):
  num_in_list=int(input("Asign the element in list: "))
  a.append(num_in_list)
max=max1(a)
print(a)
print("the max value in list is: ",max)