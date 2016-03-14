# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker

from wordmodels import LetterPattern


class PatternFinder:
    def __init__(self, engine):
        self.engine = engine
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def find_solutions(self, ciphered_message):
        message_words = ciphered_message.split()
        word_pattern_dict = self.__get_word_pattern_dict(message_words)

        self.__unscramble(word_pattern_dict, {}, 0, ciphered_message, len(word_pattern_dict))

    def __get_word_pattern_dict(self, message_words):
        word_pattern_dict = {}
        for original_word in message_words:
            pattern = LetterPattern.generate_pattern(original_word)
            letter_pattern = self.session.query(LetterPattern).filter(LetterPattern.pattern == pattern).first()
            word_pattern_dict[original_word] = letter_pattern
        return word_pattern_dict

    def __unscramble(self, word_pattern_dict, substitution_dict, depth, ciphered_message, maximum_depth):
        if depth >= maximum_depth:
            self.__displaysolution(substitution_dict, ciphered_message)
            return

        less_words_pattern = self.__find_less_words_pattern(word_pattern_dict)
        ciphered_word = less_words_pattern['word']
        letter_pattern = less_words_pattern['pattern']

        for word in letter_pattern.words:
            if self.is_dict_compatible(ciphered_word, word.name, substitution_dict):
                added_sub_dict = self.generate_substitution_dict(ciphered_word, word.name)
                old_substitution_dict = substitution_dict.copy()
                substitution_dict.update(added_sub_dict)
                sub_word_pattern_dict = word_pattern_dict.copy()
                del sub_word_pattern_dict[ciphered_word]
                self.__unscramble(sub_word_pattern_dict, substitution_dict, depth + 1, ciphered_message, maximum_depth)
                substitution_dict.clear()
                substitution_dict.update(old_substitution_dict)

    def __displaysolution(self, substitution_dict, ciphered_message):
        print self.substitute(ciphered_message, substitution_dict)

    @staticmethod
    def __find_less_words_pattern(word_pattern_dict):
        min_words = -1
        less_words_pattern = {'word': '', 'pattern': ''}
        for key, value in word_pattern_dict.items():
            if min_words == -1:
                min_words = len(value.words)
                less_words_pattern['word'] = key
                less_words_pattern['pattern'] = value
                continue

            if len(value.words) < min_words:
                min_words = len(value.words)
                less_words_pattern['word'] = key
                less_words_pattern['pattern'] = value

        return less_words_pattern

    @staticmethod
    def is_dict_compatible(ciphered_word, substitution_word, substitution_dict):
        wordsize = len(ciphered_word)

        if wordsize != len(substitution_word):
            return False

        index = 0
        while index < wordsize:
            ciphered_char = ciphered_word[index]
            subs_char = substitution_word[index]
            index += 1

            if ciphered_char not in substitution_dict:
                for key, value in substitution_dict.items():
                    if subs_char == value:
                        return False
                continue
            else:
                if subs_char != substitution_dict[ciphered_char]:
                    return False

        return True

    @staticmethod
    def generate_substitution_dict(ciphered_word, word):
        substitution_dict = {}

        size = len(ciphered_word)
        i = 0
        while i < size:
            substitution_dict[ciphered_word[i]] = word[i]
            i += 1
        return substitution_dict

    @staticmethod
    def substitute(ciphered_message, substitution_dict):
        message = ''
        size = len(ciphered_message)
        i = 0
        while i < size:
            if ciphered_message[i] in substitution_dict:
                message += substitution_dict[ciphered_message[i]].encode('utf-8')
            else:
                message += ciphered_message[i].encode('utf-8')
            i += 1
        return message
