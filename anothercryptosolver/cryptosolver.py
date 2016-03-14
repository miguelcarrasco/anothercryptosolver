#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from sqlalchemy import create_engine

from patternsearching import PatternFinder


def print_instructions(executable):
    print executable + ':'
    print 'Reads a substitution cipher text from the standard input and print all possible phrases that'
    print 'can be founded using the specified wordlist database\n'
    print 'usage: ' + executable + ' wordlist_database_name'
    print 'example: '
    print executable + " wordlist.db < encrypted_message.txt"


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print_instructions(executable=sys.argv[0])
        exit()

    ciphered_message = ''
    for line in sys.stdin.readlines():
        ciphered_message += line

    wordlistdb = args[0]
    engine = create_engine('sqlite:///' + wordlistdb,
                           echo=False, encoding='utf-8', convert_unicode=True)
    finder = PatternFinder(engine)
    finder.find_solutions(ciphered_message.rstrip().decode('utf-8'))
