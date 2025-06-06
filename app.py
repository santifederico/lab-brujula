from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/metodologia")
def metodologia():
    return render_template("metodologia.html")

@app.route('/plataforma-vivienda-suelo')
def plataforma_vivienda_suelo():
    geojson_path = os.path.join(app.static_folder, './geojson/lujan.geojson')
    
    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    features = geojson_data.get('features', [])
    table_data = []
    escalas_set = set()

    for feature in features:
        properties = feature.get('properties', {})

        # 👉 Filtrar por DIMENSION
        if properties.get('DIMENSION') != 'VIVIENDA Y SUELO':
            continue  # salteamos todo lo que no sea esa dimensión

        # 👉 Eliminar PROYECTO si está
        if 'PROYECTO' in properties:
            del properties['PROYECTO']

        # 👉 Guardar ESCALA para el selector
        escala = properties.get('ESCALA')
        if escala:
            escalas_set.add(escala)

        table_data.append(properties)

    escalas = sorted(list(escalas_set))  # para el selector

    return render_template('plataforma-vivienda-suelo.html', table_data=table_data, escalas=escalas)

@app.route('/plataforma-infraestructuras')
def plataforma_infraestructuras():
    geojson_path = os.path.join(app.static_folder, './geojson/lujan.geojson')
    
    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    features = geojson_data.get('features', [])
    table_data = []
    escalas_set = set()

    for feature in features:
        properties = feature.get('properties', {})

        # 👉 Filtrar por DIMENSION
        if properties.get('DIMENSION') != 'INFRAESTRUCTURAS':
            continue  # salteamos todo lo que no sea esa dimensión

        # 👉 Eliminar PROYECTO si está
        if 'PROYECTO' in properties:
            del properties['PROYECTO']

        # 👉 Guardar ESCALA para el selector
        escala = properties.get('ESCALA')
        if escala:
            escalas_set.add(escala)

        table_data.append(properties)

    escalas = sorted(list(escalas_set))  # para el selector

    return render_template('plataforma-infraestructuras.html', table_data=table_data, escalas=escalas)

@app.route('/plataforma-equipamientos')
def plataforma_equipamientos():
    geojson_path = os.path.join(app.static_folder, './geojson/lujan.geojson')
    
    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    features = geojson_data.get('features', [])
    table_data = []
    escalas_set = set()

    for feature in features:
        properties = feature.get('properties', {})

        # 👉 Filtrar por DIMENSION
        if properties.get('DIMENSION') != 'EQUIPAMIENTOS':
            continue  # salteamos todo lo que no sea esa dimensión

        # 👉 Eliminar PROYECTO si está
        if 'PROYECTO' in properties:
            del properties['PROYECTO']

        # 👉 Guardar ESCALA para el selector
        escala = properties.get('ESCALA')
        if escala:
            escalas_set.add(escala)

        table_data.append(properties)

    escalas = sorted(list(escalas_set))  # para el selector

    return render_template('plataforma-equipamientos.html', table_data=table_data, escalas=escalas)

@app.route('/plataforma-accesibilidad')
def plataforma_accesibilidad():
    geojson_path = os.path.join(app.static_folder, './geojson/lujan.geojson')
    
    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    features = geojson_data.get('features', [])
    table_data = []
    escalas_set = set()

    for feature in features:
        properties = feature.get('properties', {})

        # 👉 Filtrar por DIMENSION
        if properties.get('DIMENSION') != 'ACCESIBILIDAD':
            continue  # salteamos todo lo que no sea esa dimensión

        # 👉 Eliminar PROYECTO si está
        if 'PROYECTO' in properties:
            del properties['PROYECTO']

        # 👉 Guardar ESCALA para el selector
        escala = properties.get('ESCALA')
        if escala:
            escalas_set.add(escala)

        table_data.append(properties)

    escalas = sorted(list(escalas_set))  # para el selector

    return render_template('plataforma-accesibilidad.html', table_data=table_data, escalas=escalas)

@app.route('/plataforma-desarrollo-local')
def plataforma_desarrollo_local():
    geojson_path = os.path.join(app.static_folder, './geojson/lujan.geojson')
    
    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    features = geojson_data.get('features', [])
    table_data = []
    escalas_set = set()

    for feature in features:
        properties = feature.get('properties', {})

        # 👉 Filtrar por DIMENSION
        if properties.get('DIMENSION') != 'DESARROLLO LOCAL':
            continue  # salteamos todo lo que no sea esa dimensión

        # 👉 Eliminar PROYECTO si está
        if 'PROYECTO' in properties:
            del properties['PROYECTO']

        # 👉 Guardar ESCALA para el selector
        escala = properties.get('ESCALA')
        if escala:
            escalas_set.add(escala)

        table_data.append(properties)

    escalas = sorted(list(escalas_set))  # para el selector

    return render_template('plataforma-desarrollo-local.html', table_data=table_data, escalas=escalas)

@app.route("/observatorio")
def observatorio():
    return render_template("observatorio.html")

@app.route("/contacto", methods=['GET','POST'])
def contacto():
    return render_template("contacto.html")