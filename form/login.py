from wtforms import StringField,PasswordField,SubmitField,Form,widgets,SelectField,FileField,TextAreaField,DateField,IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length

#登陆
class LoginForm(FlaskForm):
    #username = StringField( validators=[DataRequired(), Length(1, 20)])
    username = StringField(label='用户名:',
        validators=[
            DataRequired(message='用户名不能为空'),
            Length(min=1, max=5, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"输入注册用户名"}
    )
    password = PasswordField(
        label='用户密码：',
        validators=[
            DataRequired(message='密码不能为空'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder": "输入用户密码"}
    )
    verify_code = StringField('验证码', validators=[DataRequired(), Length(1, 4)],render_kw={'class': 'form-control',
                   "placeholder":"输入验证码"})
    submit = SubmitField('登录',render_kw={'class':'btn btn-block btn-info'})