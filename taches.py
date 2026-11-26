# ---------------------------------------------------------------
# Gestionnaire de tâches en Python
# Les tâches sont sauvegardées dans un fichier JSON (taches.json),
# donc elles sont conservées même quand on ferme le programme.
# ---------------------------------------------------------------

import json  # module Python pour lire et écrire du JSON
import os    # module pour vérifier si un fichier existe

FICHIER = "taches.json"  # le nom du fichier où on sauvegarde


def charger_taches():
    """Lit le fichier JSON et renvoie la liste des tâches."""
    # Si le fichier n'existe pas encore (premier lancement), on part d'une liste vide
    if not os.path.exists(FICHIER):
        return []
    with open(FICHIER, "r", encoding="utf-8") as f:
        return json.load(f)  # json.load transforme le texte JSON en liste Python


def sauvegarder_taches(taches):
    """Écrit la liste des tâches dans le fichier JSON."""
    with open(FICHIER, "w", encoding="utf-8") as f:
        # indent=2 rend le fichier lisible, ensure_ascii=False garde les accents
        json.dump(taches, f, indent=2, ensure_ascii=False)


def afficher_taches(taches):
    """Affiche toutes les tâches avec leur numéro et leur état."""
    if len(taches) == 0:
        print("\nAucune tâche pour le moment.")
        return
    print("\nVos tâches :")
    for numero, tache in enumerate(taches, start=1):
        etat = "[x]" if tache["terminee"] else "[ ]"
        print(f"  {numero}. {etat} {tache['titre']}")


def ajouter_tache(taches):
    """Demande un titre et ajoute une nouvelle tâche."""
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Le titre ne peut pas être vide.")
        return
    # Une tâche = un dictionnaire Python (qui devient un objet JSON)
    taches.append({"titre": titre, "terminee": False})
    sauvegarder_taches(taches)
    print("Tâche ajoutée.")


def demander_numero(taches):
    """Demande un numéro de tâche et vérifie qu'il est valide. Renvoie l'index, ou None."""
    try:
        numero = int(input("Numéro de la tâche : "))
    except ValueError:  # si l'utilisateur n'a pas tapé un nombre
        print("Veuillez entrer un nombre.")
        return None
    if numero < 1 or numero > len(taches):
        print("Ce numéro n'existe pas.")
        return None
    return numero - 1  # en Python, les listes commencent à 0


def terminer_tache(taches):
    """Marque une tâche comme terminée."""
    index = demander_numero(taches)
    if index is not None:
        taches[index]["terminee"] = True
        sauvegarder_taches(taches)
        print("Tâche terminée.")


def supprimer_tache(taches):
    """Supprime une tâche de la liste."""
    index = demander_numero(taches)
    if index is not None:
        supprimee = taches.pop(index)  # pop retire l'élément de la liste
        sauvegarder_taches(taches)
        print(f"Tâche supprimée : {supprimee['titre']}")


def main():
    """Boucle principale : affiche le menu jusqu'à ce que l'utilisateur quitte."""
    taches = charger_taches()
    while True:
        print("\n=== GESTIONNAIRE DE TÂCHES ===")
        print("1. Voir les tâches")
        print("2. Ajouter une tâche")
        print("3. Terminer une tâche")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            afficher_taches(taches)
        elif choix == "2":
            ajouter_tache(taches)
        elif choix == "3":
            afficher_taches(taches)
            terminer_tache(taches)
        elif choix == "4":
            afficher_taches(taches)
            supprimer_tache(taches)
        elif choix == "5":
            print("À bientôt !")
            break
        else:
            print("Choix invalide, tapez un nombre entre 1 et 5.")


# Cette ligne lance le programme seulement si on exécute ce fichier directement
if __name__ == "__main__":
    main()
