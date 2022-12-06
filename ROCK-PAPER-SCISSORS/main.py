import random

def main():
    user = input("'r' for ROCK, 'p' for PAPER and 's' for 'SCISSORS\t")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer's choise: {computer}")
    
    if user == computer:
        return 'Tie!'
    
    if rules(user, computer):
       return 'Player wins!'
    
    return 'Computer wins!'

     
     
def rules(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'): 
        return True

print(main())
