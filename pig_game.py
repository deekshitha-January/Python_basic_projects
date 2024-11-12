


import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Get the number of players
while True:
    players = input("Enter the number of players (2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2 and 4.")
    else:
        print("Invalid input. Please enter a number.")

max_score = 20
player_scores = [0] * players

# Start the game
while True:
    for player_index in range(players):
        print("\nPlayer", player_index + 1, "'s turn has started!\n")
        current_score = 0
        
        # Player's turn loop
        while True:
            roll_choice = input("Would you like to roll (y)? ").lower()
            
            if roll_choice != "y":
                break
            
            value = roll()

            if value == 1:
                print("Turn over. You rolled a 1.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your current turn score is:", current_score)
                
                # Check if player reaches or exceeds max score
                if player_scores[player_index] + current_score >= max_score:
                    player_scores[player_index] += current_score
                    print(f"Player {player_index + 1} has reached {max_score} points and won the game!")
                    print("Game over. Final scores:")
                    for idx, score in enumerate(player_scores):
                        print(f"Player {idx + 1}: {score}")
                    exit()
        
        # Update player's total score
        player_scores[player_index] += current_score
        print("Player", player_index + 1, "'s total score is:", player_scores[player_index])
        
        # Check if anyone has reached max_score
        if player_scores[player_index] >= max_score:
            print(f"Player {player_index + 1} has reached {max_score} points and won the game!")
            print("Game over. Final scores:")
            for idx, score in enumerate(player_scores):
                print(f"Player {idx + 1}: {score}")
            exit()
