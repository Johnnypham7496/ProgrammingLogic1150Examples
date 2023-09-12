class Employee():

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    

    def fullname(self):
        return f'{self.first} {self.last}'
    

    def apply_raises(self):
        self.pay= int(self.pay * self.raise_amt)