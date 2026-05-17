# Tableau d'amortissement

Application web Flask qui génère des tableaux d'amortissement de prêt immobilier.

## Stack

- **Backend** : Python / Flask
- **Frontend** : HTML + CSS inline, Jinja2 pour le templating
- **Pas de base de données** — tout est calculé à la volée

## Structure

```
app.py                  # Serveur Flask + logique de calcul
templates/index.html    # Page unique (formulaire + résultats)
```

## Lancer l'app

```bash
pip install flask
python app.py
# Ouvre http://127.0.0.1:5000
```

## Routes

| Route | Méthode | Rôle |
|-------|---------|------|
| `/` | GET | Affiche le formulaire vide |
| `/calculer` | POST | Reçoit les données, calcule et renvoie le tableau |

## Formule de calcul

- **Mensualité hors assurance** : `M = C × (t / (1 - (1+t)^-n))`
  - `C` = capital emprunté
  - `t` = taux mensuel (taux annuel / 12)
  - `n` = durée en mois
- **Assurance mensuelle** : `(capital_restant × taux_assurance_annuel) / 12`
  - L'assurance est recalculée chaque mois sur le capital restant dû

## Données affichées

**Totaux** : mois totaux, intérêts totaux, assurance totale, remboursement total sans/avec assurance.

**Tableau mois par mois** : mois, intérêts, amortissement, assurance, mensualité totale, capital restant.

## Points d'amélioration connus

- Pas de `requirements.txt`
- Pas de validation des entrées (crash si champ vide)
- `dict` utilisé comme nom de variable (écrase le built-in Python)
- Pas de gestion d'erreurs sur la route `/calculer`
- `debug=True` en dur (à désactiver en production)
