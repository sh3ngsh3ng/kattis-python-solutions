# anothercandies
C=int(input())
for _ in range(C):
    input()
    n=int(input())
    sum=0
    for _ in range(n):
        sum+=int(input())
    if not sum%n:print("YES")
    else: print("NO")
