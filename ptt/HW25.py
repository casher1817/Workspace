num1 = float(input("請輸入第一個數字:"))
operater = input("請輸入運算符(+,-,*,/):")
num2 = float(input("請輸入第二個數字:"))

if operater == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operater == "-":
    result = num1 - num2
    print(f"({num1 - num2} = {result})")
elif operater == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operater == "/":
    if num2 == 0 :
        print("錯誤 : 除數不能為零")
    else:
        result = num1 / num2
        print("{num1} / {num2} = ({result})")
else:
    print("無效的運算符")