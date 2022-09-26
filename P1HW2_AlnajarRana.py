#A brief description of the project: This program calculates and displays travel expenses.
#Date 9/26/2022
#CTI-110 P1HW2- Basic Math
#Your Name : Rana Alnajar

print("This program calculates and displays travel expenses\n")
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accomodation = float(input("\nApproximately, how much will you need for accomodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

print("\n------------Travel Expenses------------")
print("Location:",destination)
print("Initial Budget:",budget)

print("\nFuel:",gas)
print("Accomodation:",accomodation)
print("Food",food)

balance = budget - gas - accomodation - food
print("\nRemaining Balance:",balance)