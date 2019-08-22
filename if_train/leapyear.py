'''
選擇性敘述的練習-leapYear
輸入一西元年，如2015。判斷此年份是否為閏年。
提示：每四年一閏，每百年不閏，每四百年一閏，每四千年不閏。
'''

year = abs(eval(input('輸入年份: ')))

if year % 4000 != 0:
    if year % 400 != 0:
        if year % 100 != 0:
            if year % 4 != 0:
                print('非閏年')
            else:
                print('閏年')

        else:
            print('非閏年')

    else:
        print('閏年')
else:
    print('閏年')