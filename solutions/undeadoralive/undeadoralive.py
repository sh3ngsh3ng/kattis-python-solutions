# undeadoralive
x = input()
ans = 0
if x.find(":)") != -1:
    ans += 1
if x.find(":(") != -1:
    ans -= 1

if x.find(":)") + x.find(":(") == -2:
    print("machine")
elif ans > 0:
    print("alive")
elif ans < 0:
    print("undead")
elif ans == 0:
    print("double agent")
