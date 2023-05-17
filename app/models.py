"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship

from . import db, Base


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )
    gender = db.Column(db.Boolean, unique=False, nullable=True)
    no_hp = db.Column(db.String(20), unique=False, nullable=True)
    foto = db.Column(db.Text, unique=False, nullable=True)
    website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    level = db.Column(db.Integer, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.name)
        
    def get_datadiri(self):
        return {
            'name': self.name,
            'email': self.email,
            'no_hp': self.no_hp,
            'gender': self.gender,
            'foto': self.foto,
            'level': self.level,
        }


class Mahasiswa(db.Model):
    __tablename__ = "mahasiswa"
    # main information
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(8))
    name = db.Column(db.String(50))
    state = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.Boolean, unique=False, nullable=True)
    batch_year = db.Column(db.DateTime, nullable=True)
    # secondary information
    gpa_score = db.Column(db.Float, nullable=True)
    toefl_score = db.Column(db.Float, nullable=True)
    parents_income = db.Column(db.Float, nullable=True)
    # geographic information
    address = db.Column(db.Text, nullable=True)
    # private information
    # phone
    # tambahan
    sertifikat = db.Column(db.Integer, nullable=True)
    prestasi = db.Column(db.Integer, nullable=True)
    organisasi = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return "<User(name='%s', nim='%s', status='%s')>" % (
            self.name,
            self.nim,
            self.state,
        )

    def get_achievement(self):
        return {
            'prestasi': self.prestasi,
            'organisasi': self.organisasi,
            'sertifikat': self.sertifikat,
            'gpa_score': self.gpa_score,
            'parents_income': self.parents_income
        }
    
class Prodi(db.Model):
    __tablename__ = "prodi"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    nama_prodi = db.Column(db.String(50))
    kode_prodi = db.Column(db.String(5))
    user_prodi = relationship("User")
    
    def __repr__(self):
        return "<Prodi(user_prodi='%s', nama_prodi='%s', kode_prodi='%s')>" % (
            self.user_prodi,
            self.nama_prodi,
            self.kode_prodi,
        )
