# 計算學生成績平均的程式

def main():
    scores = []
    n = int(input("請輸入學生人數: "))
    for i in range(n):
        score = float(input(f"請輸入第{i+1}位學生的成績: "))
        scores.append(score)
    average = sum(scores) / n if n > 0 else 0
    print(f"全班平均成績為: {average:.2f}")

if __name__ == "__main__":
    main()