#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from sqlalchemy import create_engine

from wordlistdb_management import WordListDBCreator


def print_instructions(executable):
    print executable + ':'
    print 'Reads the standard input and generates a sqlite database that can be used with susdecipher.py'
    print 'if the database already exist it adds the words passed in the standard input\n'
    print 'usage: ' + executable + ' wordlist_database_name'
    print 'example: '
    print executable + " wordlist.db < somewords.txt"


def create_db_from_stdin(wordlistdb):
    engine = create_engine('sqlite:///' + wordlistdb,
                           echo=False, encoding='utf-8', convert_unicode=True)
    dbcreator = WordListDBCreator(engine)
    dbcreator.max_words_added = 50
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            dbcreator.add_word(line)
        except KeyboardInterrupt:
            break

    dbcreator.force_commit()



if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print_instructions(executable=sys.argv[0])
        exit()
    create_db_from_stdin(wordlistdb=args[0])
