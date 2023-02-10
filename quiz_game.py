print("\nWelcome to my computer quiz \n")

playing = input("Do you want to play? ")

# lower fun. if the user typed with capitals, it will just all be lowercase // same thing with upper() 
if playing.lower() != "yes":
    quit() # quit function will just immediately terminate the program

print ("Okay! Let's play :) \n")
score =0

questions = {
    "What does CPU stand for? " : "central processing unit",
    "What does GPU stand for? " : "graphics processing unit",
    "What does RAM stand for? " : "random access memory",
    "What does PSU stand for? " : "power supply"
}

for q in questions:
    answer = input(q)
    if answer.lower() == questions[q]:
        print ("Correct")
        score +=1
    else:
        print("Incorrect")


print("You got " + str(score) + " Question Correct.")
print("You got " + str((score/len(questions))*100) + " %.")


# answer = input("What does CPU stand for? ")

# if answer.lower() == "central processing unit":
#     print ("Correct")
#     score +=1
# else: 
#     print("Incorrect")

#--------------------




