from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from data.clsConexion import clsConexion
from data.clsDatos import clsDatos

conex = clsConexion()


@app.route('/main')
def index():
    return render_template('index.html', datos=conex.consultar())

@app.route('/')
def login():
    return render_template('login.html', datos=conex.consultar())

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == "POST":
        datos = clsDatos(0, request.form['txtUsuario'], request.form['txtContra'])
        # Add the data to the database
        conex.agregarUsuario(datos)
        # Log a debug message if the data was successfully added to the database
        app.logger.debug("Datos almacenados correctamente")

        # Redirect the user to the index page
        return redirect(url_for("index"))
    else:
        return render_template('signUp.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregars():
    if request.method == "POST":
        datos = clsDatos(0, request.form['txtTexto'], request.form['txtDescrip'])
        # Add the data to the database
        conex.agregars(datos)
        # Log a debug message if the data was successfully added to the database
        app.logger.debug("Datos almacenados correctamente")

        # Redirect the user to the index page
        return redirect(url_for("index"))
    else:
        return render_template('agregar.html')

@app.route('/modificar/<int:ide>', methods=['GET'])
def modificar(ide):
    return render_template('modificar.html', datos=conex.consultar(ide))
@app.route('/exec_modificar', methods=['POST', 'GET'])
def exec_modificar():
    if request.method == 'POST':
        id = request.form['txtID']
        datos = clsDatos(id, request.form['txtTexto'], request.form['txtDescrip'])

        if conex.modificar(datos):
            app.logger.debug("Datos modificados correctamente")
        else:
            app.logger.debug("Se presentó un problema con los datos")

        # Redirige a la página 'modificar.html' utilizando el nombre de la ruta 'modificar'
        return redirect(url_for('modificar'))
    else:
        # Lógica para manejar el método GET, si es necesario
        return render_template('modificar.html')




@app.route('/exec_eliminar/<int:ide>', methods=['GET'])
def exec_eliminar(ide):
    if conex.borrar(ide):
        app.logger.debug("Datos eliminado correctamente")
    else:
        app.logger.debug("Se presentó un problema con los datos")
    return redirect(url_for('index'))

# @app.route('/page01')
# def pag_01():
#    return render_template('pag_01.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
