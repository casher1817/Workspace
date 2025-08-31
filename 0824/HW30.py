n = int(input("請輸入要計算費伯那希數列的項數:"))

def fibonacci(n):
   
    if n <= 0:
        return []

    seq = [0]  # 第一項
    if n == 1:
        return seq

    seq.append(1)  # 第二項
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])  # 後項 = 前兩項和
    return seq
result = fibonacci(n)
print(result)
