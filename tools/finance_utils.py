TAUX_TVA = 0.2  # 20 %
def prix_ttc(prix_ht, taux=TAUX_TVA):
    """Applique un taux de TVA (20 % par défaut) pour obtenir un prix TTC."""
    return prix_ht * (1 + taux)