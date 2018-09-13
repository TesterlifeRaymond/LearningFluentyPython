"""
@File: ClassInstance
@Author: Ray
@Date: 2018-04-10 11:16:47
@Version: 1.0
"""
from json import dumps


class MakeResult:
    def __init__(self, *subject):
        self.make_result = {}
        for item in subject:
            self.make_result[item.subject] = item.__dict__

    def __repr__(self):
        return "<MakeResult({})>".format(
            self.make_result
        )


class Subject:
    def __init__(self, subject, user, score):
        self.subject = subject
        self.user = user
        self._score = score


if __name__ == "__main__":
    subject_chinese = Subject("语文", "麦子", "100")
    subject_math = Subject("数学", "麦子", "66")
    make = MakeResult(subject_chinese, subject_math)
    print(MakeResult(subject_math))
    print(make)
