def game_instructions():
    print("""
Welcome to the Dungeon Adventure Game!
---------------------------------------
You find yourself in a mysterious dungeon with multiple rooms. Your goal is to find the treasure and escape victorious.

Rules and How It Works:
1. You can explore rooms by moving in different directions (north, south, etc.).
2. Each room has a unique description, and some rooms may have items.
3. You can pick up items and use them to overcome obstacles or unlock hidden areas.
4. Pay attention to the descriptions for clues and hints.

Hint to Win:
- Find the lantern to light up dark areas.
- Find the key to unlock the treasure room.
- Collect the treasure to win the game.

Commands:
- Type 'move' to explore a new room.
- Type 'pick up' to collect an item in the room.
- Type 'use' to use an item from your inventory.
- Type 'exit' to quit the game.

Good luck, adventurer!
    """)

def display_room(room):
    print(f"\n{room['description']}")
    if room['items']:
        print(f"Items here: {', '.join(room['items'])}")
    print(f"Exits: {', '.join(room['exits'].keys())}")

def move_to_room(current_room, direction, rooms):
    if direction in rooms[current_room]['exits']:
        return rooms[current_room]['exits'][direction]
    else:
        print("You can't go that way.")
        return current_room

def pick_up_item(current_room, inventory, rooms):
    if rooms[current_room]['items']:
        item = rooms[current_room]['items'].pop(0)
        inventory.append(item)
        print(f"You picked up {item}.")
    else:
        print("There is nothing to pick up here.")

def use_item(item, inventory, rooms):
    if item in inventory:
        if item == "key" and "locked door" in rooms["treasure room"]['description']:
            rooms["treasure room"]['description'] = "You see a room with a glowing treasure chest!"
            print("You used the key to unlock the treasure room!")
            inventory.remove(item)
        elif item == "lantern":
            print("The lantern lights up the dark corridor, revealing a hidden passage!")
        else:
            print(f"You can't use {item} here.")
    else:
        print("You don't have that item.")

def check_victory(current_room, inventory):
    return current_room == "treasure room" and "treasure" in inventory

def game():
    rooms = {
        "entrance": {
            "description": "You are at the entrance of an eerie dungeon.",
            "items": [],
            "exits": {"north": "dark corridor"}
        },
        "dark corridor": {
            "description": "A pitch-black corridor. You need light to proceed further.",
            "items": ["lantern"],
            "exits": {"south": "entrance", "north": "locked door"}
        },
        "locked door": {
            "description": "A locked door blocks your way.",
            "items": ["key"],
            "exits": {"south": "dark corridor", "north": "treasure room"}
        },
        "treasure room": {
            "description": "A room with a glowing treasure chest!",
            "items": ["treasure"],
            "exits": {"south": "locked door"}
        }
    }

    current_room = "entrance"
    inventory = []

    while True:
        display_room(rooms[current_room])
        if check_victory(current_room, inventory):
            print("Congratulations! You found the treasure and won the game!")
            break

        action = input("\nWhat would you like to do? (move/use/pick up/exit): ").lower()
        if action == "move":
            direction = input("Which direction? ").lower()
            current_room = move_to_room(current_room, direction, rooms)
        elif action == "pick up":
            pick_up_item(current_room, inventory, rooms)
        elif action == "use":
            item = input("Which item? ").lower()
            use_item(item, inventory, rooms)
        elif action == "exit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action.")

game_instructions()
game()
