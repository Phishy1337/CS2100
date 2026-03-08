def next_roll(rolls, n, idx):
      # Try to increment current position
      if rolls[idx] < n:
          rolls[idx] += 1
          return True

      # Hit max at this position: reset and carry left
      rolls[idx] = 1
      if idx == 0:
          return False  # overflow: no more rolls

      return next_roll(rolls, n, idx - 1)


def generate_rolls(n, r):
    rolls = [1] * r
    all_rolls = []
    all_rolls.append(rolls.copy())# first roll

    while next_roll(rolls, n, r - 1):  # start carry from rightmost index
        all_rolls.append(rolls.copy())
    
    return all_rolls

rolls = generate_rolls(6, 3)

print(rolls)
