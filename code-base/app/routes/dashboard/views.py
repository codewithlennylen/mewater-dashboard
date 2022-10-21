from flask import Blueprint, render_template
# from flask_login import login_required


# Create Blueprint
dashboard_view = Blueprint('dashboard_view',
                           __name__,
                           static_folder='static',
                           template_folder='templates')


@dashboard_view.route('/dashboard/')
# @login_required
def dashboard():

    return render_template('dashboard/dashboard.html')
