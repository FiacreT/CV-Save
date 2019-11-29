#! /usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        title = request.form['title']
        email = request.form['email']
        telephone = request.form['telephone']
        date_naissance = request.form['date_naissance']
        formation = request.form['formation']
        ecole = request.form['ecole']
        date_debut_formation = request.form['date_debut_formation']
        date_fin_formation = request.form['date_fin_formation']
        entreprise = request.form['entreprise']
        poste = request.form['poste']
        travail_fait = request.form['travail_fait']
        date_debut_work = request.form['date_debut_work']
        date_fin_work = request.form['date_fin_work']
        nom_project = request.form['nom_project']
        description = request.form['description']
        date_debut_project = request.form['date_debut_project']
        date_fin_project = request.form['date_fin_project']
        skills = request.form['skills']
        moocs = request.form['moocs']
        extra = request.form['extra']

        result = "first name : "+ first_name +"\n;"+"last_name : "+ last_name +"\n;"+"title : "+ title +"\n;"+"email : "+ email +"\n;"+"telephone : "+ telephone +"\n;"+"date_naissance : "+ date_naissance +"\n;"+"formation : "+ formation +"\n;"+"ecole : "+ ecole +"\n;"+"date_debut_formation : "+ date_debut_formation +"\n;"+"date_fin_formation : "+ date_fin_formation +"\n;"+"entreprise : "+ entreprise +"\n;"+"poste : "+ poste +"\n;"+"travail_fait : "+ travail_fait +"\n;"+"date_debut_work : "+ date_debut_work +"\n;"+"date_fin_work : "+ date_fin_work +"\n;"+"nom_project : "+ nom_project +"\n;"+"nom_project : "+ nom_project +"\n;"+"description : "+ description +"\n;"+"date_debut_project : "+ date_debut_project +"\n;"+"date_fin_project : "+ date_fin_project +"\n;"+"skills : "+ skills +"\n;"+"moocs : "+ moocs +"\n;"+"extra : "+ extra
        
        return result 
    return render_template('cv.html')



if __name__ == '__main__':
    app.run(debug=True)