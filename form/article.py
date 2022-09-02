from wtforms import StringField,PasswordField,SubmitField,Form,widgets,SelectField,FileField,TextAreaField,DateField,IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):
    title=StringField('标题',validators=[DataRequired(message='标题不能为空'),Length(min=2,max=200,message='标题长度必须大于%(min)d小于%(max)d')],render_kw={'class':'form-control'})
    titlelink = StringField('外部链接', validators=[
                                          Length(min=10, max=200, message='外部链接长度必须大于%(min)d小于%(max)d')],
                        render_kw={'class': 'form-control'})
    author = StringField('作者', validators=[
        Length(min=2, max=100, message='作者长度必须大于%(min)d小于%(max)d')],
                            render_kw={'class': 'form-control'})
    types= StringField('体裁 ', validators=[
        Length(min=2, max=100, message='体裁长度必须大于%(min)d小于%(max)d')],
                            render_kw={'class': 'form-control'})
    pubdate  = DateField('发布日期', format='%Y-%m-%d',validators=[DataRequired('日期不能为空')],
                            render_kw={'class': 'form-control'})
    cause = StringField('推荐理由', validators=[
        Length(min=10, max=200, message='推荐理由长度必须大于%(min)d小于%(max)d')],
                            render_kw={'class': 'form-control'})
    content=CKEditorField('原文',render_kw={'class':'form-control'})
    submit=SubmitField('提交',render_kw={'class':'form-control'})
