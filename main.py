bill = input("What is the bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")
percent = int(tip) / 100

bill_float = round(float(bill), 2)

tip_total = (bill_float * percent) / int(split)
tip_total2 = "{:.2f}".format(tip_total)
bill_total = (tip_total * int(split)) + bill_float
bill_total2 = "{:.2f}".format(bill_total)
bill_split = bill_total / int(split)
bill_split2 = "{:.2f}".format(bill_split)

message1 = f"Each person should tip: ${tip_total2}"
message2 = f"Total bill w/ all tips is: ${bill_total2}"
message3 = f"Splitting the bill comes to: ${bill_split2}"
print(message1)
print(message2)
print(message3)
