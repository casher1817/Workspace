length = int(input("請輸入矩形的長:"))
width = int(input("請輸入舉行的寬:"))

for i in range(length):
    for j in range(width):
        print("*", end = "")
    print()
    