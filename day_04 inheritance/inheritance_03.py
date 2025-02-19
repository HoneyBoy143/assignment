#calulate net cgpa
class person:
    def __init__(AD, n, a):
        AD.Name = n
        AD.Age = a
    def display(AD):
        print("Name:", AD.Name)
        print("Age:", AD.Age)

class student(person):
    def __init__(AD, n, a, scgpa1, scgpa2):
        super().__init__(n, a)
        AD.scgpa1 = scgpa1
        AD.scgpa2 = scgpa2
    def getMarks(AD):
        print("SCGPA1:", AD.scgpa1)
        print("SCGPA2:", AD.scgpa2)
    def calculateCGPA(AD):
        cgpa = (AD.scgpa1 + AD.scgpa2) / 2
        return cgpa

while True:
    Name = input("Enter the name or type 'exit' to leave: ")
    if Name == "exit":
        print("Thank you ;)")
        break
    Age = int(input("Enter the Age: "))
    SCGPA1 = float(input("Enter your SCGPA1: "))
    SCGPA2 = float(input("Enter your SCGPA2: "))

    s = student(Name, Age, SCGPA1, SCGPA2)
    print("\n")
    s.display()
    s.getMarks()
    cgpa = s.calculateCGPA()
    print("CGPA:", cgpa)
    print("Ur Data as being store in Database...")
    print("\n")