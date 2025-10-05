import utils.io_jon as j

ARCHIVO_CAMPERS = "campers.json"
ARCHIVO_TRAINERS = "trainers.json"
def campers_inscritos_aprobados():
    data = j.read_json(ARCHIVO_CAMPERS)
    campers = data.get("campers", [])

    inscritos = sum(1 for c in campers if c["datos"]["estado"].lower() == "inscrito")
    aprobados = sum(1 for c in campers if c["datos"]["estado"].lower() == "aprobado")

    print(f"Campers inscritos: {inscritos}")
    print(f"Campers aprobados: {aprobados}")
    


def trainers_activos():
    data = j.read_json(ARCHIVO_TRAINERS)
    trainers = data.get("trainers", [])

    con_ruta = sum(1 for t in trainers if t["datos"]["ruta"])
    sin_ruta = sum(1 for t in trainers if not t["datos"]["ruta"])

    print(f"Trainers con ruta asignada: {con_ruta}")
    print(f"Trainers sin ruta: {sin_ruta}")

def campers_bajo_rendimiento():
    data = j.read_json(ARCHIVO_CAMPERS)
    campers = data.get("campers", [])

    conteo = {"bajo": 0, "medio": 0, "alto": 0}

    for camper in campers:
        riesgo = camper["datos"]["riesgo"].lower()
        if riesgo in conteo:
            conteo[riesgo] += 1

    print("📊 Campers por nivel de riesgo:")
    for nivel, cantidad in conteo.items():
        print(f"{nivel.capitalize()}: {cantidad}")



