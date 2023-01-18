""" Routes for alumni user management """
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user


# Blueprint Configuration
alumni_bp = Blueprint(
    "alumni_bp", __name__, template_folder="templates", static_folder="static"
)

@alumni_bp.route("/alumni", methods=["GET"])
@login_required
def index():
    """ Alumni Page """
    return render_template(
        "user/alumni.jinja2",
        title="Bag Alumni | Manajemen",
        template="dashboard-template",
        current_user=current_user,
        message="You are now logged in!",
    )