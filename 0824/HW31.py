n = int(input("請輸入一個整數(>=2):"))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):  # 只需檢查到 sqrt(x)
        if x % i == 0:
            return False
    return True

def count_primes(n):
    count = 0
    for num in range(2, n+1):
        if is_prime(num):
            count += 1
    return count

def list_primes(n):
    return [x for x in range(2, n+1) if is_prime(x)]

result = count_primes(n)

print("質數的個數有:" , (result) ,"個",(list_primes(n)))    