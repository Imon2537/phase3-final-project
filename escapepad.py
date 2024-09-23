# escapepad.py
# escapepad.py

import os
from sqlalchemy.orm import sessionmaker
from model import UserProfile, GameSession, GameHistory, Leaderboard, engine
from games import tictactoe, rockpaperscissors, numberguessing

# Set up the database session
Session = sessionmaker(bind=engine)
db_session = Session()

# Clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display welcome message
def display_welcome_message():
    print("Welcome to Escapepad!")
    print("Escape, relax, and enjoy.")
    print("=" * 40)

# Main Menu
def main_menu(user):
    print("\nMain Menu:")
    print("1. Play Tic Tac Toe")
    print("2. Play Rock Paper Scissors")
    print("3. Play Number Guessing Game")
    print("4. View Game History")
    print("5. View Leaderboard")
    print("6. Exit Escapepad")
    
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        play_game(user, "Tic Tac Toe", tictactoe.tic_tac_toe)
    elif choice == "2":
        play_game(user, "Rock Paper Scissors", rockpaperscissors.rock_paper_scissors)
    elif choice == "3":
        play_game(user, "Number Guessing", numberguessing.number_guessing_game)
    elif choice == "4":
        view_game_history(user)
    elif choice == "5":
        view_leaderboard(user)
    elif choice == "6":
        print("Thanks for using Escapepad! Goodbye.")
        exit()
    else:
        print("Invalid choice. Please enter a valid option.")
        main_menu(user)

# Play a game
def play_game(user, game_name, game_func):
    # Start a new session
    session = GameSession(user_id=user.id)
    db_session.add(session)
    db_session.commit()

    clear_screen()
    outcome = game_func()

    # Record the game history
    game_history = GameHistory(session_id=session.id, game_name=game_name, outcome=outcome)
    db_session.add(game_history)
    db_session.commit()

    input("\nPress Enter to return to the main menu...")
    clear_screen()
    main_menu(user)

# View game history
def view_game_history(user):
    clear_screen()
    sessions = db_session.query(GameSession).filter_by(user_id=user.id).all()
    for session in sessions:
        print(f"Session ID: {session.id}, Games Played: {session.games_played}, Start Time: {session.start_time}")
    input("\nPress Enter to return to the main menu...")
    main_menu(user)

# View leaderboard
def view_leaderboard(user):
    clear_screen()
    leaderboard = db_session.query(Leaderboard).order_by(Leaderboard.score.desc()).all()
    for entry in leaderboard:
        print(f"Username: {entry.username}, Game: {entry.game_name}, Score: {entry.score}")
    input("\nPress Enter to return to the main menu...")
    main_menu(user)

# Create or login user
def login():
    username = input("Enter your username: ")
    user = db_session.query(UserProfile).filter_by(username=username).first()
    if user is None:
        user = UserProfile(username=username)
        db_session.add(user)
        db_session.commit()
    return user

# Run Escapepad
def escapepad():
    clear_screen()
    display_welcome_message()
    user = login()
    main_menu(user)

if __name__ == "__main__":
    escapepad()
