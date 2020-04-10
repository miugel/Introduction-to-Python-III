from room import Room
from player import Player
from item import Item

# declare all the rooms

room = {
    'outside': Room('Outside Cave Entrance', 'North of you, the cave mount beckons', [Item('Sword', 'A sword lies.'), Item('Flashlight', 'A flashlight lies.')]),
    'foyer': Room('Foyer', 'Dim light filters in from the south. Dusty passages run north and east.', [Item('Map', 'A map lies.')]),
    'overlook': Room('Grand Overlook', 'A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.', [Item('Ladder', 'A ladder lies.')]),
    'narrow': Room('Narrow Passage', 'The narrow passage bends here from west to north. The smell of gold permeates the air.', [Item('iPhone', 'An iPhone lies.')]),
    'treasure': Room('Treasure Chamber', "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", [Item('Coin', 'A coin lies.')]),
}

# link rooms together

room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']

room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']

# main

# make a new player object that is currently in the 'outside' room

print("\nEnter n, e, s, or w to move your player around.\nEnter 'take [item]' to take an item.\nEnter 'drop [item]' to drop an item.\nEnter i to view your inventory.\nEnter q anytime to exit the game.\n")
name = input('Give your player a name: ')
player = Player(name, room['outside'])
print(f'\n{player.name}, are currently in the {player.current_room.name}. {player.current_room.description}.')
for item in player.current_room.items:
    print(f'{item.description}')
move = input('\nEnter a command: ')

# write a loop that:
# prints the current room name
# prints the current description (the textwrap module might be useful here)
# waits for user input and decides what to do

# if the user enters a cardinal direction, attempt to move to the room there
# print an error message if the movement isn't allowed

# if the user enters 'q', quit the game

while move != 'q':
    if move == 'n':
        try:
            player.current_room = player.current_room.n_to
        except:
            print("\nYou can't go that way, try again.")
    elif move == 'e':
        try:
            player.current_room = player.current_room.e_to
        except:
            print("\nYou can't go that way, try again.")
    elif move == 's':
        try:
            player.current_room = player.current_room.s_to
        except:
            print("\nYou can't go that way, try again.")
    elif move == 'w':
        try:
            player.current_room = player.current_room.w_to
        except:
            print("\nYou can't go that way, try again.")

    elif len(move.split(' ')) == 2:
        if move.split(' ')[0] == 'take':
            for item in player.current_room.items:
                if item.name.lower() == move.split(' ')[1].lower():
                    player.current_room.remove_item(item)
                    player.add_item(item)
                    print(f"\nYou have added {move.split(' ')[1]} to your inventory.")
        elif move.split(' ')[0] == 'drop':
            for item in player.items:
                if item.name.lower() == move.split(' ')[1].lower():
                    player.remove_item(item)
                    player.current_room.add_item(item)
                    print(f"\nYou have removed {move.split(' ')[1]} from your inventory.")
        else:
            print('\nInvalid entry, try again.')

    elif move == 'i':
        if len(player.items) == 0:
            print('\nNo items in your inventory.')
        else:
            print(f'\nYour inventory:')
            for item in player.items:
                print(item.name)

    else:
        print('\nInvalid entry, try again.')

    print(f'\n{player.name}, are currently in the {player.current_room.name}. {player.current_room.description}.')
    if len(player.current_room.items) == 0:
        print('Room is empty.')
    else:
        for item in player.current_room.items:
            print(f'{item.description}')
    move = input('\nEnter a command: ')

print('\nGame over')