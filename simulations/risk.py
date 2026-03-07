# Risk simulation

import random

def game():
    attacker_dice = []
    defender_dice = []
    
    attacker_wins = 0
    defender_wins = 0
    
    attacker_dice.append(random.randint(1,6))
    attacker_dice.append(random.randint(1,6))
    attacker_dice.append(random.randint(1,6))
    defender_dice.append(random.randint(1,6))
    defender_dice.append(random.randint(1,6))
    attacker_dice.remove(min(attacker_dice))
    
    if attacker_dice[0] > defender_dice[0]:
        attacker_wins += 1
    else:
        defender_wins += 1
        
    if attacker_dice[1] > defender_dice[1]:
        attacker_wins += 1
    else:
        defender_wins += 1
        
    return attacker_wins, defender_wins
    
    
    
def main():
    attack_wins = 0
    defend_wins = 0
    for i in range(1000000):
        risk = game()
        attack_wins += risk[0]
        defend_wins += risk[1]
        
    attacker_win_percentage = (attack_wins / 2000000) * 100
    defender_win_percentage = (defend_wins / 2000000) * 100
        
    print(
        f"Attacker win percentage: {attacker_win_percentage}\nDefender win percentage: {defender_win_percentage}"
        )

if __name__ == "__main__":
    main()

