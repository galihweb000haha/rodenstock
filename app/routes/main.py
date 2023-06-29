"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for, request, jsonify, send_file
from flask_login import current_user, login_required, logout_user
from openpyxl import Workbook
from io import BytesIO

import sys, requests, pandas, math
 
# setting path
sys.path.insert(1, '/home/galih/flasklogin-tutorial/app')


from app import db

from app.models import Mahasiswa
from app.models import Prestasi
from app.models import Organisasi
from app.models import Sertifikat
from app.models import AdminProdi

from app.forms import MahasiswaForm
from app.forms import ReportSelectionForm
from app.helper import galih_helper

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""

    # panel card information
    ammount_admin = AdminProdi.query.count()
    datas = Mahasiswa.query.all()
    panel_card = ({
        'admin_prodi_ammount': ammount_admin,
        'mahasiswa_ammount': len(datas)
    })
    
    relevan_count = 0
    tidak_relevan_count = 0
    for data in datas:
        if data.relevan == 1:
            relevan_count = relevan_count + 1
        if data.relevan == 0:
            tidak_relevan_count = tidak_relevan_count + 1
    relevan_percentage = round(relevan_count / len(datas) * 100)
    tidak_relevan_percentage = round(tidak_relevan_count / len(datas) * 100)
            

    return render_template(
        "dashboard.jinja2",
        title="Dashboard",
        template="dashboard-template",
        current_user=current_user,
        message="You are now logged in!",
        relevan_percentage=relevan_percentage, 
        tidak_relevan_percentage=tidak_relevan_percentage,
        panel_card=panel_card,
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
    mahasiswa = [] if not nim else Mahasiswa.query.filter_by(nim=nim).first()

    
    if mahasiswa:
        sertifikat = Sertifikat.query.filter_by(mahasiswa_id=mahasiswa.id).all()
        organisasi = Organisasi.query.filter_by(mahasiswa_id=mahasiswa.id).all()
        prestasi = Prestasi.query.filter_by(mahasiswa_id=mahasiswa.id).all()
        
        data_pencapaian = [prestasi, organisasi, sertifikat]
    else:
        data_pencapaian = []

    # production --> start
    # detail_mahasiswa = {'data': [[]]} if not nim else galih_helper.Api.get_mhs(nim)
    # detail_mahasiswa = detail_mahasiswa['data'][0]
    # production --> end

    # development --> start
    detail_mahasiswa = [[]] if not nim else galih_helper.TestingApi.get_mhs_by_nim(nim)
    # development --> end
    print("===========", detail_mahasiswa, "==============")


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
        detail_mahasiswa=detail_mahasiswa,
        form=form,
        preview=None,
        data_pencapaian=data_pencapaian,
    )

@main_bp.route("/report", methods=["GET"])
@login_required
def report():
    """Report Page"""
    # data = [
    #     {
    #         "nama": "M Galih Fikran Syah",
    #         "semester": "8 (Delapan)",
    #         "prodi": "Teknik Informatika",
    #         "relevan": "Relevan"
    #     },
    #     {
    #         "nama": "Dewangga",
    #         "semester": "8 (Delapan)",
    #         "prodi": "Teknik Informatika",
    #         "relevan": "Relevan"
    #     },
    #     {
    #         "nama": "Apriliana",
    #         "semester": "8 (Delapan)",
    #         "prodi": "Teknik Informatika",
    #         "relevan": "Relevan"
    #     },
    # ]
    # INI NGAMBIL DARI DATABASE SAJA YAK!!!!!!
    batch_year = db.session.query(Mahasiswa.batch_year).group_by(Mahasiswa.batch_year).all()

    form = ReportSelectionForm()
    nims = Mahasiswa.query.with_entities(Mahasiswa.nim).all()
    data = galih_helper.PredictModel.predict_multiple(nims)
    

    return render_template(
        "report/report.jinja2",
        title="Report",
        template="dashboard-template",
        datas=data,
        current_user=current_user,
        form=form,
    )

@main_bp.route("/report/rincian/<nim>", methods=["GET"])
@login_required
def rincian(nim):
    mhs = Mahasiswa.query.filter_by(nim=nim).all()[0]

    # attribut utama  
    sertifikat = Sertifikat.query.filter_by(mahasiswa_id=mhs.id).all() 
    prestasi = Prestasi.query.filter_by(mahasiswa_id=mhs.id).all() 
    organisasi = Organisasi.query.filter_by(mahasiswa_id=mhs.id).all() 

    help = galih_helper.Utility
    informasi_tambahan = ({
        'sertifikat': sertifikat,
        'prestasi': prestasi,
        'organisasi': organisasi,
    })

    return render_template(
        "report/rincian.jinja2",
        title="Report",
        template="dashboard-template",
        mhs=mhs,
        informasi_tambahan=informasi_tambahan,
        current_user=current_user,
        help=help,
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
    # mahasiswa = Mahasiswa.query.all()
    # prodi = galih_helper.Api.get_prodi()
    mahasiswa = galih_helper.TestingApi.get_mhs()
    mahasiswa = mahasiswa['mahasiswa']
    print(mahasiswa)
    prodi = galih_helper.TestingApi.get_prodi()
    prodi = prodi['prodi']

    
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

    # pembobotan terhadap attribut utama
    prestasi = galih_helper.Pembobotan.pembobotan_prestasi(request.form.getlist('prestasi'))
    organisasi = galih_helper.Pembobotan.pembobotan_organisasi(request.form.getlist('organisasi'))
    sertifikat = galih_helper.Pembobotan.pembobotan_sertifikat(request.form.getlist('sertifikat'))
  
    nama_prestasi = request.form.getlist('nama_prestasi')
    nama_organisasi = request.form.getlist('nama_organisasi')
    nama_sertifikat = request.form.getlist('nama_sertifikat')

    # attribut tambahan
    nim = request.form['nim2']
    name = request.form['nama']
    gender = 0 if request.form['jk'].lower() == 'p' else 1
    # state = 0 if request.form['state'].lower() == 'Aktif' else 1
    # batch_year = request.form['batch_year']
    gpa_score = request.form['ipk']
    parents_income = request.form['parents_income']
    pekerjaan_ortu = request.form['pekerjaan_ortu']
    data_mhs = Mahasiswa.query.filter_by(nim=nim).first()


    # Masukkin achievement ke database
    # 1. prestasi
    for index, value in enumerate(request.form.getlist('prestasi')):
        prestasi_store = Prestasi(mahasiswa_id=data_mhs.id, nama_prestasi=nama_prestasi[index], jenis_prestasi=value)
        db.session.add(prestasi_store)
        db.session.commit()
    # 2. organisasi
    for index, value in enumerate(request.form.getlist('organisasi')):
        organisasi_store = Organisasi(mahasiswa_id=data_mhs.id, nama_organisasi=nama_organisasi[index], peran_organisasi=value)
        db.session.add(organisasi_store)
        db.session.commit()
    # 3. Sertifikat
    for index, value in enumerate(request.form.getlist('sertifikat')):
        sertifikat_store = Sertifikat(mahasiswa_id=data_mhs.id, nama_sertifikat=nama_sertifikat[index], jenis_sertifikat=value)
        db.session.add(sertifikat_store)
        db.session.commit()
    

    if not data_mhs:
        # create data
        mhs = Mahasiswa(nim=nim, gender=gender, gpa_score=gpa_score, name=name, sertifikat=sertifikat, organisasi=organisasi, prestasi=prestasi, parents_income=parents_income, pekerjaan_ortu=pekerjaan_ortu)
        db.session.add(mhs)
        db.session.commit()

        # predict relevance
        res = galih_helper.PredictModel.predict(nim)
        data_mhs.relevan = res[0]
        data_mhs.predict_proba = res[1]

        db.session.commit()
    else:
        # update data
        res = galih_helper.PredictModel.predict(nim)

        existing_mhs = Mahasiswa.query.filter_by(nim=nim).first()
        existing_mhs.gpa_score = gpa_score
        existing_mhs.prestasi = prestasi
        existing_mhs.organisasi = organisasi
        existing_mhs.sertifikat = sertifikat
        existing_mhs.gender = gender
        existing_mhs.relevan = res[0]
        existing_mhs.predict_proba = res[1]
        # existing_mhs.state = state
        # existing_mhs.batch_year = batch_year
        
        db.session.commit()
    
    return redirect(url_for("main_bp.basic_input"))
   

@main_bp.route("/input_batch", methods=["POST"])
def input_batch():
    """Import Batch"""
    # Read the File using Flask request
    file = request.files['file']
    # generate filename

    # save file in local directory
    # file.save("upload/"+file.filename)
    # book = xlrd.open_workbook("upload/"+file.filename)
    # sheet = book.sheet_by_name()

    kumpulin_ayok = []
    nim_compare = None
    data = pandas.read_excel(file)
    for index, row in data[0:len(data.index)].iterrows():
        # each row is returned as a pandas series
        nim = row['nim']
        nama = row['nama']
        jk = True if row['jk'] == 'laki-laki' else False
        ipk = row['ipk']
        penghasilan_ortu = row['penghasilan_ortu']
        pekerjaan_ortu = row['pekerjaan_ortu']

        nama_prestasi = row['nama_prestasi'] if row['nama_prestasi'] == row['nama_prestasi']  else False 
        tingkat_prestasi = row['tingkat_prestasi'] if row['tingkat_prestasi'] == row['tingkat_prestasi'] else False
        nama_sertifikat = row['nama_sertifikat'] if row['nama_sertifikat'] == row['nama_sertifikat'] else False
        jenis_sertifikat = row['jenis_sertifikat'] if row['jenis_sertifikat'] == row['jenis_sertifikat'] else False
        nama_organisasi = row['nama_organisasi'] if row['nama_organisasi'] == row['nama_organisasi'] else False
        peran_organisasi = row['peran_organisasi'] if row['peran_organisasi'] == row['peran_organisasi'] else False

        if nim_compare != nim or nim_compare is None:
            nim_compare = nim
            current_mahasiswa = Mahasiswa.query.filter_by(nim=nim).first()

            if current_mahasiswa:
                if nama: current_mahasiswa.name = nama
                if ipk: current_mahasiswa.gpa_score = ipk
                if jk: current_mahasiswa.gender = jk
                if penghasilan_ortu: current_mahasiswa.parents_income = penghasilan_ortu
                if pekerjaan_ortu: current_mahasiswa.pekerjaan_ortu = pekerjaan_ortu
                db.session.commit()
            else :
                mhs = Mahasiswa(nim=nim, gender=jk, gpa_score=ipk, name=nama, parents_income=penghasilan_ortu, pekerjaan_ortu=pekerjaan_ortu)
                db.session.add(mhs)
                db.session.commit()

            kumpulin_ayok.append(
                {
                    'nim': nim,
                    'prestasi': [nama_prestasi, tingkat_prestasi],
                    'sertifikat': [nama_sertifikat, jenis_sertifikat],
                    'organisasi': [nama_organisasi, peran_organisasi],
                }                 
            )

        else:
            nim_compare = nim
            kumpulin_ayok.append(
                {
                    'nim': nim,
                    'prestasi': [nama_prestasi, tingkat_prestasi],
                    'sertifikat': [nama_sertifikat, jenis_sertifikat],
                    'organisasi': [nama_organisasi, peran_organisasi],
                }                 
            )
    
    start_nim = None
    count_index = 0 
    removed_list = []
 
    while count_index < len(kumpulin_ayok):
        prestasi_per_mahasiswa = []
        sertifikat_per_mahasiswa = []
        organisasi_per_mahasiswa = []
        for index, ka in enumerate(kumpulin_ayok):
            if start_nim == ka['nim'] or start_nim is None:
                if index not in removed_list:
                    start_nim = ka['nim']
                    removed_list.append(index)

                    if ka['prestasi'][0] is not False:
                        prestasi_per_mahasiswa.append([ka['prestasi'][0], galih_helper.Pembobotan.bobot['prestasi'][ka['prestasi'][1]]])
                    if ka['sertifikat'][0] is not False:
                        sertifikat_per_mahasiswa.append([ka['sertifikat'][0], galih_helper.Pembobotan.bobot['sertifikat'][ka['sertifikat'][1]]])
                    if ka['organisasi'][0] is not False:
                        organisasi_per_mahasiswa.append([ka['organisasi'][0], galih_helper.Pembobotan.bobot['organisasi'][ka['organisasi'][1]]])
        
        if (index+1) not in removed_list:
            if start_nim is not None:

                print(">>>>>>>>>>>>>>>>>>>>", start_nim)
                res = galih_helper.PredictModel.predict(start_nim)
                mhs = Mahasiswa.query.filter_by(nim=start_nim).first()
                mhs.prestasi = galih_helper.Pembobotan.pembobotan_prestasi(prestasi_per_mahasiswa)
                mhs.sertifikat = galih_helper.Pembobotan.pembobotan_sertifikat(sertifikat_per_mahasiswa)
                mhs.organisasi = galih_helper.Pembobotan.pembobotan_organisasi(organisasi_per_mahasiswa)

                mhs.relevan = res[0]
                mhs.predict_proba = res[1]
                db.session.commit()


        
        count_index = count_index + 1
        start_nim = None


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
# @main_bp.route("/get_mhs", methods=["GET"])
# def get_mhs():
#     """ Get Mahasiswa From OASE """
#     nim = request.args.get('nim')
#     oase_key = '785a4062ab84fad16'
#     api_server = 'https://localhost/OASE'
#     response = requests.get("{api_server}/api/Mahasiswa/getMhsByNIMSiputa?oase_key={oase_key}&nim={nim}".format(nim=nim, oase_key=oase_key, api_server=api_server), verify=False)
#     return response.json()

# @main_bp.route("/get_tahun_angkatan", methods=["GET"])
# def get_tahun_angkatan():
#     """ Get Tahun Angkatan From OASE """
#     oase_key = '785a4062ab84fad16'
#     api_server = 'http://localhost:45275'
#     response = requests.get("{api_server}/api/Mahasiswa/tahun_angkatan?oase_key={oase_key}".format(oase_key=oase_key, api_server=api_server))
#     return response.text

# @main_bp.route("/get_mhs_by_tahun_prodi", methods=["GET"])
# def get_mhs_by_tahun_prodi():
#     """ Get Mahasiswa From OASE """
#     tahun = request.args.get('tahun')
#     prodi = request.args.get('prodi')
#     oase_key = '785a4062ab84fad16'
#     api_server = 'https://localhost/OASE'
    
#     response = requests.get("{api_server}/api/Mahasiswa/getMahasiswaByTahunProdiSiputa?oase_key={oase_key}&tahun={tahun}&prodi={prodi}".format(tahun=tahun, prodi=prodi, oase_key=oase_key, api_server=api_server), verify=False)
#     return response.json()

# API INCOME BACKEND SIMULATION
@main_bp.route("/get_mhs", methods=["GET"])
def get_mhs():
    nim_name = request.args.get('nim')
    nim = nim_name.split('-')[0]
    data = []
    return galih_helper.TestingApi.get_mhs_by_nim(nim)