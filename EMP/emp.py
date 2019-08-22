'''
有一小公司，其人事薪資的制度如下：
公司每個員工皆有姓名、性別、到職日、電話和住址等基本資料。
一般職員只有本薪；一級主管則另有本薪、午餐津貼、交通津貼和職務加給；
二級主管則有本薪、午餐津貼和職務加給。午餐津貼為1800元，交通津貼為
2000元，職務加給一級主管為5000元，二級主管為3000元。
每個員工皆有可能加班，加班費為本薪除以240乘以1.5倍再乘以加班時數。
在main()中產生六個實例分別為一級主管、二級主管及一般職員且分有加班及
無加班兩種(資料直接透過建構子hard code在程式中)，並列印其基本資料及當
月薪資。
'''

class Employee:
    def __init__(self, name, sex, date, cell, address):
        self.name = name
        self.sex = sex
        self.date = date
        self.cell = cell
        self.address = address
        self.salary = 40000

    def total_salary(self, hour):

        try:

            if hour < 0:
                raise ValueError
            total_salary = self.salary + (self.salary // 240 * 1.5 * hour)
            print('總薪資:', total_salary)
        except:
            print('加班時數不可為負數')


    def __str__(self):
        return ('姓名:{0}/性別:{1}/到職日:{2}/電話:{3}/地址{4}/本薪:{5}'.format(
            self.name, self.sex, self.date, self.cell, self.address,self.salary))
'''
def main():
    emp = Employee('Jax', 'M', '2016-09-12', '123456789', 'TY')
    print(emp)
    hour = eval(input('輸入加班時數:'))
    emp.total_salary(hour)
    emp = Employee('Mary', 'F', '2014-07-01', '987654321', 'NTP')
    print(emp)
    hour = eval(input('輸入加班時數:'))
    emp.total_salary(hour)
main()
'''