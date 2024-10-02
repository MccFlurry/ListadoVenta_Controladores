from bd import obtener_conexion

def insertar_venta(cliente, responsable_venta, descripcion, cantidad, precio, descuento, enlace_informacion, enlace_imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO razm_venta (cliente, responsable_venta, descripcion, cantidad, precio, descuento, enlace_informacion, enlace_imagen) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, 
            (cliente, responsable_venta, descripcion, cantidad, precio, descuento, enlace_informacion, enlace_imagen))
    conexion.commit()
    conexion.close()

def obtener_ventas():
    conexion = obtener_conexion()
    ventas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM razm_venta")
        ventas = cursor.fetchall()
    conexion.close()
    return ventas

def eliminar_venta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM razm_venta WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_venta_por_id(id):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM razm_venta WHERE id = %s", (id,))
        venta = cursor.fetchone()
    conexion.close()
    return venta

def actualizar_venta(cliente, responsable_venta, descripcion, cantidad, precio, descuento, enlace_informacion, enlace_imagen, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE razm_venta 
            SET cliente = %s, responsable_venta = %s, descripcion = %s, cantidad = %s, precio = %s, descuento = %s, 
                enlace_informacion = %s, enlace_imagen = %s 
            WHERE id = %s""",
            (cliente, responsable_venta, descripcion, cantidad, precio, descuento, enlace_informacion, enlace_imagen, id))
    conexion.commit()
    conexion.close()
