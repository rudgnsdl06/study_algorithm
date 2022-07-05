start = input()

x_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y_index = [str(i+1) for i in range(8)]

x = x_index.index(start[0])
y = y_index.index(start[1])

moves = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
count = 0

for move in moves:
    nx = x+move[0]
    ny = y+move[1]
    if nx>7 or ny>7 or nx<0 or ny<0:
        continue
    count += 1

print(count)