# coffeecupcombo
n = int(input())
x = list(map(int, [*input()]))
count_pass = 0
for i in range(n):
    if count_pass > 0:
        if x[i] == 1:
            count_pass = 2
        else:
            x[i] = 1
            count_pass -= 1
    else:
        if x[i] == 1:
            count_pass += 2
print(x.count(1))
