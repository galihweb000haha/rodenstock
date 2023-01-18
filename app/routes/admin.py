""" Routes for admin user """
from flask import Blueprint, flash, redirect, render_template, request, url_for

# Blueprint Configuration
admin_bp = Blueprint(
    "admin_bp", __name__, template_folder="templates", static_folder="static"
)

@admin_bp.route("/", methods=["GET"])
def index():
    """ Dashboard for user Admin """
    return "Dashboard Admin"




