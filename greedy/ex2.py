n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

num = 0
for i in range(m):
    if i%4 != 3:
        num += first
    else:
        num += second

print(num)