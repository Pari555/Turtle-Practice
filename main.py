import turtle

# Ask the user how many sides they want
# Create the polygon based on the user input
# Range = (3, 10), do an error checking, if they input 2 , tell then that is invalid.

turtle.shape("turtle")

whileloop = True
while(whileloop == True):
  userInput = int(input("How many sides do you want: "))
  if(userInput >= 3 and userInput <= 10):
    whileloop = False
  else:
    print("Error: That is not the correct number of sides.")

for i in range(userInput):
  turtle.forward(100)
  turtle.right(360/userInput)
