import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Johnny', 'Pham', 70000)
        self.emp_2 = Employee('Anh', 'Huynh', 70000)


    def tearDown(self):
        pass


    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Johnny.Pham@email.com')
        self.assertEqual(self.emp_2.email, 'Anh.Huynh@email.com')

        self.emp_1.first = 'Anh'
        self.emp_2.first = 'Johnny'

        self.assertEqual(self.emp_1.email, 'Anh.Pham@email.com')
        self.assertEqual(self.emp_2.email, 'Johnny.Huynh@email.com')


    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Johnny Pham')
        self.assertEqual(self.emp_2.fullname, 'Anh Huynh')

        self.emp_1.first = 'Anh'
        self.emp_2.first = 'Johnny'

        self.assertEqual(self.emp_1.fullname, 'Anh Pham')
        self.assertEqual(self.emp_2.fullname, 'Johnny Huynh')


    def test_apply_raise(self):
        self.emp_1.apply_raises()
        self.emp_2.apply_raises()

        self.assertEqual(self.emp_1.pay, 73500)
        self.assertEqual(self.emp_2.pay, 73500)



if __name__ == '__main__':
    unittest.main()