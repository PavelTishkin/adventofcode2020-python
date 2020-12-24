max_game = 1


def main():
    input_file = open('input/day22.txt', 'r')
    decks_txt = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    deck1, deck2 = load_decks(decks_txt)
    deck, _, _ = play_game(deck1, deck2)
    score = calculate_score(deck)

    print('Answer 1: {}'.format(score))

    deck1, deck2 = load_decks(decks_txt)
    deck1, deck2, winner, insta_win = play_rec_game(deck1, deck2)
    if winner == 1:
        score = calculate_score(deck1)
    else:
        score = calculate_score(deck2)

    print('Answer 2: {}'.format(score))


def load_decks(decks_txt):
    curr_player = 1
    deck1 = []
    deck2 = []
    for deck_line in decks_txt:
        if deck_line == 'Player 1:':
            curr_player = 1
        elif deck_line == 'Player 2:':
            curr_player = 2
        elif deck_line == '':
            continue
        else:
            if curr_player == 1:
                deck1.append(int(deck_line))
            else:
                deck2.append(int(deck_line))

    return deck1, deck2


def play_round(deck1, deck2):
    card1 = deck1[0]
    card2 = deck2[0]
    deck1 = deck1[1:]
    deck2 = deck2[1:]
    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)

    return deck1, deck2


def play_game(deck1, deck2):
    round_count = 0
    while len(deck1) != 0 and len(deck2) != 0:
        deck1, deck2 = play_round(deck1, deck2)
        round_count += 1
    if deck1:
        return deck1, 1, round_count
    else:
        return deck2, 2, round_count


def calculate_score(deck):
    score = 0
    deck = deck[::-1]
    for idx, card in enumerate(deck):
        score += (idx + 1) * card
    return score


def play_rec_round(deck1, deck2, prev_rounds, curr_game, curr_round):
    global max_game
    insta_win = False
    if get_decks_hash(deck1, deck2, curr_game) in prev_rounds:
        return deck1, [], 1, True
    else:
        prev_rounds.add(get_decks_hash(deck1, deck2, curr_game))
    card1 = deck1[0]
    card2 = deck2[0]
    deck1 = deck1[1:]
    deck2 = deck2[1:]

    if len(deck1) >= card1 and len(deck2) >= card2:
        sub_deck1 = deck1[:card1]
        sub_deck2 = deck2[:card2]
        max_game += 1
        _, _, winner, insta_win = play_rec_game(sub_deck1, sub_deck2, prev_rounds, max_game, 1)
        if insta_win:
            winner = 1
    elif card1 > card2:
        winner = 1
    else:
        winner = 2

    if winner == 1:
        deck1.append(card1)
        deck1.append(card2)
        return deck1, deck2, winner, insta_win
    else:
        deck2.append(card2)
        deck2.append(card1)
        return deck1, deck2, winner, insta_win


def play_rec_game(deck1, deck2, prev_rounds=set(), curr_game=1, curr_round=1):
    insta_win = False
    while len(deck1) != 0 and len(deck2) != 0:
        deck1, deck2, winner, insta_win = play_rec_round(deck1, deck2, prev_rounds, curr_game, curr_round)
        curr_round += 1

    return deck1, deck2, winner, insta_win


def get_decks_hash(deck1, deck2, curr_game):
    combined_deck = deck1[:]
    combined_deck.extend(deck2[:])
    combined_deck.append(curr_game)
    combined_deck.append(len(deck1))
    combined_deck.append(len(deck2))
    return hash(','.join(f'{n}' for n in combined_deck))


if __name__ == '__main__':
    main()
