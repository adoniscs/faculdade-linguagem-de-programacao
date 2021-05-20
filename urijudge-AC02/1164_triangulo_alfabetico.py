import string
n = int(input())
alph = string.ascii_uppercase

for num in range(1,n+1):
    if n >= 1 and n <= 26:
        print(num * alph[num-1])    
