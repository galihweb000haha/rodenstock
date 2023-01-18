"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

from .models import Mahasiswa


class SignupForm(FlaskForm):
    """User Sign-up Form."""

    name = StringField("Name", validators=[DataRequired()])
    email = StringField(
        "Email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    confirm = PasswordField(
        "Confirm Your Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    website = StringField("Website", validators=[Optional()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """User Log-in Form."""

    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Enter a valid email")]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Masuk")


class MahasiswaForm(FlaskForm):
    """ Input Data Mahasiswa """
    list_selection = [(t.id, t.nim) for t in Mahasiswa.query.all()]
    list_selection.insert(0, (None, 'Pilih NIM')) 
    nim = SelectField('nim', 
        choices=list_selection, validate_choice=False, validators=[DataRequired(), Length(min=8, message="Jumlah NIM adalah 8"), Length(max=8, message="Jumlah NIM adalah 8"),])
    submit = SubmitField("Simpan")