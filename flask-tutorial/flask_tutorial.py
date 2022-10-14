from flask import Flask, render_template
import sqlite3 as sql
#le 'as' est un alias. Pour éviter sqlite3.connect

app = Flask(__name__)

@app.route("/") # "/" = homepage. Il va automatiquement aller voir dans /templates
def hello_world():
    return render_template("homepage.html")

@app.route("/if3/") # mettre un backlash à la fin car il y a un sous-domaine avec name. Pour pas avoir d'erreur si on n'a pas de name
@app.route("/if3/<name>") # on définit la route qu'on veut
def interface(name=None):
    return render_template("interface3.html", name=name) #si on veut skipper certains variables, paramètres, il faut préciser comme anchor="topleft"

@app.route("/tasks/<user>")
def tasks(user=None):

    connection = sql.connect("db.sqlite") # pas tasks, mais le nom du fichier de la base de données. Entre guillemets.
    cursor = connection.cursor() # c'est ce qui va nous permettre d'éxecuter la query. La connection est un tunnel vers le DB, le cursor c'est comme le train
    query = f"SELECT * FROM tasks WHERE user='{user}';"  #pas besoin de ';'
    cursor.execute(query)
    
    results = cursor.fetchall()
    connection.commit()
    connection.close()

    return render_template("tasks.html", user=user, tasks=results) # le premier task est celui défini dans l'html {{ task }} et le second est la variable défini dans ma fonction.
    # !!! Pas oublier de modifier ici aussi le task en tasks !