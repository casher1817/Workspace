def is_prime(n):
    for i in range( 2 , n ):
        if n % i == 0:
            return False
    return True

n = int(input("請輸入一個大於1的正整數: "))

for i in range(2, n):
    n = is_prime(i)
    if n:
        print(i, end=" ")
