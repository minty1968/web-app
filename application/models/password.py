import random, sys, csv, os, platform, string
from os import path
from flask import url_for
import pandas as pd


class Password(object):
    def __init__(self,easy,medium,hard,_id):
        self.easy = easy
        self.medium = medium
        self.hard = hard
        self._id = _id

    def random_password(easy, medium, hard):
        pass_easy = ''
        pass_medium = ''
        pass_hard = ''
        password = ''
        passwd = ''
        # Check to see which radio button user selected, then generate a password
        if easy:
            pass_easy = string.ascii_lowercase + string.ascii_uppercase
            password = random.sample(pass_easy, 8)
        elif medium:
            pass_medium = string.ascii_lowercase + string.ascii_uppercase + string.digits
            password = random.sample(pass_medium, 15)
        elif hard:
            pass_hard = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            password = random.sample(pass_hard, 30)
        else:
            return False
        # Turn the created list into a string
        for ele in password:
            passwd += ele
        return passwd



    def generate_word(diceRoll):
        randWords = ''
        decodedWord = ''

        basedir = path.abspath(path.dirname(__file__))
        plat = platform.system

        if plat == 'Windows':
            file_path = (path.join(basedir, '..\common\wordlist.csv'))
        else:
            file_path = (path.join(basedir, '../common/wordlist.csv'))

        # Access word file and search for above code, then assign the word to a variable
        # This will be repeated for total number of words requested by user.
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                wordCode = row[0]
                if wordCode == diceRoll:
                    decodedWord = row[1] + ' '
        return decodedWord


    def words_password(easy, medium, hard):
        # Set up variables
        diceRoll = ''
        randWords = ''
        decodedWord = ''
        word_list = ''
        dice1 = 0
        dice2 = 0
        dice3 = 0
        dice4 = 0
        dice5 = 0
        # Check to see which radio button user selected, then generate a password
        if easy:
            # Generate 5 random numbers between 1 and 6 which will be used for word assignment
            dice1=random.randint(1, 6)
            dice2=random.randint(1, 6)
            dice3=random.randint(1, 6)
            dice4=random.randint(1, 6)
            dice5=random.randint(1, 6)
            diceRoll=str(dice1)+str(dice2)+str(dice3)+str(dice4)+str(dice5)
        elif medium:
            # Generate 5 random numbers between 1 and 6 which will be used for word assignment
            dice1=random.randint(1, 6)
            dice2=random.randint(1, 6)
            dice3=random.randint(1, 6)
            dice4=random.randint(1, 6)
            dice5=random.randint(1, 6)
            diceRoll=str(dice1)+str(dice2)+str(dice3)+str(dice4)+str(dice5)
        elif hard:
            # Generate 5 random numbers between 1 and 6 which will be used for word assignment
            dice1=random.randint(1, 6)
            dice2=random.randint(1, 6)
            dice3=random.randint(1, 6)
            dice4=random.randint(1, 6)
            dice5=random.randint(1, 6)
            diceRoll=str(dice1)+str(dice2)+str(dice3)+str(dice4)+str(dice5)
        else:
            return False
        return diceRoll
