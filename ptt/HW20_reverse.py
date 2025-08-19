def reverse_string(s):
    
  reversed_string = ""
  for char in s:  
    reversed_string = char + reversed_string
  return reversed_string

input_string = input("請輸入一個字串: ")
reversed_string = reverse_string(input_string)
print(f"反轉後的字串是: {reversed_string}")