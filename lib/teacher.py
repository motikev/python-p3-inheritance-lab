#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        if self.knowledge:
            random_index = random.randint(0, len(self.knowledge) -1)

            return self.knowledge[random_index]
        else:
            return "I have no knowledge to teach."

knowledge_list = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

def test_teacher_knowledge():
    teacher = Teacher("My", "Teacher", knowledge_list)  # Provide knowledge_list here
    assert teacher.knowledge == knowledge_list

teacher = Teacher("John", "Doe", knowledge_list)

print(teacher.knowledge)