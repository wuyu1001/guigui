from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, StringField
from wtforms.validators import DataRequired

class CurrentWeatherForm(FlaskForm):
    city = TextField('城市', validators=[DataRequired()])
    query = SubmitField('查询')

    
class ForecastWeatherForm(FlaskForm):
    city = TextField('城市', validators=[DataRequired()])
    day = StringField('天数', validators=[DataRequired()])
    query = SubmitField('查询')


class HistoryWeatherForm(FlaskForm):  
    city = TextField('城市', validators=[DataRequired()])
    date = StringField('日期', validators=[DataRequired()])
    query = SubmitField('查询')
