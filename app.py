from tools.notes_utils import moyenne, est_admis, formater_rapport
from tools.finance_utils import prix_ttc
from tools.constants import  TAUX_TVA
notes = []
prix = 350
# Utilisation via import ciblé
m = moyenne(notes)
print(f"Moyenne calculée (from import) : {m:.2f}")

# Constante globale
prix_ttc_calcule=prix_ttc(prix)
print(f"Prix TTC pour {prix} € HT (taux {TAUX_TVA*100:.0f}%) : {prix_ttc_calcule:.2f} €")

# Exemple de test d'admission
note_test = 11
print(f"Admis ? {est_admis(note_test)}")
if __name__ == "__main__":
    print("Exécution depuis app.py")
    print("Tests rapides de utils.py")
    print(moyenne([10, 12, 14]))