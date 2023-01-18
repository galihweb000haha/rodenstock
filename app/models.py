"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, Base


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "flasklogin-users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )
    website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.username)


class Mahasiswa(db.Model):
    __tablename__ = "mahasiswa"
    # main information
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(8))
    name = db.Column(db.String(50))
    state = db.Column(db.String(20))
    gender = db.Column(db.Boolean, unique=False)
    batch_year = db.Column(db.DateTime)
    # secondary information
    gpa_score = db.Column(db.Float, nullable=True)
    toefl_score = db.Column(db.Float, nullable=True)
    parents_income = db.Column(db.Float, nullable=True)
    # geographic information
    address = db.Column(db.Text, nullable=True)
    # private information
    # phone
    
    def __repr__(self):
        return "<User(name='%s', nim='%s', status='%s')>" % (
            self.nama,
            self.nim,
            self.status,
        )