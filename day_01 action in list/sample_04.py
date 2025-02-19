#find lowest value in list

b = [12, 23, 34, 45]
min_value = b[0]
for num in b:
  if num < min_value:  # Compare each number with the current minimum
    min_value = num
print(min_value)
