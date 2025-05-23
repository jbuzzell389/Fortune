import random

lucky_num = random.randint(1,100)

def fortune():

    fortune_color = input("\nPick a color: Red, Green, or Blue\n\n")

    if fortune_color == "red" or fortune_color == "Red":
        fortune_text = 'You will have a great day!'
    elif fortune_color == "green" or fortune_color == "Green":
        fortune_text = 'Today will be tough....but worth it.'
    elif fortune_color == "blue" or fortune_color == "Blue":
        fortune_text = 'You will get a cool job this year.'
    else:
        print("\nPlease try again")
        fortune()
    print(f'\n{fortune_text}\n\nYour lucky number is {lucky_num}\n')

fortune()
