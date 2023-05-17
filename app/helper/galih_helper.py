# from flask import Blueprint, redirect, render_template, url_for, request
# from flask_login import current_user, login_required, logout_user

from flask import request
import requests


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
    