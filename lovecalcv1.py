#Love Calculator v1.0
#Program that uses logical operator to make calculations 
#based upon user input

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Add the two names together
combined_name = name1 + name2

#Setting all to lower case
lower_case_string = combined_name.lower()

#Getting letter count from combined strings
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
score_check = int(love_score)
################ LOGIC BLOCK ###############
if score_check < 10 or score_check > 90 :
    print(f"Your score is {score_check}, you go together like coke and mentos.")
elif score_check >= 40 and score_check <=50:
    print(f"Your score is {score_check}, you are alright together")
else:
    print(f"Your score is {score_check}.")        
