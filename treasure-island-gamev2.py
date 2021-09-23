#Version 2.0
#Add choice logic block based upon user input
################ ASCII Art Header #################
print('''
                                             * )
                                         `(      *
                   ()                   *     )
                  <^^>                     (   .
                 .-""-.                      )
      .---.    ."-....-"-._     _...---''`/. '
     ( (`\ \ .'            ``-''    _.-"'`
      \ \ \ : :.                 .-'
       `\`.\: `:.             _.'
       (  .'`.`            _.'
        ``    `-..______.-'
                  ):.  (
                ."-....-".
              .':.        `.
              "-..______..-"

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the magic lamp")
################### LOGIC BLOCK ##################
choice1 = input('You\'re in the middle of the forest with a path leading left or right. Which way do you want to go? Type "left" or "right" \n') .lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
         choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
         if choice3 == "red":
            print("As you open the door you are incinerated with a fireball. Game Over.")
         elif choice3 == "yellow":
            print("You found the magic lamp! You Win!")
         elif choice3 == "blue":
            print("As you open the door a tentacle grabs you and closes the door. Game Over.")
         else:
            print("Cats swarm your feet as you stand there. The begin to eat you. Game Over.")
    else:
        print("As you swim across the lake you are attacked by giant shark. Game Over")    
else:
    print("You fall into a pit of snakes and die. Game Over")    
