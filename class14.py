import random
start = input('請決定隨機數字範圍開始: ')
end = input('請決定隨機數字範圍結束: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    count += 1
    num = input('請輸入數字: ')
    num = int(num)
    if num == r:
        print('你猜中了')
        break
        print('這是猜的第', count, '次')
    elif num < r:
        print('再大一點')
    elif num > r:
        print('再小一點')
    print('這是猜的第', count, '次')

