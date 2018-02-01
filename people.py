N, M = map(int, input().split())
data2D = []
for i in range(M):
    data = []
    data = map(int, input().split())
    data2D.append(list(data))

dict = {data2D[0][1]: 0, data2D[0][0]:data2D[0][1] - data2D[0][2]}
for i in range(1, M):
    if data2D[i][1] in dict:
