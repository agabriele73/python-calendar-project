from flask import Blueprint, render_template, redirect
import sqlite3
from datetime import datetime
import os
from .forms import AppointmentForm


calendar_bp = Blueprint('calendar_bp', __name__, url_prefix='/')
DB_FILE=os.environ.get('DB_FILE')



@calendar_bp.route('/', methods=['GET', 'POST'])
def main():
    form = AppointmentForm()
    # Use this code snippet in running your INSERT statement
    # You must have named the attributes on your AppointmentForm
    # class what was recommended in the table for this to work.
    params = {
        'name': form.name.data,
        'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
        'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
        'description': form.description.data,
        'private': form.private.data
    }
    sql_statement = '''
        INSERT INTO appointments (name, start_datetime,  end_datetime,  description,
        private) VALUES (:name, :start_datetime, :end_datetime, :description, :private)   
    '''
    if form.validate_on_submit():
        with sqlite3.connect(DB_FILE) as conn:
            curs = conn.cursor()
            curs.execute(sql_statement, params)
        return redirect('/')
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        rows = curs.execute(
            '''
            SELECT *
            FROM appointments
            order by start_datetime
            '''
            ).fetchall()
        

        for  row in rows:
            lst = list(row)
            print('----', lst)
            starttime_obj = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            endtime_obj = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')

        return render_template('main.html', rows=rows, form=form)

        


        # starttime_str = rows[0][2]
        # starttime_obj = datetime.strptime(starttime_str, '%Y-%m-%d %H:%M:%S')
        # endtime_str = rows[0][3]
        # endtime_obj = datetime.strptime(endtime_str, '%Y-%m-%d %H:%M:%S')
        
