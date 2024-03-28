high_income = True
good_credit = False
credit = 350
cost = int(1_000_000)

if good_credit:
   down_payment = str(cost * 0.1 )
else:
    down_payment = str(cost * 0.2 )
print(f"Down Payment: ${down_payment}")

if high_income or credit>310:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

