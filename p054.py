hands = []
with open("p054_poker.txt") as f:
    for line in f:
        hand = line.split()
        hands.append([hand[0:5],hand[5:10]])

ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['D','C','H','S']

def value(card):
	if card[0] == 'T':
		return 0.10
	if card[0] == 'J':
		return 0.11
	if card[0] == 'Q':
		return 0.12
	if card[0] == 'K':
		return 0.13
	if card[0] == 'A':
		return 0.14
	else:
		return 1.0*int(card[0])/100

RFs = []
for suit in suits:
	rflush = [ r + suit for r in ranks[-5:] ]
	RFs.append(set(rflush))

def rf(hand):
	if set(hand) in RFs:
		return 9
	else:
		return 0

SFs = []
for suit in suits:
	for i in range(9):
		sflush = [ r + suit for r in ranks[i:i+5] ]
		SFs.append(set(sflush))

def sf(hand):
	vals = [value(card) for card in hand]
	if set(hand) in SFs:
		return 8 + max(vals)
	else:
		return 0

def foak(hand):
	hand = sorted([card[0] for card in hand])
	for r in ranks:
		if hand.count(r) == 4:
			return 7 + value(r)
	return 0

fullhouses = []
for r1 in ranks:
	for r2 in ranks:
		if r1 != r2:
			myfh = [r1] * 2 + [r2] * 3
			fullhouses.append(sorted(myfh))

def fh(hand):
	hand = [card[0] for card in hand]
	vals = [value(card) for card in hand]
	if sorted(hand) in fullhouses:
		return 6 + max(vals)
	else:
		return 0

def flush(hand):
	mysuits = []
	vals = [value(card) for card in hand]
	for card in hand:
		mysuits.append(list(card)[1])
	if mysuits == [mysuits[0]] * 5:
		return 5 + max(vals)
	return 0

straights = []
for i in range(9):
	mystraight = ranks[i:i+5]
	straights.append(sorted(mystraight))

def straight(hand):
	hand = [card[0] for card in hand]
	if sorted(hand) in straights:
		hand = [value(card[0]) for card in hand]
		return 4 + max(hand)
	else:
		return 0

def toak(hand):
	hand = sorted([card[0] for card in hand])
	for r in ranks:
		if hand.count(r) == 3:
			return 3 + value(r)
	return 0

def twopair(hand):
	hand = sorted([card[0] for card in hand])
	for r1 in ranks:
		if hand.count(r1) == 2:
			hand.remove(r1)
			hand.remove(r1)
			for r2 in ranks:
				if r2 != r1:
					if hand.count(r2) == 2:
						return 2 + max(value(r1),value(r2))
	return 0

def pair(hand):
	hand = sorted([card[0] for card in hand])
	for r in ranks:
		if hand.count(r) == 2:
			return 1 + value(r)
	return 0

def highest(hand):
	vals = [value(card) for card in hand]
	return max(vals)

wins = 0
ties = 0
types = [rf,sf,foak,fh,flush,straight,toak,twopair,pair,highest]
for [X,Y] in hands:
	evals1 = [type(X) for type in types]
	a = max(evals1)
	evals2 = [type(Y) for type in types]
	b = max(evals2)
	if a == b:
		if a == b:
			a = evals1[-1]
			b = evals2[-1]
			if a > b:
				wins += 1
			if a == b:
				ties += 1
	if a > b:
		wins += 1

print wins