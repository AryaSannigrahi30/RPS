# ✊ Rock-Paper-Scissors Game

A simple and beginner-friendly Rock-Paper-Scissors Game built using Python. This project allows the user to choose rock, paper, or scissors while the computer randomly selects one of the three choices. The program compares both choices and determines the winner. The user can continue playing multiple rounds or quit the game whenever they want.

## 📌 Features

- Allows the user to choose Rock, Paper, or Scissors.
- Computer randomly selects Rock, Paper, or Scissors.
- Determines the winner based on the game rules.
- Displays the user's choice.
- Displays the computer's choice.
- Shows whether the user wins, loses, or gets a draw.
- Allows the user to play multiple rounds.
- Provides an option to quit the game.
- Handles invalid user input.
- Simple and easy-to-use command-line interface.
- Beginner-friendly Python project.

## 🛠️ Technologies Used

- Python
- Random Module

## 📂 Project Structure

Rock-Paper-Scissors/
│
├── RPS.py
└── README.md

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository using the following command:

```bash
git clone https://github.com/your-username/RPS.git
```

Open the project folder:

```bash
cd RPS
```

Run the Python program:

```bash
python RPS.py
```

Enter `rock`, `paper`, or `scissors` when prompted.

To exit the game, enter:

```text
quit
```

## 💻 Example Output

```text
===== ROCK PAPER SCISSORS =====

Enter rock, paper, scissors (or quit): rock

You chose: rock
Computer chose: scissors
You Win! 🎉

Enter rock, paper, scissors (or quit): paper

You chose: paper
Computer chose: paper
It's a Draw! 🤝

Enter rock, paper, scissors (or quit): quit

Thanks for playing!
```

The computer's choice will be different each time because the program uses random selection.

## 🧠 How It Works

The program first imports Python's built-in `random` module.

A list containing the three possible choices is created:

```python
choices = ["rock", "paper", "scissors"]
```

The program then asks the user to enter their choice. The `.lower()` function is used so that inputs such as `Rock`, `ROCK`, and `rock` are treated in the same way.

The computer randomly selects one option using:

```python
computer = random.choice(choices)
```

The program then compares the user's choice with the computer's choice.

The rules of the game are:

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- Same choices result in a Draw.

The program uses `if`, `elif`, and `else` statements to determine the result.

The `while True` loop allows the user to play continuously until they enter `quit`.

If the user enters an invalid choice, the program displays an error message and asks for another choice.

## 🎮 Game Rules

| User Choice | Computer Choice | Result |
|-------------|-----------------|--------|
| Rock | Scissors | User Wins |
| Scissors | Paper | User Wins |
| Paper | Rock | User Wins |
| Rock | Paper | Computer Wins |
| Paper | Scissors | Computer Wins |
| Scissors | Rock | Computer Wins |
| Rock | Rock | Draw |
| Paper | Paper | Draw |
| Scissors | Scissors | Draw |

## 🎯 Purpose

The purpose of this project is to create a simple interactive Rock-Paper-Scissors game while practicing basic Python programming concepts such as user input, variables, lists, loops, conditional statements, modules, and random selection.

## 📚 Learning Outcome

Through this project, I learned how to use Python's built-in `random` module, take input from users, work with lists, use loops and conditional statements, validate user input, and implement basic game logic.

This project also helped me gain practical experience in developing an interactive command-line application using Python.

## 🔍 Program Concepts Used

- Variables
- Lists
- User Input
- `if`, `elif`, and `else` statements
- `while` loop
- `break` and `continue`
- String methods
- Random selection
- Basic game logic
- Input validation
- Python modules

## 🚀 Future Improvements

The project can be improved in the future by:

- Adding score tracking for the user and computer.
- Adding a best-of-three or best-of-five game mode.
- Adding a graphical user interface (GUI).
- Adding sound effects and animations.
- Adding different difficulty levels.
- Adding a high-score system.
- Creating a more attractive and interactive interface.

## 🙏 Acknowledgement

This project was created as part of a Python Internship Task. It helped me understand and practice fundamental Python programming concepts through a practical and interactive project.

## 👨‍💻 Author

**Arya Sannigrahi**

CSE Student
