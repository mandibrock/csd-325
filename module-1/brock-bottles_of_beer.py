# ----------------------------------------------
# Author: Amanda Brock
# Date: January 18, 2026
# Assignment: Module 2.2
# Purpose of Code: Asks the user how many bottles of beer are on the wall
# and counts down to 1, displaying the lyrics of the song along the way.
# At the end, the program reminds the user to buy more beer.
# ----------------------------------------------

def countdown(bottles): # This is the function to count down the number of beer bottles.

    # Loops until there is only 1 bottle left
    while bottles > 1:
        # Display the current number of bottles
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        # Decrease bottles by 1
        bottles -= 1
        # Display the action of taking one down
        print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")

    # Special case for 1 bottle
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall.\n")


def main(): # Main program function

    # Ask user for number of bottles
    bottles = int(input("How many bottles of beer are on the wall? "))
    # Call the countdown function with the user's input
    countdown(bottles)
    # Print reminder to buy more beer
    print("Time to buy more beer!")


main()