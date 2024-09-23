## ESCAPEPAD(CLI GAMING PLARTFORM)
Escapepad is a Python-based Command-Line Interface (CLI) gaming platform designed for users seeking a fun and relaxing escape from their daily routines. It offers a variety of games that can be played directly from the terminal and includes features such as game history tracking, leaderboards, and user session management.

### Features
1. Multiple Games:
- Tic Tac Toe
- Rock Paper Scissors
- Number Guessing Game
2. Game History Tracking: 
- Records the outcomes (win/lose/draw) of each game played by the user.
3. Leaderboard: 
- Displays top scores for competitive games, allowing users to see how they rank against others.
4. Session Tracking:
- Manages user sessions and tracks the games played in each session.
5. Database Integration:
- SQLAlchemy is used to store user profiles, session history, game outcomes, and leaderboard data.

### Installation and Setup
#### Prerequisites
. Python 3.x
. pip for package management
#### Installation
- Clone the repository:
git clone https://github.com/username/escapepad.git
cd escapepad

- Install the required dependencies:
pip install -r requirements.txt

- Set up the database:

python database_setup.py
- Run the main application:
python escapepad.py
#### How to Play
When you run the escapepad.py file, you'll be presented with a main menu:

Main Menu:
1. Play Tic Tac Toe
2. Play Rock Paper Scissors
3. Play Number Guessing Game
4. View Game History
5. View Leaderboard
6. Exit Escapepad
## Games
1. Tic Tac Toe: Classic two-player game where you aim to get three of your symbols in a row (horizontally, vertically, or diagonally).
2. Rock Paper Scissors: A best-of-three game where you choose between rock, paper, or scissors, trying to beat the computer.
3. Number Guessing Game: Try to guess the randomly generated number within a limited number of attempts.
## Game History and Leaderboards
- Game History: View all the games you’ve played, along with the outcomes.
- Leaderboard: Displays the top scores for competitive games like Rock Paper Scissors.
## Database Models
Escapepad uses SQLAlchemy for database management. Below is a summary of the key models:

- User: Tracks user information.
- Session: Logs individual sessions where a user plays games.
- GameSession: Keeps track of each session’s specific games.
- GameHistory: Records the outcomes (win/lose) for each game played.
- Leaderboard: Stores scores for competitive games.
## Testing
- The project includes test cases for each game to ensure they are functioning as expected. To run the tests:

python3 escapepad.py

- This will also allow you to play the games interactively during testing.

## Future Features
- User Authentication: Add features for registering and logging in users.
- Additional Games: More games could be added to make the platform even more engaging.
- Game Save/Resume: Implement save-and-resume functionality for games with longer play durations.
## Contributing
If you would like to contribute to this project, please fork the repository, make your changes, and create a pull request. We welcome contributions that improve the platform or add new features!

## AUTHOR
ian mwenda
software engineering student

https://www.loom.com/share/6e79bf8f2ff54714901720878ec5e64f?sid=f62ec095-23ef-49b7-9dbd-de9480ce27c7