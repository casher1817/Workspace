weight = float(input("請輸入您的體重(kg): "))
height = float(input("請輸入您的身高(cm): "))
BMI = weight/((height/100)**2) 
print("您的BMI為: {:.1f}".format(BMI))
      
if BMI < 18.5 :
    print("您的體重過輕")
elif 18.5 <= BMI <= 24.9 :
    print("您的體重在正常範圍")
elif 25 <= BMI <= 29.9:
    print("體重過重囉")
else :
    print("您是肥胖的")