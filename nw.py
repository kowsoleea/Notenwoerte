#-------------------------------------------------------------------------------
# Name:        module1
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

ALLOWED         =   set(['a', 'h', 'c', 'd', 'e', 'f', 'g'])

def isvalid(word):
    valid = True
    i = 0
    while (valid and  i < len(word)):
        valid = word[i] in ALLOWED
        i = i + 1
    return valid

def main():
    infile = open(DICT_FILE, 'r')
    outfile = open(OUT_FILE, 'w')

    word = infile.readline()
    print word
    while word != '':
        if isvalid(word):
            outfile.write(word + '\n')
            print word
        word = infile.readline()

    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
