-- Crear tabla para Licitantes
CREATE TABLE Licitantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla para Proveedores
CREATE TABLE Proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(20),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla para Licitaciones
CREATE TABLE Licitaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    licitante_id INT NOT NULL,
    descripcion TEXT,
    fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_fin TIMESTAMP,
    estado ENUM('Abierta', 'Cerrada', 'Cancelada') DEFAULT 'Abierta',
    FOREIGN KEY (licitante_id) REFERENCES Licitantes(id)
);

-- Crear tabla para Ofertas
CREATE TABLE Ofertas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    licitacion_id INT NOT NULL,
    proveedor_id INT NOT NULL,
    monto_ofrecido DECIMAL(10,2) NOT NULL,
    fecha_oferta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('Pendiente', 'Aceptada', 'Rechazada') DEFAULT 'Pendiente',
    FOREIGN KEY (licitacion_id) REFERENCES Licitaciones(id),
    FOREIGN KEY (proveedor_id) REFERENCES Proveedores(id)
);

-- Crear tabla para Bitácoras
CREATE TABLE Bitacoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    licitacion_id INT NOT NULL,
    descripcion TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (licitacion_id) REFERENCES Licitaciones(id)
);