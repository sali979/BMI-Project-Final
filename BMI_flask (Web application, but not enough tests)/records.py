from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user

from __init__ import db

# our main app blueprint
from bmi.record import Record

record = Blueprint('record', __name__)


@record.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':  # if the request is a GET we return the create page
        return render_template("create.html")

    else:
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        target = float(request.form.get('target'))
        gender = request.form.get('weight')
        user_id = current_user.id
        dob = request.form.get('date_of_birth')

        print(dob)

        # new_record = Record(gender=gender, weight=weight, user_id=user_id, height=height, date_of_birth=dob)
        new_record = Record(height, weight, user_id, gender, dob,target)

        if new_record:
            flash("Record added successfully")
        # add the new event to the database
        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for('main.dashboard'))
