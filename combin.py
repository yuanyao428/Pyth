import random, sys, time
N = int(input())
player = [i for i in range(N)]
min_table = [[[] for col in range(N//4)] for row in range(4)]

def judge(times, table, N):
    random.shuffle(player)
    for i in range(N//4):
        for j in range(4):
            table[times][i].append(player[i * 4 + j])

max_game = 0
min_game = 10
test_times = 0
while test_times < 1:
    table = [[[] for col in range(N//4)] for row in range(4)]
    game = [[0 for col in range(N)] for row in range(N)]
    for times in range(4):
        judge(times, table, N)
        times += 1
    for i in range(4):
        for j in range(N//4):
            a = table[i][j][0]
            b = table[i][j][1]
            c = table[i][j][2]
            d = table[i][j][3]
            game[a][b] += 1
            game[a][c] += 1 
            game[a][d] += 1
            game[b][c] += 1 
            game[b][d] += 1
            game[c][d] += 1
    for i in range(N):
        for j in range(i + 1, N):
            temp = 0
            temp = game[i][j] + game[j][i]
            if max_game < temp:
                max_game = temp
    if max_game < min_game:
        min_game = max_game
        min_table = table
    
    test_times += 1
    print(min_game)
    

print(min_game)
for i in range(N):
        print(game[i])
for i in range(4):
    print(min_table[i])
