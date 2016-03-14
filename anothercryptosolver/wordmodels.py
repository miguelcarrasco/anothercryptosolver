# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class LetterPattern(Base):
    __tablename__ = 'LetterPattern'

    id = Column(Integer, primary_key=True)
    pattern = Column(String, unique=True, index=True)
    words = relationship("Word")

    def __repr__(self):
        return self.pattern

    @staticmethod
    def from_word(word):
        return LetterPattern(pattern=LetterPattern.generate_pattern(word))

    @staticmethod
    def generate_pattern(word):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']

        alphacount = 0
        pattern_dict = dict()
        for char in word:
            if (char not in pattern_dict):
                pattern_dict[char] = alphabet[alphacount]
                alphacount += 1

        pattern = ''
        for char in word:
            pattern += pattern_dict[char]

        return pattern


class Word(Base):
    __tablename__ = 'Word'
    id = Column(Integer, primary_key=True)
    letter_pattern_id = Column(Integer, ForeignKey('LetterPattern.id'))
    name = Column(String, unique=True, index=True)

    def __repr__(self):
        return self.name
