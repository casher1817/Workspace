principal = int(input("請輸入您的本金: "))
rate = float(input("請輸入年利率(百分比): "))
years = int(input("請輸入存款年數: "))
interest = principal * (rate / 100) * years
print(f"您在{years}年後的利息為: {interest:.2f}元")