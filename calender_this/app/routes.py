from flask import Blueprint, render_template
import os


calendar_bp = Blueprint('calendar_bp', __name__, url_prefix='/')
DB_FILE=os.environ.get('DB_FILE')


@calendar_bp.route('/')
def main():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        rows = curs.fetchall()
        return render_template('main.html', rows=rows)
