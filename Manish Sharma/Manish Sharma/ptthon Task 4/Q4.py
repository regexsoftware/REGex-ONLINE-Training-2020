with open('Sharma.txt') as fh1, open('Manish.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from Sharma.txt, line2 from Manish.txt
        print(line1+line2)
		
