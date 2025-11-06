game_over = "Game Over!"
print(r'''
                                __- -
                               (   
                              _))_ 
                              |  |________
                     .-------"""""   |    """""------.
                    /.".\            |            /.".\
                   /.   .\           |           /.   .\
                  /.     .\          |          /.     .\
                 /.  ___ '.|__....--"T"--....__|.' ___  .\
                |   |_|_|  |   _..   |   --.   |  |_|_|  |
                |   |_|_|  |  |  |   |   |_|   |  |_|_|  |
                |__________|__|..+--"""--....__|_________|   

''')
print("You have arrived at the Witch's House.")
print("Your mission is to find the Golden Apple.")

#First choice
while True:
    choice1 = input("Will you enter through the Door, or go around the back?\n").lower()

    if choice1 in ("door", "through the door", "go through the door"):
         print("The Witch is waiting for you, and strikes you down with her broom!")
         print(f"{game_over}")
         exit() #Game ends
    elif choice1 in ("back", "go around", "go around the back", "Go around", "Go around the back", "go round the back", "round the back"):
        print("You quietly walk around the back of the cottage.")
        break
    else:
        print("I didn't understand that, please try again.")


#Second choice
print("You find a broken window full of sharp glass, and on the ground there is a rock.")
while True:
    choice2 = input("Would you like to crawl through the window, or clear the glass with the rock?\n").lower()

    if choice2 in ("window", "crawl", "crawl through the window", "crawl through window"):
        print("You cut yourself and scream, the Witch appears and finishes you off with her broom.")
        print(f"{game_over}")
        exit()  # Game ends
    elif choice2 in ("clear glass", "rock"):
        print("You grab the rock.")
        break
    else:
        print("I didn't understand that, please try again.")

#Third choice
print(r'''
                   ____________________________________________________________________    
                  |    |__I__I__I__I__I__I__I__I__I_|       _-       %       %         |
                  | _- |_I__I__I__I__I__I__I__I__I__|-_              %       %     _-  | 
                  |    |__I__I__I__I__I__I__I__I__I_|                %       %         |
                  |  - |_I__I__I__I__I__I__I__I__I__|               ,j,      %w ,      |
                  | -  |__I__I__I__I__I__I__I__I__I_|  -_ -        / ) \    /%mMmMm.   |
                  |    |_I__I__I__I__I__I__I__I__I__|             //|  |   ;  `.,,'    |
                  |-_- /                            \             w |  |   `.,;`       |
                  |   /                              \    -_       / ( |    ||         |
                  |  /                                \           //\_'/    (.\    -_  |
                  | /__________________________________\          w  \/   -  ``'       |
                  | |__________________________________|                               |
                  |    |   _______________________   |     _-            -             |
                  |_-  |  |                       |  |                        _-       |
                  |    |  |                     _ |  |  T  T  T  T  T                  |
                  | _-_|  |    __.'`'`'`''`;__ /  |  |  |  |  |  |  |        _-     -  |
                  |    |  | _/U  `'.'.,.,".'  U   |  |  | (_) |  |  |                  |
                  |    |  |   |               |   |  | / \    @ [_]d b    _@_     |    |   
                  |    |  |   |      `', `,   |   |  | |_|   ____         [ ]     |    |
                  |_-  |  |   |   `') ( )'    |   |  | ______\__/_________[_]__   |    | 
                  |    |  |   |____(,`)(,(____|   |  |/________________________\  |    |
                  |    |  |  /|   `@@(@@)@)'  |\  |  | ||            _____   ||   |    |
                  |    |  | //!\  @@)@@)@@@( /!   |  | ||   _--      \   /   ||  /|\   |
                  |__lc|__|/_____________________\|__|_||____________/###\___||_|||||__|
                 / -_  _ -      _ -   _-_    -  _ - _ -|| -_    _  - \___/_- || |||||-_ \ 
                 ''')


print("You carefully remove the glass with the rock and discard it on the ground.")
print("Crawling through the window, you find yourself in a kitchen.")
print("To your left, there is a golden box. To your right, an old grimoire.")

while True:
    choice3 = input("Do you open the box, or the grimoire? Be quick! The Witch is coming down the stairs.\n").lower()

    if choice3 in ("box", "golden box", "the box", "the golden box", "open box", "open the box"):
        print("You have been tricked! A cloud of poison rises from the box and immediately kills you.")
        print(f"{game_over}")
        exit()  # Game ends
    elif choice3 in ("the grimoire", "book", "the book", "grimoire", "open book", "open grimoire"):

        print(r'''
                     ,--./,-.
                    / #      \
                   |          |
                    \        /    
                     `._,._,'
                ''')
        print("Behold! The Golden Apple was hidden within! You make your escape with the treasure.")
        print("Thank you for playing!")
        break

    else:
        print("You hesitated and your choice wasn't clear, but before you had chance")
        print("to make a new choice, the Witch cast a spell on you.")
        print("You have turned to stone, and will spend the rest of your days in the Witch's garden.")
        print(f"{game_over}")
        exit()  # Game ends


