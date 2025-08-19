def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2,n+1):
            result *= i
        return result
num = int(input("請輸入一個正整數: "))
fact = factorial(num)
print(f" {num}!= {fact}")