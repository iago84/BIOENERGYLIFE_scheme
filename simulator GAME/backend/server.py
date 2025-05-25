from flask import Flask, jsonify
from flask_cors import CORS
from controller import cargar_inicial, evolucionar
from db import celulas_table, organulos_table, logs_table

app = Flask(__name__)
CORS(app)  # Permitir CORS para acceder desde index.html

# Cargar sistema al iniciar
cargar_inicial()

@app.route('/')
def home():
    return jsonify({"message": "Simulador Energético activo"})

@app.route('/evolucionar')
def run_evolucion():
    resultado = evolucionar(1)
    return jsonify({"resultado": resultado})

@app.route('/estado')
def estado():
    celulas = celulas_table.all()
    organulos = organulos_table.all()
    return jsonify({"celulas": celulas, "organulos": organulos})

@app.route('/log')
def log():
    logs = logs_table.all()[-10:]
    return jsonify({"logs": logs})

if __name__ == '__main__':
    app.run(debug=True)
