import random

def play_game():
    options = ["rock", "paper", "scissors"]
    play_round = 0
    player_score = 0
    loop_tag = "yes"

    print("Welcome to Rock, Paper, Scissors!")

    while loop_tag == "yes":
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        while player_choice not in options:
            player_choice = input("Invalid choice. Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(options)    
        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            player_score += 1
            print("Player wins!")
        else:
            print("Computer wins!")
        loop_tag = input("Do you want to play again? (yes/no): ").lower()
        while loop_tag not in ["yes", "no"]:
            loop_tag = input("Invalid choice. Do you want to play again? (yes/no): ").lower()
        play_round += 1
    
    print(f"You've played {play_round} rounds, your score is {player_score}. Thanks for playing!")


play_game()