#! /usr/bin/env python3

# Q. 整数a1,a2,...anが与えられ、その中からいくつか選び、和をkにすることができるか
# => a1から順に和の計算要素に加えるか決める深さ優先検索の問題
n = 4
a = [1, 2, 4, 7]
k = 15

def dfs(i: int, s: int):
    # 最深にたどり着いたら、和がkに等しいか判定
    if i == n:
        return s == k

    # a[i]は使わない場合
    if dfs(i + 1, s):
        return True

    # a[i]を使う場合
    if dfs(i + 1, s + a[i]):
        return True

    return False

if dfs(0, 0):
    print('Yes')
else:
    print('No')

# Q. sがスタート, gがゴール, #が塀で、ゴールたどり着けるか (動きは上下左右)
H, M = 10, 10
inp = """
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#...
"""

c = []
sx, sy = 0, 0
gx, gy = 0, 0
for i, r in enumerate(inp.split()):
    r = list(r)
    c.append(r)
    for j, s in enumerate(r):
        if s == 's':
            sx = i
            sy = j
        elif s == 'g':
            gx = i
            gy = j

# 上下左右のベクトル
vx = [0, 1, 0, -1]
vy = [-1, 0, 1, 0]
result = False

def dfs(x, y):
    # 現在地を#で塗り替えて移動できないようにする
    c[x][y] = 'X'

    for i in range(4):
        nx, ny = x + vx[i], y + vy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= H or c[nx][ny] == '#':
            pass
        elif c[nx][ny] == 'g':
            global result
            result = True
            return
        elif c[nx][ny] == '.':
            dfs(nx, ny)

dfs(sx, sy)
print(result)
