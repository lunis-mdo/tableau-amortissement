# Tableau d'amortissement de prêt

Application web qui génère un tableau d'amortissement complet à partir des paramètres d'un emprunt immobilier.

## Fonctionnalités

- Calcul de la mensualité hors et avec assurance
- Tableau mois par mois : intérêts, amortissement, assurance, capital restant
- Récapitulatif des totaux sur toute la durée du prêt

## Installation

```bash
pip install -r requirements.txt
python app.py
```

Puis ouvrir [http://127.0.0.1:5000](http://127.0.0.1:5000) dans un navigateur.

## Paramètres

| Champ | Description |
|-------|-------------|
| Capital emprunté | Montant du prêt en € |
| Durée | Durée en années |
| Taux d'intérêts | Taux annuel en % |
| Taux d'assurance | Taux annuel en % (calculé sur le capital restant dû) |

## Stack

- Python / Flask
- HTML / CSS / Jinja2
