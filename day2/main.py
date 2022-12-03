def decode_input(input):
    return (ord(input[0]) -64, ord(input[-1]) -87)

def decode_second_input(input):
    their_hand = ord(entry[0]) -64

    if (your_value :=entry[-1]) == "X":
        if their_hand == 1:
            return their_hand, 3
        else:
            return their_hand, their_hand - 1
    elif your_value == "Z":
        if their_hand == 3:
            return their_hand, 1
        else:
            return their_hand, their_hand + 1
    else:
        return their_hand, their_hand


def play_round(their_hand: int, your_hand: int) -> int:
    win = 6
    tie = 3

    if your_hand == their_hand:
        return your_hand + tie
    elif your_hand == 1 and their_hand == 3:
        return your_hand + win
    elif your_hand == 3 and their_hand == 1:
        return your_hand
    elif your_hand -1 == their_hand:
        return your_hand + win
    elif your_hand + 1 == their_hand:
        return your_hand
    

if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.readlines()

    results = 0
    results_2 = 0
    for entry in data:
        your_hand, their_hand = decode_input(entry.strip("\n"))
        your_hand_2, their_hand_2 = decode_second_input(entry.strip("\n"))
        results += play_round(your_hand, their_hand)
        results_2 += play_round(your_hand_2, their_hand_2)

    print(f'First part score: {results}')
    print(f'Second part score: {results_2}')