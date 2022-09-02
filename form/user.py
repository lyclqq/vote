from wtforms import StringField,PasswordField,SubmitField,Form,widgets,SelectField,FileField,TextAreaField,DateField,IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length

class UserForm(FlaskForm):
    username=StringField(label='用户名：',
                         validators=[DataRequired(message='用户名能为空'),Length(1,20)],
                         render_kw={'class':'form-control',"palcehlder":"注册用户名"})
    usertype=SelectField(label='用户类型:', render_kw={'class': 'form-control'}, choices=[('admin','admin'),('user1','user1'),('user2','user2')])

    submit=SubmitField('新建',render_kw={'class':'btn btn-block btn-info'})