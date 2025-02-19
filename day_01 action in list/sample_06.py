#calulate avg of list

z=[12,23,34,45]
sum=0
avg=0
for i in z:
  sum+=i
  avg=sum/len(z)
print(avg)