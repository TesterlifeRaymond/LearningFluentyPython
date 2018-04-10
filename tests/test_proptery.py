"""
@File: test_proptery
@Author: Ray
@Date: 2018-02-02 15:59:13
@Version: 1.0
"""


class TProperty(object):
    """ doc_string """
    def __init__(self, args):
        """
        
        @param : args
        @return: TODO
        """
        self.args = args

    @property
    def get_args(self):
        return self.args


if __name__ == "__main__":
    t = TProperty("Ray")
    print(t.get_args)
        
