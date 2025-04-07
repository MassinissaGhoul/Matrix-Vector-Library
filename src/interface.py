from Matrix import Matrix
from Vector import Vector


def interface_pivot():
    print("\n--- Test de l'opération de Pivot ---")
    print("Cet outil vous permet de tester l'opération de pivot sur un tableau augmenté.")
    choix = input(
        "Utiliser le tableau d'exemple ou saisir votre propre tableau ? (1 = Exemple, 2 = Saisie personnalisée) : ").strip()

    if choix == "2":
        # Saisie personnalisée d'un tableau augmenté
        while True:
            try:
                nb_lignes = int(input("Entrez le nombre de lignes du tableau augmenté : "))
                nb_colonnes = int(input("Entrez le nombre de colonnes du tableau augmenté : "))
                if nb_lignes <= 0 or nb_colonnes <= 0:
                    print("Les dimensions doivent être strictement positives.")
                    continue
                break
            except ValueError:
                print("Veuillez entrer des entiers valides.")
        tableau = []
        for i in range(nb_lignes):
            while True:
                try:
                    row = list(map(float, input(
                        f"Ligne {i + 1} (séparez les {nb_colonnes} nombres par des espaces) : ").split()))
                    if len(row) != nb_colonnes:
                        print(f"Il faut exactement {nb_colonnes} valeurs.")
                        continue
                    tableau.append(row)
                    break
                except ValueError:
                    print("Veuillez entrer des nombres valides.")
    else:
        # Tableau d'exemple fixe
        tableau = [
            [2, 1, 5],
            [1, -1, 1]
        ]
        print("Tableau d'exemple utilisé :")
        for row in tableau:
            print(row)

    # Saisie de la position du pivot
    while True:
        try:
            pivot_row = int(input("Entrez l'indice de la ligne pivot (0-indexé) : "))
            pivot_col = int(input("Entrez l'indice de la colonne pivot (0-indexé) : "))
            break
        except ValueError:
            print("Veuillez entrer des entiers valides.")

    # Création d'une instance dummy pour accéder à la méthode pivot
    dummy = Matrix([[0]])
    try:
        dummy.pivot(tableau, pivot_row, pivot_col)
        print("\nTableau après opération de pivot :")
        for row in tableau:
            print(row)
    except Exception as e:
        print("Erreur lors de l'opération de pivot :", e)


def interface_simplex():
    print("\n--- Test du Simplex ---")
    print("Ce test permet de résoudre un problème de programmation linéaire en forme standard :")
    print("  Maximiser z = c^T x sous Ax <= b et x >= 0")
    try:
        m = int(input("Entrez le nombre de contraintes (m) : "))
        n = int(input("Entrez le nombre de variables d'origine (n) : "))
        if m <= 0 or n <= 0:
            print("Les valeurs doivent être strictement positives.")
            return
    except ValueError:
        print("Entrée invalide.")
        return

    print("\nSaisissez la matrice A :")
    A_rows = []
    for i in range(m):
        while True:
            try:
                row = list(map(float, input(f"Ligne {i + 1} (séparez les {n} nombres par des espaces) : ").split()))
                if len(row) != n:
                    print(f"Il faut exactement {n} valeurs.")
                    continue
                A_rows.append(row)
                break
            except ValueError:
                print("Veuillez entrer des nombres valides.")
    A = Matrix(A_rows)

    # Saisie du vecteur b
    while True:
        try:
            b_elements = list(
                map(float, input(f"Entrez le vecteur b ({m} éléments, séparés par des espaces) : ").split()))
            if len(b_elements) != m:
                print(f"Il faut exactement {m} valeurs.")
                continue
            break
        except ValueError:
            print("Veuillez entrer des nombres valides.")
    b = Vector(b_elements)

    # Saisie du vecteur c (pour la fonction objectif)
    while True:
        try:
            c_elements = list(
                map(float, input(f"Entrez le vecteur c ({n} éléments, séparés par des espaces) : ").split()))
            if len(c_elements) != n:
                print(f"Il faut exactement {n} valeurs.")
                continue
            break
        except ValueError:
            print("Veuillez entrer des nombres valides.")
    c = Vector(c_elements)

    try:
        sol, opt_val = A.simplex(b, c)
        print("\nSolution optimale pour les variables d'origine :")
        print(sol)
        print("Valeur optimale :", opt_val)
    except Exception as e:
        print("Erreur lors du calcul du Simplex :", e)


def main():
    print("====================================")
    print("Matrix-Vector Library - Interface de Test")
    print("====================================")
    while True:
        print("\nMenu :")
        print("1. Tester l'opération de Pivot")
        print("2. Tester le Simplex")
        print("3. Quitter")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            interface_pivot()
        elif choix == "2":
            interface_simplex()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
