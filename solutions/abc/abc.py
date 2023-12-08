# abc
ls = sorted(map(int, input().split()))
o = list(map(ord, input()))
print(*[ls[o[0]-65], ls[o[1]-65], ls[o[2]-65]])
