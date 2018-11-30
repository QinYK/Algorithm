array = [False] * 100

# n 为要翻第几张牌，在数组中使用要-1
# m 为翻牌间隔
for n in range(2, 101):
    m = n - 1
    while n < 100:
        array[n - 1] = not array[n - 1]
        n = m + n + 1

for i in range(0, 100):
    if array[i] is False:
        print(i + 1)
