
from flask_app.__init__ import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route("/")
def get_dojos():
    dojos = Dojo.get_dojos()
    return render_template("index.html", dojos = dojos)

@app.route('/new_dojo', methods=['POST'])
def add_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save_dojo(request.form)
    return redirect("/")

#@app.route('/dojo/<int:dojo_id>')
#def show_dojo(dojo_id):
 #   data = {
  #      "dojo_id": dojo_id
   # }
    #dojo =Dojo.get_dojo_and_ninjas(data)
    #return render_template('dojo_show.html', dojo = dojo)