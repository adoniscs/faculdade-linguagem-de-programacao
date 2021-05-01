A, B = input().split()
A = int(A)
B = int(B)

if A > B and A % B == 0:
    print("Sao Multiplos")
elif B > A and B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
