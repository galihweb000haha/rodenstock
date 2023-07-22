"""Routes for user authentication."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user

import sys
 
# setting path
sys.path.insert(1, '/home/galih/flasklogin-tutorial/app')

from app import login_manager
from app.forms import LoginForm, SignupForm
from app.models import User, AdminProdi
from app import db

# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)


@auth_bp.route("/signup", methods=["GET", "POST"])
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
            login_user(user)  # Log in as newly created user
            return redirect(url_for("main_bp.dashboard"))
        flash("A user already exists with that email address.")
    return render_template(
        "signup.jinja2",
        title="Create an Account.",
        form=form,
        template="signup-page",
        body="Sign up for a user account.",
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.dashboard"))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            flash("Berhasil Login!")
            return redirect(next_page or url_for("main_bp.dashboard"))
        flash("Email atau Password Salah")
        return redirect(url_for("auth_bp.login"))
    return render_template(
        "login.jinja2",
        form=form,
        title="Log in.",
        template="login-page",
        body="Log in with your User account.",
    )


@auth_bp.route("/forgot", methods=["GET"])
def forgot():
    email = request.args.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        admin_prodi = AdminProdi.query.filter_by(user_id=user.id).first()
        admin_prodi.request_reset = True
        db.session.commit()
        flash("Cek email Anda secara berkala !", 'success')
    else:
        flash("Email yang Anda masukkan tidak terdaftar !", 'danger')

    return redirect(url_for("auth_bp.login"))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("Anda harus login terlebih dahulu!")
    return redirect(url_for("auth_bp.login"))
