#-------------------------------------------------------------------------------
# Name:        nw
# Purpose:
#
# Author:      ivan
#
# Created:     13.12.2015
# Copyright:   (c) ivan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

DICT_FILE       =   'german.dic'
OUT_FILE        =   'woerte.txt'

ALLOWED         =   set(['a', 'h', 'c', 'd', 'e', 'f', 'g', 'A', 'H', 'C', 'D', 'E', 'F', 'G'])

def isvalid(word):
	i = 0
	s = word.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
	l = len(s) - 1
	while ((i < l) and (s[i] in ALLOWED)):
		i = i + 1
	return i >= l

def main():
	infile = open(DICT_FILE, 'r')
	outfile = open(OUT_FILE, 'w')
	word = infile.readline()
	while word != '':
		if isvalid(word):
			outfile.write(word)
		word = infile.readline()
	infile.close()
	outfile.close()

if __name__ == '__main__':
    main()
