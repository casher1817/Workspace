sentance = input("請輸入一串以空白分隔的字串:")

def reverse_words(sentence):
    words = sentence.split(" ")           
    reversed_words = [word[::-1] for word in words]  
    return " ".join(reversed_words)
result = reverse_words(sentance)
print(result)


