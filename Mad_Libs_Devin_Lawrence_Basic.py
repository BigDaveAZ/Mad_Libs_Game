# FileName: Mad_Libs_Devin_Lawrence_Basic
# # Name: Devin Lawrence
# Period: 5th Hour
# Date: May 9, 2025

def play_madlib():
    # Prompt user for seven inputs
    animal = input("Enter a silly animal: ")
    place = input("Enter a place: ")
    object = input("Enter a weird object: ")
    action = input("Enter an action verb: ")
    color = input("Enter a color: ")
    food = input("Enter a food: ")
    adjective = input("Enter an adjective: ")
    
    # Print the Mad Lib story
    print("\nYour Mad Lib Story:\n")
    print(f"In the {adjective} land of {place}, a {color} {animal} named a Steve roamed.")
    print(f"One day, Steve found a {object} and decided to {action} it to help others.")
    print(f"Using the {object}, Devin shared {food} with everyone in {place}.")
    print(f"Thanks to Steve's kind act, the whole land became more {adjective}!")
    
# Run the game
play_madlib()