# from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user

from flask import request, jsonify
import requests
from app.models import Mahasiswa, Prodi, Prestasi, Organisasi, Sertifikat

import pandas as pd
import numpy as np

from jcopml.utils import load_model


class Api():
    def getAllMhsFilterByProdiandThak(prodi, thak):
        oase_key = '785a4062ab84fad16'
        api_server = 'https://oase.poltektegal.ac.id'
        response = requests.get("{api_server}/api/Mahasiswa/getAllMhsFilterByProdiandThak_ss?oase_key={oase_key}&prodi={prodi}&thak={thak}".format(oase_key=oase_key, prodi=prodi, thak=thak, api_server=api_server), verify=False)
        return response.json()

    def getMhsByNim(nim):
        """ Get Mahasiswa From OASE """
        oase_key = '785a4062ab84fad16'
        api_server = 'https://oase.poltektegal.ac.id'
        response = requests.get("{api_server}/api/Mahasiswa/getMhsByNIM_ss?oase_key={oase_key}&nim={nim}".format(nim=nim, oase_key=oase_key, api_server=api_server), verify=False)
        return response.json()
        
    def getProdi():
        """ Get All Prodi from OASE """
        oase_key = '785a4062ab84fad16'
        api_server = 'https://oase.poltektegal.ac.id'
        response = requests.get("{api_server}/api/Mahasiswa/getProdi_ss?oase_key={oase_key}".format(oase_key=oase_key, api_server=api_server), verify=False)
        return response.json()
    
    def getMhsFilterBySmt():
        oase_key = '785a4062ab84fad16'
        api_server = 'https://oase.poltektegal.ac.id'
        response = requests.get("{api_server}/api/Mahasiswa/getMhsFilterBySmt_ss?oase_key={oase_key}".format(oase_key=oase_key, api_server=api_server), verify=False)
        return response.json()
    
    def getMhsFilterByProdiandSmt(prodi):
        oase_key = '785a4062ab84fad16'
        api_server = 'https://oase.poltektegal.ac.id'
        response = requests.get("{api_server}/api/Mahasiswa/getMhsFilterBySmt_ss?oase_key={oase_key}&prodi={prodi}".format(oase_key=oase_key, api_server=api_server, prodi=prodi), verify=False)
        return response.json()
    
    def getIPKMhs(nim, prodi):
        oase_key = '785a4062ab84fad16'
        api_server = 'https://oase.poltektegal.ac.id'
        response = requests.get("{api_server}/api/Mahasiswa/getIPK_ss?oase_key={oase_key}&nim={nim}&prodi={prodi}".format(oase_key=oase_key, api_server=api_server, nim=nim, prodi=prodi), verify=False)
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
                'tingkat internasional': 3,
                'tingkat nasional': 2,
                'tingkat regional': 1,
            },
            'sertifikat':{
                'sertifikat kompetensi': 3,
                'sertifikat kursus': 2,
                'sertifikat seminar/sebinar': 1,
            },
            'organisasi':{
                'pengurus': 2,
                'anggota': 1,
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
        count_prestasi = 0
        for prestasi in list_prestasi:
            count_prestasi += int(prestasi[1])

        return count_prestasi

class PredictModel():
    def predict(nim):
        model = load_model("/Users/dsn/Documents/rodenstock/app/model/best.pkl")
        mahasiswa = Mahasiswa.query.filter_by(nim=nim).first()
        x_pred = pd.DataFrame([[mahasiswa.gender, mahasiswa.pekerjaan_ortu, mahasiswa.parents_income, mahasiswa.gpa_score, mahasiswa.sertifikat, mahasiswa.prestasi, mahasiswa.organisasi]], columns=["jk", "pekerjaan_ortu", "penghasilan_ortu", "ipk", "sertifikasi", "prestasi", "organisasi"])

        if x_pred['pekerjaan_ortu'][0] not in ['buruh', 'wiraswasta', 'pegawai swasta', 'swasta', 'pns']:
             x_pred['pekerjaan_ortu'] = 2
        else:
            x_pred['pekerjaan_ortu'].replace(['buruh', 'wiraswasta', 'pegawai swasta', 'swasta', 'pns'],
                    [1, 2, 2, 2, 3], inplace=True)
        res = model.predict(x_pred)[0]
        predictions = model.predict_proba(x_pred)
        # tmp = predictions.tolist()
        
        return [0 if res == 'Tidak Relevan' else 1, round(predictions.tolist()[0][0], 2) * 100]

    def predict_multiple(nims):
        # pembobotan multiple tidak digunakan kembali [DEPRECATED]
        # load model
        model = load_model("/Users/dsn/Documents/rodenstock/app/model/best.pkl")
        results = []
        # search student by nim
        for nim in nims:
            mahasiswa = Mahasiswa.query.filter_by(nim=nim[0]).first()
            prodi = Prodi.query.filter_by(kode_prodi=mahasiswa.prodi).first()
            if mahasiswa:
                # prepare the data
                # gender = "L" if mahasiswa.gender else "P" 
                x_pred = pd.DataFrame([[mahasiswa.gender, mahasiswa.pekerjaan_ortu, mahasiswa.parents_income, mahasiswa.gpa_score, mahasiswa.sertifikat, mahasiswa.prestasi, mahasiswa.organisasi]], columns=["jk", "pekerjaan_ortu", "penghasilan_ortu", "ipk", "sertifikasi", "prestasi", "organisasi"])
                if x_pred['pekerjaan_ortu'][0] not in ['buruh', 'wiraswasta', 'pegawai swasta', 'swasta', 'pns']:
                    x_pred['pekerjaan_ortu'] = 2
                else:
                    x_pred['pekerjaan_ortu'].replace(['buruh', 'wiraswasta', 'pegawai swasta', 'swasta', 'pns'],
                            [1, 2, 2, 2, 3], inplace=True)
                
                # predict
                res = model.predict(x_pred)[0]
                data_result = {
                        "nama": mahasiswa.name,
                        "nim": mahasiswa.nim,
                        "semester": mahasiswa.semester,
                        "prodi": prodi.nama_prodi,
                        "relevan": res
                    }
                
                results.append(data_result)
        return results
            
    
class Utility():
    def format_rupiah(nominal):
    # Mengecek apakah nominal negatif atau positif
        if nominal < 0:
            is_negative = True
            nominal = abs(nominal)
        else:
            is_negative = False

        # Mengonversi nominal menjadi string dan menambahkan desimal dengan 2 digit
        nominal_str = "{:,.2f}".format(nominal)

        # Membuat format rupiah dengan menambahkan "Rp" di depan dan tanda "-" jika negatif
        if is_negative:
            nominal_str = "Rp" + "-" + nominal_str
        else:
            nominal_str = "Rp" + nominal_str

        return nominal_str
    
    def obj_to_arr(obj):
        list = []
        for i in obj:
            list.append(i[0])
        return list


class Analisis():
    def calculate_boxplot(data):
        if data:
            # korelasi prestasi dengan prediksi
            q1 = np.percentile(data, 25)
            q2 = np.percentile(data, 50)
            q3 = np.percentile(data, 75)

            # IQR adalah perbedaan antara Q3 dan Q1, yaitu IQR = Q3 - Q1.
            IQR = q3 - q1

            # Pencilan atau outliers adalah data yang berada di luar rentang Q1 - 1,5 * IQR hingga Q3 + 1,5 * IQR. Data di luar rentang ini akan ditandai sebagai pencilan pada boxplot
            wishker_top = q1 - 1.5 * IQR
            wishker_bottom = q3 + 1.5 * IQR

            return [wishker_top, q1, q2, q3, wishker_bottom]
        else:
            return [0,0,0,0,0]
