# Jake Brown IT140 Intro to Scripting
# Project Two Submission

print('Welcome to the clean up your house before your crazy mother comes over game!')
print('Travel between rooms and collect all the items before you find the boss!\n')

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
    'Child Room': 'Dad\'s Tools',
    'Backyard': 'Squirt Gun',
    'Garage': 'None',
    'Living Room': 'None'
}


# Define function moveroom
def moveroom():
    current_position = location_index[0]
    print('Your current position is the', current_position)
    print('You may proceed to the following:', rooms[current_position])
    print('Please enter your move or EXIT to stop\n')

    current_possible_moves = []

    # Populate list of possible moves from current position
    for i in rooms[current_position]:
        current_possible_moves.append(i)

    desired_move = input().upper()

    # FIXME : add a loop that spits out a neater version of directions/locations

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
def inventory():
    # Establish local vars for processing and an empty list to store possible items
    current_position = location_index[0]
    current_possible_items = []
    current_room_item = items[current_position]

    # If no item available, then return to loop
    if current_room_item.upper() == 'VILLAIN' and len(item_collection) < 6:
        print('You do not have all the items and the Villain has killed you!')
        print('Game Over!\nWhomp Whomppp')
        exit()
    elif current_room_item.upper() == 'NONE':
        print('No items in this room\n')
        return

    # Print contents of current inventory
    print('You have collected the following items:', item_collection, '\n')

    # If statement to process if room's item is in your inventory
    # Prompt user to pick up the item
    if current_room_item not in item_collection:
        print('You have come across the item', current_room_item, 'in', current_position)
        print('Would you like to pick it up?\n')
        prompt_answer = input().upper()
        if prompt_answer == 'YES':
            item_collection.append(current_room_item)
        elif prompt_answer == 'NO':
            print('You need all items to win!')
        current_possible_items.clear()
    elif current_room_item in item_collection:
        print('No items left in room')


# Start alive_status bit to 1 indicating player is alive
# Set inventory status bit to 0 indicating that inventory hasn't been fulfilled
# Establish location list holding the current location and init as Living Room to start game
alive_status = 1
inventory_status = 0
location_index = ['Living Room']

# Establish empty item collection list to store collected items in
item_collection = []

# establish list of valid move inputs and an empty list of possible moves
valid_moves = ['NORTH', 'EAST', 'SOUTH', 'WEST']


# Define showstatus function that incorporates moveroom and inventory functions

def showstatus():
    moveroom()
    inventory()

    # Print inventory items
    print('You have the following items:', item_collection)

    # If statement to capture whether you have all the items
    # Once all items are captured, game is over!
    # Also let payer know how many more items they need to win
    if len(item_collection) >= 6:
        print('You won!\nYou gathered all the items.  Thanks for playing!')
        exit()
    elif len(item_collection) < 6:
        total_items = len(item_collection)
        print('You need', 6 - total_items, 'more items to win!\n')


# While loop to make game run through until you're not alive
while alive_status > 0:
    showstatus()
