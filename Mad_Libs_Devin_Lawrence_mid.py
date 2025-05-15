# FileName: Mad_Libs_Devin_Lawrence_mid.py
# # Name: Devin Lawrence
# Period: 5th Hour
# Date: May 9, 2025

# Function to play a fun Mad Lib game
def is_valid_word(word):
    # Check if the input is a valid word (letters only, no numbers or special characters)
    return word.isalpha()

def play_madlib():
    # Ask for seven words with clear, fun prompts
    print("\n=================================")
    adjective1 = input("Pick a cool adjective (describes something, like 'sparkly' or 'gross'): ")
    while not is_valid_word(adjective1):
        adjective1 = input("Please enter a valid adjective (letters only, like 'sparkly' or 'gross'): ")
    
    noun1 = input("Choose a noun (a thing or place, like 'pizza' or 'cave'): ")
    verb1 = input("Give an action word ending in -ing (something you do, like 'running' or 'laughing'): ")
    animal = input("Name a silly animal (a funny creature, like 'panda' or 'octopus'): ")
    place = input("Pick a fun place (somewhere cool, like 'beach' or 'spaceship'): ")
    object = input("Choose a weird thing (something odd, like 'slipper' or 'donut'): ")
    adjective2 = input("Pick another adjective (describes something, like 'shiny' or 'fuzzy'): ")
    while not is_valid_word(adjective2):
        adjective2 = input("Please enter a valid adjective (letters only, like 'shiny' or 'fuzzy'): ")

    # Make a longer Mad Lib story with Devin as the hero
    story = f"In the {adjective1} {place}, a {adjective2} {animal} was {verb1} with a {object}! "
    story += f"Suddenly, the heroic Devin zoomed in, holding a {noun1}, and shouted, 'This {object} needs a {adjective1} adventure!' "
    story += f"Devin led the {animal} through {place}, waving the {noun1} like a champion. "
    story += f"They spotted a {adjective2} {object} {verb1} on top of a giant {noun1}! "
    story += f"With a {adjective1} grin, Devin cheered, 'This is the wildest day in {place}!' "
    story += f"Devin and the {animal} built a {adjective2} fort out of {noun1}s and invited every {animal} around. "
    story += f"Soon, the whole {place} was {verb1} with {object}s, and Devin declared, "
    story += f"'This {adjective1} party will make us legends!'"

    # Show the story with multiple print commands
    print("\n=================================")
    print("\n=== Your Wacky Mad Lib Story ===")
    print("Get ready for an epic adventure!\n")
    print(story)
    print("\n=================================")
    print("\nThanks for playing!")
    print("Hope you had a blast in", place + "!")
    print("This game was made by D-E-V-I-N!")

# Welcome message with multiple print commands
print("Welcome to the Awesome Mad Lib Game!")
print("Give us some silly words to make a funny story!")
print("Follow the prompts and let's create something epic!\n")

# Start the game
play_madlib()