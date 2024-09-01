import random



def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)



def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"



def print_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")



def main():
    user_score = 0
    computer_score = 0
    


    while True:
        print("\nWelcome to Rock, Paper, Scissors Game!")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        

        print_result(user_choice, computer_choice, result)
        

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break



if __name__ == "__main__":
    main()