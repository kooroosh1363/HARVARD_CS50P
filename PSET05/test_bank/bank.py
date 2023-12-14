def main():
    #get user input
    greeting = input("Greeting: ")
    #store the result of value function
    value_to_print = value(greeting)
    print(f"${value_to_print}")



def value(greeting):
    #convert greeting in all lower and without whitespaces
    greeting = greeting.lower().strip()
    #check if the answer has hello
    if "hello" in greeting:
        return 0
    #check if answer atarts 'h'
    elif 'h' == greeting[0]:
        return 20
    #otherwise return 100
    else:
        return 100


if __name__ == "__main__":
    main()