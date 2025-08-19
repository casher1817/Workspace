money = int(input("請輸入金額: "))
if money >= 1000 :
    discount = 0.2  
    print("您的折扣後金額為: {:.0f}".format(money *(1- discount)),"元")
      
elif money >= 500 and money < 1000:
    discount = 0.1
    print("您的折扣後金額為: {:.0f}".format(money *(1- discount)),"元")
else:
    discount = 0
    print("您的折扣後金額為: {:.0f}".format(money *(1- discount)),"元")