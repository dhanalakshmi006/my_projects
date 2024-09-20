print("Quiz Game")
name=(input("Enter Your Name: "))
score=0
print("Instructions: You have to Answer 5 questions. Each will have 4 option. Each right answer equals 5 points. You should type your choice i.e. A/B/C/D")
print("Let's start")
print ("1) Which one is the smallest ocean in the World?")
print("A - Indian")
print("B - Pacific")
print("C - Atlantic")
print("D - Arctic")
answer1=(input("Enter Your Choice: ")).upper()
if answer1== "D":
    print("correct answer")
    score = score+5
elif answer1== "A"or "B" or "C":
    print("You're wrong, correct answer is D - Arctic ")
else:
    print("invalid choice")

print("2) Which country gifted the 'Statue of Liberty' to USA in 1886?")
print("A -France")
print("B - Canada")
print("C - Brazil")
print("D - England")
answer2=(input("Enter Your Choice: ")).upper()
if answer2== "A":
    print("correct answer")
    score = score+5
elif answer2== "D"or "B" or "C":
    print("You're wrong, correct answer is A - France")
else:
    print("invalid choice")

print("3) Dead Sea is located between which two countries?")
print("A - Jordan and Sudan")
print("B - Jordan and Israel")
print ("C - Turkey and UAE")
print ("D - UAE and Egypt")
answer3=(input("Enter Your Choice: ")).upper()
if answer3== "B":
    print("correct answer")
    score = score+5
elif answer3== "D"or "A" or "C":
    print("You're wrong, correct answer is B - Jordan and Israel")
else:
    print("invalid choice")

print("4) in which ocean Bermuda Triangle region is located?")
print("A - Atlantic")
print ("B - Indian")
print(" C - Pacific")
print ("D - Arctic")
answer4=(input("Enter Your Choice: ")).upper()
if answer4== "A":
    print("correct answer")
    score = score+5
elif answer4== "D"or "B" or "C":
    print("You're wrong, correct answer is A - Atlantic")
else:
    print("invalid choice")

print("5) Which country is known as the playground of Europe?")
print("A - Austria")
print("B - Holland")
print("C - Switzerland")
print("D -  Italy")
answer5=(input("Enter Your Choice: ")).upper()
if answer5== "C":
    print("correct answer")
    score = score+5
elif answer5== "D"or "B" or "A":
    print("You're wrong, correct answer is C - Switzerland")
else:
    print("invalid choice")

if score == 10:
   print("Good Job!,", name, ",You scored :", score, "points in total.  ""Better luck next time!")
elif score == 5:
    print("Good Job!,", name, ",You scored :", score, "points in total.  ""Better luck next time!")

elif score == 25:
    print("Excellent!,", name, ",You scored :", score, "points in total.")
elif score == 0:
    print("Try Again!,", name, ",You scored :", score, "points in total.  ""Better luck next time!")
else:
    print("Good Job!,", name, ",You scored :", score, "points in total.  ")
