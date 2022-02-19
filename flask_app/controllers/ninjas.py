
from flask_app.__init__ import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/new_ninja')
def send():
    dojos=Dojo.get_dojos()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/add_ninja', methods=['POST'])
def new_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    dojo_id = Ninja.save_ninja(request.form)
    print('@'*20)
    print(dojo_id)
    return redirect(f"/dojo/{request.form['dojo_id']}")

@app.route('/dojo/<int:dojo_id>')
def show_ninja(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    ninja = Dojo.get_dojo_and_ninjas(data)
    return render_template('dojo_show.html', ninja=ninja)