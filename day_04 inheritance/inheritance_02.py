#using while loop to input
class person:
    def __init__(AD, n, a):
        AD.Name = n
        AD.Age = a
    def display(AD):
        print("Name:", AD.Name)
        print("Age:", AD.Age)

class student(person):
    def __init__(AD, n, a, m):
        super().__init__(n, a)
        AD.mark = m
    def getMarks(AD):
        print("Marks:", AD.mark)

while True:
    Name=input("Enter the name or type 'exit' to leave: ")
    if Name== "exit":
      print("thank u ;)")
      break
    Age=int(input("Enter the Age: "))
    Marks=int(input("Enter your Marks: "))

    s=student(Name, Age, Marks)
    print("\n")
    s.display()
    s.getMarks()
    print("Ur Data as being store in Database...")
    print("\n")

