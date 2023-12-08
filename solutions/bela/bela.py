# bela
y, x = input().split()
suit = x

dict = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "T": 10,
    "8": 0,
    "7": 0
}

score = 0
for i in range(int(y)*4):
    z = input()
    if z[0] == 'J':
        if z[1] == suit:
            score += 20
        else:
            score +=2
    elif z[0] == '9':
        if z[1] == suit:
            score += 14
        else:
            score += 0
    else:
        score += dict[z[0]]
        

print(score)
