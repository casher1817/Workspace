def extract_digits(s):
    result = ""
    for ch in s:
        if ch.isdigit():      
            result += ch
    return result

s = input("請輸入一串字元:")
result = extract_digits(s)      
print(result)   