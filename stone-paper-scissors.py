import random

# Start the game loop
for _ in range(1, 100):
    # Ask for user input
    user_choice = input("\nEnter your choice (stone/paper/scissors): ").strip().lower()

    if user_choice == '':
        print("Please provide an input!\n")
        continue  # Skip to next iteration if input is empty

    # Validate user input
    if user_choice not in ['stone', 'paper', 'scissors']:
        print("Invalid choice! Please enter stone, paper, or scissors.")
        continue

    # Computer randomly selects an option
    comp_choice = random.choice(['stone', 'paper', 'scissors'])
    print(f"Computer chose: {comp_choice}")

    # Determine winner
    if user_choice == comp_choice:
        print("It's a draw!")
    elif (
        (user_choice == 'stone' and comp_choice == 'scissors') or
        (user_choice == 'paper' and comp_choice == 'stone') or
        (user_choice == 'scissors' and comp_choice == 'paper')
    ):
        print("You win!")
    else:
        print("You lose!")
