import random
from collections import Counter

from combinations import nextCombination
from permutation import returnPermutationsWithRepetition


def iter_combinations_indices(n, r):
    if r > n or r <= 0:
        return

    values = list(range(1, r + 1))
    yield values.copy()

    while nextCombination(n, values):
        yield values.copy()


def card_from_index(index):
    rank = (index % 13) + 2  # 2..14 where 14 is Ace
    suit = index // 13       # 0..3
    return rank, suit


def is_straight(ranks):
    unique = sorted(set(ranks))
    if len(unique) != 5:
        return False, None

    if unique == [2, 3, 4, 5, 14]:
        return True, 5

    if unique[-1] - unique[0] == 4:
        return True, unique[-1]

    return False, None


def classify_hand(cards):
    ranks = [r for r, _ in cards]
    suits = [s for _, s in cards]

    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)

    flush = len(set(suits)) == 1
    straight, high_straight = is_straight(ranks)

    if straight and flush:
        if high_straight == 14:
            return "royal_flush"
        return "straight_flush"

    if counts[0] == 4:
        return "four_of_a_kind"

    if counts[0] == 3 and counts[1] == 2:
        return "full_house"

    if flush:
        return "flush"

    if straight:
        return "straight"

    if counts[0] == 3:
        return "three_of_a_kind"

    if counts[0] == 2 and counts[1] == 2:
        return "two_pair"

    if counts[0] == 2:
        return "one_pair"

    return "high_card"


def five_card_stud_probabilities():
    categories = [
        "royal_flush",
        "straight_flush",
        "four_of_a_kind",
        "full_house",
        "flush",
        "straight",
        "three_of_a_kind",
        "two_pair",
        "one_pair",
        "high_card",
    ]

    counts = {c: 0 for c in categories}
    total = 0

    for combo in iter_combinations_indices(52, 5):
        cards = [card_from_index(i - 1) for i in combo]
        category = classify_hand(cards)
        counts[category] += 1
        total += 1

    print("5-Card Stud (exact using combinations)")
    print(f"Total hands: {total}")
    for c in categories:
        probability = counts[c] / total
        print(f"{c}: {counts[c]}  probability={probability:.8f}")


def compare_risk_dice(attacker_roll, defender_roll):
    attacker = sorted(attacker_roll, reverse=True)
    defender = sorted(defender_roll, reverse=True)

    battles = min(len(attacker), len(defender))
    attacker_wins = 0
    defender_wins = 0

    for i in range(battles):
        if attacker[i] > defender[i]:
            attacker_wins += 1
        else:
            defender_wins += 1

    return attacker_wins, defender_wins


def risk_exact_probabilities():
    matchups = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

    print("Risk (exact using permutations with repetition)")
    for attacker_dice, defender_dice in matchups:
        outcome_counts = Counter()
        total = 0

        _, all_rolls = returnPermutationsWithRepetition(6, attacker_dice + defender_dice)
        for roll in all_rolls:
            attacker_roll = [v + 1 for v in roll[:attacker_dice]]
            defender_roll = [v + 1 for v in roll[attacker_dice:]]
            outcome = compare_risk_dice(attacker_roll, defender_roll)
            outcome_counts[outcome] += 1
            total += 1

        print(f"\nAttacker dice={attacker_dice} Defender dice={defender_dice}")
        print(f"Total outcomes (6^{attacker_dice + defender_dice}): {total}")
        for outcome in sorted(outcome_counts.keys(), reverse=True):
            probability = outcome_counts[outcome] / total
            print(f"Attacker wins {outcome[0]} / Defender wins {outcome[1]}: {probability:.6f}")


def risk_simulation(trials=200000):
    matchups = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

    print("\nRisk (simulation)")
    for attacker_dice, defender_dice in matchups:
        outcome_counts = Counter()

        for _ in range(trials):
            attacker_roll = [random.randint(1, 6) for _ in range(attacker_dice)]
            defender_roll = [random.randint(1, 6) for _ in range(defender_dice)]
            outcome = compare_risk_dice(attacker_roll, defender_roll)
            outcome_counts[outcome] += 1

        print(f"\nAttacker dice={attacker_dice} Defender dice={defender_dice}")
        print(f"Trials: {trials}")
        for outcome in sorted(outcome_counts.keys(), reverse=True):
            probability = outcome_counts[outcome] / trials
            print(f"Attacker wins {outcome[0]} / Defender wins {outcome[1]}: {probability:.6f}")


def main():
    risk_exact_probabilities()
    risk_simulation()
    print()
    five_card_stud_probabilities()


if __name__ == "__main__":
    main()
