# from flask import Blueprint, redirect, render_template, url_for, request
# from flask_login import current_user, login_required, logout_user

from flask import request, jsonify
import requests
from app.models import Mahasiswa
import pandas as pd

from jcopml.utils import load_model

class Api():
    def get_mhs(nim):
        """ Get Mahasiswa From OASE """
        oase_key = '785a4062ab84fad16'
        api_server = 'https://localhost/OASE'
        response = requests.get("{api_server}/api/Mahasiswa/getMhsByNIMSiputa?oase_key={oase_key}&nim={nim}".format(nim=nim, oase_key=oase_key, api_server=api_server), verify=False)
        return response.json()
        
    def get_prodi():
        """ Get All Prodi from OASE """
        oase_key = '785a4062ab84fad16'
        api_server = 'https://localhost/OASE'
        response = requests.get("{api_server}/api/Mahasiswa/getProdiSiputa?oase_key={oase_key}".format(oase_key=oase_key, api_server=api_server), verify=False)
        return response.json()

class TestingApi():
    def get_mhs():
        response = requests.get("http://127.0.0.1:4000/api/get_mahasiswa", verify=False)
        return response.json()
    
    def get_prodi():
        response = requests.get("http://127.0.0.1:4000/api/get_prodi", verify=False)
        return response.json()

    def get_mhs_by_nim(nim):
        response = requests.get("http://127.0.0.1:4000/api/get_mahasiswa_by_nim/"+nim, verify=False)
        return response.json()


# kaji ulang mengenai pembobotan
class Pembobotan():
    bobot = {
            'prestasi':{
                'Tingkat Internasional': 3,
                'Tingkat Nasional': 2,
                'Tingkat Regional': 1,
            },
            'sertifikat':{
                'Sertifikat Keahlian': 3,
                'Sertifikat Kursus': 2,
                'Sertifikat Seminar/Webinar': 1,
            },
            'organisasi':{
                'Pengurus': 2,
                'Anggota': 1,
            },
        }
        
    def pembobotan_sertifikat(list_sertifikat):
        # list_sertifikat = [
        #     ["Oracle Certification", 1],
        #     ["Huawei Certification", 1],
        # ]
        count_sertifikat = 0
        for sertifikat in list_sertifikat:
            count_sertifikat += int(sertifikat[1])

        return count_sertifikat

    def pembobotan_organisasi(list_organisasi):
        # list_organisasi = [
        #     ["RANA", 1],
        #     ["Banyu Biru", 2],
        # ]
        count_organisasi = 0
        for organisasi in list_organisasi:
            count_organisasi += int(organisasi[1])

        return count_organisasi

    def pembobotan_prestasi(list_prestasi):
        # list_prestasi = [
        #     ["INVFEST 6.0 Juara 1", 2],
        #     ["Programming Competition", 2],
        # ]
        print( ">>>>>>>>>>>>>>>>>>>>>", list_prestasi, "<<<<<<<<<<<<<<<<<<")
        count_prestasi = 0
        for prestasi in list_prestasi:
            count_prestasi += int(prestasi[1])

        return count_prestasi

class PredictModel():
    def predict(nim):
        model = load_model("/opt/project_ta/siputa/app/model/best.pkl")
        mahasiswa = Mahasiswa.query.filter_by(nim=nim).first()
        x_pred = pd.DataFrame([[mahasiswa.gender, mahasiswa.pekerjaan_ortu, mahasiswa.parents_income, mahasiswa.gpa_score, mahasiswa.sertifikat, mahasiswa.prestasi, mahasiswa.organisasi]], columns=["jk", "pekerjaan_ortu", "penghasilan_ortu", "ipk", "sertifikasi", "prestasi", "organisasi"])
        x_pred['pekerjaan_ortu'].replace(['buruh', 'wiraswasta', 'pegawai swasta', 'swasta', 'pns'],
                [1, 2, 2, 2, 3], inplace=True)
        res = model.predict(x_pred)[0]
        predictions = model.predict_proba(x_pred)
        tmp = predictions.tolist()
        
        return [0 if res == 'Tidak Relevan' else 1, round(predictions.tolist()[0][0], 2) * 100]

    def predict_multiple(nims):
        # load model
        model = load_model("/opt/project_ta/siputa/app/model/best.pkl")
        results = []
        # search student by nim
        for nim in nims:
            mahasiswa = Mahasiswa.query.filter_by(nim=nim[0]).first()
            if mahasiswa:
                # prepare the data
                # gender = "L" if mahasiswa.gender else "P" 
                x_pred = pd.DataFrame([[mahasiswa.gender, mahasiswa.pekerjaan_ortu, mahasiswa.parents_income, mahasiswa.gpa_score, mahasiswa.sertifikat, mahasiswa.prestasi, mahasiswa.organisasi]], columns=["jk", "pekerjaan_ortu", "penghasilan_ortu", "ipk", "sertifikasi", "prestasi", "organisasi"])
                x_pred['pekerjaan_ortu'].replace(['buruh', 'wiraswasta', 'pegawai swasta', 'swasta', 'pns'],
                            [1, 2, 2, 2, 3], inplace=True)
                # predict
                res = model.predict(x_pred)[0]
                data_result = {
                        "nama": mahasiswa.name,
                        "semester": 8,
                        "prodi": "Teknik Informatika",
                        "relevan": res
                    }
                
                results.append(data_result)
        return results
            
    

