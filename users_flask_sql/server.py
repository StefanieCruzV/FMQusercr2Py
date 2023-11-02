from cgitb import html
from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
 


@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "uname": request.form["uname"],
        "ulastname": request.form["ulastname"],
        "uemail": request.form["uemail"]
        # guarda los valores del formulario
        }
   
    User.save(data) # manda llamar al metodo para guardar
    users = User.get_all() # regresa los valores del metodo get all y almacena todos los datos de lbd
    print(users)
    return render_template("users.html",users=users) # lo que me regreso de la base al html
        # si es otra pagina 


if __name__ == "__main__":
    app.run(debug=True)

            
