N, M = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0]*M for i in range(N)]

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

dx = (-1, 0, 1, 0) #행간 이동
dy = (0, 1, 0, -1) #열간 이동

def turn_left():
    global direction
    direction -= 1
    direction %= 4

count = 0
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny
        d[nx][ny] == 1
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0
        
print(count)