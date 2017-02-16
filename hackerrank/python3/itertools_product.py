from itertools import product
A = map(int,input().split())
B = map(int,input().split())
A.sort()
B.sort()

ans = [A,B]
AxB = list(product(*ans))

for i in AxB:
	print(i, end="")
