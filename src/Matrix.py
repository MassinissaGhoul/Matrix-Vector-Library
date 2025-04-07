from Vector import Vector

class Matrix:
    def __init__(self, rows):
        if not rows:
            raise ValueError("La matrice ne peut être vide.")
        self.rows = [Vector(row) for row in rows]
        self.nrows = len(self.rows)
        self.ncols = len(self.rows[0].elements)
        for row in self.rows:
            if len(row.elements) != self.ncols:
                raise ValueError("pas même taille")

    def __add__(self, other):
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("pas même taille")
        new_rows = [row1 + row2 for row1, row2 in zip(self.rows, other.rows)]
        return Matrix([row.elements for row in new_rows])

    def __sub__(self, other):
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("pas même taille")
        new_rows = [row1 - row2 for row1, row2 in zip(self.rows, other.rows)]
        return Matrix([row.elements for row in new_rows])

    def get_column(self, j):
        return [row.elements[j] for row in self.rows]

    def __mul__(self, other):
        if self.ncols != other.nrows:
            raise ValueError("pas même taille")
        new_matrix = []
        for i in range(self.nrows):
            new_row = []
            for j in range(other.ncols):
                col_vector = Vector(other.get_column(j))
                new_row.append(self.rows[i] @ col_vector)
            new_matrix.append(Vector(new_row))
        return Matrix([row.elements for row in new_matrix])

    def __str__(self):
        rows_str = [[str(x) for x in row.elements] for row in self.rows]
        col_widths = [max(len(row[j]) for row in rows_str) for j in range(self.ncols)]
        horizontal_line = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
        formatted_rows = [horizontal_line]
        for row in rows_str:
            formatted_row = "| " + " | ".join(row[j].rjust(col_widths[j]) for j in range(self.ncols)) + " |"
            formatted_rows.append(formatted_row)
            formatted_rows.append(horizontal_line)
        return "\n".join(formatted_rows)

    def pivot(self, tableau, pivot_row, pivot_col):
        """
        Réalise l'opération de pivot sur le tableau.
        Normalise la ligne pivot puis annule la colonne pivot pour toutes les autres lignes.
        """
        pivot_value = tableau[pivot_row][pivot_col]
        if abs(pivot_value) < 1e-10:
            raise ValueError("Pivot nul ou presque nul")
        num_cols = len(tableau[0])
        # Normalisation de la ligne pivot
        tableau[pivot_row] = [x / pivot_value for x in tableau[pivot_row]]
        num_rows = len(tableau)
        # Annulation de la colonne pivot dans les autres lignes
        for i in range(num_rows):
            if i != pivot_row:
                factor = tableau[i][pivot_col]
                for j in range(num_cols):
                    tableau[i][j] -= factor * tableau[pivot_row][j]

    def gauss(self, tableau):
        """
        Effectue l'élimination de Gauss-Jordan sur le tableau augmenté.
        On suppose que le tableau représente un système de n équations à n inconnues (n lignes et n+1 colonnes).
        """
        n = len(tableau)
        for i in range(n):
            # Recherche de la ligne de pivot avec le coefficient maximal en valeur absolue
            max_row = i
            for k in range(i + 1, n):
                if abs(tableau[k][i]) > abs(tableau[max_row][i]):
                    max_row = k
            if abs(tableau[max_row][i]) < 1e-10:
                raise ValueError("Pivot nul, système singulier")
            tableau[i], tableau[max_row] = tableau[max_row], tableau[i]
            self.pivot(tableau, i, i)
        return tableau

    def solve(self, b: Vector) -> Vector:
        """
        Résout le système linéaire Ax = b en utilisant l'élimination de Gauss-Jordan.
        La méthode construit le tableau augmenté, applique gauss() puis extrait la solution.
        """
        if self.nrows != self.ncols:
            raise ValueError("La matrice n'est pas carrée")
        if len(b.elements) != self.nrows:
            raise ValueError("La dimension de b ne correspond pas à la matrice")
        n = self.nrows
        # Construction du tableau augmenté
        A = [self.rows[i].elements[:] + [b.elements[i]] for i in range(n)]
        self.gauss(A)
        solution = [A[i][-1] for i in range(n)]
        return Vector(solution)

    def simplex(self, b: Vector, c: Vector):
        """
        Résout un problème de programmation linéaire sous la forme standard :
          maximiser    c^T x
          sous les contraintes  Ax <= b,  x >= 0.
        On ajoute des variables d'écart (slack) pour transformer les inégalités en égalités.
        La méthode construit le tableau du Simplex, effectue les itérations à l'aide de pivot()
        et retourne la solution optimale pour les variables d'origine ainsi que la valeur optimale.
        """
        m = len(b.elements)  # nombre de contraintes
        n = len(c.elements)  # nombre de variables d'origine
        # Construction du tableau : pour chaque contrainte, on ajoute la colonne des variables d'écart et le terme constant.
        tableau = []
        for i in range(m):
            row = []
            row.extend(self.rows[i].elements)  # coefficients des variables d'origine
            for j in range(m):  # ajout de la matrice identité pour les slack variables
                row.append(1 if i == j else 0)
            row.append(b.elements[i])  # terme constant
            tableau.append(row)
        # Ligne objective (la dernière ligne) : -c pour maximisation, 0 pour les slack, et 0 comme terme constant.
        obj_row = []
        for i in range(n):
            obj_row.append(-c.elements[i])
        for j in range(m):
            obj_row.append(0)
        obj_row.append(0)
        tableau.append(obj_row)

        # Variables de base initiales : les variables d'écart, indices n, n+1, ..., n+m-1.
        basic_vars = [n + i for i in range(m)]
        num_rows = m + 1
        num_cols = n + m + 1

        # Boucle du Simplex
        while True:
            # Recherche de la variable entrante : choisir la colonne avec coefficient négatif dans la ligne objective
            pivot_col = None
            min_value = 0
            for j in range(num_cols - 1):
                if tableau[-1][j] < min_value:
                    min_value = tableau[-1][j]
                    pivot_col = j
            if pivot_col is None:
                # La solution est optimale
                break

            # Critère du minimum ratio pour déterminer la variable sortante
            pivot_row = None
            min_ratio = float('inf')
            for i in range(m):
                if tableau[i][pivot_col] > 1e-10:
                    ratio = tableau[i][-1] / tableau[i][pivot_col]
                    if ratio < min_ratio:
                        min_ratio = ratio
                        pivot_row = i
            if pivot_row is None:
                raise ValueError("Le problème est non borné")
            self.pivot(tableau, pivot_row, pivot_col)
            basic_vars[pivot_row] = pivot_col

        # Extraction de la solution pour les variables d'origine
        solution = [0] * (n + m)
        for i in range(m):
            basic_var = basic_vars[i]
            if basic_var < n:
                solution[basic_var] = tableau[i][-1]
        optimal_value = tableau[-1][-1]
        return Vector(solution[:n]), optimal_value


def main():
    """
    print("\n--- Test résolution par pivot de Gauss ---")
    # Système 3x3 :
    #     2x1 +   x2 -  x3 =  8
    #   - 3x1 -   x2 + 2x3 = -11
    #   - 2x1 +   x2 + 2x3 = -3
    A = Matrix([[2, 1, -1],
                [-3, -1, 2],
                [-2, 1, 2]])
    b = Vector([8, -11, -3])
    solution = A.solve(b)
    print("Solution du système Ax = b :")
    print(solution)

    print("\n--- Test du Simplex ---")
    # Problème de PL : Maximiser z = 3x1 + 2x2
    # sous les contraintes :
    #    x1 + x2 <= 4
    #    x1 <= 2
    #    x2 <= 3
    # avec x1, x2 >= 0
    A_simplex = Matrix([[1, 1],
                         [1, 0],
                         [0, 1]])
    b_simplex = Vector([4, 2, 3])
    c_simplex = Vector([3, 2])
    sol, opt_val = A_simplex.simplex(b_simplex, c_simplex)
    print("Solution optimale (x1, x2) :")
    print(sol)
    print("Valeur optimale :", opt_val)
    # Système à résoudre :
    #  2x₁ +  x₂ - 9x₃ = 8
    #   x₁ + 2x₂ - 2x₃ = 3
    #  3x₁ + 2x₂ + 2x₃ = 5
    A = Matrix([
        [2, 1, -9],
        [1, 2, -2],
        [3, 2,  2]
    ])
    b = Vector([8, 3, 5])
    solution = A.solve(b)
    print("Solution du système Ax = b :")
    print(solution)
    """



if __name__ == "__main__":
    main()
