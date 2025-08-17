# 輸入長方形的長和寬，計算面積和周長

length = float(input("請輸入長方形的長(公分):) "))  
width = float(input("請輸入長方形的寬(公分): "))

area = length * width
perimeter = 2 * (length + width)
print(f"面積: {area:.2f} 平方公分")
print(f"周長: {perimeter:.2f} 公分")