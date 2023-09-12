import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Johnny', 'Pham', 70000)
        emp_2 = Employee('Anh', 'Huynh', 70000)


        self.assertEqual(emp_1.email, 'Johnny.Pham@email.com')
        self.assertEqual(emp_2.email, 'Anh.Huynh@email.com')

        emp_1.first = 'Anh'
        emp_2.first = 'Johnny'

        self.assertEqual(emp_1.email, 'Anh.Pham@email.com')
        self.assertEqual(emp_2.email, 'Johnny.Huynh@email.com')


    def test_fullname(self):
        emp_1 = Employee('Johnny', 'Pham', 70000)
        emp_2 = Employee('Anh', 'Huynh', 70000)

        self.assertEqual(emp_1.fullname, 'Johnny Pham')
        self.assertEqual(emp_2.fullname, 'Anh Huynh')

        emp_1.first = 'Anh'
        emp_2.first = 'Johnny'

        self.assertEqual(emp_1.fullname, 'Anh Pham')
        self.assertEqual(emp_2.fullname, 'Johnny Huynh')




if __name__ == '__main__':
    unittest.main()