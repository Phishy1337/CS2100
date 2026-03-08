# Risk simulation
import random

class Count:
    def __init__(self, n, r):
        self.count = 0
        self.n = n
        self.r = r

    def increment(self, count=1):
        self.count += count 

    def setN(self, n):
        self.n = n
    
    def setR(self, r):
        self.r = r

    def getCount(self):
        return self.count 



def next_roll(rolls, n, idx):
      if rolls[idx] < n:
          rolls[idx] += 1
          return True

      rolls[idx] = 1
      if idx == 0:
          return False

      return next_roll(rolls, n, idx - 1)


def generate_rolls(n, r, counter=None):
    if counter is None:
        counter = Count(n, r)

    rolls = [1] * r
    all_rolls = []
    all_rolls.append(rolls.copy())
    counter.increment()

    while next_roll(rolls, n, r - 1):  
        all_rolls.append(rolls.copy())
        counter.increment()

    return counter.getCount(), all_rolls

def game():
    countA, attacker_dice = generate_rolls(6, 3)
    countD, defender_dice = generate_rolls(6, 2)
    
    attacker_wins = 0
    defender_wins = 0
    attacker_win_2 = 0
    defender_win_2 = 0
    split = 0


    total_matchups = countA * countD

    for attacker_set in attacker_dice:
        attacker_sorted = sorted(attacker_set, reverse=True)

        for defender_set in defender_dice:
            defender_sorted = sorted(defender_set, reverse=True)

            a_round_wins = 0
            d_round_wins = 0

            if attacker_sorted[0] > defender_sorted[0]:
                attacker_wins += 1
                a_round_wins += 1
            else:
                defender_wins += 1
                d_round_wins += 1

            if attacker_sorted[1] > defender_sorted[1]:
                attacker_wins += 1
                a_round_wins += 1
            else:
                defender_wins += 1
                d_round_wins += 1

            if a_round_wins == 2:
                attacker_win_2 += 1
            elif d_round_wins == 2:
                defender_win_2 += 1
            else:
                split += 1

    total_dice_comparisons = total_matchups * 2

    attacker_win_percentage = (attacker_wins / total_dice_comparisons) * 100
    defender_win_percentage = (defender_wins / total_dice_comparisons) * 100

    attacker_win_2_percentage = (attacker_win_2 / total_matchups) * 100
    defender_win_2_percentage = (defender_win_2 / total_matchups) * 100
    split_percentage = (split / total_matchups) * 100

    return (attacker_win_percentage,
        defender_win_percentage,
        total_matchups,
        attacker_win_2_percentage,
        defender_win_2_percentage,
        split_percentage) 
    
    
    
def main():
    (attacker_win_percentage, 
     defender_win_percentage, 
     total_matchups, 
     attacker_win_2_percentage, 
     defender_win_2_percentage, 
     split_percentage) = game()
    print()
    print("RISK ROLL PERMUTATIONS:")
    print(f"Attacker roles: 216\nDefender roles: 36\nTotal matchups: 216 * 36 = {total_matchups}")
    print()
    print(f"BATTLE OUTCOMES:")
    print(f"Attacker wins both: {attacker_win_2_percentage}\nDefender wins both: {defender_win_2_percentage}\nSplit 1-1: {split_percentage}")
    print()
    print("CHANCE OF WINNING:")
    print(f"Attacker: {attacker_win_percentage}\nDefender: {defender_win_percentage}")
        
if __name__ == "__main__":
    main()
