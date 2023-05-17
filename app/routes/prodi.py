""" Routes for prodi user management """
from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required, logout_user

from app.models import Prodi
from app.models import User

from app.forms import SignupForm
from app import db

# Blueprint Configuration
prodi_bp = Blueprint(
    "prodi_bp", __name__, template_folder="templates", static_folder="static"
)

@prodi_bp.route("/prodi", methods=["GET", "POST"])
@login_required
def index():
    """ Prodi Page """
    data_prodi = Prodi.query.join(User, Prodi.user_id==User.id).all()
    form = SignupForm()
    referrer = request.referrer
    
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            # create new user
            user = User(
                name=form.name.data, email=form.email.data, level=2
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            # create user prodi
            prodi = Prodi(
                user_id=user.id, nama_prodi="Teknik Informatika", kode_prodi="09"
            )
            db.session.add(prodi)
            db.session.commit()
            flash("User admin prodi berhasil dibuat.")
            return redirect(referrer)

        
        flash("Pengguna telah menggunakan email yang diinputkan.")
        return redirect(referrer)
        
    return render_template(
        "user/prodi.jinja2",
        title="Admin Prodi",
        template="dashboard-template",
        current_user=current_user,
        message="You are now logged in!",
        data_prodi=data_prodi,
        form=form,
    )
        
@prodi_bp.route("/delete_prodi/<int:user_id_param>", methods=["GET"])
@login_required
def delete_prodi(user_id_param):
    """ Delete user prodi """
    Prodi.query.filter_by(user_id = user_id_param).delete()
    User.query.filter_by(id = user_id_param).delete()

    db.session.commit()
    flash("User admin prodi berhasil dihapus.")
    return redirect(request.referrer)

@prodi_bp.route("/signup", methods=["GET", "POST"])
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data, email=form.email.data, website=form.website.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            return redirect(url_for("main_bp.index"))
        flash("A user already exists with that email address.")
    return render_template(
        "signup.jinja2",
        title="Create an Account.",
        form=form,
        template="signup-page",
        body="Sign up for a user account.",
    )
