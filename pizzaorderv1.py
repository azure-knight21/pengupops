#Interactive Coding Exercise -- Pizza Order Practice
#Program that makes uses of the if-then logic in a pizza ordering
#system

#Block of code that gets initial data input from the user
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
################ END OF INPUT BLOCK #####################
#Block of code that determines price based upon decisions made 
#the user in ordering a pizza

#Initialize variable to allow for incrementation
bill = 0

#Start bill charge by size selection
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

#Check additions to pizza
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese =="Y":
    bill += 1

#Present final bill to customer
print(f"Your total for this pizza order is $ {bill}")