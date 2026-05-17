"""
Created on Tue Feb  3 21:03:06 2026

@author: lmdo
"""
from flask import Flask, render_template, request

app = Flask(__name__)#

#route 1 : affiche le formulaire vide à remplir
@app.route('/') # C'est l'étiquette. Elle dit au serveur : "Si quelqu'un tape l'adresse de base (le /), lance la fonction juste en dessous"
def accueil():
    return render_template('index.html', entrees=dict())# renvoie le contenu du fcihier html

#route 2 : reçoit les données et fait les calculs
    
@app.route('/calculer', methods=['POST'])
def calculer():
    formulaire = request.form
    capital = float(formulaire.get('capital'))
    duree = float(formulaire.get('duree'))
    interets = float(formulaire.get('interets'))/100
    assurance = float(formulaire.get('assurance'))/100
    
    print(f"Tu veux emprunter {capital} €")
    print(f"l'emprunt est sur {duree} années")
    print(f"Tu payeras {interets*100}% d'intérêts")
    print(f"Ton assurance est de {assurance*100} %")
    # calcul : 
    tableau =[]
    totaux = {}
    capital_restant = capital
    interets_mensuels = interets/12
    duree_mois = int(duree*12)
    mensu_hors_assu = capital*(interets_mensuels/(1-(1+interets_mensuels)**(-duree_mois)))
    totaux['remboursement_total_sans_assur'] = round(duree_mois *mensu_hors_assu, 2)
    totaux['mois_totaux'] = duree_mois

    for i in range(1, duree_mois+1) :
        ligne = {}
        interets_du_mois = capital_restant * interets_mensuels
        capital_remb_mois = mensu_hors_assu - interets_du_mois
        capital_restant -=  capital_remb_mois
        mensu_assur = (capital_restant * assurance) / 12
        mensu_total = mensu_assur + mensu_hors_assu
        ligne['mois'] = i
        ligne['interets_du_mois'] = round(interets_du_mois, 2)
        totaux['interets_totaux'] = round(totaux.get('interets_totaux', 0) + ligne['interets_du_mois'], 2)
        ligne['capital_restant'] = round(capital_restant, 2)
        ligne['capital_remb_mois'] = round(capital_remb_mois, 2)
        ligne['mensu_assur'] = round(mensu_assur, 2)
        totaux['assur_totaux'] = round(totaux.get('assur_totaux', 0) + ligne['mensu_assur'],2)
        ligne['mensu_total'] = round(mensu_total, 2)
        totaux['remboursement_total'] = round(totaux.get('remboursement_total', 0) + ligne['mensu_total'], 2)
        tableau.append(ligne)
    return render_template('index.html', resultats = tableau, totaux=totaux, entrees=request.form)


    



# lancement (à la fin)
if __name__ == '__main__':
    app.run(debug=True)