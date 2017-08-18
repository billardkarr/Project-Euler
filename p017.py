outer = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def inwords(thous,hund,ten,ones):
	if (thous == 0) & (hund == 0):
		if ten > 1:
			return tens[ten] + ' ' + outer[ones]
		if ten == 1:
			return teens[ones]
		if ten == 0:
			return outer[ones]

	if (thous == 0) & (hund > 0):
		if ten > 1:
			return outer[hund] + ' hundred and ' + tens[ten] + ' ' + outer[ones]
		if ten == 1:
			return outer[hund] + ' hundred and ' + teens[ones]
		if ten == 0:
			if ones == 0:
				return outer[hund] + ' hundred'
			else:
				return outer[hund] + ' hundred and ' + outer[ones]

	if thous == 1:
		return 'one thousand'

longstring = ''
for i in range(1,1000+1):
	ones = i % 10
	ten = ((i - ones)/10) % 10
	hund = ((i - 10*ten - ones)/100) % 10
	thous = ((i - 100*hund - 10*ten - ones)/1000) % 10
	longstring += inwords(thous,hund,ten,ones)
	print inwords(thous,hund,ten,ones)

longstring = longstring.replace(' ','')
print len(longstring)
