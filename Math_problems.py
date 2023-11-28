import math


# Program to display the Fibonacci sequence up to n-th term

def fibonaci():
    nterms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


option = input("pick either degrees or radians:")
if option.lower() == "degrees":
    degrees = float(input("input degrees:"))
    print(f"That is {(degrees * math.pi) / 180} radians")
#Either pick above which is degrees or the bottom part which is radians.

elif option.lower() == "radians":
    convert = list(input("You most likely have it e.g 7π we'll convert it to "
    "decimals so we can calculate the exact degrees you want to get:"))
    pi_removal = convert.remove('π')
    str(print(f"Your radian is now {pi_removal}"))
    radians = float(input("input radians:"))
    print(f"{(radians * 180) / math.pi}")
