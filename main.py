from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos en memoria
productos = []
contador_id = 1

# Crear producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    global contador_id
    data = request.json
    producto = {
        'id': contador_id,
        'nombre': data['nombre'],
        'descripcion': data['descripcion'],
        'precio': data['precio']
    }
    productos.append(producto)
    contador_id += 1
    return jsonify(producto), 201

# Ver todos los productos
@app.route('/productos', methods=['GET'])
def ver_productos():
    return jsonify(productos)

# Ver un producto por ID
@app.route('/productos/<int:id>', methods=['GET'])
def ver_producto(id):
    for producto in productos:
        if producto['id'] == id:
            return jsonify(producto)
    return jsonify({'error': 'No encontrado'}), 404

# Actualizar producto
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    for producto in productos:
        if producto['id'] == id:
            producto['nombre'] = data['nombre']
            producto['descripcion'] = data['descripcion']
            producto['precio'] = data['precio']
            return jsonify(producto)
    return jsonify({'error': 'No encontrado'}), 404

# Eliminar producto
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p['id'] != id]
    return jsonify({'mensaje': 'Producto eliminado'})

# CRUD de productos de monitoreo satelital
if __name__ == '__main__':
    app.run(debug=True)