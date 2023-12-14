def main():
    #get user input
    message = input("Input: ")
    #remove all vowels
    message_without_vowels = shorten(message)
    #print output:
    print("Output: " + message_without_vowels)

def shorten(word):
    message_without_vowels = ""
    #loop through every letter
    for letter in word:
        #check if it is not vowels whether inputtet in upper case
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            #add the letter
            message_without_vowels += letter
    #return the new word
    return message_without_vowels

if __name__ == "__main__":
    main()