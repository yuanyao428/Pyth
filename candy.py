N = int(input())
x1 = input()
x2 = input()
for i in range(N):
    arr1 = list(map(int, x1.split()))
for i in range(N):
    arr2 = list(map(int, x2.split()))
sumarr2 = 0
for i in range(N):
    sumarr2 += arr2[i]
sum = arr1[0] + sumarr2
for i in range(1, N):
    temp = 0
    for j in range(i):
        temp += arr1[j]
        temp -= arr2[j]
    temp = temp + arr2[j] + sumarr2
    if temp > sum:
        sum = temp
print(sum)