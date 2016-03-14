# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker

from wordmodels import Base, Word, LetterPattern


class WordListDBCreator:
    def __init__(self, engine):
        self.engine = engine
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.session_add_counter = 0
        self.total_word_counter = 0
        self.max_words_added = 500

    def force_commit(self):
        self.session.commit()

    def add_word(self, word):
        word = word.strip().lower().decode('utf-8')
        word_model = self.session.query(Word).filter(Word.name == word).first()
        if not word_model:
            pattern = LetterPattern.generate_pattern(word)

            letter_pattern = self.session.query(LetterPattern).filter(LetterPattern.pattern == pattern).first()
            if not letter_pattern:
                letter_pattern = LetterPattern.from_word(word)
            word_model = Word(name=word)
            letter_pattern.words.append(word_model)
            self.session.add(letter_pattern)
            self.session_add_counter += 1

        # To speed up the word capture, we do commit when
        if self.session_add_counter >= self.max_words_added:
            self.session.commit()
            self.total_word_counter += self.session_add_counter
            print str(self.total_word_counter) + ' words added...'
            self.session_add_counter = 0
