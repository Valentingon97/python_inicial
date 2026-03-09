-- Crear base de datos
CREATE DATABASE IF NOT EXISTS curso_python_db_tu_nombre
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE curso_python_db_tu_nombre;

-- Tabla Categoria
CREATE TABLE Categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla Producto
CREATE TABLE Producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    id_categoria INT NOT NULL,
    precio_gs INT NOT NULL CHECK (precio_gs >= 0),
    iva_porcentaje SMALLINT NOT NULL CHECK (iva_porcentaje IN (0,5,10)),
    CONSTRAINT fk_producto_categoria FOREIGN KEY (id_categoria)
    REFERENCES Categoria(id_categoria)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- Tabla Inventario
CREATE TABLE Inventario (
    id_producto INT PRIMARY KEY,
    cantidad INT NOT NULL DEFAULT 0 CHECK (cantidad >= 0),
    stock_minimo INT NOT NULL DEFAULT 0 CHECK (stock_minimo >= 0),
    CONSTRAINT fk_inventario_producto FOREIGN KEY (id_producto)
    REFERENCES Producto(id_producto)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);



-- 1. Trigger: al insertar producto, crear fila en Inventario
DROP TRIGGER IF EXISTS after_insert_producto;

DELIMITER $$
CREATE TRIGGER after_insert_producto
AFTER INSERT ON Producto
FOR EACH ROW
BEGIN
    -- Inserta fila en Inventario con cantidad 0 y stock_minimo 0
    INSERT INTO Inventario (id_producto, cantidad, stock_minimo)
    VALUES (NEW.id_producto, 0, 0);
END$$
DELIMITER ;

-- 2. DML (Inserción de datos)
INSERT INTO Categoria (nombre) VALUES
('Panificados'),
('Bebidas'),
('Limpieza');

INSERT INTO Producto (nombre, id_categoria, precio_gs, iva_porcentaje)
VALUES
('Arroz 1kg', 1, 16000, 10),
('Azúcar 1kg', 1, 15000, 10),
('Gaseosa 2L', 2, 25000, 5),
('Pan (unidad)', 1, 2500, 0);

-- 3. Verificar contenido de tablas
SELECT * FROM Categoria;
SELECT * FROM Producto;
SELECT * FROM Inventario;

-- 4. Actualizar el Stock de los productos
-- (Aumenta 50 unidades al producto con ID 3)
UPDATE Inventario
SET cantidad = cantidad + 50
WHERE id_producto = 3;

-- 5. Actualizar precio (Ejemplo)
UPDATE Producto
SET precio_gs = 17000
WHERE id_producto = 1;

-- 6. Recuperar productos y sus categorías y su stock (JOIN)
SELECT 
    p.nombre AS Producto, 
    c.nombre AS Categoria, 
    i.cantidad AS Stock
FROM Producto p
JOIN Categoria c ON p.id_categoria = c.id_categoria
JOIN Inventario i ON p.id_producto = i.id_producto;
