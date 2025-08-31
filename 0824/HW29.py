text = input("請輸入一串以空白分隔的字串:")

def remove_duplicates(text):
    
    seen = set()
    result = []
    for word in text.split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)
result = remove_duplicates(text)
print(result)