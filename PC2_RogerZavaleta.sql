CREATE TABLE razm_venta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(255) NOT NULL,
    responsable_venta VARCHAR(255) NOT NULL,
    descripcion VARCHAR(500),
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descuento DECIMAL(10, 2),
    enlace_informacion VARCHAR(500),
    enlace_imagen VARCHAR(500)
);
