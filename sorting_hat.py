# Write code below

Gryffindor = 0
Ravenclaw = 0 
Hufflepuff = 0
Slytherin = 0

# Question about your likes
print("Do you like Dawn or Dusk? ")
question_answer1 = int(input(" 1) Dawn \n 2) Dusk \n"))

# Each house gets a point when the answer is suitable for the house
if question_answer1 == 1:
  Gryffindor +=1
  Ravenclaw +=1
elif question_answer1 == 2:
  Hufflepuff +=1 
  Slytherin +=1
else:
  print("Wrong input. You have to choose between 1 and 2")


print("When I am dead, I want people to remember me as: ")
question_answer2 = int(input(" 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n"))

if question_answer2 == 1:
  Hufflepuff += 2
elif question_answer2 == 2:
  Slytherin += 2
elif question_answer2 == 3:
  Ravenclaw += 2
elif question_answer2 == 4:
  Gryffindor += 2
else:
  print("Wrong input. Please choose between 1 - 4")

print(" Which kind of instrument most pleases your ear?")
question_answer3 = int(input(" 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum \n"))

if question_answer3 == 1:
  Slytherin += 4
elif question_answer3 == 2:
  Hufflepuff += 4
elif question_answer3 == 3:
  Ravenclaw += 4
elif question_answer3 == 4:
  Gryffindor += 4
else:
  print("Wrong input. Please choose between 1 - 4")

# Calculate the maximum score among all houses
max_score = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

# Print the house with the maximum score
if Gryffindor == max_score:
    print("You belong to Gryffindor!")
elif Ravenclaw == max_score:
    print("You belong to Ravenclaw!")
elif Hufflepuff == max_score:
    print("You belong to Hufflepuff!")
elif Slytherin == max_score:
    print("You belong to Slytherin!")
else:
    print("There was a tie or no house was selected.")