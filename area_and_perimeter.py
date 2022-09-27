#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Sep 2022
# This program calculates the area and perimeter of a circle
#    with radius inputted from the user

import math


def main():
    # this function calculates the area and perimeter of a rectangle

    # input
    length_of_rectangle = int(input("Enter length of rectangle (mm): "))
    width_of_rectangle = int(input("Enter width of rectangle (mm): "))

    # process
    area_of_rectangle = length_of_rectangle * width_of_rectangle
    perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)

    # output
    print("")
    print("Area is {0} mm².".format(area_of_rectangle))
    print("Perimeter is {0}3 mm.".format(perimeter_of_rectangle))


    print("\nDone.")


if __name__ == "__main__":
    main()
