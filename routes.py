from flask import request, render_template
from app import app, db
from models import Table

@app.route('/')
def home():
    return 'Hello !'


@app.route('/add', methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        table = Table(
            id=request.form[id],
            country=request.form[country],
            capital=request.form[capital],
            population=request.form[population],
            language=request.form[language]          
        )
    return render_template("/index.html")


@app.route('/edit', methods = ["GET", "POST"])
def edit():
    if request.method == "POST":
        table = Table(
            id=request.form["id"]
        )
        test = Table.query.filter_by(id=table.id).first()

    return render_template("/edit.html")


@app.route('/delete', methods = ["GET", "POST"])
def delete():
    if request.method == "POST":
        table = Table(
            country=request.form["country"],
        )
        id_test = Table.query.filter_by(id=table.id).first()
        if user_test == None:
            result = "нет"
        else:
            db.session.delete(id_test)
            db.session.commit()
            result = "удалёно"
    return render_template("/delete.html", result=result)
 

        
@app.route('/see', methods = ["GET","POST"])
def see():
    return render_template("/table.html",)