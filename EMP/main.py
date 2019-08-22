from EMP.emp import Employee
from EMP.leader2 import Leader_2
from EMP.leader1 import Leader_1


def main():
    emp = Employee('Jax', 'M', '2016-09-12', '123456789', 'TY')
    print(emp)
    hour = 46
    emp.total_salary(hour)
    emp = Employee('Mary', 'F', '2014-07-01', '987654321', 'NTP')
    print(emp)
    hour = 0
    emp.total_salary(hour)
    leader2 = Leader_2('James', 'M', '2003-09-12', '741852963', 'GS')
    print(leader2)
    hour = 46
    leader2.total_salary(hour)
    leader2 = Leader_2('keven', 'M', '2007-07-01', '369258147', 'TN')
    print(leader2)
    hour = 0
    leader2.total_salary(hour)
    leader1 = Leader_1('Kobe', 'M', '1997-03-25', '951736482', 'TC')
    print(leader1)
    hour = 46
    leader1.total_salary(hour)
    leader1 = Leader_1('O,neal', 'M', '1994-04-30', '159738246', 'YL')
    print(leader1)
    hour = 0
    leader1.total_salary(hour)

main()