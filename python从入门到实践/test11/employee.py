class Employee():
    def __init__(self, last_name, first_name, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.salary = salary

    def give_raise(self, rise=5000):
        self.salary += rise


import unittest  # pytest


# @pytest.mark.pamametrize("rise,expected",
#                          [(None, 15000),
#                           (10000, 20000),
#                           ])
class TestRaise(unittest.TestCase):
    def setUp(self):
        self.e = Employee('bob', 'Mac', 10000)
        print('-----------setup')

    def tearDown(self):
        print('-----------tear')

    def test_give_default_raise(self):
        self.e.give_raise()
        assert self.e.salary == 15000
        print('-----------default')

    def test_give_custom_raise(self):
        self.e.give_raise(10000)
        assert self.e.salary == 20000
        print('-----------custom')


if __name__ == '__main__':
    unittest.main()
