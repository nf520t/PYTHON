'''
輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”
'''

month = eval(input('輸入月份: '))
if 1 <= month <= 3:
    print('春')
elif 4 <= month <= 6:
    print('夏')
elif 7 <= month <= 9:
    print('秋')
elif 10 <= month <= 12:
    print('冬')
else:
    print('輸入錯誤')

