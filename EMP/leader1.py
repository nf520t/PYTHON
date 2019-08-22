from EMP.leader2 import Leader_2

class Leader_1(Leader_2):
    def __init__(self, name, sex, date, cell, address):
        super(Leader_2, self) . __init__(name, sex, date, cell, address)
        self.salary = 60000
        self.post = 5000
        self.lunch = 2000

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
    leader1 = Leader_1('Kobe', 'M', '1997-03-25', '951736482', 'TC')
    print(leader1)
    hour = eval(input('輸入加班時數:'))
    leader1.total_salary(hour)
    leader1 = Leader_1('O,neal', 'M', '1994-04-30', '159738246', 'YL')
    print(leader1)
    hour = eval(input('輸入加班時數:'))
    leader1.total_salary(hour)

main()
'''