class Student:
    school="Somerville"  # creating a static variable for the class Student

    def __init__(self,roll,age):
        self.roll = roll
        self.age = age


rohith = Student(1234, 20)
print(Student.school)
print(rohith.age)
print(rohith.roll)

# for second student
rohan = Student(5678, 21)
print(Student.school)
print(rohan.roll)
print(rohan.school)
