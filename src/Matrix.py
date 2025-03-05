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
                # Conversion de la colonne (liste) en Vector
                col_vector = Vector(other.get_column(j))
                new_row.append(self.rows[i] @ col_vector)
            new_matrix.append(Vector(new_row))
        return Matrix([row.elements for row in new_matrix])

    def __str__(self):
        rows_str = [[str(x) for x in row.elements] for row in self.rows]
        # Déterminer la largeur maximale pour chaque colonne
        col_widths = [max(len(row[j]) for row in rows_str) for j in range(self.ncols)]

        # Construire une ligne horizontale de séparation
        horizontal_line = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

        # Construire chaque ligne de la matrice avec les bordures
        formatted_rows = [horizontal_line]
        for row in rows_str:
            formatted_row = "| " + " | ".join(row[j].rjust(col_widths[j]) for j in range(self.ncols)) + " |"
            formatted_rows.append(formatted_row)
            formatted_rows.append(horizontal_line)

        return "\n".join(formatted_rows)
    def solve(self, b: Vector) -> Vector:

        if self.nrows != self.ncols:
            raise ValueError("La matrice n'est pas carrée")
        if len(b.elements) != self.nrows:
            raise ValueError("La dimension de b ne correspond pas à la matrice")

        n = self.nrows
        # Création de la matrice
        A = [self.rows[i].elements[:] + [b.elements[i]] for i in range(n)]

        for i in range(n):
            max_row = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > abs(A[max_row][i]):
                    max_row = k
            if A[max_row][i] == 0:
                raise ValueError("Flop pivot non nul")
            A[i], A[max_row] = A[max_row], A[i]

            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n + 1):
                    A[j][k] -= factor * A[i][k]

        x = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            s = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (A[i][n] - s) / A[i][i]
        return Vector(x)


def main():
    print("\n--- Test résolution par pivot de Gauss ---")
    # Exemple de système 3x3 :
    #    2x +   y -   z =  8
    #  - 3x -   y + 2z = -11
    #  - 2x +   y + 2z = -3
    A = Matrix([[2, 1, -1],
                [-3, -1, 2],
                [-2, 1, 2]])
    b = Vector([8, -11, -3])
    solution = A.solve(b)
    print("Solution du système Ax = b :")
    print(solution)


if __name__ == "__main__":
    main()
