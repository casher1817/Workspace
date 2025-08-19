n = int(input("請輸入一個正整數:"))

total = 0

for num in range(2 , n) :
    is_prime = True
    for i in range(2 , int(num**0.5) + 1):
        if num % i == 0 :
            is_prime = False
            break
    if is_prime:
        total += num
print("所有小於",n ,"的質數總和為:", total)
