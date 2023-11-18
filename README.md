# motioncut-python-task-2

# README: Adventure game (Task 2)

## Author: KEDHARESHWARA SUBBA REDDY S

## Batch:(5th NOVEMBER- 5th DECEMBER)

## Domain: PYTHON Programming

## Aim

To design and develop a text-based adventure game in Python. This project offers a fantastic opportunity to hone your programming skills, particularly in game development and user interaction.

## Description

Text-based Adventure Game in Python: Embark on an interactive journey with a captivating storyline, immersive user choices, and multiple endings.




  ## Working of the Code 



1. **Introduction (`introduction()`):**
   - The game begins with a welcome message, introducing the player to the Treasure Hunt Adventure and the quest for the hidden treasure in a dense forest.

2. **Choose Path (`choose_path()`):**
   - The player encounters a fork in the path and is prompted to choose between going left or right.
   - The choice determines the direction the player takes, leading to different parts of the adventure.

3. **Explore Cave (`explore_cave()`):**
   - If the player chooses the left path, they enter a dark cave.
   - Within the cave, the player faces another decision between a well-lit tunnel and a pitch-black tunnel.

4. **Dark Tunnel (`dark_tunnel()`):**
   - Choosing the pitch-black tunnel leads the player to a dark and eerie tunnel.
   - The player must decide whether to follow a dim light or stay in the dark.

5. **Crystal Room (`crystalroom()`):**
   - If the player chooses to follow the light, they discover a magical crystal, leading them to a crystal room filled with treasure.
   - This room signifies the successful completion of the game.

6. **Cross River (`cross_river()`):**
   - If the player initially chooses the right path, they come across a wide river.
   - The player must decide between using a boat or a rickety bridge to cross the river.

7. **Boat Success:**
   - Choosing the boat successfully navigates the player across the river.
   - After crossing, the player faces another decision point.

8. **Find Treasure (`find_treasure()`):**
   - Upon successfully navigating obstacles, the player finds the hidden treasure, and the game congratulates them as the legendary treasure hunter.

9. **Key 1 (`key1()`):**
   - If the player finds a key during the adventure, they can use it to exit an additional door and leave the island safely, albeit without the treasure.

10. **Game Over (`game_over()`):**
    - If the player makes a wrong choice or encounters a game-ending scenario (e.g., falling off the bridge), the game ends with a "Thanks for playing" message.

11. **Main (`main()`):**
    - Orchestrates the flow of the game by calling the different functions based on the player's choices, using a loop until the game concludes.
