"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for, request, jsonify, send_file
from flask_login import current_user, login_required, logout_user
from openpyxl import Workbook
from io import BytesIO

import sys, requests, pandas
 
# setting path
sys.path.insert(1, '/home/galih/flasklogin-tutorial/app')


from app import db
from app.models import Mahasiswa
from app.forms import MahasiswaForm
from app.helper import galih_helper

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

# @main_bp.route("/prodi", methods=["GET"])
# @login_required
# def dashboard_prodi():
#     """Dashboard for prodi"""
#     return render_template(
#         "dashboard_prodi.jinja2",
#         title="Dashboard",
#         template="dashboard-template",
#         current_user=current_user,
#         message="You are now logged in!",
#     )

# @main_bp.route("/alumni", methods=["GET"])
# @login_required
# def dashboard_alumni():
#     """Dashboard for alumni"""
#     return render_template(
#         "dashboard_alumni.jinja2",
#         title="Dashboard",
#         template="dashboard-template",
#         current_user=current_user,
#         message="Yo are now logged in!",
#     )

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
    nim = request.args.get('nim')
    mahasiswa = [] if not nim  else Mahasiswa.query.filter_by(nim=nim).first()
    detail_mahasiswa = {'data': [[]]} if not nim else galih_helper.Api.get_mhs(nim)
    
    # cuman buat pengingat
    list_selection = [(t.id, t.nim) for t in Mahasiswa.query.all()]
    print(list_selection)
    # hahaha

    return render_template(
        "data/basic_input.jinja2",
        title="Basic Input",
        template="dashboard-template",
        current_user=current_user,
        mahasiswa=mahasiswa,
        detail_mahasiswa=detail_mahasiswa['data'][0],
        form=form,
        preview=None,
    )

@main_bp.route("/report", methods=["GET"])
@login_required
def report():
    """Report Page"""
    data = [
        {
            "nama": "M Galih Fikran Syah",
            "semester": "8 (Delapan)",
            "prodi": "Teknik Informatika",
            "relevan": "Relevan"
        },
        {
            "nama": "Dewangga",
            "semester": "8 (Delapan)",
            "prodi": "Teknik Informatika",
            "relevan": "Relevan"
        },
        {
            "nama": "Apriliana",
            "semester": "8 (Delapan)",
            "prodi": "Teknik Informatika",
            "relevan": "Relevan"
        },
    ]
    return render_template(
        "report.jinja2",
        title="Report",
        template="dashboard-template",
        datas=data,
        current_user=current_user
    )

@main_bp.route("/excel/download")
@login_required
def download_excel():
    wb = Workbook()
    ws = wb.active
    ws.append(['Nama', 'Semester', 'Prodi', 'Hasil Prediksi'])
    ws.append(['Galih Fikran Syah', '8 (Delapan)', 'Teknik Informatika','Relevan'])
    ws.append(['Gaston', '8 (Delapan)', 'Teknik Informatika','Relevan'])
    ws.append(['Zainudin', '8 (Delapan)', 'Teknik Informatika','Relevan'])
    ws.append(['Rohim', '8 (Delapan)', 'Teknik Informatika','Relevan'])
    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    return send_file(file_stream, attachment_filename="tdd-excel.xlsx", as_attachment=True)

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
    prodi = galih_helper.Api.get_prodi()
    
    return render_template(
        "data/data_master.jinja2",
        title="Data Master",
        template="dashboard-template",
        current_user=current_user,
        mahasiswa=mahasiswa,
        prodi=prodi,
    )

@main_bp.route("/export_import", methods=["GET"])
@login_required
def export_import():
    """ Export & Import """
    data = ['Nilai IPK', 'Nilai TOEFL', 'Keaktifan Mahasiswa', 'Penghasilan Ortu']
    return render_template(
        "export_import.jinja2",
        title="Export/Import",
        template="dashboard-template",
        current_user=current_user,
        data=data
    )

@main_bp.route("/get_achievement", methods=["GET"])
def get_achievement():
    nim = request.args.get('nim')
    return {'data' : Mahasiswa.query.filter_by(nim=nim).first().get_achievement()}

@main_bp.route("/input_data", methods=["POST"])
def input_data():
    """Single Import"""
    nim = request.form['nim2']
    gpa_score = request.form['ipk']
    prestasi = request.form['prestasi']
    organisasi = request.form['organisasi']
    sertifikat = request.form['sertifikat']
    nama_lengkap = request.form['nama_lengkap']
    gender = 0 if request.form['jk'].lower() == 'p' else 1
    state = 0 if request.form['state'].lower() == 'Aktif' else 1
    batch_year = request.form['batch_year']

    data_mhs = Mahasiswa.query.filter_by(nim=nim).first()
    
    if not data_mhs:
        # create data
        mhs = Mahasiswa(nim=nim, gender=gender, gpa_score=gpa_score, state=state, batch_year=batch_year, name=nama_lengkap, sertifikat=sertifikat, organisasi=organisasi, prestasi=prestasi)
        db.session.add(mhs)
        db.session.commit()

        return redirect(url_for("main_bp.basic_input"))

    else:
        # update data
        existing_mhs = Mahasiswa.query.filter_by(nim=nim).first()
        existing_mhs.gpa_score = gpa_score
        existing_mhs.prestasi = prestasi
        existing_mhs.organisasi = organisasi
        existing_mhs.sertifikat = sertifikat
        existing_mhs.gender = gender
        existing_mhs.state = state
        existing_mhs.batch_year = batch_year
        
        db.session.commit()
        return redirect(url_for("main_bp.basic_input"))

@main_bp.route("/input_batch", methods=["POST"])
def input_batch():
    """Import Batch"""
    # Read the File using Flask request
    file = request.files['file']
    # generate filename

    # save file in local directory
    file.save("upload/"+file.filename)
 
    # Parse the data as a Pandas DataFrame type
    data = pandas.read_excel(file)
 
    # Return HTML snippet that will render the table
    preview_excel = data.to_html()

    form = MahasiswaForm()
    nim = request.args.get('nim')
    mahasiswa = [] if not nim  else Mahasiswa.query.filter_by(nim=nim).first()
    detail_mahasiswa = {'data': [[]]} if not nim else galih_helper.Api.get_mhs(nim)
    
    # cuman buat pengingat
    list_selection = [(t.id, t.nim) for t in Mahasiswa.query.all()]
    print(list_selection)
    # hahaha
    return render_template(
        "data/basic_input.jinja2",
        title="Basic Input",
        template="dashboard-template",
        current_user=current_user,
        mahasiswa=mahasiswa,
        detail_mahasiswa=detail_mahasiswa['data'][0],
        form=form,
        preview=preview_excel,
    )

@main_bp.app_errorhandler(404)
def handle_404(err):
    return render_template('404.jinja2'), 404

@main_bp.app_errorhandler(500)
def handle_500(err):
    return render_template('500.jinja2'), 500

# API INCOME OASE
@main_bp.route("/get_mhs", methods=["GET"])
def get_mhs():
    """ Get Mahasiswa From OASE """
    nim = request.args.get('nim')
    oase_key = '785a4062ab84fad16'
    api_server = 'https://localhost/OASE'
    response = requests.get("{api_server}/api/Mahasiswa/getMhsByNIMSiputa?oase_key={oase_key}&nim={nim}".format(nim=nim, oase_key=oase_key, api_server=api_server), verify=False)
    return response.json()

@main_bp.route("/get_tahun_angkatan", methods=["GET"])
def get_tahun_angkatan():
    """ Get Tahun Angkatan From OASE """
    oase_key = '785a4062ab84fad16'
    api_server = 'http://localhost:45275'
    response = requests.get("{api_server}/api/Mahasiswa/tahun_angkatan?oase_key={oase_key}".format(oase_key=oase_key, api_server=api_server))
    return response.text

@main_bp.route("/get_mhs_by_tahun_prodi", methods=["GET"])
def get_mhs_by_tahun_prodi():
    """ Get Mahasiswa From OASE """
    tahun = request.args.get('tahun')
    prodi = request.args.get('prodi')
    oase_key = '785a4062ab84fad16'
    api_server = 'https://localhost/OASE'
    
    response = requests.get("{api_server}/api/Mahasiswa/getMahasiswaByTahunProdiSiputa?oase_key={oase_key}&tahun={tahun}&prodi={prodi}".format(tahun=tahun, prodi=prodi, oase_key=oase_key, api_server=api_server), verify=False)
    return response.json()