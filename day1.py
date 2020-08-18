nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

a = a[d:] + a[:d]

for digit in a:
        print(digit, end=" ")

print("\n")