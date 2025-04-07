class Vector:
    def __init__(self, elements) -> None:
        self.elements = list(elements)

    def push_back(self, element: int) -> None:
        self.elements.append(element)

    def add_vector(self, second_vector: 'Vector') -> 'Vector':
        if len(self.elements) != len(second_vector.elements):
            raise ValueError("Les vecteurs ont une taille différente")

        return Vector([a + b for a, b in zip(self.elements, second_vector.elements)])

    def sub_vector(self, second_vector: 'Vector') -> 'Vector':
        if len(self.elements) != len(second_vector.elements):
            raise ValueError("Les vecteurs ont une taille différente")

        return Vector([a - b for a, b in zip(self.elements, second_vector.elements)])

    def multiply_vector(self, second_vector: 'Vector') -> 'Vector':


        if len(self.elements) != len(second_vector.elements):
            raise ValueError("Les vecteurs ont une taille différente")

        return Vector([a * b for a, b in zip(self.elements, second_vector.elements)])

    def scalar_product(self, second_vector: 'Vector') -> 'int':
        if len(self.elements) != len(second_vector.elements):
            raise ValueError("Les vecteurs ont une taille différente")

        return sum([a * b for a, b in zip(self.elements, second_vector.elements)])

    def are_orthogonal(self, second_vector: 'Vector') -> 'bool':
        if len(self.elements) != len(second_vector.elements):
            raise ValueError("Les vecteurs ont une taille différente")

        return self.scalar_product(second_vector) == 0

    def __add__(self, second_vector: 'Vector') -> 'Vector':
        return self.add_vector(second_vector)

    def __sub__(self, second_vector: 'Vector') -> 'Vector':
        return self.sub_vector(second_vector)

    def __mul__(self, second_vector: 'Vector') -> 'Vector':
        return self.multiply_vector(second_vector)
    __rmul__ = __mul__
    def __matmul__(self, second_vector: 'Vector') -> 'int':
        return self.scalar_product(second_vector)

    def __str__(self) -> str:
        # Convertir chaque élément en chaîne de caractères
        rows_str = [str(x) for x in self.elements]
        # Déterminer la largeur maximale pour aligner les éléments proprement
        max_width = max(len(s) for s in rows_str) if rows_str else 0
        # Construire une ligne horizontale de séparation
        horizontal_line = "+" + "-" * (max_width + 2) + "+"

        # Construire chaque ligne du vecteur avec les bordures
        formatted_rows = [horizontal_line]
        for s in rows_str:
            formatted_rows.append("| " + s.rjust(max_width) + " |")
            formatted_rows.append(horizontal_line)

        return "\n".join(formatted_rows)
    ## ========================= operation plus raide avec les EGALITES (+=, *= -=) =========================
    def __iadd__(self, second_vector: 'Vector') -> 'Vector':
        new_vector = self.add_vector(second_vector)
        self.elements = new_vector.elements
        return self


    def __isub__(self, second_vector: 'Vector') -> 'Vector':
        new_vector = self.sub_vector(second_vector)
        self.elements = new_vector.elements
        return self

    def __imul__(self, second_vector: 'Vector') -> 'Vector':
        new_vector = self.multiply_vector(second_vector)
        self.elements = new_vector.elements
        return self



def main():
    # Création de deux vecteurs de même taille pour les opérations arithmétiques
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    print("v1 =", v1.elements)
    print("v2 =", v2.elements)

    # Test de push_back sur v1
    print("\n--- Test push_back ---")
    v1.push_back(7)
    print("v1 après push_back(7) =", v1.elements)

    # Pour les opérations suivantes, on utilise des vecteurs de même taille
    v3 = Vector([1, 2, 3])
    v4 = Vector([4, 5, 6])

    # Test de l'addition
    print("\n--- Test addition ---")
    somme = v3 + v4  # équivaut à v3.add_vector(v4)
    print("v3 + v4 =", somme)

    # Test de la soustraction
    print("\n--- Test soustraction ---")
    difference = v3 - v4  # équivaut à v3.sub_vector(v4)
    print("v3 - v4 =", difference)

    # Test de la multiplication élément par élément
    print("\n--- Test multiplication élément par élément ---")
    produit = v3 * v4  # équivaut à v3.multiply_vector(v4)
    print("v3 * v4 =", produit)

    # Test du produit scalaire avec l'opérateur @
    print("\n--- Test produit scalaire ---")
    scalaire = v3 @ v2 # équivaut à v3.scalar_product(v4)
    print("v3 @ v4 =", scalaire)

    print("\n--- Test __STR__ ---")
    print(v1.__str__())


if __name__ == "__main__":
    main()
