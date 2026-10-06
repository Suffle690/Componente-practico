class Estudiante:

    def __init__(self, id, nombre, apellido, email, carnet):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet
        self.materias = []

    def agregar_nota(self, materia, nota):
        self.materias.append({
            "materia": materia,
            "nota": nota
        })

    def materias_en_comun(self, otro):
        comunes = set()

        for materia in self.materias:
            for materia2 in otro.materias:
                if materia["materia"] == materia2["materia"]:
                    comunes.add(materia["materia"])

        return comunes

    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "materias": self.materias
        }

    @classmethod
    def desde_diccionario(cls, datos):
        estudiante = cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["carnet"]
        )

        estudiante.materias = datos.get("materias", [])

        return estudiante

