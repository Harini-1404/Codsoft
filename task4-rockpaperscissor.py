import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
