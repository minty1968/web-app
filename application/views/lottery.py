"""Routes for lottery pages."""
from flask import Blueprint, render_template, request, flash, url_for
from application.models.lottery import Lottery

# Blueprint Configuration
lotteryBP = Blueprint('lottery', __name__,
                      template_folder='application/templates/lottery/',
                      static_folder='application/static', url_prefix='/lottery')


@lotteryBP.route('/lotto', methods=['GET', 'POST'])
def lottoIndex():
  """ Lottery Draw route. """

  return render_template('lottery/lottoIndex.html')


@lotteryBP.route('/national-lottery', methods=['GET', 'POST'])
def lotto():
    """National Lottery route.  First we generate 6 numbers between 1 and 59, then sort them. """

    sorted_random_nums = Lottery.get_sorted_main_numbers(59, 6)
    tot_main_num = Lottery.get_tot_main_numbers(sorted_random_nums)
    avg_main_nums = Lottery.get_avg_main_numbers(tot_main_num, 6)
    lottery_data = Lottery.get_db_draw_info('lotto')

    return render_template('lottery/lotto.html', body="National Lottery",
                           title='Sharpe Digital Solutions | National Lottery',
                           lottery_data=lottery_data, sorted_random_nums=sorted_random_nums,
                           avg_main_nums=avg_main_nums, tot_main_num=tot_main_num)


@lotteryBP.route('/national-lottery-hotpicks', methods=['GET', 'POST'])
def lotto_hp():
    """National Lottery Hotpicks route.  First we generate x numbers between 1 and 59, then sort them. """

    sorted_random_nums = Lottery.get_sorted_main_numbers(59, 6)
    tot_main_num = Lottery.get_tot_main_numbers(sorted_random_nums)
    avg_main_nums = Lottery.get_avg_main_numbers(tot_main_num, 6)
    lottery_data = Lottery.get_db_draw_info('lotto-hotpicks')

    return render_template('lottery/lottoHP.html', body="National Lottery Hotpicks",
                           title='Sharpe Digital Solutions | National Lottery Hotpicks',
                           lottery_data=lottery_data, sorted_random_nums=sorted_random_nums,
                           avg_main_nums=avg_main_nums, tot_main_num=tot_main_num)


@lotteryBP.route('/euromillions', methods=['GET', 'POST'])
def euro():
    """Euromillions route.  First we generate 5 numbers between 1 and 50, then sort them.
        We then generate two bonus numbers between 1 and 12."""

    sorted_random_nums = Lottery.get_sorted_main_numbers(50, 5)
    tot_main_num = Lottery.get_tot_main_numbers(sorted_random_nums)
    avg_main_nums = Lottery.get_avg_main_numbers(tot_main_num, 5)

    sorted_random_bonus = Lottery.get_sorted_bonus_numbers(12, 2)
    tot_bonus_num = Lottery.get_tot_bonus_numbers(sorted_random_bonus)
    avg_bonus_nums = Lottery.get_avg_bonus_numbers(tot_bonus_num, 2)
    lottery_data = Lottery.get_db_draw_info('euromillions')

    return render_template('lottery/euro.html', lottery_data=lottery_data, body="Euromillions",
                           title='Sharpe Digital Solutions | Euromillions',
                           sorted_random_nums=sorted_random_nums, avg_main_nums=avg_main_nums,
                           tot_main_num=tot_main_num, tot_bonus_num=tot_bonus_num,
                           sorted_bonus_nums=sorted_random_bonus, avg_bonus_nums=avg_bonus_nums)


@lotteryBP.route('/euromillions-hotpicks', methods=['GET', 'POST'])
def euro_hp():
    """Euromillions Hotpicks route.  First we generate x numbers between 1 and 50, then sort them. """

    sorted_random_nums = Lottery.get_sorted_main_numbers(50, 5)
    tot_main_num = Lottery.get_tot_main_numbers(sorted_random_nums)
    avg_main_nums = Lottery.get_avg_main_numbers(tot_main_num, 5)
    lottery_data = Lottery.get_db_draw_info('euromillions-hotpicks')

    return render_template('lottery/euroHP.html', body="Euromillions Hotpicks",
                           title='Sharpe Digital Solutions | Euromillions Hotpicks',
                           lottery_data=lottery_data, sorted_random_nums=sorted_random_nums,
                           tot_main_num=tot_main_num, avg_main_nums=avg_main_nums)


@lotteryBP.route('/set-for-life', methods=['GET', 'POST'])
def s4l():
    """Set for Life route.  First we generate 5 numbers between 1 and 47, then sort them.
        We then generate a bonus number between 1 and 10."""

    sorted_random_nums = Lottery.get_sorted_main_numbers(47, 5)
    tot_main_num = Lottery.get_tot_main_numbers(sorted_random_nums)
    avg_main_nums = Lottery.get_avg_main_numbers(tot_main_num, 5)
    sorted_random_bonus = Lottery.get_sorted_bonus_numbers(10, 1)
    lottery_data = Lottery.get_db_draw_info('set-for-life')

    return render_template('lottery/s4l.html', body="Set for Life",
                           title='Sharpe Digital Solutions | Set for Life',
                           lottery_data=lottery_data, sorted_random_bonus=sorted_random_bonus,
                           sorted_random_nums=sorted_random_nums,
                           avg_main_nums=avg_main_nums, tot_main_num=tot_main_num)


@lotteryBP.route('/thunderball', methods=['GET', 'POST'])
def thunder():
    """Thunderball route.  First we generate 5 numbers between 1 and 39, then sort them.
        We then generate a bonus number between 1 and 14."""

    sorted_random_nums = Lottery.get_sorted_main_numbers(39, 5)
    tot_main_num = Lottery.get_tot_main_numbers(sorted_random_nums)
    avg_main_nums = Lottery.get_avg_main_numbers(tot_main_num, 5)
    sorted_random_bonus = Lottery.get_sorted_bonus_numbers(14, 1)
    lottery_data = Lottery.get_db_draw_info('thunderball')

    return render_template('lottery/thunder.html', body="Thunderball",
                           title='Sharpe Digital Solutions | Thunderball',
                           lottery_data=lottery_data, sorted_random_bonus=sorted_random_bonus,
                           sorted_random_nums=sorted_random_nums,
                           avg_main_nums=avg_main_nums, tot_main_num=tot_main_num)
