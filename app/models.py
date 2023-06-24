"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import Integer, ForeignKey, String, Column, Enum
from sqlalchemy.orm import relationship

from . import db, Base


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    pekerjaan_ortu = db.Column(db.String(70), nullable=True)
    # geographic information
    address = db.Column(db.Text, nullable=True)

    # private information
    # phone
    # tambahan
    sertifikat = db.Column(db.Integer, nullable=True)
    prestasi = db.Column(db.Integer, nullable=True)
    organisasi = db.Column(db.Integer, nullable=True)
    relevan = db.Column(db.Boolean, unique=False, nullable=True)
    predict_proba = db.Column(db.Integer, nullable=True)
    

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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_prodi = db.Column(db.String(50))
    kode_prodi = db.Column(db.String(5))
    
    def __repr__(self):
        return "<Prodi(nama_prodi='%s', kode_prodi='%s')>" % (
            self.nama_prodi,
            self.kode_prodi,
        )
    
class AdminProdi(db.Model):
    __tablename__ = "admin_prodi"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    prodi_id = db.Column(db.Integer, db.ForeignKey(Prodi.id), primary_key=True)
    def __repr__(self):
        return "<AdminProdi(user_id='%s', prodi_id='%s')>" % (
            self.user_id,
            self.prodi_id,
        )

class Prestasi(db.Model):
    __tablename__ = "prestasi"
    mahasiswa_id = db.Column(db.Integer, db.ForeignKey(Mahasiswa.id), primary_key=True)
    nama_prestasi = db.Column(db.String(70))
    jenis_prestasi = db.Column(db.Integer)

class Sertifikat(db.Model):
    __tablename__ = "sertifikat"
    mahasiswa_id = db.Column(db.Integer, db.ForeignKey(Mahasiswa.id), primary_key=True)
    nama_sertifikat = db.Column(db.String(70))
    jenis_sertifikat = db.Column(db.Integer)

class Organisasi(db.Model):
    __tablename__ = "organisasi"
    mahasiswa_id = db.Column(db.Integer, db.ForeignKey(Mahasiswa.id), primary_key=True)
    nama_organisasi = db.Column(db.String(70))
    peran_organisasi = db.Column(db.Integer)

    
    