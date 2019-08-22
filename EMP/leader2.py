''''''

from EMP.emp import Employee

class Leader_2(Employee):
    def __init__(self, name, sex, date, cell, address):
        super(Leader_2, self) . __init__(name, sex, date, cell, address)
        self.salary = 50000
        self.post = 3000
        self.lunch = 1800

    def  total_salary(self, hour):

        try:
            if hour < 0:
                raise ValueError
            total_salary = self.salary + (self.salary // 240 * 1.5 * hour) + self.lunch + self.post
            print('總薪資:', total_salary)
        except:
            print('加班時數不可為負數')

    def __str__(self):
        return ('姓名:{0}/性別:{1}/到職日:{2}/電話:{3}/地址{4}/本薪:{5}'.format(
            self.name, self.sex, self.date, self.cell, self.address, self.salary))
'''
def main():
    leader2 = Leader_2('James', 'M', '2003-09-12', '741852963', 'GS')
    print(leader2)
    hour = eval(input('輸入加班時數:'))
    leader2.total_salary(hour)
    leader2 = Leader_2('keven', 'M', '2007-07-01', '369258147', 'TN')
    print(leader2)
    hour = eval(input('輸入加班時數:'))
    leader2.total_salary(hour)

main()
'''