from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
from flask_cors import CORS

CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}}) 

# Endpoint GET para devolver los datos
@app.route('/api/elementos', methods=['GET'])
def obtener_elementos():
    try:
        elementos = [
            {"id": 1, "nombre": "Coca", "descripcion": "Refresco sabor Cola"},
            {"id": 2, "nombre": "Limonada", "descripcion": "Rica bebida hecha con juego de limon y agua mineral"},
            {"id": 3, "nombre": "Piñada", "descripcion": "Defrescante bebida hecha con jugo de piña, coco y bacardi"}
        ]
        return jsonify(elementos), 200
    except Exception as e:
        return jsonify({"error": "Ocurrió un error"}), 500  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)   