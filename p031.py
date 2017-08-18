coins = [200,100,50,20,10,5,2,1]
bill = 200

Totals = [0]
NewTotals = []
for i in range(len(coins)):
	coin = coins[i]
	for t in Totals:
		NewTotals += range(t,bill+1,coin)
	Totals = NewTotals
	NewTotals = []

print Totals.count(bill)