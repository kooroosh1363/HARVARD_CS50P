def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)


def convert(fraction):
    while True:
        try:
            #try to split the fuel
            numerator, denominator = fraction.split("/")
            #convert into integers
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            #calculate the percentage
            f = new_numerator / new_denominator
            #check if its less than 1 and stop the loop
            if f <= 1:
                #multiply percentage by 100
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    #check if percentage is less than 1 , return E
    if percentage <= 1:
        return "E"
    #check if percentage is greater than 99 , return F
    elif percentage >= 99:
        return "F"
    #otherwise, return the %
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()