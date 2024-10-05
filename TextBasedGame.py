# Gabriel Castillo

# Show instructions at the beginning of the game
def show_instructions():
    print("Ogre Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the Ogre.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


# Shows what room player is in, rooms that within view, and inventory
def show_status():
    print("You are currently in the: ", currentRoom)
    print("The rooms you can see are: ", rooms[currentRoom])
    print("Inventory", inventory)


# This method whether all items have been gathered to defeat the Ogre
def check_inventory():
    if len(inventory) == 6:
        print(
            "Congratulations! You have collected all the required items and have slayed the Ogre. Thank you for playing.")
        exit(1)

    if currentRoom == 'Dungeon' and len(inventory) != 6:
        print("You have failed to gather all required items. You lost the game.")
        exit(1)


# Checks the room whether the item is available
def check_for_item():
    for item in rooms.get(currentRoom):
        if item == 'item':
            print("You see a ", rooms.get(currentRoom).get(item))

        elif item == 'Ogre':
            check_inventory()


# Obtain the item from the room
def obtain_item(room_item):
    if rooms.get(currentRoom).get('item') is None:
        print("This item has been retrieved or not a valid item")

    elif room_item in rooms.get(currentRoom).get('item'):
        inventory.append(rooms.get(currentRoom).pop('item'))


# A dictionary for the simplified Ogre text game
# The dictionary links a room to other rooms.
rooms = {
    'Village': {'South': 'Cave', 'North': 'Dungeon'},
    'Cave': {'North': 'Village', 'East': 'Jungle', 'West': 'River', 'item': 'Shovel'},
    'Jungle': {'East': 'Cave', 'North': 'Forest', 'item': 'Sword'},
    'Forest': {'South': 'Jungle', 'North': 'Woods', 'item': 'P. Onion'},
    'Woods': {'South': 'Forest', 'East': 'Dungeon', 'item': 'Stones'},
    'River': {'West': 'Cave', 'North': 'Plains', 'item': 'Gem'},
    'Plains': {'South': 'River', 'item': 'Blanket'},
    'Dungeon': {'South': 'Village', 'West': 'Woods', 'item': 'Ogre'},
}

# Place player in the village
currentRoom = list(rooms.keys())[0]
inventory = []

EXIT = True
show_instructions()
while EXIT:
    # Show players status
    print()
    show_status()
    check_inventory()

    # Get command from player
    # What is the command?
    command = input("Enter your move: ")

    # when the user uses the "go command"
    if command[:2] == "go":  # test if the user used the "go" command

        # get the argument after the word "go"
        direction = command[3:]

        # test if the user can move in that direction
        if direction in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][direction]
            check_for_item()
        else:
            print("That is not a valid direction")
    # obtain the string item
    elif command[:3] == 'get':
        item = command[4:]
        obtain_item(item)
    else:
        print("That is not a valid command")
