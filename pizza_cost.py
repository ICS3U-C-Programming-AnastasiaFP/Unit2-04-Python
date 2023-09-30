#!/usr/bin/env python3
# Created by: Anastasia Friedenstein PAtino
# Created on: September 30th, 2023
# This program asks the user for the diameter of the
# pizza. It then calculates and displays the total cost
# of the pizza with tax
import constants


def main():
    # insert diameter
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # calculations for the price
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # total cost is displayed
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
