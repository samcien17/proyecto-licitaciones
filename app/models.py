from datetime import datetime
from . import db

class Licitante(db.Model):
    __tablename__ = 'Licitantes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(100))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    licitaciones = db.relationship('Licitacion', backref='licitante', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'correo': self.correo,
            'fecha_registro': self.fecha_registro.isoformat()
        }

class Proveedor(db.Model):
    __tablename__ = 'Proveedores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    ofertas = db.relationship('Oferta', backref='proveedor', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'telefono': self.telefono,
            'fecha_registro': self.fecha_registro.isoformat()
        }

class Licitacion(db.Model):
    __tablename__ = 'Licitaciones'
    
    id = db.Column(db.Integer, primary_key=True)
    licitante_id = db.Column(db.Integer, db.ForeignKey('Licitantes.id'), nullable=False)
    descripcion = db.Column(db.Text)
    fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_fin = db.Column(db.DateTime)
    estado = db.Column(db.Enum('Abierta', 'Cerrada', 'Cancelada'), default='Abierta')
    ofertas = db.relationship('Oferta', backref='licitacion', lazy=True)
    bitacoras = db.relationship('Bitacora', backref='licitacion', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'licitante_id': self.licitante_id,
            'descripcion': self.descripcion,
            'fecha_inicio': self.fecha_inicio.isoformat(),
            'fecha_fin': self.fecha_fin.isoformat() if self.fecha_fin else None,
            'estado': self.estado
        }

class Oferta(db.Model):
    __tablename__ = 'Ofertas'
    
    id = db.Column(db.Integer, primary_key=True)
    licitacion_id = db.Column(db.Integer, db.ForeignKey('Licitaciones.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('Proveedores.id'), nullable=False)
    monto_ofrecido = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_oferta = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.Enum('Pendiente', 'Aceptada', 'Rechazada'), default='Pendiente')

    def to_dict(self):
        return {
            'id': self.id,
            'licitacion_id': self.licitacion_id,
            'proveedor_id': self.proveedor_id,
            'monto_ofrecido': float(self.monto_ofrecido),
            'fecha_oferta': self.fecha_oferta.isoformat(),
            'estado': self.estado
        }

class Bitacora(db.Model):
    __tablename__ = 'Bitacoras'
    
    id = db.Column(db.Integer, primary_key=True)
    licitacion_id = db.Column(db.Integer, db.ForeignKey('Licitaciones.id'), nullable=False)
    descripcion = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'licitacion_id': self.licitacion_id,
            'descripcion': self.descripcion,
            'fecha': self.fecha.isoformat()
        }