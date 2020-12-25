"""Routes for password generator pages."""
from flask import Blueprint, render_template, request
from application.models.password import Password

# Blueprint Configuration
passwdBP = Blueprint('password', __name__,
                        template_folder='application/templates/password/',
                        static_folder='static')


@passwdBP.route('/password', methods=['GET', 'POST'])
def passwd():
    """Password route."""
    easy = ''
    medium = ''
    hard = ''
    pass_comp = ''
    password = ''

    if request.method == 'POST':
        pass_type = request.form.get('passType')
        pass_comp = request.form.get('complex')
        if pass_comp == 'easy':
            easy=True
            medium=False
            hard=False
            rolls = 2
        elif pass_comp == 'medium':
            easy=False
            medium=True
            hard=False
            rolls = 4
        elif pass_comp == 'hard':
            easy=False
            medium=False
            hard=True
            rolls = 6
        else:
            easy=False
            medium=False
            hard=False

        if pass_type == 'random':
            password = Password.random_password(easy, medium, hard)
        elif pass_type == 'words':
            for num in range(rolls):
                dice_roll = Password.words_password(easy, medium, hard)
                gen_word = Password.generate_word(dice_roll)
                password = password + gen_word
        else:
            return False
        return render_template('password/passwd.html', body="Password Generator",
                               title='Sharpe Digital Solutions | Password Generator',
                               password=password)
    return render_template('password/passwd.html', body="Password Generator",
                           title='Sharpe Digital Solutions | Password Generator')
