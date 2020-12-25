"""Routes for lottery pages."""
from flask import Blueprint, render_template, request, flash

# Blueprint Configuration
baseBP = Blueprint('base', __name__,
                      template_folder='application/templates/base/',
                      static_folder='application/static', url_prefix='/')


@baseBP.route('/', methods=['GET', 'POST'])
@baseBP.route('/index', methods=['GET', 'POST'])
@baseBP.route('/home', methods=['GET', 'POST'])
def home():
    """  Main Index or Home page.  """


    return render_template('index.html', body="Web App",
                           title='Sharpe Digital Solutions')
