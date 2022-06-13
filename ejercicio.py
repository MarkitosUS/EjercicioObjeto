import json

class Vehiculo():

    matricula = None
    puertas = None

    def __init__(self, data = None):
        if data is not None:
            self.matricula = data["matricula"]
            self.puertas = data["puertas"]

    def to_json(self):
        return json.dumps(
            {
                "matricula": self.matricula,
                "puertas": self.puertas
            }
        )

# Creamos un objeto vehiculo con el primer constructor para darle variables
vehiculo = Vehiculo()
vehiculo.matricula = "123 HQS"
vehiculo.puertas = 5

# Guardamos en el archivo vehiculo.json los datos del vehiculo
with open("vehiculo.json", "w") as f:
    f.write(vehiculo.to_json())

# Creamos una nueva variable para un nuevo vehiculo con los datos que cargamos del archivo vehiculo.json
vehiculo_cargado = Vehiculo(json.load(open("vehiculo.json", "r")))

print(f"El vehiculo {vehiculo_cargado.matricula} tiene {vehiculo_cargado.puertas} puertas")