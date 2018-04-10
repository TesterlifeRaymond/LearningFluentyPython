"""
@File: NamedTule
@Author: Ray
@Date: 2018-03-15 17:41:14
@Version: 1.0
"""
from collections import namedtuple


Grade = namedtuple("Grade", ("score", "weight"))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subject = {}

    def subject(self, name):
        if name not in self._subject:
            self._subject[name] = Subject()
        return self._subject[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subject.values():
            total += subject.average_grade()
            count += 1
        return total / count


class GradeBook:
    def __init__(self):
        self.students = {}

    def student(self, name):
        if name not in self.students:
            self.students[name] = Student()
        return self.students[name]


if __name__ == "__main__":
    book = GradeBook()
    albert = book.student("Albert Eninstein")
    math = albert.subject('Math')
    math.report_grade(80, 0.10)
    print(math)
    print(albert.average_grade())
