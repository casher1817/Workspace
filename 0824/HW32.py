numbers = list(map(int, input("請輸入一串以空白分隔的整數:").split()))

def second_largest(numbers):
    
    unique_nums = sorted(set(numbers), reverse=True)  
    if len(unique_nums) < 2:
        return "NA"
    return unique_nums[1]

result = second_largest(numbers)

print(result)


