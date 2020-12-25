import os, random
import pymongo
from pymongo import MongoClient


class Lottery(object):
    def __init__(self, ball1, ball2, ball3, ball4, ball5, ball6, main_total, main_avg, bonus1, bonus2, bonus_total,
                 bonus_avg, machine, ballset, _id):
        self.ball1 = ball1
        self.ball2 = ball2
        self.ball3 = ball3
        self.ball4 = ball4
        self.ball5 = ball5
        self.ball6 = ball6
        self.main_total = main_total
        self.main_avg = main_avg
        self.bonus1 = bonus1
        self.bonus2 = bonus2
        self.bonus_total = bonus_total
        self.bonus_avg = bonus_avg
        self.machine = machine
        self.ballset = ballset
        self._id = _id

    def get_sorted_main_numbers(max_main, balls):
        random_nums = random.sample(range(1, max_main), balls)
        print(random_nums)
        sorted_random_main = sorted(random_nums)
        print(sorted_random_main)
        return sorted_random_main

    def get_sorted_bonus_numbers(max_bonus, balls):
        random_nums = random.sample(range(1, max_bonus), balls)
        sorted_random_bonus = sorted(random_nums)
        print(sorted_random_bonus)
        return sorted_random_bonus

    def get_tot_main_numbers(main):
        tot_num = 0
        print(main)
        for num in main:
            tot_num = tot_num + num
        print(tot_num)
        return tot_num

    def get_tot_bonus_numbers(bonus):
        tot_num = 0
        for num in bonus:
            tot_num = tot_num + num
        print(tot_num)
        return tot_num

    def get_avg_main_numbers(tot_main_num, balls):
        avg_main_nums = tot_main_num / balls
        avg_main_nums = round(avg_main_nums, 1)
        print(avg_main_nums)
        return avg_main_nums

    def get_avg_bonus_numbers(tot_bonus_num, balls):
        avg_bonus_nums = tot_bonus_num / balls
        avg_bonus_nums = round(avg_bonus_nums, 1)
        print(avg_bonus_nums)
        return avg_bonus_nums

    def get_db_draw_info(draw_type):
        db_conn = os.environ['MONGO_URI']
        myconn = pymongo.MongoClient(db_conn)
        mydb = myconn['thor']
        mycol = mydb[draw_type]
        lottery_data = mycol.find({})
        print(lottery_data)
        return lottery_data
