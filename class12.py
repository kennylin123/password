password = 'a123456'
y = 0
while y < 3:
    x = input('請輸入密碼: ')
    if x == password:
        print('登入成功')
        break
    else:
        y = y + 1
        print('密碼錯誤 還有', 3 - y, '次機會')
        if y == 3:
            print('輸入次數已達上限')