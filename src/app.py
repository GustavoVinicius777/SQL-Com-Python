from flask import Flask, render_template, request, redirect
from dao import ClienteDAO
from models import Cliente

app = Flask(__name__)
dao = ClienteDAO()

@app.route("/")
def home():
    clientes = dao.listar()
    return render_template("index.html", clientes=clientes)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]

        dao.salvar(Cliente(nome=nome, email=email, telefone=telefone))
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cliente = dao.buscar(id)
    if request.method == "POST":
        dao.atualizar(
            Cliente(
                id=id,
                nome=request.form["nome"],
                email=request.form["email"],
                telefone=request.form["telefone"]
            )
        )
        return redirect("/")
    return render_template("edit.html", cliente=cliente)

@app.route("/delete/<int:id>")
def delete(id):
    dao.deletar(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
