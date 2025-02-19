class office:
  def __init__(AD,name,id,age,salary):
    AD.name=name
    AD.id=id
    AD.age=age
    AD.salary=salary

def display(AD):
  print("Name:",AD.name)
  print("ID:",AD.id)
  print("Age:",AD.age)
  print("Salary:",AD.salary)

while True:
  name=input("enter the name or exit the loop: ")
  if name=="exit":
    break
  id=int(input("enter the id: "))
  age=int(input("enter the age: "))
  salary=int(input("enter the salary: "))

  employee=office(name,id,age,salary)
  display(employee)