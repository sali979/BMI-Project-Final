from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from __init__ import create_app, db

# our main app blueprint
from bmi.record import Record
from services.bmi_calculator import bmi_evaluation

main = Blueprint('main', __name__)


@main.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    records = Record.query.filter_by(user_id=current_user.id).all()
    total_records = len(records)

    # make recommendation
    # for record in records:
    #     record['bmi'] = bmi_evaluation(records[0].height, records[0].weight)

    return render_template("dashboard.html", user=current_user, records=records, total_records=total_records)


app = create_app()  # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
