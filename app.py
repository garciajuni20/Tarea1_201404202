from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar las canciones
canciones = []

@app.route('/agregar', methods=['POST'])
def agregar_cancion():
    data = request.json
    nueva_cancion = {
        'nombre': data['nombre'],
        'artista': data['artista'],
        'album': data['album']
    }
    canciones.append(nueva_cancion)
    return jsonify(nueva_cancion), 200

@app.route('/ver', methods=['GET'])
def ver_canciones():
    return jsonify(canciones)


if __name__ == '__main__':
    app.run(debug=True)
