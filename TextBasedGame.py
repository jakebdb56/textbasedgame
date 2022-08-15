# Jake Brown IT140 Intro to Scripting
# Project Two Submission

# Print welcome screen and basic info.  press any key to start
def showinstructions():
    print('\nWelcome to the clean up your house before your crazy mother comes over game!')
    print('Travel between rooms and collect all the items before you find the villain.')
    print('Otherwise, she will let out a horrific screech and kill you!\n')
    print('To navigate, enter room direction. To pick up item enter "yes" at the prompt.\n')
    advance = input('PRESS ENTER TO START\n\n')

# Dictionary of rooms and moves possible for each room in the game
rooms = {
    'Dining Room': {'EAST': 'Kitchen'},
    'Kitchen': {'WEST': 'Dining Room', 'EAST': 'Garage', 'SOUTH': 'Living Room'},
    'Garage': {'WEST': 'Kitchen'},
    'Master Bedroom': {'EAST': 'Living Room'},
    'Living Room': {'NORTH': 'Kitchen', 'EAST': 'Sunroom', 'SOUTH': 'Child Room', 'WEST': 'Master Bedroom'},
    'Sunroom': {'WEST': 'Living Room', 'SOUTH': 'Backyard'},
    'Child Closet': {'EAST': 'Child Room'},
    'Child Room': {'NORTH': 'Living Room', 'WEST': 'Child Closet'},
    'Backyard': {'NORTH': 'Sunroom'}
}

# Dictionary of rooms that list their respective items and a status bit indicating if it is present
items = {
    'Dining Room': 'Villain',
    'Kitchen': 'Cutlery',
    'Master Bedroom': 'Stuffed Monkey',
    'Sunroom': 'Ear Plugs',
    'Child Closet': 'Tools',
    'Child Room': 'Rad Dad T-Shirt',
    'Backyard': 'Squirt Gun',
    'Garage': 'None',
    'Living Room': 'None'
}


# Define function moveroom
def moveroom():
    current_position = location_index[0]

    print('You may proceed to the following:', rooms[current_position], '\n')
    print('Please enter your move (North/East/South/West) or EXIT to stop\n')

    current_possible_moves = []

    # Populate list of possible moves from current position
    for i in rooms[current_position]:
        current_possible_moves.append(i)

    desired_move = input().upper()

    # Run if/elif to determine if the input is a valid move
    # If the move is valid, print the move, clear the possible moves list and store location index
    # If exit is entered, exit program
    if desired_move not in current_possible_moves and desired_move != 'EXIT':
        print('Invalid input, try again!\n')
    elif desired_move in current_possible_moves:
        new_room = rooms[current_position][desired_move]
        print('Moving Rooms\n')
        current_possible_moves.clear()
        location_index[0] = new_room
    elif desired_move == 'EXIT':
        print('Thanks for playing, Bye!')
        exit()


# Define inventory function to process items and inventory
def showstatus():
    # Establish local vars for processing and an empty list to store possible items
    current_position = location_index[0]
    current_possible_items = []
    current_room_item = items[current_position]

    # If statement to capture whether you have all the items
    # Once all items are captured go find the boss to defeat her
    # Also let payer know how many more items they need to win
    if len(item_collection) >= 6 and current_room_item.upper() == 'VILLAIN':
        print('You won!!!\nYou gathered all the items and defeated the boss!\n\n＼(^o^)／\n\nThanks for playing!')
        exit()
    elif current_room_item.upper() == 'VILLAIN' and len(item_collection) < 6:
        print('You do not have all the items and the crazy mother has killed you!!!')
        print('You died!\nGame Over!\n')
        print('░▒▒ 💀 ▒▒░')
        exit()
    elif current_room_item.upper() == 'NONE':
        print('There are no items in the', current_position)
        return

    # Print current location and current inventory contents
    print('Your current position is the', current_position)

    if len(item_collection) < 6:
        total_items = len(item_collection)
        print('You have the following items:', item_collection, '\n')
        print('You need', 6 - total_items, 'more items to win!\n')
    elif len(item_collection) >= 6:
        print('YOU HAVE ALL THE ITEMS, GO FIGHT THE BOSS!!!')

    # If statement to process if room's item is in your inventory
    # Prompt user to pick up the item if item not already in inventory
    if current_room_item not in item_collection:
        print('You have come across the item', current_room_item, 'in', current_position)
        print('Would you like to pick it up? (enter "yes" to pick up item)\n')
        prompt_answer = input().upper()
        if prompt_answer == 'YES':
            item_collection.append(current_room_item)
            print('Great, you picked up', current_room_item, '\n')
        elif prompt_answer == 'NO':
            print('You need all items to win!')
        current_possible_items.clear()
    elif current_room_item in item_collection:
        print('No items left in room')


# Start alive_status bit to 1 indicating player is alive and enabling loop to run
# Establish location list holding the current location and init as Living Room to start game
alive_status = 1
location_index = ['Living Room']

# Establish empty item collection list to store collected items in
item_collection = []

# Print instructions
showinstructions()

# While loop to make game run through until you're not alive
while alive_status > 0:
    showstatus()
    moveroom()
