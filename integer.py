#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May 12 2021
# This program asks the user to type in an integer
# and tells the user if the integer is postive, negative or just zero


def main():

    # get the user's integer number
    num = float(input("Enter a number: "))
    print("")

    # check to see if the integer is postive, negative or just zero
    if num > 0:
        print("The number {} is postive.".format(num))
    elif num < 0:
        print("The number {} is negative.".format(num))
    else:
        print("The number {} is just zero.".format(num))


if __name__ == "__main__":
    main()
