import random
def poke():
    cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']*4+['min_joker','max_joker']
    random.shuffle(cards)
    others = cards[0:3]
    player1 = cards[3::3]
    player2 = cards[4::3]
    player3 = cards[5::3]
    '''检验一下'''
    print(player1)
    print(player2)
    print(player3)
    print(others)
    with open('player1.txt', 'w') as f:
        f.write(' '.join(map(str, player1)))
    with open('player2.txt', 'w') as f:
        f.write(' '.join(map(str, player2)))
    with open('player3.txt', 'w') as f:
        f.write(' '.join(map(str, player3)))
    with open('others.txt', 'w') as f:
        f.write(' '.join(map(str, others)))

if __name__ == '__main__':
    poke()

