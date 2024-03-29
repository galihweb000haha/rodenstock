""" Routes for prodi user management """
from flask import Blueprint, flash, redirect, render_template, url_for, request, abort
from flask_login import current_user, login_required, logout_user
from flask_mail import Message

from app.models import Prodi
from app.models import AdminProdi
from app.models import User
from app.forms import SignupForm, ProdiForm, Mahasiswa
from app import app, db, mail

from functools import wraps
from datetime import datetime
import re


def requires_access_level(access_level):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            # Dapatkan hak akses pengguna saat ini, misalnya dari objek pengguna yang telah diautentikasi
            user_access_level = current_user.level

            if user_access_level > access_level:
                # Jika hak akses pengguna tidak memenuhi persyaratan, hentikan permintaan dan kembalikan respons 403 Forbidden
                abort(403)

            # Jika hak akses pengguna memenuhi persyaratan, lanjutkan eksekusi fungsi asli
            return func(*args, **kwargs)

        return decorated_function

    return decorator




# Blueprint Configuration
prodi_bp = Blueprint(
    "prodi_bp", __name__, template_folder="templates", static_folder="static"
)

def send_email(subject, recipient, body):
    msg = Message(subject=subject,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[recipient])
    msg.body = body
    mail.send(msg)

@prodi_bp.route("/prodi", methods=["GET", "POST"])
@login_required
@requires_access_level(1)
def index():
    """ Prodi Page """
    data_prodi = Prodi.query.all()
    data_admin_prodi = AdminProdi.query.join(User, AdminProdi.user_id==User.id).join(Prodi, AdminProdi.kode_prodi==Prodi.kode_prodi).all()
    counter = ({
        'ammount_prodi': len(data_prodi),
        'ammount_admin_prodi': len(data_admin_prodi),
    })
    
    return render_template(
        "user/prodi/index.jinja2",
        title="Admin Prodi",
        template="dashboard-template",
        current_user=current_user,
        message="You are now logged in!",
        data_prodi=data_prodi,
        data_admin_prodi=data_admin_prodi,
        counter=counter,
    )

@prodi_bp.route("/prodi/kelola_prodi", methods=["GET", "POST"])
@login_required
@requires_access_level(1)
def prodi():
    data_prodi = Prodi.query.all()
    form = ProdiForm()
    referrer = request.referrer

    if form.validate_on_submit():

        pattern = re.compile("[0-9]+")
        if not (pattern.fullmatch(form.code.data) and len(form.code.data) == 2):
            flash("Kode prodi tidak valid.", 'success')
            return redirect(referrer)

        existing_prodi = Prodi.query.filter_by(nama_prodi=form.name.data).first()
        existing_kode_prodi = Prodi.query.filter_by(kode_prodi=form.code.data).first()
        if existing_kode_prodi is None and existing_prodi is None:
            
            prodi = Prodi(
                nama_prodi=form.name.data, kode_prodi=form.code.data
            )
            db.session.add(prodi)
            db.session.commit()

            flash("Prodi berhasil dibuat.", 'success')
            return redirect(referrer)
        
        flash("Nama prodi atau kode prodi sudah ada.", 'danger')
        return redirect(referrer)

    
    return render_template(
        "user/prodi/prodi.jinja2",
        title="Program Studi",
        template="dashboard-template",
        current_user=current_user,
        data_prodi=data_prodi,
        form=form,
    )

@prodi_bp.route("/prodi/delete_prodi/<string:kode_prodi>", methods=["GET"])
@login_required
@requires_access_level(1)
def delete_prodi(kode_prodi=None):
    prodi_is_exists = Mahasiswa.query.filter_by(prodi=kode_prodi).all()
    referrer = request.referrer
    if prodi_is_exists:
        flash("Prodi tidak dapat dihapus. Beberapa mahasiswa berelasi dengan prodi tersebut. ", 'danger')
    else:
        db.session.query(Prodi).filter_by(kode_prodi=kode_prodi).delete()
        db.session.commit()
        flash("Prodi berhasil dihapus.", 'success')

    return redirect(referrer)



@prodi_bp.route("/prodi/kelola_admin", methods=["GET", "POST"])
@login_required
@requires_access_level(1)
def admin_prodi():
    data_admin_prodi = db.session.query(
         AdminProdi, User, Prodi,
    ).filter(
         AdminProdi.user_id==User.id,
    ).filter(
         AdminProdi.kode_prodi==Prodi.kode_prodi,
    ).all()    

    form = SignupForm()
    referrer = request.referrer
    
    if form.validate_on_submit():
        if form.prodi.data == 'None':
            flash("Pilih prodi terlebih dahulu!", 'danger')
            return redirect(referrer)
        
        if form.confirm.data != form.password.data:
            flash("Konfirmasi password tidak cocok dengan password yang Anda masukkan!", 'danger')
            return redirect(referrer)
        
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            # create new user
            user = User(
                name=form.name.data, email=form.email.data, level=2
            )
            user.set_password(form.password.data)
            user.created_on = datetime.now()
            db.session.add(user)
            db.session.commit()

            # create user prodi
            admin = AdminProdi(
                user_id=user.id, kode_prodi=form.prodi.data
            )
            db.session.add(admin)
            db.session.commit()
            flash("User admin prodi berhasil dibuat.", 'success')
            return redirect(referrer)

        
        flash("Pengguna lain telah menggunakan email yang diinputkan.", 'danger')
        return redirect(referrer)

    else: 
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error in field '{field}': {error}")
        
    return render_template(
        "user/prodi/admin_prodi.jinja2",
        title="Admin Prodi",
        template="dashboard-template",
        current_user=current_user,
        message="You are now logged in!",
        data_admin_prodi=data_admin_prodi,
        form=form,
    )


@prodi_bp.route("/prodi/delete_admin/<int:user_id_param>", methods=["GET"])
@login_required
@requires_access_level(1)
def delete_admin(user_id_param):
    """ Delete user prodi """
    AdminProdi.query.filter_by(user_id = user_id_param).delete()
    User.query.filter_by(id = user_id_param).delete()

    db.session.commit()
    flash("User admin prodi berhasil dihapus.", 'success')
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
        flash("A user already exists with that email address.", 'danger')
    return render_template(
        "signup.jinja2",
        title="Create an Account.",
        form=form,
        template="signup-page",
        body="Sign up for a user account.",
    )

@prodi_bp.route("/prodi/reset_admin/<int:user_id>", methods=["GET"])
@login_required
@requires_access_level(1)
def reset_admin(user_id):
    default_passwd = 'galihganteng'
    user = User.query.get(user_id)
    if user:
        user.set_password(default_passwd)
        admin_prodi = AdminProdi.query.filter_by(user_id=user_id).first()
        admin_prodi.request_reset = False
        db.session.commit()
        recipient = user.email
        subject = "PERMINTAAN RESET PASSWORD"
        body = "Password berhasil di reset menjadi 'galihganteng'"
        send_email(subject, recipient, body)    
        flash("Password berhasil direset!", 'success')
        return redirect(request.referrer)
    
    flash("User admin tidak ditemukan!", 'danger')
    return redirect(request.referrer)