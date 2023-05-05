from flask_wtf import FlaskForm
from wtforms.fields import ( BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField)
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime, timedelta

def get_time():
    time_now = datetime.now()
    time_now = timedelta(time_now)
    return time_now
def validate_end_date(form, field):
    start = datetime.combine(form.start_date.data, form.start_time.data)
    end = datetime.combine(form.end_date.data, form.end_time.data)
    if start >= end:
        msg = 'End date/time must come after start date/time'
        raise ValidationError(msg)
    
    
class AppointmentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    start_date = DateField('start_date', validators=[DataRequired()],  default=datetime.today())
    start_time = TimeField('start_time', validators=[DataRequired()], default=datetime.now().timetz())
    end_date = DateField('end_date', validators=[DataRequired()],  default=datetime.today())
    end_time = TimeField('end_time', validators=[DataRequired()], default=datetime.now().timetz())
    description = TextAreaField('description', validators=[DataRequired()])
    private = BooleanField('private')
    submit = SubmitField('Submit Appointment')