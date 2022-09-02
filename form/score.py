from wtforms import StringField,PasswordField,SubmitField,Form,widgets,SelectField,FileField,TextAreaField,DateField,IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,NumberRange

class ScoreForm(FlaskForm):
    score=IntegerField('得分',validators=[DataRequired(message='得分不能为空'),NumberRange(min=50,max=100,message='得分只能为50-100')],render_kw={'class':'form-control','placeholder':'得分只能为50-100'})
    submit=SubmitField('提交',render_kw={'class':'btn btn-block'})

class ScoreadminForm(FlaskForm):
    submit = SubmitField('提交', render_kw={'class': 'btn btn-block'})