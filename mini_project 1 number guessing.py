import random

top_of_range = input("Enter a number to set the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter a number greater than Zero")
        quit()
else:
    print("Enter a number next time ")
    quit()
    