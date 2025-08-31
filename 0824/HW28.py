score = float(input("請輸入你的分數:"))

def grade(score):

    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:    
        return "B"
    elif 70 <= score < 80:
        return "C"      
    elif 60 <= score < 70:
        return "D"  
    elif 0 <= score < 60:
        return "F"

    else:
        return "無效的分數" 
rsult = grade(score)
print(rsult)