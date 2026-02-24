"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.
Reqirements:
Set up the while loop with a flag
Use a guard clause to validate input to take only strings - provide a message and continue if it isn't a string
"""

user_input: str = ""
correct_input: bool = False

while user_input != "n":

    while not correct_input:
        user_input = input("Enter a pizza topping: ")

        if user_input.isdigit():
            print("Error: Invalid Input.")
            continue

        print(f"{user_input} will be added to your pizza.")
        correct_input = True
    
    user_input = input("Would you like to add more toppings? y/n: ")
    correct_input = False