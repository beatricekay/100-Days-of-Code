#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill?"))
bill_and_tip = bill * (100+tip)/100
per_pax = round(bill_and_tip / people , 2)
# per_pax = "{:.2f}".format(bill_and_tip / people)
# Alternative way to ensure that if the bill is $19.60, it displays as $19.60 and not $19.6
print(f"Each person should pay: ${per_pax}")
