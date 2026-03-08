# 5 Card Stud Simulation
# Read 1 second after**

from combinations import nextCombination, returnCombinations, printCombinations
import random

def game(hand):
    
    suit = []
    rank = []
    
    for v in hand:
        suit.append(v // 13)
        rank.append(v % 13)
    
    suit.sort()
    rank.sort()
    
    is_flush = (suit[0] == suit[4])
    
    is_consecutive = (rank[0] == rank[1] - 1 == rank[2] - 2 == rank[3] - 3 == rank[4] - 4)
    is_broadway = (rank == [0, 9, 10, 11, 12])
    is_straight = is_consecutive or is_broadway

    if is_flush and is_broadway:
        return "RF"
    
    if is_flush and is_straight:
        return "SF"
    
    if rank[0] == rank[3] or rank[1] == rank[4]:
        return "fourK"
        
    if rank[0] == rank[2] and rank[3] == rank[4] or rank[0] == rank[1] and rank[2] == rank[4]:
        return "FH"
        
    if is_flush:
        return "F"
        
    if is_straight:
        return "S"   
    
    if rank[0] == rank[2] or rank[1] == rank[3] or rank[2] == rank[4]:
        return "threeK"
    
    if rank[0] == rank[1] and rank[2] == rank[3]: 
        return "twoP"
    
    if rank[1] == rank[2] and rank[3] == rank[4]:
        return "twoP"
    
    if rank[0] == rank[1] and rank[3] == rank[4]:
        return "twoP"
    
    if rank[0] == rank[1] or rank[1] == rank[2] or rank[2] == rank[3] or rank[3] == rank[4]:
        return "oneP"
    
    else:
        return "N"


def main():
    RF = 0
    SF = 0
    fourK = 0
    FH = 0
    F = 0
    S = 0
    threeK = 0
    twoP = 0
    oneP = 0
    N = 0
    
    count, combinations = returnCombinations(52, 5)
    count = count.getCount()
    
    
    for i in range(count):
        result = game(combinations[i])
        
        if result == "RF":
            RF += 1
        elif result == "SF":
            SF += 1
        elif result == "fourK":
            fourK += 1
        elif result == "FH":
            FH += 1
        elif result == "F":
            F += 1
        elif result == "S":
            S += 1
        elif result == "threeK":
            threeK += 1
        elif result == "twoP":
            twoP += 1
        elif result == "oneP":
            oneP += 1
        elif result == "N":
            N += 1
            
            
    print(f"""
        TOTALS
        ------------------------------------------------------------
        Royal Flush: {RF}
        Straight Flush: {SF}
        Four of a kind: {fourK}
        Full house: {FH}
        Flush: {F}
        Straight: {S}
        Three of a kind: {threeK}
        Two pair: {twoP}
        One pair: {oneP}
        Nothing: {N}"""
        )
            
    RFP =     (RF / count) * 100
    SFP =     (SF / count) * 100
    fourKP =  (fourK / count) * 100
    FHP =     (FH / count) * 100
    FP =      (F / count) * 100
    SP =      (S / count) * 100
    threeKP = (threeK / count) * 100
    twoPP =   (twoP / count) * 100
    onePP =   (oneP / count) * 100
    NP =      (N / count) * 100

    print("\n")
    print(f"""
        PERCENTAGES
        ------------------------------------------------------------
        Royal flush %: {round(RFP, 8)}
        Straight flush %: {round(SFP, 5)}
        Four of a kind %: {round(fourKP, 5)}
        Full house %: {round(FHP, 5)}
        Flush %: {round(FP, 5)}
        Straight %: {round(SP, 5)}
        Three of a kind %: {round(threeKP, 5)}
        Two pair %: {round(twoPP, 5)}
        One pair %: {round(onePP, 5)}
        Nothing %: {round(NP, 5)}
    """)

    
if __name__ == "__main__":
    main()
