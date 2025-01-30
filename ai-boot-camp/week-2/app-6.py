class Vektor():

    def __init__(self, _x = 1, _y = 1):
        self.x = _x
        self.y = _y
        self.magnitude = ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "Bu nesne bir vektör nesensidir. x, y ve büyüklük özellikleri taşır."

    def __add__(self, vector):
        n_x = self.x + vector.x
        n_y = self.y + vector.y

        return Vektor(n_x, n_y)
    
vector1 = Vektor(3, 5)
vector2 = Vektor(5, 7)

vector3 = vector1 + vector2

print(f"""

    Vektör : vektör1
        {str(vector1)}
      
      {vector1.x}, {vector1.y}, {vector1.magnitude}

    """)

print(f"""

    Vektör : vektör2
        {str(vector2)}
      
      {vector2.x}, {vector2.y}, {vector2.magnitude}

    """)

print(f"""

    Vektör : vektör3
        {str(vector3)}
      
      {vector3.x}, {vector3.y}, {vector3.magnitude}

    """)
