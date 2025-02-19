class person:
  def __init__(AD,n,a):
    AD.Name=n
    AD.Age=a
  def display(AD):
    print("Name:",AD.Name)
    print("Age:",AD.Age)
class student(person):
  def __init__(AD, n, a,m):
    super().__init__(n, a)
    AD.mark=m
  def getMarks(AD):
    print("Marks:",AD.mark)

s1=student("Abhimanyu",19,90)
s1.display()
s1.getMarks()
print("\n")

s2=student("Suyash",18,80)
s2.display()
s2.getMarks()
print("\n")

s3=student("Pooja",18,89)
s3.display()
s3.getMarks()
print("\n")

s4=student("Saniya",18,85)
s4.display()
s4.getMarks()
print("\n")