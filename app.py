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

@app.route("/observatorio")
def observatorio():
    return render_template("observatorio.html")

@app.route("/contacto", methods=['GET','POST'])
def contacto():
    return render_template("contacto.html")