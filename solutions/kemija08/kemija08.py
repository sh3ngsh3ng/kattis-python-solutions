# kemija08
x = input()
res = ""
vowels = ('a', 'e', 'i','o','u')
counter = 0
while counter < len(x):
    res+=x[counter]
    if x[counter] in vowels:

        counter += 3
    else:
        counter += 1
print(res)