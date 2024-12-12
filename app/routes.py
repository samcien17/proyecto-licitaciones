from flask import Blueprint, jsonify, request
from . import db
from .models import Licitante, Proveedor, Licitacion, Oferta, Bitacora
from datetime import datetime

api = Blueprint('api', __name__)

# Rutas para Licitantes
@api.route('/licitantes', methods=['GET'])
def get_licitantes():
    licitantes = Licitante.query.all()
    return jsonify([licitante.to_dict() for licitante in licitantes])

@api.route('/licitantes/<int:id>', methods=['GET'])
def get_licitante(id):
    licitante = Licitante.query.get_or_404(id)
    return jsonify(licitante.to_dict())

@api.route('/licitantes', methods=['POST'])
def create_licitante():
    data = request.get_json()
    nuevo_licitante = Licitante(
        nombre=data['nombre'],
        direccion=data.get('direccion'),
        telefono=data.get('telefono'),
        correo=data.get('correo')
    )
    db.session.add(nuevo_licitante)
    db.session.commit()
    return jsonify(nuevo_licitante.to_dict()), 201

@api.route('/licitantes/<int:id>', methods=['PUT'])
def update_licitante(id):
    licitante = Licitante.query.get_or_404(id)
    data = request.get_json()
    
    licitante.nombre = data.get('nombre', licitante.nombre)
    licitante.direccion = data.get('direccion', licitante.direccion)
    licitante.telefono = data.get('telefono', licitante.telefono)
    licitante.correo = data.get('correo', licitante.correo)
    
    db.session.commit()
    return jsonify(licitante.to_dict())

@api.route('/licitantes/<int:id>', methods=['DELETE'])
def delete_licitante(id):
    licitante = Licitante.query.get_or_404(id)
    db.session.delete(licitante)
    db.session.commit()
    return jsonify({'message': 'Licitante eliminado correctamente'})

# Rutas para Proveedores
@api.route('/proveedores', methods=['GET'])
def get_proveedores():
    proveedores = Proveedor.query.all()
    return jsonify([proveedor.to_dict() for proveedor in proveedores])

@api.route('/proveedores/<int:id>', methods=['GET'])
def get_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    return jsonify(proveedor.to_dict())

@api.route('/proveedores', methods=['POST'])
def create_proveedor():
    data = request.get_json()
    nuevo_proveedor = Proveedor(
        nombre=data['nombre'],
        correo=data.get('correo'),
        telefono=data.get('telefono')
    )
    db.session.add(nuevo_proveedor)
    db.session.commit()
    return jsonify(nuevo_proveedor.to_dict()), 201

@api.route('/proveedores/<int:id>', methods=['PUT'])
def update_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    data = request.get_json()
    
    proveedor.nombre = data.get('nombre', proveedor.nombre)
    proveedor.correo = data.get('correo', proveedor.correo)
    proveedor.telefono = data.get('telefono', proveedor.telefono)
    
    db.session.commit()
    return jsonify(proveedor.to_dict())

@api.route('/proveedores/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return jsonify({'message': 'Proveedor eliminado correctamente'})

# Rutas para Licitaciones
@api.route('/licitaciones', methods=['GET'])
def get_licitaciones():
    licitaciones = Licitacion.query.all()
    return jsonify([licitacion.to_dict() for licitacion in licitaciones])

@api.route('/licitaciones/<int:id>', methods=['GET'])
def get_licitacion(id):
    licitacion = Licitacion.query.get_or_404(id)
    return jsonify(licitacion.to_dict())

@api.route('/licitaciones', methods=['POST'])
def create_licitacion():
    data = request.get_json()
    nueva_licitacion = Licitacion(
        licitante_id=data['licitante_id'],
        descripcion=data.get('descripcion'),
        fecha_fin=datetime.fromisoformat(data['fecha_fin']) if 'fecha_fin' in data else None,
        estado='Abierta'
    )
    db.session.add(nueva_licitacion)
    db.session.commit()
    return jsonify(nueva_licitacion.to_dict()), 201

@api.route('/licitaciones/<int:id>', methods=['PUT'])
def update_licitacion(id):
    licitacion = Licitacion.query.get_or_404(id)
    data = request.get_json()
    
    licitacion.descripcion = data.get('descripcion', licitacion.descripcion)
    if 'fecha_fin' in data:
        licitacion.fecha_fin = datetime.fromisoformat(data['fecha_fin'])
    licitacion.estado = data.get('estado', licitacion.estado)
    
    db.session.commit()
    return jsonify(licitacion.to_dict())

@api.route('/licitaciones/<int:id>', methods=['DELETE'])
def delete_licitacion(id):
    licitacion = Licitacion.query.get_or_404(id)
    db.session.delete(licitacion)
    db.session.commit()
    return jsonify({'message': 'Licitación eliminada correctamente'})

# Rutas para Ofertas
@api.route('/ofertas', methods=['GET'])
def get_ofertas():
    ofertas = Oferta.query.all()
    return jsonify([oferta.to_dict() for oferta in ofertas])

@api.route('/ofertas/<int:id>', methods=['GET'])
def get_oferta(id):
    oferta = Oferta.query.get_or_404(id)
    return jsonify(oferta.to_dict())

@api.route('/ofertas', methods=['POST'])
def create_oferta():
    data = request.get_json()
    nueva_oferta = Oferta(
        licitacion_id=data['licitacion_id'],
        proveedor_id=data['proveedor_id'],
        monto_ofrecido=data['monto_ofrecido'],
        estado='Pendiente'
    )
    db.session.add(nueva_oferta)
    db.session.commit()
    return jsonify(nueva_oferta.to_dict()), 201

@api.route('/ofertas/<int:id>', methods=['PUT'])
def update_oferta(id):
    oferta = Oferta.query.get_or_404(id)
    data = request.get_json()
    
    oferta.monto_ofrecido = data.get('monto_ofrecido', oferta.monto_ofrecido)
    oferta.estado = data.get('estado', oferta.estado)
    
    db.session.commit()
    return jsonify(oferta.to_dict())

@api.route('/ofertas/<int:id>', methods=['DELETE'])
def delete_oferta(id):
    oferta = Oferta.query.get_or_404(id)
    db.session.delete(oferta)
    db.session.commit()
    return jsonify({'message': 'Oferta eliminada correctamente'})

# Rutas para Bitácoras
@api.route('/bitacoras', methods=['GET'])
def get_bitacoras():
    bitacoras = Bitacora.query.all()
    return jsonify([bitacora.to_dict() for bitacora in bitacoras])

@api.route('/bitacoras/<int:id>', methods=['GET'])
def get_bitacora(id):
    bitacora = Bitacora.query.get_or_404(id)
    return jsonify(bitacora.to_dict())

@api.route('/bitacoras', methods=['POST'])
def create_bitacora():
    data = request.get_json()
    nueva_bitacora = Bitacora(
        licitacion_id=data['licitacion_id'],
        descripcion=data.get('descripcion')
    )
    db.session.add(nueva_bitacora)
    db.session.commit()
    return jsonify(nueva_bitacora.to_dict()), 201

@api.route('/bitacoras/<int:id>', methods=['PUT'])
def update_bitacora(id):
    bitacora = Bitacora.query.get_or_404(id)
    data = request.get_json()
    
    bitacora.descripcion = data.get('descripcion', bitacora.descripcion)
    
    db.session.commit()
    return jsonify(bitacora.to_dict())

@api.route('/bitacoras/<int:id>', methods=['DELETE'])
def delete_bitacora(id):
    bitacora = Bitacora.query.get_or_404(id)
    db.session.delete(bitacora)
    db.session.commit()
    return jsonify({'message': 'Bitácora eliminada correctamente'})

# Rutas adicionales para relaciones
@api.route('/licitaciones/<int:id>/ofertas', methods=['GET'])
def get_ofertas_por_licitacion(id):
    """Obtener todas las ofertas de una licitación específica"""
    ofertas = Oferta.query.filter_by(licitacion_id=id).all()
    return jsonify([oferta.to_dict() for oferta in ofertas])

@api.route('/licitaciones/<int:id>/bitacoras', methods=['GET'])
def get_bitacoras_por_licitacion(id):
    """Obtener todas las bitácoras de una licitación específica"""
    bitacoras = Bitacora.query.filter_by(licitacion_id=id).all()
    return jsonify([bitacora.to_dict() for bitacora in bitacoras])

@api.route('/proveedores/<int:id>/ofertas', methods=['GET'])
def get_ofertas_por_proveedor(id):
    """Obtener todas las ofertas de un proveedor específico"""
    ofertas = Oferta.query.filter_by(proveedor_id=id).all()
    return jsonify([oferta.to_dict() for oferta in ofertas])

# Manejadores de errores
@api.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Recurso no encontrado'}), 404

@api.errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': 'Solicitud incorrecta'}), 400

@api.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Error interno del servidor'}), 500