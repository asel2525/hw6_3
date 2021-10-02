class Banc():
    def __init__(self, credit, comission, percentage):
        self.credit = credit
        self.comission = comission
        self.percentage = percentage

    def hello(self):
        self.hi = 'hi'

    def get_data(self):
        return f'Сумма кредита - {self.credit}\n' \
               f'Cумма всех комиссий (разовых и ежемесячных) - {self.comission}\n' \
               f'Проценты по кредиту - {self.percentage} %'

    @property
    def credit_calc(self):
        return self.credit + self.comission + self.percentage

person = Banc(20, 45, 60)
print(person.get_data())
print(person.credit_calc)

person.hello()
print(person.hi)