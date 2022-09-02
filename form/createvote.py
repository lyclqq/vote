from wtforms import StringField,PasswordField,SubmitField,Form,widgets,SelectField,FileField,TextAreaField,DateField,IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length

class Createvote(FlaskForm):
    types=SelectField(label='处理类型',render_kw={'class':'form-control'},choices=[('不处理'),('生成投票')])
    submit=SubmitField('确定',render_kw={'class':'form-control'})