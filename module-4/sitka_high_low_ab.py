"""
sitka_high_low_ab.py

This program reads weather data for Sitka from a CSV file and allows the user
to choose whether they want to see daily high temperatures, low temperatures,
or exit the program.
"""

import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt
from pathlib import Path


# Get the CSV file from the same directory as this script
# This avoids issues with where the program is run from
csv_file = Path(__file__).with_name("sitka_weather_2018_simple.csv")


# Load weather data once at the start so we don’t keep reopening the file
dates, highs, lows = [], [], []

try:
    with open(csv_file) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # Skip the header row

        # Go through each row in the CSV file
        for row in reader:
            # Convert the date string into a datetime object
            current_date = datetime.strptime(row[2], "%Y-%m-%d")

            # Convert temperature values to integers
            high = int(row[5])
            low = int(row[6])

            # Store the values so we can plot them later
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

except FileNotFoundError:
    print("Weather data file not found. Program cannot continue.")
    sys.exit()


# Display menu options for the user
def display_menu():
    print("\n--- Sitka Weather Menu ---")
    print("Type one of the following options:")
    print("highs - view daily high temperatures")
    print("lows  - view daily low temperatures")
    print("exit  - quit the program")


# Plot temperature data based on the user’s choice
def plot_temps(temp_list, color, title):
    fig, ax = plt.subplots()
    ax.plot(dates, temp_list, c=color)

    plt.title(title, fontsize=24)
    plt.xlabel("")
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


# Main program loop runs until the user chooses to exit
while True:
    try:
        display_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "highs":
            # Show high temperatures in red
            plot_temps(highs, "red", "Daily High Temperatures - 2018")

        elif choice == "lows":
            # Show low temperatures in blue
            plot_temps(lows, "blue", "Daily Low Temperatures - 2018")

        elif choice == "exit":
            # Exit the program cleanly
            print("Exiting program. Have a good day!")
            break

        else:
            # Handle invalid menu options
            print("Invalid option. Please type: highs, lows, or exit.")

    except KeyboardInterrupt:
        # Allow the user to exit using Ctrl+C
        print("\nCaught Ctrl+C — exiting program. Goodbye!")
        break
