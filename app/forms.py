"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

from .models import Mahasiswa, Prodi

from . import db


class SignupForm(FlaskForm):
    """User Sign-up Form."""

    name = StringField("Nama Lengkap", validators=[DataRequired()])

    list_selection = [(t.kode_prodi, str(t.nama_prodi) ) for t in Prodi.query.all()]
    list_selection.insert(0, (None, '-- Pilih Program Studi --')) 
    prodi = SelectField('prodi',  validators=[
            DataRequired(),
        ],choices=list_selection)
    
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
        "Konfirmasi Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    website = StringField("Website", validators=[Optional()])
    submit = SubmitField("Simpan")


class LoginForm(FlaskForm):
    """User Log-in Form."""

    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Enter a valid email")]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Masuk")


class MahasiswaForm(FlaskForm):
    """ Input Data Mahasiswa """
    list_selection = [(t.id, str(t.nim) + '-' + t.name ) for t in Mahasiswa.query.all()]
    list_selection.insert(0, (None, 'Masukkan NIM atau Nama')) 
    nim = SelectField('nim', 
        choices=list_selection, validate_choice=False, validators=[Length(min=8, message="Jumlah NIM adalah 8"), Length(max=8, message="Jumlah NIM adalah 8"),])
    submit = SubmitField("Simpan")

class ReportSelectionForm(FlaskForm):
    list_selection = [(t.kode_prodi, str(t.nama_prodi) ) for t in Prodi.query.all()]
    list_selection.insert(0, (None, '-- Pilih Program Studi --')) 
    prodi = SelectField('prodi', choices=list_selection)

    batch_year = db.session.query(Mahasiswa.batch_year).group_by(Mahasiswa.batch_year).all()
    list_selection = [(t[0], str(t[0]) ) for t in batch_year]
    list_selection.insert(0, (None, '-- Pilih Tahun Akademik --')) 
    batch_year = SelectField('batch_year', choices=list_selection)

class ProdiForm(FlaskForm):
    name = StringField("Nama Prodi", validators=[DataRequired()])
    code = StringField("Kode Prodi", validators=[DataRequired()])
    
    submit = SubmitField("Simpan")
