
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar/formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    edad = request.form['edad']
    ciudad = request.form['ciudad']

@app.route('/procesar/formulario', methods=['POST'])
def procesar_ciudades():
    nombre = request.form.get('nombre')
    edad = request.form.get('edad')
    ciudad = request.form.get('ciudad')
    sexo = request.form.get('sexo')
    condiciones = request.form.get('condiciones')

errores = []

if not nombre:
    errores.append("El nombre es obligatorio.")
if not edad:
    errores.append("La edad es obligatoria.")
if not condiciones:
    errores.append("Debes aceptar las condiciones.")

if errores:
 return "<br>".join(errores) + "<br><br><a href='/'>Volver</a>"

return f"""
<h2>Datos válidos</h2>
<ul>
<li><b>Nombre:</b> {nombre}</li>
<li><b>Edad:</b> {edad}</li>
<li><b>Ciudad:</b> {ciudad}</li>
<li><b>Sexo:</b> {sexo}</li>
</ul>
<a href="/">Volver al formulario</a>
"""

    # Aquí devolvemos los datos a la plantilla HTML para mostrarlos
 return render_template('resultado.html', nombre=nombre, edad=edad, ciudad=ciudad)

if __name__ == '__main__':
    app.run(debug=True)


# Para ejecutar el script, primero hay que instalar Flask:
# pip install Flask

# Luego, ejecutar el script:
# python app.py

# Acceder a http://127.0.0.1:5000
# Para detener la ejecución, presionar Ctrl+C en la terminal
# http://127.0.0.1:5000/ va a al formulario
# http://127.0.0.1:5000/procesar va a la página de resultados