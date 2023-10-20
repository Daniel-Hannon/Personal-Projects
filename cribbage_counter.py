import numpy as np


def count_points(hand, flip):
    suits = [card[-1] for card in hand]
    ranks = [card[:-1] for card in hand]
    rank_dict = {'J':11, 'Q':12, 'K':13}
    nums= []
    values = []
    for i in range(len(ranks)):
        if ranks[i] in rank_dict:
            nums.append(rank_dict[ranks[i]])
            values.append(10)
        elif ranks[i] == 'A':
            nums.append(1)
            values.append(1)
        else:
            nums.append(int(ranks[i]))
            values.append(int(ranks[i]))

    if flip[:-1] in rank_dict:
        nums.append(rank_dict[flip[:-1]])
        values.append(10)
    elif flip[:-1] == 'A':
        nums.append(1)
        values.append(1)
    else:
        nums.append(int(flip[:-1]))
        values.append(int(flip[:-1]))

    pairs_dict = {}
    for card in nums:
        if card in pairs_dict:
            pairs_dict[card] += 1
        else:
            pairs_dict[card] = 1

    straight_dict = {}
    nums = sorted(nums)
    for card in nums:
        if card in straight_dict:
            straight_dict[card] += 1
        else:
            straight_dict[card] = 1
    
    values = sorted(values)
    
    flush_points = check_flush(suits, flip[-1])
    print("flush points=", flush_points)
    pair_points = check_pairs(pairs_dict)
    print("pair points= ", pair_points)
    straight_points = check_straight(straight_dict)
    print("straight points= ", straight_points)
    fifteens_points = check_fifteens(values)
    print("fifteen points=", fifteens_points)
    nob_point= check_nobs(hand, flip)
    print("For his nob=", nob_point)
    return flush_points + pair_points + straight_points + fifteens_points + nob_point

def check_nobs(hand, flip):
    for card in hand:
        if card[:-1] == 'J' and card[-1] == flip[-1]:
            return 1
    return 0

def check_pairs(pair_dict):
    total = 0
    for key in pair_dict.keys():
        if pair_dict[key] == 2:
            total += 2
            pair_dict[key] = 0
        elif pair_dict[key] == 3:
            total += 6
            pair_dict[key] = 0
        elif pair_dict[key] == 4:
            total += 12
            pair_dict[key] = 0
    return total

def check_flush(suits, flip):
    suits_dict= {}  
    for suit in suits:
        if suit in suits_dict:
            suits_dict[suit] += 1
        else:
            suits_dict[suit] = 1
    
    for suit in suits_dict.keys():
        if suits_dict[suit] > 3:
            if flip == suit:
                return suits_dict[suit]+1
            else:
                return suits_dict[suit]
    return 0

def check_fifteens(values, start=0):
    total = 0
    all_subsets = []
    for i in range(start, len(values)):
        all_subsets.append([values[i]])
        for j in range(i+1, len(values)):
            all_subsets.append([values[i], values[j]])
            for k in range(j+1, len(values)):
                all_subsets.append([values[i], values[j], values[k]])
                for l in range(k+1, len(values)):
                    all_subsets.append([values[i], values[j], values[k], values[l]])
                    for m in range(l+1, len(values)):
                        all_subsets.append([values[i], values[j], values[k], values[l], values[m]])
                        if len(values) < 6:
                            continue
                        for n in range(m+1, len(values)):
                            all_subsets.append([values[i], values[j], values[k], values[l], values[m], values[n]])
                            for o in range(n+1, len(values)):
                                all_subsets.append([values[i], values[j], values[k], values[l], values[m], values[n], values[o]])
    for subset in all_subsets:
        if sum(subset) == 15:
            total += 2
    return total   

def check_straight(straight_dict):
    total = 0
    for key in straight_dict:
        mulit = straight_dict[key]
        count = 0
        if key+1 in straight_dict:
            if key+2 in straight_dict:
                count+=3
                if key+3 in straight_dict:
                    count+=1
                    if key+4 in straight_dict:
                        count+=1
                        if key+5 in straight_dict:
                            count+=1
                            if key+6 in straight_dict:
                                count+=1
                            mulit *= straight_dict[key+5]
                            straight_dict[key+5] = 0
                        mulit *= straight_dict[key+4]
                        straight_dict[key+4] = 0
                    mulit *= straight_dict[key+3]
                    straight_dict[key+3] = 0
                mulit *= straight_dict[key+2]
                straight_dict[key+2] = 0
            mulit *= straight_dict[key+1]
        total+= count*mulit
    return total
                                        

if __name__ == '__main__':
    import sys
    #take in input from command line
    hand = sys.argv[1:-1]
    flip = sys.argv[-1]
    
    print(hand, flip)
    points= count_points(hand, flip)
    print(points)

