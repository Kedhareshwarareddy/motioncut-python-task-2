def introduction():
    print("Welcome to the Treasure Hunt Adventure!")
    print("You find yourself in a dense forest, and legends speak of a hidden treasure deep within.")
    
    print("Your goal is to navigate through the forest, overcome obstacles, and find the treasure.")
    

def choose_path():
    print("\nYou come across a fork in the path. Do you want to go left or right?")
    choice = input("Enter 'left' or 'right': ")
    if choice == "left":
        return "cave"
    elif choice == "right":
        return "river"
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        return choose_path()

def explore_cave():
    print("\nYou enter a dark cave.")
    
    print("As you move deeper, you see two tunnels. One is well-lit, and the other is pitch black.")
    choice = input("Enter 'lit' or 'dark': ")
    if choice == "lit":
        print("\nYou find a key that might unlock the next door on your journey.")
        return "key"
    elif choice == "dark":
        print("\nIt's too dark to see, and you a enter a dark tunnel")
        return "dark_tunnel"
    else:
        print("Invalid choice. Please enter 'lit' or 'dark'.")
        return explore_cave()
def dark_tunnel():
    print("\nYou enter a dark and eerie tunnel.")
    print("Strange whispers surround you, and you see a dim light in the distance.")
    choice = input("Do you want to 'follow' the light or 'stay' in the dark? ")
    if choice == "follow":
        print("\nYou discover a magical crystal that illuminates your path.")
        return "crystal_room"
    elif choice == "stay":
        print("\nThe darkness consumes you, and you get lost. Game Over!")
        return "game_over"
    else:
        print("Invalid choice. Please enter 'follow' or 'stay'.")
        return dark_tunnel()

def cross_river():
    print("\nYou come across a wide river.")
    
    print("You need to find a way to cross it. A boat is available, but there's also a rickety bridge.")
    choice = input("Enter 'boat' or 'bridge': ")
    if choice == "boat":
        print("\nYou successfully navigate the boat across the river.")
        return "boat_success"
    elif choice == "bridge":
        print("\nThe bridge collapses, and you fall into the river.YOU DIE!")
        return "game_over"
    else:
        print("Invalid choice. Please enter 'boat' or 'bridge'.")
        return cross_river()

def find_treasure():
    print("\nCongratulations! You find the hidden treasure!")
    
    print("You are now the legendary treasure hunter!")
    return "game_over"

def key1():
    print("You found key to an exit door.You got out of island safely without treasure.THANKS FOR PLAYING THE GAME")
    exit()
def crystalroom():
    print("following the light,it will lead you to a room")
    print("You enter a crystal room filled with TREASURE!!!!!")
    print("\n At the end of room you will find an escape room")
    print("congratulations!YOU ARE THE LEGENDARY REASURE HUNTER")
    return "game_over"

def game_over():
    print("\nThanks for playing the Treasure Hunt Adventure!")
    exit()

def main():
    introduction()
    current_location = choose_path()

    while True:
        if current_location == "cave":
            current_location = explore_cave()
        elif current_location == "river":
            current_location = cross_river()
        elif current_location=="dark_tunnel":
            current_location=dark_tunnel()
        elif current_location=="crystal_room":
            current_location=crystalroom()
        elif current_location == "key":
            current_location ==key1()
        elif current_location == "boat_success":
            print("\nYou reach the other side of the river.")
            current_location = choose_path()
        elif current_location == "game_over":
            game_over()

if __name__ == "__main__":
    main()

