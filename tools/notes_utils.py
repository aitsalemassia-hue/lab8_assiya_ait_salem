SEUIL_ADMISSION = 10
def moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)


def est_admis(note, seuil=SEUIL_ADMISSION):
    """Retourne True si la note est ≥ au seuil (par défaut 10)."""
    return note >= seuil

def formater_rapport(notes):
    """Construit une petite chaîne de rapport à partir d'une liste de notes."""
    moyenne_classe = moyenne(notes)
    notes_valides = [note for note in notes if est_admis(note)]
    lignes = [
        "=== Rapport des notes ===",
        f"Notes : {notes}",
        f"Moyenne : {moyenne_classe:.2f}",
        f"Nombre d'étudiants admis : {len(notes_valides)}",
    ]
    return "\n".join(lignes)