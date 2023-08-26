#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, knowledge):
        self.knowledge.append(knowledge)

# Example usage:
student = Student("Alice", "Smith")
student.learn("Python programming")
student.learn("Data structures")
print(student.knowledge)  # Output: ['Python programming', 'Data structures']