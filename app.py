
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