#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Dec 2022
# This program finds the largest number of an array of randomly generated numbers

import random


def finding_number(random_list):
    # This function finds the largest number

    largest_number = random_list[0]
    for element in random_list:
        if element > largest_number:
            largest_number = element

    return largest_number


def main():
    # This is the main function

    generated_random_list = []

    print("Here is a list of random numbers:")
    print("")

    for counter in range(0, 10):
        random_number = random.randint(1, 100)
        generated_random_list.append(random_number)
        print("The random number {0} is: {1}".format(counter + 1, random_number))

    biggest_number = finding_number(generated_random_list)
    print("\nThe largest number is {0}".format(biggest_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
