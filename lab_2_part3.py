# Lab 2, Part 3, Student Dataclass, John Cokins

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    college_id: str
    GPA: float
# dataclass makes input more readable in my opinion
# the string method has less readable output so lets customize it

    def __str__(self):
        return f'Name: {self.name}\nStudent ID: {self.college_id}\nGPA: {self.GPA}'

def main():
    # Checking we can print a student object formatted how we wanted
    john = Student('John', 'sj12939', 3.4)
    print(john)

    # Checking we can print or access the information by individual property
    sam = Student('Sam', 'ids9219', 3.5)
    print(sam.name)
    print(sam.college_id)
    print(sam.GPA)

main()