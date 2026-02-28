Ogre Text Adventure Game
Overview

The Ogre Text Adventure Game is a Python-based text adventure where players navigate through different rooms, collect items, and aim to defeat the Ogre. The goal is to collect all six required items before reaching the Dungeon.

The game demonstrates basic Python programming concepts such as dictionaries, functions, loops, and conditionals while providing an interactive gameplay experience.

--------------------------------------------------

Project Structure:
project_root/
│
├── main.py       # Main game logic and loop
├── README.md     # Project documentation

-------------------------------------------------

How to Play

1. Run the game with Python:
   python main.py

2. The game starts in the Village. Follow the instructions displayed.
3. Commands:
  • Move: go North, go South, go East, go West
  • Collect items: get 'item name'
4. Objective:
  • Collect all 6 items:
    • Shovel
    • Sword
    • P. Onion
    • Stones
    • Gem
    • Blanket
  • Reach the Dungeon to defeat the Ogre.

  • If you enter the Dungeon without all items, the game ends in a loss.

--------------------------------------------------

Features:
• Text-based adventure with multiple rooms.
• Inventory management to track collected items.
• Room-based navigation using directions.
• Automatic checks for victory or defeat conditions.
• Interactive gameplay with input validation.

--------------------------------------------------

Python Concepts Used:
• Dictionaries – for room mapping and items.
• Functions – modular game logic (show_status, check_inventory, obtain_item, etc.).
• Loops – continuous gameplay until victory or loss.
• Conditionals – handle player actions and game rules.
• Lists – manage player inventory.

----------------------------------------------------

Example Gameplay:
You are currently in the: Village
The rooms you can see are: {'South': 'Cave', 'North': 'Dungeon'}
Inventory []

Enter your move: go South

You are currently in the: Cave
The rooms you can see are: {'North': 'Village', 'East': 'Jungle', 'West': 'River', 'item': 'Shovel'}
Inventory []

You see a Shovel
Enter your move: get Shovel

Shovel added to your inventory!

--------------------------------

Requirements
• Python 3.x
  No external libraries are required; the game runs using standard Python libraries.

--------------------------------

Notes:
• This game is designed for learning and demonstration of Python fundamentals.
• You can expand the game by adding more rooms, items, or complex challenges.
