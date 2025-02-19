class student:
    def __init__(ad,name,age):
      ad.name = name
      ad.age = age
    def display(ad):
      print(ad.name, ad.age)

s1=student("Abhimanyu", 19)
s1.display()
s2=student("Suyash", 18)
s2.display()