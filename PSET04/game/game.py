from random import randint


while True:

    #ask for game level
    try:
        level = int(input("Level: ").strip())

        #check if user input is a positive int
        if level >= 1:
            random = randint(1, level)
            #ask user to make a guess
            while True:
                a = int(input("Guess: ").strip())

                #comparison of user input and random generated number
                try:
                    if a > random:
                        print("Too large!")
                    elif a < random:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break

                #ask again for an input (guess)
                except (TypeError, ValueError):
                    continue

            break

    #ask again for an input (level)
    except (TypeError, ValueError):
        continue
