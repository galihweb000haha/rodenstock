# Predict Route
from flask import Blueprint, redirect, render_template, url_for, request, jsonify
from flask_login import current_user, login_required, logout_user

from app import db
from app.models import Mahasiswa

predict_bp = Blueprint(
    "predict_bp", __name__, template_folder="templates", static_folder="static"
)

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from jcopml.tuning import random_search_params as rsp
from sklearn.compose import ColumnTransformer

from jcopml.utils import load_model

@predict_bp.route("/predict", methods=["GET"])
def model_prediction():
    # search student by nim
    nim = request.args.get('nim')
    mahasiswa = Mahasiswa.query.filter_by(nim=nim).first()
    if mahasiswa:
        # prepare the data
        gender = "L" if mahasiswa.gender else "P" 
        x_pred = pd.DataFrame([[gender, mahasiswa.sertifikat, mahasiswa.prestasi, mahasiswa.organisasi]], columns=["JK", "Sertifikat", "Prestasi", "Organisasi"])
        # predict
        model = load_model("../model/best.pkl")
        res = model.predict(x_pred)[0]
        return jsonify({
            "status": 200,
            "result": res,
        })
    return jsonify({
            "status": 404,
            "result": [],
        })
    
@predict_bp.route("/predict_multiple", methods=["GET"])
def model_prediction_multiple():
    # load model
    model = load_model("/opt/project_ta/siputa/app/model/best.pkl")
    results = []
    # search student by nim
    nims = request.args.get('nim')
    nims = nims.split('-')
    for nim in nims:
        mahasiswa = Mahasiswa.query.filter_by(nim=nim).first()
        if mahasiswa:
            # prepare the data
            # gender = "L" if mahasiswa.gender else "P" 
            x_pred = pd.DataFrame([[mahasiswa.gender, mahasiswa.pekerjaan_ortu, mahasiswa.parents_income, mahasiswa.gpa_score, mahasiswa.sertifikat, mahasiswa.prestasi, mahasiswa.organisasi]], columns=["jk", "pekerjaan_ortu", "penghasilan_ortu", "ipk", "sertifikasi", "prestasi", "organisasi"])
            x_pred['pekerjaan_ortu'].replace(['buruh', 'wiraswasta', 'pegawai swasta', 'swasta', 'pns'],
                        [1, 2, 2, 2, 3], inplace=True)
            # predict
            res = model.predict(x_pred)[0]
            results.append([nim, res])
        else:
            results.append("Data belum lengkap")

    return jsonify({
            "status": 200,
            "result": results,
        })
