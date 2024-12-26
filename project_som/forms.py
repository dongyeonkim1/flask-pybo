from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class UserCreateForm(FlaskForm):
    userid = StringField('사용자 아이디', validators=[DataRequired(), Length(min=5, max=25)])
    username = StringField('사용자 이름', validators=[DataRequired(), Length(min=3, max=25)])
    student_id = StringField('학번', validators=[DataRequired(), Length(min=8, max=8)])
    major = StringField('전공', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


class UserLoginForm(FlaskForm):
    userid = StringField('사용자 아이디', validators=[DataRequired(), Length(min=5, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

