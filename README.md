# Crossing Road – Turtle Crossing Game 🐢🚗

This is a recreation of the classic "Frogger"-style game using Python's `turtle` module. It was built as part of the **100 Days of Code: The Complete Python Pro Bootcamp**.

---

##  Game Overview

Guide your turtle safely across a busy road filled with moving cars. Each successful crossing speeds up traffic, increasing the challenge. Avoid collisions — touching a car ends the game.

---

##  Project Structure

- **`main.py`** – The entry point:
  - Sets up the screen
  - Creates the player turtle
  - Initializes the car manager and scoreboard
  - Runs the main game loop

- **`player.py`** – Contains the `Player` class:
  - Manages turtle movement (controls, starting position)
  - Handles detecting successful crossings

- **`car_manager.py`** – Contains the `CarManager` class:
  - Creates and stores multiple cars
  - Moves them across the screen
  - Increases speed as you progress

- **`scoreboard.py`** – Contains the `Scoreboard` class:
  - Displays the current level at the top
  - Shows "Game Over" upon collision

---

##  How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/IvanShepeta/CrossingRoad.git
   cd CrossingRoad

