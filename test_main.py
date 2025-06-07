import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_crear_producto(client):
    response = client.post('/productos', json={
        'nombre': 'GPS Tracker',
        'descripcion': 'Rastreo satelital',
        'precio': 100
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['nombre'] == 'GPS Tracker'

def test_ver_todos_los_productos(client):
    response = client.get('/productos')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_ver_producto_por_id(client):
    # Primero creamos un producto
    client.post('/productos', json={
        'nombre': 'GPS Tracker',
        'descripcion': 'Rastreo satelital',
        'precio': 100
    })
    response = client.get('/productos/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1

def test_actualizar_producto(client):
    client.post('/productos', json={
        'nombre': 'GPS Tracker',
        'descripcion': 'Rastreo satelital',
        'precio': 100
    })
    response = client.put('/productos/1', json={
        'nombre': 'Nuevo GPS',
        'descripcion': 'Actualizado',
        'precio': 120
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['nombre'] == 'Nuevo GPS'

def test_eliminar_producto(client):
    client.post('/productos', json={
        'nombre': 'GPS Tracker',
        'descripcion': 'Rastreo satelital',
        'precio': 100
    })
    response = client.delete('/productos/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['mensaje'] == 'Producto eliminado'