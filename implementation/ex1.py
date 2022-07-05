n = int(input())
x, y = 1, 1
plans = input().split()

#LRUD
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i, move_type in enumerate(move_types):
        if plan == move_type:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    else:
        x, y = nx, ny

print(x, y)