
heigt = float(input("請輸入身高(cm): "))
weight = float(input("請輸入體重(kg): "))
bmi = weight / ((heigt / 100) ** 2)
print("BMI: {:.2f}".format(bmi))
