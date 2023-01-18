"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user


import sys
 
# setting path
sys.path.insert(1, '/home/galih/flasklogin-tutorial/app')

from app.models import Mahasiswa
from app.forms import MahasiswaForm

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        "dashboard.jinja2",
        title="Dashboard",
        template="dashboard-template",
        current_user=current_user,
        message="You are now logged in!",
    )


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))

@main_bp.route("/basic_input", methods=["GET"])
@login_required
def basic_input():
    """Input Students Data"""
    form = MahasiswaForm()

    return render_template(
        "basic_input.jinja2",
        title="Basic Input",
        template="dashboard-template",
        current_user=current_user,
        form=form,
    )
@main_bp.route("/settings", methods=["GET"])
@login_required
def settings():
    """ Settings """
    return render_template(
        "settings.jinja2",
        title="Settings",
        template="dashboard-template",
        current_user=current_user,
    )

@main_bp.route("/data_master", methods=["GET"])
@login_required
def data_master():
    """Students Data"""
    mahasiswa = Mahasiswa.query.all()
    return render_template(
        "data/data_master.jinja2",
        title="Data Master",
        template="dashboard-template",
        current_user=current_user,
        mahasiswa=mahasiswa,
    )

@main_bp.route("/export_import", methods=["GET"])
@login_required
def export_import():
    """ Export & Import """
    return "Export & Import Page"

@main_bp.app_errorhandler(404)
def handle_404(err):
    return render_template('404.jinja2'), 404

@main_bp.app_errorhandler(500)
def handle_500(err):
    return render_template('500.jinja2'), 500