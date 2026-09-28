print("Welcome to the tip caculator!")

bill = float(input("please enter the total bill: "))

percentage = int(input("What percentage would you like to give? 10, 12, 15, or 20?"))

tip_percent = bill*(percentage/100)

total_money = tip_percent+bill

print("the tip amount is $", + tip_percent )
print("the total amount is $", + total_money)
