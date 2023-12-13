from random import randint


#meaning of each level using 3 dicts in a list
levellist = [{1: [0, 9]}, {2: [10, 99]}, {3: [100, 999]}]


def main():
    slevel = get_level()
    pset = generate_integer(slevel)

    #success counter
    done = 0

    #ask user the random generate question
    for question in pset:
        #fail counter
        life = 0

        while True:
            try:
                ans = int(input(f"{question} = "))
                a, b = question.strip(" ").split("+")

                #input vs true ans
                if life == 2:
                    print("EEE")
                    print(f"{question} = {(int(a) + int(b))}")
                    break
                elif ans != (int(a) + int(b)):
                    life += 1
                    print("EEE")
                else:
                    done += 1
                    life = 0
                    break


            #wrong input type
            except ValueError:
                print("EEE")
                life += 1
                continue

    print(f"Score: {done}")


def get_level():
    #get level from user
    while True:
        try:
            level = int(input("Level: "))
            #if it was less than 1 or more than 3 ask again
            if level <= 3 and level > 0:
                return level

        #wrong input : ask again
        except ValueError:
            continue


def generate_integer(level):
    #10 random psets
    pset = []

    #set difficulty
    lower = levellist[level - 1][level][0]
    higher = levellist[level -1][level][1]

    #built problem sets according to user input
    for _ in range(0, 10):
        pset.append(f"{randint(lower, higher)} + {randint(lower, higher)}")

    return pset


if __name__ == "__main__":
    main()

