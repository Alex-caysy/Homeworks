

class MyClass:
    def __init__(self, attr):
        self.attr = attr

    def attr_plus_two(self, number):
        return self.attr + number + 2


def func_summ(a, b):
    return a + b


my_obj = MyClass(123)
sum = func_summ(2, 3)
