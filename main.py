from flask import Flask, render_template, request, redirect
import ra_controlador_venta

app = Flask(__name__)

@app.route("/")
@app.route("/razm_ventas")
def razm_ventas():
    ventas = ra_controlador_venta.obtener_ventas()
    ventas_calculadas = []
    for venta in ventas:
        precio = float(venta[5]) 
        deduccion = round(precio / 1.18, 2)
        porcentaje_18 = round(deduccion * 0.18, 2)
        venta_calculada = list(venta) + [deduccion, porcentaje_18]
        ventas_calculadas.append(venta_calculada)
    return render_template("ventas_zm.html", ventas=ventas_calculadas)

@app.route("/razm_agregar_venta")
def razm_formulario_agregar_venta():
    return render_template("agregar_venta_zm.html")

@app.route("/razm_guardar_venta", methods=["POST"])
def razm_guardar_venta():
    cliente = request.form["cliente"]
    responsable_venta = request.form["responsable_venta"]
    descripcion = request.form["descripcion"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]
    descuento = request.form["descuento"]
    enlace_informacion = request.form["enlace_informacion"]
    enlace_imagen = request.form["enlace_imagen"]
    ra_controlador_venta.insertar_venta(cliente, responsable_venta, descripcion, cantidad, precio, descuento, enlace_informacion, enlace_imagen)
    return redirect("/razm_ventas")

@app.route("/razm_eliminar_venta", methods=["POST"])
def razm_eliminar_venta():
    ra_controlador_venta.eliminar_venta(request.form["id"])
    return redirect("/razm_ventas")

@app.route("/razm_editar_venta/<int:id>")
def razm_editar_venta(id):
    venta = ra_controlador_venta.obtener_venta_por_id(id)
    return render_template("editar_venta_zm.html", venta=venta)

@app.route("/razm_actualizar_venta", methods=["POST"])
def razm_actualizar_venta():
    id = request.form["id"]
    cliente = request.form["cliente"]
    responsable_venta = request.form["responsable_venta"]
    descripcion = request.form["descripcion"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]
    descuento = request.form["descuento"]
    enlace_informacion = request.form["enlace_informacion"]
    enlace_imagen = request.form["enlace_imagen"]
    ra_controlador_venta.actualizar_venta(cliente, responsable_venta, descripcion, cantidad, precio, descuento, enlace_informacion, enlace_imagen, id)
    return redirect("/razm_ventas")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
