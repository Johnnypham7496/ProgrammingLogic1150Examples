import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    # setup and teardown class are working with the class itself rather than the instance. 
    # Used mainly for one time otherwise this end up being costly
    @classmethod
    def setUpClass(cls):
        print('setupClass\n')

    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # code below are instances
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Johnny', 'Pham', 70000)
        self.emp_2 = Employee('Anh', 'Huynh', 70000)


    def tearDown(self):
        print('tearDown\n')


    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Johnny.Pham@email.com')
        self.assertEqual(self.emp_2.email, 'Anh.Huynh@email.com')

        self.emp_1.first = 'Anh'
        self.emp_2.first = 'Johnny'

        self.assertEqual(self.emp_1.email, 'Anh.Pham@email.com')
        self.assertEqual(self.emp_2.email, 'Johnny.Huynh@email.com')


    def test_fullname(self):
        print('test fullname')
        self.assertEqual(self.emp_1.fullname, 'Johnny Pham')
        self.assertEqual(self.emp_2.fullname, 'Anh Huynh')

        self.emp_1.first = 'Anh'
        self.emp_2.first = 'Johnny'

        self.assertEqual(self.emp_1.fullname, 'Anh Pham')
        self.assertEqual(self.emp_2.fullname, 'Johnny Huynh')


    def test_apply_raise(self):
        print('test apply_raises')
        self.emp_1.apply_raises()
        self.emp_2.apply_raises()

        self.assertEqual(self.emp_1.pay, 73500)
        self.assertEqual(self.emp_2.pay, 73500)


    


if __name__ == '__main__':
    unittest.main()