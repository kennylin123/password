import random
r = random.randint(1,100)
count = 0
while True:
    count += 1
    num = input('請輸入數字: ')
    num = int(num)
    if num == r:
        print('你猜中了')
    elif num < r:
        print('再大一點')
    elif num > r:
        print('在小一點')
    print('這是猜的第', count, '次')

