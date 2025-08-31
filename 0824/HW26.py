value = float(input("請輸入溫度值: "))
unit = input("請輸入溫度單位 (C/F): ")

def convert_temperature(value, unit):

    if unit.upper() == 'C':
        # 攝氏轉華氏
        converted = (value * 9/5) + 32
        return f"{converted:.2f} F"
    elif unit.upper() == 'F':
        # 華氏轉攝氏
        converted = (value - 32) * 5/9
        return f"{converted:.2f} C"
    else:
        return "無效的單位，請輸入 'C' 或 'F'"
result = convert_temperature(value, unit)
print(result)


