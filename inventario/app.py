from flask import Flask, render_template, request, flash, redirect
# traemos dependecia de pymongo para la conexion a la base de datos
from pymongo import MongoClient

app = Flask(__name__)
# ponemos la conexion y la base de datos
client = MongoClient('localhost', 27017)
db = client.activos_almacen


@app.route('/introducir_activo', methods=['GET'])
def tipos():
    tipo = ['Torre', 'Portatil', 'Monitor', 'Moviles', 'Hardware equipos', 'Cableado general', 'Otros', 'EPIS']
    ubi = ['Dingus', 'Etoolinnovation', 'Mexico', 'Canarias']
    status = ['OK', 'KO', 'Testing']
    if request.method == 'POST':
        tipos = request.form['tipo']
        ubicacion = request.form['ubi']
        estado = request.form['status']
        flash(str(tipos))
        flash(str(ubicacion))
        flash(str(estado))
    return render_template('insert.html', tipo=tipo, ubi=ubi, status=status)


@app.route('/enviar_activo')
def enviar_activo():
    tipe = request.args['tipo']
    mark = request.args['marca']
    model = request.args['modelo']
    quantity = request.args['cantidad']
    ubication = request.args['ubicacion']
    status = request.args['estado']
    url = request.args['url']
    observations = request.args['observaciones']

    db.inventario_almacen.insert_one(
        {"tipe": tipe,
         "mark": mark,
         "model": model,
         "quantity": quantity,
         "ubication": ubication,
         "status": status,
         "url": url,
         "observations": observations
         }
    )

    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def inventario():
    activos = db.inventario_almacen.find()
    id = db.inventario_almacen.find_one({'mark': 'Asus', 'model': 'VS239', 'ubication': 'Dingus', 'status': 'OK'})[u'_id']
    db.inventario_almacen.update_one({'_id': id}, {'$set': {"quantity": 1}})
    return render_template('index.html', activos=activos, id=id)


if __name__ == "__main__":
    app.run(debug=True, port=80)
