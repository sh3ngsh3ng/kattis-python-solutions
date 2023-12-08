# jackolanternjuxtaposition
x = input().split()
sum = 0
for idx,i in enumerate(x):
    if idx == 0:
        sum += int(i)
        continue
    sum *= int(i)
print(sum)