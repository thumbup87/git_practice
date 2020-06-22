import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee('seung-tai', 'kang')
        self.employee2 = Employee('Jane', 'Marshal')
    
    def test_give_default_raise(self):
        self.assertEqual(5000, self.employee1.annual_salary)

    def test_give_custom_raise(self):
        self.employee2.give_raise(1000)
        self.assertEqual(6000, self.employee2.annual_salary)

if __name__ == '__main__':
    unittest.main()

#test class does not need __init__ method
#all funtions need (self)
#in setup method testing class are instantiated and used throughout the test
#import unittest module and classes being tested
            

